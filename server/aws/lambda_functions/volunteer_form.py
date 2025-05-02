import json
import boto3
import uuid
import datetime
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# Environment & Constants
DYNAMODB_TABLE = 'VolunteerSubmissions'
S3_BUCKET = 'unitedrelief-volunteer-files'
GMAIL_USER = os.environ['GMAIL_USER']
GMAIL_APP_PASSWORD = os.environ['GMAIL_APP_PASSWORD']

def lambda_handler(event, context):
    try:
        logger.info("Received event")

        # Parse incoming JSON body
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

        # Save to DynamoDB
        table = dynamodb.Table(DYNAMODB_TABLE)
        table.put_item(Item={
            "email": email,
            "submittedAt": submittedAt,
            "id": str(uuid.uuid4()),
            "firstName": firstName,
            "lastName": lastName,
            "city": city,
            "state": state,
            "willingToTravel": str(willingToTravel),
            "message": message
        })

        # Backup to S3
        file_name = f"volunteers/{email.replace('@', '_at_')}_{submittedAt}.json"
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=file_name,
            Body=json.dumps(body),
            ContentType='application/json'
        )

        # Send confirmation email via Gmail SMTP
        subject = "Thank you for volunteering with UnitedRelief!"
        body_text = f"""Hi {firstName},

Thank you for volunteering with UnitedRelief!

Here’s what we received:
- Name: {firstName} {lastName}
- Email: {email}
- City/State: {city}, {state}
- Willing to Travel: {willingToTravel}
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
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, email, msg.as_string())
        server.quit()

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Credentials": "true"
            },
            "body": json.dumps({"message": "Volunteer submission received!"})
        }

    except Exception as e:
        logger.exception("Error during volunteer submission")
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Credentials": "true"
            },
            "body": json.dumps({"error": "Something went wrong processing your submission."})
        }
