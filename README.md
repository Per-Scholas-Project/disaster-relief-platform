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

<div align="center">

  <!-- Top-level AWS logo -->
  <img src="client/assets/logos/aws-logos/AWS-Cloud-logo_32.svg" alt="AWS Cloud" height="80" style="margin-bottom: 16px;" />

  <!-- Service icons wrapped underneath -->
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px;">
    <img src="client/assets/logos/aws-logos/Lambda.svg" alt="AWS Lambda" height="40" />
    <img src="client/assets/logos/aws-logos/Simple-Storage-Service.svg" alt="Amazon S3" height="40" />
    <img src="client/assets/logos/aws-logos/DynamoDB.svg" alt="Amazon DynamoDB" height="40" />
    <img src="client/assets/logos/aws-logos/CloudFormation.svg" alt="AWS CloudFormation" height="40" />
    <img src="client/assets/logos/aws-logos/Secrets-Manager.svg" alt="AWS Secrets Manager" height="40" />
    <img src="client/assets/logos/aws-logos/CloudWatch.svg" alt="AWS CloudWatch" height="40" />
    <img src="client/assets/logos/aws-logos/API-Gateway.svg" alt="Amazon API Gateway" height="40" />
    <img src="client/assets/logos/aws-logos/Simple-Notification-Service.svg" alt="Amazon SNS" height="40" />
  </div>

</div>


### Backend (`server/`)
- **Python (AWS Lambda)** – Stateless business logic
- **Amazon API Gateway** – Triggers Lambda with HTTP requests
- **Amazon DynamoDB** – NoSQL storage for submissions
- **Amazon S3** – Stores image uploads and JSON backups
- **Amazon SNS** – Notifies admins of new submissions
- **Gmail SMTP** – Sends confirmation emails to users
- **Amazon Secrets Manager** – Protects credentials like Gmail passwords
- **Amazon CloudFormation** – Manages all infrastructure as code
- **Amazon IAM & CloudWatch** – Secures access and logs Lambda activity
- **Amazon CloudTrail**

---
## 🧱 Tech Stack

### Frontend (`client/`)
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)  
  HTML, CSS, and JavaScript for responsive UI and form components

- 🖼️ Form validation, image preview, and mobile-friendly layout

### Backend (`server/`)
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)  
  Python (Lambda functions)
- ![API Gateway](https://img.shields.io/badge/AWS%20API%20Gateway-FF9900?style=flat&logo=amazonaws&logoColor=white)  
  RESTful endpoints for form handling
- ![DynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=flat&logo=amazon-dynamodb&logoColor=white)  
  NoSQL data storage
- ![S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=flat&logo=amazon-aws&logoColor=white)  
  Stores image uploads and backups
- ![SNS](https://img.shields.io/badge/Amazon%20SNS-FF9900?style=flat&logo=amazonaws&logoColor=white)  
  Admin alert notifications
- ![Secrets Manager](https://img.shields.io/badge/AWS%20Secrets%20Manager-336666?style=flat&logo=amazonaws&logoColor=white)  
  Protects Gmail credentials
- ![IAM](https://img.shields.io/badge/AWS%20IAM-4E8CDF?style=flat&logo=amazonaws&logoColor=white)  
  Scoped Lambda permissions
- ![CloudFormation](https://img.shields.io/badge/AWS%20CloudFormation-FF4F8B?style=flat&logo=amazonaws&logoColor=white)  
  Infrastructure-as-Code
- ![CloudWatch](https://img.shields.io/badge/Amazon%20CloudWatch-2D572C?style=flat&logo=amazon-aws&logoColor=white)  
  Lambda monitoring and logs
- ![Gmail SMTP](https://img.shields.io/badge/Gmail%20SMTP-D14836?style=flat&logo=gmail&logoColor=white)  
  Sends email confirmations


---

## 👥 Project Contributors

We’re a multidisciplinary team of developers and cloud engineers committed to scalable and impactful technology.

| Name                                                        | Role                                                       |
|-------------------------------------------------------------|------------------------------------------------------------|
| [**Sauel Almonte**](https://www.linkedin.com/in/sauel-almonte/) | Full-Stack Engineer & Cloud Solutions Architect (**Lead**) |
| [**Imran Masud**](https://www.linkedin.com/in/imran-masud-im/) | Backend Engineer (AWS Lambda & Python)                     |
| [**Ahmet Aygun**](https://www.linkedin.com/in/ahmet-aygun/) | Frontend Developer (UI & Interaction)                      |
| [**Michelle Quashie**](https://www.linkedin.com/in/michellequashie/) | AWS Security Architect (IAM & Secrets Manager)             |
| [**Jamaal Foster**](https://www.linkedin.com/in/jamaal-foster/) | AWS Security Architect (Policy Enforcement)                |
| [**Nathnael Girma**](https://www.linkedin.com/in/nathnael-girma/) | Frontend Developer (UX & Forms)                            |

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
