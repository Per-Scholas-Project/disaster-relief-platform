from server.aws.lambda_functions.package import boto3
from server.aws.lambda_functions.package.botocore.exceptions import ClientError
import os

class DynamoDBService:
    def __init__(self, table_name=None):
        self.table_name = table_name or os.getenv("DYNAMODB_TABLE", "AidRequests")
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(self.table_name)

    def save_request(self, aid_request: dict) -> dict:
        try:
            self.table.put_item(Item=aid_request)
            return {"success": True, "message": "Aid request saved successfully"}
        except ClientError as e:
            raise RuntimeError(f"Failed to save aid request: {e.response['Error']['Message']}")

    def get_all_requests(self) -> list:
        try:
            aid_requests = []
            response = self.table.scan()
            aid_requests.extend(response.get("Items", []))

            while "LastEvaluatedKey" in response:
                response = self.table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
                aid_requests.extend(response.get("Items", []))

            return aid_requests
        except ClientError as e:
            raise RuntimeError(f"Failed to retrieve aid requests: {e.response['Error']['Message']}")
