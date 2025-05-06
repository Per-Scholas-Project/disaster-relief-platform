import os
import json
import boto3
from botocore.exceptions import ClientError

# AWS clients
s3 = boto3.client("s3")

# Environment variable
BUCKET_NAME = os.environ.get("S3_BUCKET", "unitedrelief-submissions")

def lambda_handler(event, context):
    # === Handle CORS preflight ===
    if event.get("httpMethod") == "OPTIONS":
        return cors_response(200, {"message": "CORS preflight successful"})

    try:
        # Parse query parameters
        params = event.get("queryStringParameters", {}) or {}
        key = params.get("key")

        if not key:
            return cors_response(400, {"error": "Missing 'key' parameter"})

        # Generate the presigned URL
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': key
            },
            ExpiresIn=86400  # 24 hours in seconds
        )

        return cors_response(200, {"url": url})

    except ClientError as e:
        return cors_response(500, {"error": f"AWS error: {str(e)}"})
    except Exception as e:
        return cors_response(500, {"error": f"Server error: {str(e)}"})


def cors_response(status_code, body_dict):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://unitedrelief.vercel.app",  # ✅ Exact domain
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,GET",
            "Access-Control-Allow-Credentials": "true"
        },
        "body": json.dumps(body_dict)
    }
