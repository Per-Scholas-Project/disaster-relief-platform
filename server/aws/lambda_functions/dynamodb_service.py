import boto3
from botocore.exceptions import ClientError
import os
from typing import Optional, Dict, List, Any

class DynamoDBService:
    def __init__(self, table_name: Optional[str] = None):
        self.table_name = table_name or os.getenv("DYNAMODB_TABLE", "ReliefRequests")
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(self.table_name)

    def save_request(self, aid_request: Dict[str, Any]) -> Dict[str, str]:
        try:
            self.table.put_item(Item=aid_request)
            return {"success": True, "message": "Aid request saved successfully"}
        except ClientError as e:
            raise RuntimeError(f"Failed to save aid request: {e.response['Error']['Message']}")

    def get_all_requests(self) -> List[Dict[str, Any]]:
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
