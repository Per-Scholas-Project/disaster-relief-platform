# 🌍 United Relief – Disaster Relief Coordination Platform

United Relief is a full-stack disaster response platform built on AWS to connect disaster victims with volunteers and aid organizations.  
This backend-driven application automates request intake, file handling, notifications, and storage using scalable, secure AWS cloud services.

🔗 **Live Demo:** [United Relief](https://unitedrelief.vercel.app/)

---

## 💡 Why It Matters

Natural disasters demand fast, coordinated action. United Relief empowers local communities to:

- Submit structured help requests
- Mobilize volunteers
- Notify admin teams in real-time
- Store sensitive data securely

Its **serverless**, **scalable**, and **cost-efficient** architecture ensures operational readiness — especially when crisis hits.

---

## 🚀 Key Features & Capabilities

### 📝 Relief Request Submissions
- Victims request food, shelter, medical aid, and logistical help via structured form input

### 🤝 Volunteer Signups
- Community members offer availability, skills, and location

### 📷 Image Uploads
- Relief forms support image uploads (damage, ID, etc.) securely stored in S3

### 📧 Email & Admin Alerts
- Users receive confirmation via Gmail SMTP
- Admins/collaborators receive alerts via AWS SNS

### 🔐 Secure Cloud Architecture
- IAM role scoping and AWS Secrets Manager protect credentials and access

### ⚙️ Fully Serverless Infrastructure
- Built entirely with AWS Lambda, API Gateway, CloudFormation, and DynamoDB

---
## 🧱 Tech Stack
<div align="center">
  <!-- Service icons wrapped underneath -->
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px;">
    <img src="client/assets/logos/front-end/html-1.svg" alt="HTML" height="60" />
    <img src="client/assets/logos/front-end/css-3.svg" alt="CSS" height="60" />
    <img src="client/assets/logos/front-end/javascript-r.svg" alt="JavaScript" height="60" />
  </div>

</div>

### Frontend (`client/`)
- **HTML/CSS/JavaScript** – Lightweight, accessible UI for all devices
- **Form validation & file preview** – Ensures user input accuracy
- **RESTful integration** – Submits requests via API Gateway

<br>
<div align="center">

  <!-- Top-level AWS logo -->
  <img src="client/assets/logos/aws-logos/AWS-Cloud-logo_32.svg" alt="AWS Cloud" height="80" style="margin-bottom: 16px;" />

  <!-- Service icons wrapped underneath -->
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px;">
    <img src="client/assets/logos/aws-logos/Lambda.svg" alt="AWS Lambda" height="50" />
    <img src="client/assets/logos/aws-logos/Simple-Storage-Service.svg" alt="Amazon S3" height="50" />
    <img src="client/assets/logos/aws-logos/DynamoDB.svg" alt="Amazon DynamoDB" height="50" />
    <img src="client/assets/logos/aws-logos/CloudFormation.svg" alt="AWS CloudFormation" height="50" />
    <img src="client/assets/logos/aws-logos/Secrets-Manager.svg" alt="AWS Secrets Manager" height="50" />
    <img src="client/assets/logos/aws-logos/CloudWatch.svg" alt="AWS CloudWatch" height="50" />
    <img src="client/assets/logos/aws-logos/CloudTrail.svg" alt="AWS CloudTrail" height="50" />
    <img src="client/assets/logos/aws-logos/API-Gateway.svg" alt="Amazon API Gateway" height="50" />
    <img src="client/assets/logos/aws-logos/Simple-Notification-Service.svg" alt="Amazon SNS" height="50" />
    <img src="client/assets/logos/aws-logos/Config.svg" alt="Amazon Config" height="50" />
    <img src="client/assets/logos/aws-logos/Shield.svg" alt="Amazon Shield" height="50" />
    <img src="client/assets/logos/aws-logos/IAM-Identity-Center.svg" alt="Amazon IAM Access Analyzer" height="50" />
    <img src="client/assets/logos/aws-logos/Identity-and-Access-Management.svg" alt="Amazon IAM" height="50" />
    <img src="client/assets/logos/aws-logos/Identity-and-Access-Management.svg" alt="Amazon IAM" height="50" />
  </div>

</div>

### Backend (`server/`)
1. **AWS IAM (Identity and Access Management)** – Manages roles and permissions for Lambda, API Gateway, DynamoDB, and S3 with least-privilege policies.


2. **Amazon S3** – Stores uploaded relief images **relief-images/**, volunteer backups **volunteers/**, and Lambda deployment ZIPs.


3. **Amazon DynamoDB** – NoSQL storage for relief request **ReliefRequests** and volunteer form submissions **VolunteerSubmissions**.


4. **AWS Lambda (Python)** – Stateless compute for backend form processing, file uploads, email sending, SNS alerts, and presigned URL generation.


5. **Amazon API Gateway** – REST API endpoints that trigger Lambda functions for relief and volunteer forms, and image retrieval.


6. **Amazon CloudFormation** – Infrastructure as Code for reproducible deployment of Lambda, IAM, S3, DynamoDB, API Gateway, and environment variables.


7. **Amazon CloudWatch** – Logs and monitors Lambda function execution, errors, and debugging events.


8. **Amazon Secrets Manager** – Stores Gmail credentials securely **unitedrelief/gmail** for use in Lambda SMTP email delivery.


9. **Amazon SNS (Simple Notification Service)** – Sends email notifications to admins when forms are submitted topic: **unitedrelief-submissions-alerts**.


10. **Gmail SMTP (via smtplib)** – Sends confirmation emails to users after submission, integrated through Python's **smtplib**.


11. **AWS Config** – Tracks configuration changes in critical resources like S3, IAM, Lambda, and API Gateway for auditability.


12. **AWS Shield Standard** – Provides automatic DDoS protection for API Gateway and AWS-managed endpoints.


13. **AWS IAM Access Analyzer** – Continuously scans IAM roles/policies for public or cross-account exposure.


14. **AWS Budgets** – Monitors costs with a **5 monthly budget and email alerts at $0.01 usage**.


15. **AWS Cost Explorer** – Analyzes cost trends and breakdowns by service to support budgeting and optimization.


16. **AWS Free Tier Usage Alerts** – Sends notifications when resource usage approaches free tier limits to avoid surprise charges.

---

## 👥 Project Contributors

We’re a multidisciplinary team of developers and cloud engineers committed to scalable and impactful technology.

| Name                                                        | Role                                                           |
|-------------------------------------------------------------|----------------------------------------------------------------|
| [**Sauel Almonte**](https://www.linkedin.com/in/sauel-almonte/) | (**Lead**) Full-Stack Engineer & AWS Cloud Solutions Architect |
| [**Imran Masud**](https://www.linkedin.com/in/imran-masud-im/) | Backend Engineer (AWS Lambda & Python)                         |
| [**Ahmet Aygun**](https://www.linkedin.com/in/ahmet-aygun/) | Frontend Developer (UI/UX with AWS Integration)                          |
| [**Nathnael Girma**](https://www.linkedin.com/in/nathnael-girma/) | Frontend Developer (UI/UX with AWS Integration)                                |
| [**Michelle Quashie**](https://www.linkedin.com/in/michellequashie/) | AWS Security Architect (IAM & Secrets Manager)                 |
| [**Jamaal Foster**](https://www.linkedin.com/in/jamaal-foster/) | AWS Security Architect (Policy Enforcement)                    |

---

## 🗂 Project Structure
```plaintext
disaster-relief-platform/
├── client/
│   ├── assets/
│   │   ├── fonts/
│   │   ├── icons/
│   │   ├── images/
│   │   └── logos/
│   ├── pages/
│   │   └── forms/
│   ├── scripts/
│   │   ├── components/
│   │   ├── forms/
│   │   ├── utils/
│   │   └── index.js
│   ├── styles/
│   └── index.html
├── server/
│   ├── aws/
│   │   ├── deployment/
│   │   ├── infrastructure/
│   │   └── lambda_functions/
│   ├── scripts/
│   └── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/disaster-relief-platform.git
cd disaster-relief-platform
```

### 2. Deploy Infrastructure (CloudFormation)

```bash
cd server/scripts
bash deploy_infra_stack.sh
```

### 3. Deploy Lambda Functions
```bash
bash deploy_relief_request.sh
bash deploy_volunteer_form.sh
bash deploy_presigned_url_lambda.sh
```

### 4. Subscribe Admins to SNS
```bash
bash subscribe_admins.sh
```

---

### 🔐 Security Notes
- Secrets are encrypted in AWS Secrets Manager
- Lambda roles are tightly scoped via IAM
- All endpoints served over HTTPS via API Gateway

---
# DISCLAIMER

*THE SOFTWARE IS PROVIDED **"AS IS"**, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT*.

*IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE* .

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

MIT License

*Copyright (c) 2025 Dream Team*

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     
copies of the Software, and to permit persons to whom the Software is         
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
