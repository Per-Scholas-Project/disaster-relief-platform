import boto3
import os
import base64
import logging
import binascii

class S3Service:
    def __init__(self, bucket_name=None):
        self.bucket_name = bucket_name or os.getenv("BUCKET_NAME")
        if not self.bucket_name:
            raise ValueError("S3 bucket name is missing. Set BUCKET_NAME in environment variables.")
        self.s3 = boto3.client("s3")

    def upload_image_and_get_url(self, request_id, image_base64):
        try:
            if not isinstance(request_id, str) or not request_id.strip():
                raise ValueError("Invalid request_id")
            if not image_base64:
                raise ValueError("No image data provided for upload")

            logging.info(f"Uploading image for request_id: {request_id}")

            # === Remove base64 prefix (if present) ===
            if image_base64.startswith("data:image/jpeg;base64,"):
                image_base64 = image_base64[len("data:image/jpeg;base64,"):]

            # === Fix padding for base64 decoding ===
            image_base64 += '=' * ((4 - len(image_base64) % 4) % 4)

            image_data = base64.b64decode(image_base64)

            # === Generate S3 key ===
            key = f"aid-requests/{request_id}.jpg"

            # === Upload to S3 ===
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=image_data,
                ContentType="image/jpeg"
            )

            # === Construct Public S3 URL ===
            image_url = f"https://{self.bucket_name}.s3.amazonaws.com/{key}"
            logging.info(f"Image successfully uploaded to: {image_url}")
            return image_url

        except binascii.Error:
            logging.error("Invalid base64 encoding")
            raise ValueError("Invalid base64 encoding")

        except Exception as e:
            logging.error(f"S3 upload failed: {e}")
            raise RuntimeError(f"Failed to upload image to S3: {e}")
