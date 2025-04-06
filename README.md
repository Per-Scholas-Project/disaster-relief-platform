# 🌍 Disaster Relief Coordinating Platform

A backend-driven platform to connect disaster victims with volunteers and resources. Built using AWS services like Lambda, API Gateway, DynamoDB, and S3.

---

## 🚀 Features

- 📝 Submit Help Requests (food, shelter, rescue, etc.)
- 📷 Upload photos of damage or supplies
- 👥 User Registration & Login (via AWS Cognito)
- 📡 Real-time coordination status
- 🔔 Optional SMS/Email alerts (via AWS SNS)

---

## 🧱 Tech Stack

### Frontend (`client/`)
- HTML/CSS/JavaScript
- Sends help requests to AWS API Gateway
- Displays submitted requests (future feature)

### Backend (`server/`)
- AWS Lambda (Python)
- API Gateway
- DynamoDB (data storage)
- S3 (photo uploads)
- Cognito (user auth)
- Optional: SNS for alerts

---

# 🗂 Project Structure
## 🌍 Disaster Relief Coordinating Platform

```plaintext
disaster-relief-platform/
├── client/                  # Frontend files (HTML/JS/CSS)
├── server/                  # Lambda functions (Python)
│   ├── submit_help_request/
│   ├── fetch_requests/
│   └── signup_login/
├── infrastructure/          # (Optional) API configs, IAM roles
├── .env                     # Local environment variables (excluded from Git)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/disaster-relief-platform.git
cd disaster-relief-platform
```

### 2. Install Python Dependencies

```bash
cd server/submit_help_request
pip install -r requirements.txt -t .
```

### 3. Environment Variables
```bash
cp .env.example .env
```
- AWS_ACCESS_KEY_ID=your-access-key
- AWS_SECRET_ACCESS_KEY=your-secret-access-key
- AWS_REGION=us-east-1
- COGNITO_USER_POOL_ID=your-pool-id
- COGNITO_CLIENT_ID=your-client-id
- DYNAMODB_TABLE=requests
- S3_BUCKET=relief-platform-uploads

### 4. Deploying to AWS
- Manual via AWS Console (upload ZIPs)
- AWS CLI (recommended for repeatability)
- SAM / Serverless Framework (optional for infrastructure-as-code)

### Example Manual Deployment Steps:
1. Zip the Lambda code:
    ```bash
    cd server/submit_help_request
    zip -r function.zip .
    ```

2. Upload the ZIP to AWS Lambda via the Console or:
    ```bash
    aws lambda update-function-code \
      --function-name SubmitHelpRequest \
      --zip-file fileb://function.zip
    ```

3. Set environment variables in the Lambda console or use AWS CLI.

---

### 5. API Endpoints

| Method | Endpoint                         | Description                      |
|--------|----------------------------------|----------------------------------|
| POST   | `/submit-help-request`          | Submit a new request for help   |
| GET    | `/fetch-requests`               | View all open help requests     |
| POST   | `/signup` / `/login` (optional) | User registration/login (Cognito) |

All endpoints are routed through **API Gateway** and trigger their corresponding **Lambda functions**.

---

### 6. Security Notes
- All secrets are stored in AWS Lambda environment variables
- Never store credentials in code
- All endpoints are served over HTTPS via API Gateway
- Cognito used for secure login

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

MIT License

Copyright (c) 2025 Sauel Almonte

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     
copies of the Software, and to permit persons to whom the Software is         
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
