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

### Frontend (`client/`)
- **HTML/CSS/JavaScript** – Lightweight, accessible UI for all devices
- **Form validation & file preview** – Ensures user input accuracy
- **RESTful integration** – Submits requests via API Gateway

### Backend (`server/`)
- **Python (AWS Lambda)** – Stateless business logic
- **Amazon API Gateway** – Triggers Lambda with HTTP requests
- **Amazon DynamoDB** – NoSQL storage for submissions
- **Amazon S3** – Stores image uploads and JSON backups
- **Amazon SNS** – Notifies admins of new submissions
- **Gmail SMTP** – Sends confirmation emails to users
- **AWS Secrets Manager** – Protects credentials like Gmail passwords
- **AWS CloudFormation** – Manages all infrastructure as code
- **AWS IAM & CloudWatch** – Secures access and logs Lambda activity

---

## 👥 Project Contributors

We’re a multidisciplinary team of developers and cloud engineers committed to scalable and impactful technology.

| Name | Role                                                       |
|------|------------------------------------------------------------|
| **Sauel Almonte** | Full-Stack Engineer & Cloud Solutions Architect (**Lead**) |
| **Imran Masud** | Backend Engineer (AWS Lambda & Python)                     |
| **Ahmet Aygun** | Frontend Developer (UI & Interaction)                      |
| **Michelle Quashie** | AWS Security Architect (IAM & Secrets Manager)             |
| **Jamaal Foster** | AWS Security Architect (Policy Enforcement)                |
| **Nathnael Girma** | Frontend Developer (UX & Forms)                            |

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
