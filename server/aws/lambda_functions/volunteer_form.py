import json
import boto3
import uuid
import datetime
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from botocore.exceptions import ClientError

# === Logging ===
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# === AWS Clients ===
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
sns = boto3.client('sns')
secretsmanager = boto3.client('secretsmanager')

# === Environment Variables ===
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']              # e.g. VolunteerSubmissions
S3_BUCKET = os.environ['S3_BUCKET']                        # e.g. unitedrelief-submissions
SECRET_NAME = os.environ['GMAIL_SECRET_NAME']              # e.g. unitedrelief/gmail
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']                # e.g. arn:aws:sns:...

def lambda_handler(event, context):
    # === CORS Preflight Support ===
    if event.get("httpMethod") == "OPTIONS":
        return cors_response(200, {"message": "CORS preflight successful"})

    try:
        logger.info("Processing volunteer submission event")

        # Parse request body
        body = json.loads(event.get('body', '{}'))

        # Extract fields
        firstName = body.get("firstName")
        lastName = body.get("lastName")
        email = body.get("email")
        city = body.get("city")
        state = body.get("state")
        willingToTravel = body.get("willingToTravel")
        message = body.get("message")
        submittedAt = datetime.datetime.utcnow().isoformat()

        # === Save to DynamoDB ===
        table = dynamodb.Table(DYNAMODB_TABLE)
        table.put_item(Item={
            "email": email,
            "submittedAt": submittedAt,
            "id": str(uuid.uuid4()),
            "firstName": firstName,
            "lastName": lastName,
            "city": city,
            "state": state,
            "willingToTravel": "Yes" if willingToTravel else "No",
            "message": message
        })

        # === Backup to S3 ===
        safe_email = email.replace('@', '_at_').replace('.', '_dot_')
        key = f"volunteers/{safe_email}_{submittedAt}.json"
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=key,
            Body=json.dumps(body),
            ContentType='application/json'
        )

        # === Fetch Gmail credentials securely ===
        creds = get_gmail_credentials()
        GMAIL_USER = creds['GMAIL_USER']
        GMAIL_PASS = creds['GMAIL_APP_PASSWORD']

        # === Send confirmation email ===
        subject = "Thank you for volunteering with UnitedRelief!"
        body_text = f"""Hi {firstName},

Thank you for volunteering with UnitedRelief!

Here’s what we received:
- Name: {firstName} {lastName}
- Email: {email}
- City/State: {city}, {state}
- Willing to Travel: {"Yes" if willingToTravel else "No"}
- Message: {message}

We’ll follow up with next steps soon!

– UnitedRelief Team
"""

        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body_text, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, email, msg.as_string())
        server.quit()

        # === Send Admin Notification via SNS ===
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="New Volunteer Submission",
            Message=f"""A new volunteer form was submitted by {email}.

Details:
Name: {firstName} {lastName}
City/State: {city}, {state}
Willing to Travel: {"Yes" if willingToTravel else "No"}
Message: {message}
"""
        )

        return cors_response(200, {"message": "Volunteer submission received!"})

    except Exception as e:
        logger.exception("Error in volunteer_form")
        return cors_response(500, {"error": "Something went wrong processing your submission."})


# === Secrets Manager ===
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

# === CORS Helper ===
def cors_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST",
            "Access-Control-Allow-Credentials": "true"
        },
        "body": json.dumps(body)
    }
