import uuid
import boto3
import os
import logging
from datetime import datetime
from dynamodb_service import DynamoDBService
from s3_service import S3Service

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Service:
    def __init__(self):
        self.bucket_name = os.getenv("BUCKET_NAME", "disaster-aid-images-2025")
        self.sns_topic_arn = os.getenv("SNS_TOPIC_ARN", "arn:aws:sns:us-east-1:650856831762:disaster-aid-alerts")
        self.s3_service = S3Service(self.bucket_name)
        self.dynamo_service = DynamoDBService()
        self.sns_client = boto3.client('sns')

    def submit_aid_request(self, body):
        try:
            # Validate required fields
            required_fields = ["name", "email", "request_type", "description"]
            missing = [f for f in required_fields if not body.get(f)]
            if missing:
                return {
                    "statusCode": 400,
                    "body": {"message": f"Missing fields: {', '.join(missing)}"}
                }

            request_id = str(uuid.uuid4())
            image_url = ""

            # Handle optional image
            if "image_base64" in body:
                try:
                    image_url = self.s3_service.upload_image_and_get_url(request_id, body["image_base64"])
                except Exception as e:
                    logger.exception("Image upload failed")
                    return {
                        "statusCode": 500,
                        "body": {"message": "Image upload failed", "error": str(e)}
                    }

            # Prepare item for DynamoDB
            aid_request = {
                "request_id": request_id,
                "name": body["name"],
                "email": body["email"],
                "request_type": body["request_type"],
                "description": body["description"],
                "status": "Pending",
                "timestamp": datetime.utcnow().isoformat(),
                "image_url": image_url
            }

            try:
                self.dynamo_service.save_request(aid_request)
            except Exception as e:
                logger.exception("DynamoDB save failed")
                return {
                    "statusCode": 500,
                    "body": {"message": "Failed to save request to DynamoDB", "error": str(e)}
                }

            # Send SNS notification
            try:
                self.sns_client.publish(
                    TopicArn=self.sns_topic_arn,
                    Message=(
                        f"New Aid Request Submitted\n"
                        f"Type: {aid_request['request_type']}\n"
                        f"Name: {aid_request['name']}\n"
                        f"Email: {aid_request['email']}\n"
                        f"Description: {aid_request['description']}"
                    ),
                    Subject="New Aid Request"
                )
            except Exception as e:
                logger.warning("SNS notification failed")
                return {
                    "statusCode": 500,
                    "body": {"message": "SNS notification failed", "error": str(e)}
                }

            return {
                "statusCode": 201,
                "body": {"message": "Aid request submitted", "request_id": request_id}
            }

        except Exception as e:
            logger.exception("Unexpected error in submit_aid_request")
            return {
                "statusCode": 500,
                "body": {"message": "Failed to process aid request", "error": str(e)}
            }

    def get_all_requests(self):
        try:
            requests = self.dynamo_service.get_all_requests()
            return {"statusCode": 200, "body": requests}
        except Exception as e:
            logger.exception("Failed to fetch aid requests")
            return {
                "statusCode": 500,
                "body": {"message": "Failed to retrieve aid requests", "error": str(e)}
            }
