import uuid
import boto3
import os
from datetime import datetime
from dynamodb_service import DynamoDBService
from s3_service import S3Service

class Service:
    def __init__(self):
        self.bucket_name = os.getenv("BUCKET_NAME", "disaster-aid-images-2025")
        self.s3_service = S3Service(self.bucket_name)
        self.dynamo_service = DynamoDBService()
        self.sns_client = boto3.client('sns')
        self.sns_topic_arn = os.getenv("SNS_TOPIC_ARN", "arn:aws:sns:us-east-1:650856831762:disaster-aid-alerts")

    def submit_aid_request(self, body):
        try:
            # Validate required fields
            required_fields = ["name", "email", "request_type", "description"]
            for field in required_fields:
                if field not in body:
                    return {
                        "statusCode": 400,
                        "body": {"message": f"Missing field: {field}"}
                    }

            request_id = str(uuid.uuid4())
            image_url = None

            # Handle optional image
            if "image_base64" in body:
                try:
                    image_url = self.s3_service.upload_image_and_get_url(request_id, body["image_base64"])
                except Exception as e:
                    return {
                        "statusCode": 500,
                        "body": {"message": "Image upload failed", "error": str(e)}
                    }

            # Build request object
            aid_request = {
                "request_id": request_id,
                "name": body["name"],
                "email": body["email"],
                "request_type": body["request_type"],
                "description": body["description"],
                "status": "Pending",
                "timestamp": datetime.utcnow().isoformat(),
                "image_url": image_url or ""
            }

            # Save to DynamoDB
            try:
                self.dynamo_service.save_request(aid_request)
            except Exception as e:
                return {
                    "statusCode": 500,
                    "body": {"message": "Failed to save request to DynamoDB", "error": str(e)}
                }

            # Send SNS notification
            message = (
                f"📢 New Aid Request Submitted!\n"
                f"Type: {aid_request['request_type']}\n"
                f"From: {aid_request['name']} ({aid_request['email']})\n"
                f"Description: {aid_request['description']}"
            )

            try:
                self.sns_client.publish(
                    TopicArn=self.sns_topic_arn,
                    Message=message,
                    Subject="New Aid Request Notification"
                )
            except Exception as e:
                return {
                    "statusCode": 500,
                    "body": {"message": "SNS notification failed", "error": str(e)}
                }

            return {
                "statusCode": 201,
                "body": {"message": "Aid request submitted", "request_id": request_id}
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": {"message": "Failed to process aid request", "error": str(e)}
            }

    def get_all_requests(self):
        try:
            data = self.dynamo_service.get_all_requests()
            return {"statusCode": 200, "body": data}
        except Exception as e:
            return {
                "statusCode": 500,
                "body": {"message": "Failed to retrieve aid requests", "error": str(e)}
            }
