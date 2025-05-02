import json
import boto3
import os
import uuid
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from requests_toolbelt.multipart import decoder
import base64

# === AWS Clients ===
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# === Environment Variables ===
DYNAMODB_TABLE = 'ReliefRequests'
S3_BUCKET = 'unitedrelief-volunteer-files'
GMAIL_USER = os.environ['GMAIL_USER']
GMAIL_APP_PASSWORD = os.environ['GMAIL_APP_PASSWORD']

def lambda_handler(event, context):
    try:
        # === Decode multipart/form-data ===
        content_type = event['headers'].get('content-type') or event['headers'].get('Content-Type')
        body = event['body']
        if event.get("isBase64Encoded"):
            body = base64.b64decode(body)

        multipart_data = decoder.MultipartDecoder(body, content_type)

        fields = {}
        files = []

        for part in multipart_data.parts:
            content_disposition = part.headers.get(b'Content-Disposition', b'').decode()
            if 'filename' in content_disposition:
                files.append({
                    "filename": get_filename(content_disposition),
                    "content": part.content,
                    "content_type": part.headers.get(b'Content-Type', b'').decode()
                })
            else:
                name = get_field_name(content_disposition)
                fields[name] = part.text

        # === Extract Fields ===
        firstName = fields.get("firstName")
        lastName = fields.get("lastName")
        email = fields.get("email")
        phone = fields.get("phone")
        city = fields.get("city")
        state = fields.get("state")
        assistanceType = fields.get("assistanceType")
        description = fields.get("description")
        submittedAt = datetime.datetime.utcnow().isoformat()

        # === Save to DynamoDB ===
        table = dynamodb.Table(DYNAMODB_TABLE)
        table.put_item(Item={
            "email": email,
            "submittedAt": submittedAt,
            "id": str(uuid.uuid4()),
            "firstName": firstName,
            "lastName": lastName,
            "phone": phone,
            "city": city,
            "state": state,
            "assistanceType": assistanceType,
            "description": description
        })

        # === Upload Files to S3 ===
        for f in files:
            filename = f"relief-images/{uuid.uuid4()}_{f['filename']}"
            s3.put_object(
                Bucket=S3_BUCKET,
                Key=filename,
                Body=f['content'],
                ContentType=f['content_type']
            )

        # === Send Confirmation Email ===
        send_email_confirmation(email, firstName, lastName, phone, city, state, assistanceType, description)

        # === Return Success Response ===
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({"message": "Relief request received successfully!"})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

# === Helper: Extract field name from Content-Disposition ===
def get_field_name(content_disposition):
    for item in content_disposition.split(";"):
        if item.strip().startswith("name="):
            return item.strip().split("=")[1].strip('"')
    return None

# === Helper: Extract filename from Content-Disposition ===
def get_filename(content_disposition):
    for item in content_disposition.split(";"):
        if item.strip().startswith("filename="):
            return item.strip().split("=")[1].strip('"')
    return None

# === Helper: Send Confirmation Email ===
def send_email_confirmation(to_email, firstName, lastName, phone, city, state, assistanceType, description):
    subject = "UnitedRelief - Your Aid Request Was Received"
    body_text = f"""Hi {firstName},

Your request for aid has been received:

- Name: {firstName} {lastName}
- Phone: {phone}
- Location: {city}, {state}
- Type: {assistanceType}
- Description: {description}

We will follow up with you shortly.

– UnitedRelief Team
"""

    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body_text, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    server.sendmail(GMAIL_USER, to_email, msg.as_string())
    server.quit()
