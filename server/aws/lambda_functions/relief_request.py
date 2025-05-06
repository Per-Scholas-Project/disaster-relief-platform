import json
import boto3
import uuid
import os
import base64
import datetime
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from botocore.exceptions import ClientError
from requests_toolbelt.multipart import decoder
from io import BytesIO

# === Logging ===
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# === AWS Clients ===
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
sns = boto3.client('sns')
secretsmanager = boto3.client('secretsmanager')

# === Environment Variables ===
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
S3_BUCKET = os.environ['S3_BUCKET']
SECRET_NAME = os.environ['GMAIL_SECRET_NAME']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    try:
        logger.info("Received event for relief request")

        if event.get("httpMethod") == "OPTIONS":
            return cors_response(200, {"message": "CORS preflight successful"})

        content_type = event["headers"].get("content-type") or event["headers"].get("Content-Type")
        body = event["body"]
        if event.get("isBase64Encoded"):
            body = base64.b64decode(body)
        else:
            body = body.encode('utf-8')

        multipart_data = decoder.MultipartDecoder(body, content_type)

        form_data = {}
        image_keys = []

        for part in multipart_data.parts:
            content_disposition = part.headers.get(b'Content-Disposition', b'').decode()
            if "filename=" in content_disposition:
                filename = content_disposition.split("filename=")[1].strip('"')
                key = f"relief-images/{uuid.uuid4()}_{filename}"
                s3.upload_fileobj(
                    Fileobj=BytesIO(part.content),
                    Bucket=S3_BUCKET,
                    Key=key,
                    ExtraArgs={'ContentType': part.headers.get(b'Content-Type', b'application/octet-stream').decode()}
                )
                image_keys.append(key)
            else:
                name = content_disposition.split("name=")[1].strip('"')
                form_data[name] = part.text

        submission_id = str(uuid.uuid4())
        submitted_at = datetime.datetime.utcnow().isoformat()

        dynamo_item = {
            "id": submission_id,
            "submittedAt": submitted_at,
            "firstName": form_data.get("firstName"),
            "lastName": form_data.get("lastName"),
            "email": form_data.get("email"),
            "phone": form_data.get("phone"),
            "city": form_data.get("city"),
            "state": form_data.get("state"),
            "assistanceType": form_data.get("assistanceType"),
            "description": form_data.get("description"),
            "imageKeys": image_keys
        }

        # Save to DynamoDB
        table = dynamodb.Table(DYNAMODB_TABLE)
        table.put_item(Item=dynamo_item)

        # Fetch Gmail credentials securely
        creds = get_gmail_credentials()
        GMAIL_USER = creds['GMAIL_USER']
        GMAIL_PASS = creds['GMAIL_APP_PASSWORD']

        # Compose and send confirmation email
        subject = "UnitedRelief – Request Received"
        email_body = f"""Hi {form_data.get('firstName')},

Thank you for submitting your relief request. We’ve received the following:

- Name: {form_data.get('firstName')} {form_data.get('lastName')}
- Phone: {form_data.get('phone')}
- City/State: {form_data.get('city')}, {form_data.get('state')}
- Type of Assistance: {form_data.get('assistanceType')}
- Description: {form_data.get('description')}

We'll follow up soon.

– UnitedRelief Team
"""

        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = form_data.get("email")
        msg['Subject'] = subject
        msg.attach(MIMEText(email_body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, form_data.get("email"), msg.as_string())
        server.quit()

        # === Send Admin Notification via SNS ===
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="New Relief Request Submission",
            Message=f"""A new relief request has been submitted by {form_data.get("email")}.

Details:
Name: {form_data.get("firstName")} {form_data.get("lastName")}
Phone: {form_data.get("phone")}
City/State: {form_data.get("city")}, {form_data.get("state")}
Type of Assistance: {form_data.get("assistanceType")}
Description: {form_data.get("description")}
Images: {len(image_keys)} file(s) uploaded
"""
        )

        return cors_response(200, {"message": "Relief request submitted successfully."})

    except Exception as e:
        logger.exception("Error in relief_request")
        return cors_response(500, {"error": str(e)})


# === Fetch Gmail credentials securely ===
def get_gmail_credentials():
    try:
        response = secretsmanager.get_secret_value(SecretId=SECRET_NAME)
        secret = json.loads(response["SecretString"])
        return {
            "GMAIL_USER": secret["GMAIL_USER"],
            "GMAIL_APP_PASSWORD": secret["GMAIL_APP_PASSWORD"]
        }
    except ClientError as e:
        raise RuntimeError(f"Failed to retrieve Gmail credentials: {e}")

# === CORS Response Helper ===
def cors_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://unitedrelief.vercel.app",  # ✅ Set exact origin
            "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
            "Access-Control-Allow-Credentials": "true"
        },
        "body": json.dumps(body)
    }
