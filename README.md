# 🌍 United Relief
## Disaster Relief Coordination Platform
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
<div align="center">
  <!-- Service icons wrapped underneath -->
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px;">
    <img src="client/assets/logos/front-end/html-1.svg" alt="HTML" height="60" />
    <img src="client/assets/logos/front-end/css-3.svg" alt="CSS" height="60" />
    <img src="client/assets/logos/front-end/javascript-r.svg" alt="JavaScript" height="60" />
  </div>
</div>

- **HTML/CSS/JavaScript** – Lightweight, accessible UI for all devices
- **Form validation & file preview** – Ensures user input accuracy
- **RESTful integration** – Submits requests via API Gateway

---
### Backend (`server/`)
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

## 🔐 Security & Identity Management

**Services:**
- **AWS IAM** – Manages roles and permissions for Lambda, API Gateway, DynamoDB, and S3 using least-privilege policies.
- **AWS IAM Access Analyzer** – Continuously scans IAM roles and policies for public or cross-account exposure.
- **AWS Config** – Tracks configuration changes to resources like S3, IAM, Lambda, and API Gateway for auditability.
- **AWS Shield Standard** – Automatically provides DDoS protection for API Gateway and other AWS-managed endpoints.
- **Amazon Secrets Manager** – Securely stores credentials, such as Gmail credentials at `unitedrelief/gmail`, for Lambda use.

**Purpose & Implementation:**
- Enforces strict access control between AWS services to prevent over-permissioning.
- Identifies unintended public or external access using IAM Access Analyzer.
- Monitors changes to infrastructure configuration for compliance and security.
- Secures email credentials without embedding them in code.
- Protects public APIs from DDoS attacks automatically.

---

## ⚙️ Application Logic & Integration

**Services:**
- **AWS Lambda (Python)** – Handles stateless compute for form processing, file uploads, email dispatch, presigned URL generation, and SNS alerts.
- **Amazon API Gateway** – RESTful interface that connects frontend forms with backend Lambda functions.
- **Amazon SNS** – Sends alert emails to admins on form submission using the topic `unitedrelief-submissions-alerts`.
- **Gmail SMTP (via smtplib)** – Sends confirmation emails to users after submission via Python’s `smtplib`, integrated with Lambda.

**Purpose & Implementation:**
- Processes backend logic serverlessly and scales with traffic demand.
- Connects external users securely to internal AWS logic.
- Notifies stakeholders in real-time on critical form activity.
- Ensures timely communication with users using secure and integrated email delivery.

---

## 🗂️ Storage & Data Management

**Services:**
- **Amazon DynamoDB** – Stores structured application data such as `ReliefRequests` and `VolunteerSubmissions` using NoSQL tables.
- **Amazon S3** – Stores uploaded assets such as images (`relief-images/`), volunteer backups (`volunteers/`), and Lambda deployment ZIPs.

**Purpose & Implementation:**
- Dynamically stores and retrieves structured user data with low latency.
- Ensures secure, scalable file storage for uploads and deployments.
- Uses logical prefixes in S3 for easy organization and access.
- All storage is natively integrated with Lambda functions for seamless read/write operations.

---

## 🧰 Infrastructure & Monitoring

**Services:**
- **Amazon CloudFormation** – Defines infrastructure (Lambda, IAM, S3, DynamoDB, API Gateway, environment variables) using code templates for repeatable deployments.
- **Amazon CloudWatch** – Collects logs, execution traces, and error metrics from Lambda functions for real-time monitoring.
- **Amazon CloudTrail** – Tracks account activity and service usage for security audits and compliance reporting.

**Purpose & Implementation:**
- Uses Infrastructure as Code (IaC) to manage deployments consistently across environments.
- Enables debugging, performance tuning, and alerting through real-time telemetry.
- Provides traceability and governance of all API activity.

---

## 💰 Cost Management

**Services:**
- **AWS Budgets** – Enforces a monthly cost cap with email alerts starting at $0.01 usage.
- **AWS Cost Explorer** – Analyzes and visualizes cost breakdowns across AWS services for optimization.
- **AWS Free Tier Usage Alerts** – Sends alerts when usage approaches or exceeds Free Tier limits.

**Purpose & Implementation:**
- Prevents unexpected billing by proactively alerting at minimal usage thresholds.
- Helps analyze and optimize usage for cost efficiency.
- Supports budgeting efforts during development and production phases.

---
## 🖼️ AWS System Architecture

Here is a diagram that illustrates the architecture of the **UnitedRelief** system:

![UnitedRelief AWS System Architecture](/client/assets/aws-system-architectured/UnitedRelief%20AWS%20System%20Architecture-6.png)

## Future Scope & Improvements

As **UnitedRelief** continues to evolve, we plan to expand our AWS infrastructure beyond the current Free Tier–eligible services to enhance performance, scalability, and long-term sustainability. Below are key areas of focus for future implementation:

### ⚙️ Front-End Improvements

**React.js, VITE, and TailwindCSS**  
- We plan to modernize the front-end by migrating to **React.js**, which will enable us to build a more dynamic, responsive, and maintainable user interface. 
- Using **VITE** as a build tool will significantly speed up the development process with fast hot module reloading, making the user experience smoother. 
- Additionally, we will implement **TailwindCSS** to streamline our CSS management, enabling quick and customizable designs with minimal effort.

Key Goals:
- **Revamping the UI/UX:** Giving the front-end a complete facelift to enhance usability and user engagement.
- **Improved Performance:** Reducing load times with optimized React.js components and VITE’s efficient build process.
- **Responsive Design:** Ensuring the platform is highly responsive across devices using TailwindCSS’s utility-first approach.

### ⚙️ Compute & Scalability

- **Amazon EC2 (Elastic Compute Cloud)**  
  We aim to introduce **EC2 instances** for workloads requiring persistent compute environments, such as background batch processing, analytics, or scalable backend services that exceed **Lambda’s execution limits**.

- **Amazon ECS / EKS (Containerization)**  
  Future containerization of services using **Amazon ECS (Elastic Container Service)** or **EKS (Elastic Kubernetes Service)** will enable microservice-based architecture. This shift would allow for:
  - Easier scaling and deployment of modular services
  - Improved development workflows using **Docker**
  - Enhanced CI/CD pipelines and version control over runtime environments

- **AWS Lambda@Edge**  
  To reduce latency and enhance performance, **Lambda@Edge** will be used to run code closer to the user’s location, improving content delivery and real-time data processing for end users.

### 🧠 Machine Learning & Data Intelligence

- **Amazon SageMaker**  
  To support future data-driven decision-making, we plan to explore **Amazon SageMaker** for building and deploying machine learning models. Possible use cases include:
  - Predicting high-need zones for resource allocation
  - Automating categorization of relief requests
  - Prioritization models for volunteer assignments

- **Amazon Comprehend**  
  We may implement **Amazon Comprehend** for natural language processing (NLP) to analyze and categorize user-submitted relief requests, enabling more efficient prioritization and response.

### 🔐 Advanced Security & Compliance

- **AWS WAF Advanced & AWS Shield Advanced**  
  As public traffic increases, we may upgrade to **Advanced WAF rules** and **Shield Advanced** for enhanced threat detection, custom mitigation, and 24/7 DDoS response support.

- **AWS Secrets Manager**  
  **AWS Secrets Manager** will be used to securely store and manage sensitive credentials, such as API keys and database passwords, ensuring that sensitive information is handled securely.

- **AWS Organizations & Control Tower**  
  For larger deployments or multi-team collaboration, **AWS Organizations** and **Control Tower** could be introduced to centrally govern security, compliance, and billing across multiple accounts.

### 📈 Data Warehousing & Analytics

- **Amazon Redshift / Athena**  
  For future data reporting and business intelligence, we anticipate using **Amazon Redshift** or **Amazon Athena** to run complex queries across archived relief and volunteer data.

### 🔄 Infrastructure Automation & CI/CD

- **AWS CodePipeline / CodeBuild**  
  Introducing infrastructure automation through **AWS CodePipeline**, **CodeBuild**, and related services will streamline updates, automate deployments, and enable **DevOps** best practices.

---

These enhancements will help **UnitedRelief** support larger operational scale, reduce manual workload, and enable intelligent response strategies—all while maintaining security, governance, and cost-efficiency as the platform grows.

#### Preview of whats to come.

![Sneak Peak](/client/assets/images/upgrade-2.png)

---

## 👥 Project Contributors

We’re a multidisciplinary team of developers and cloud engineers committed to scalable and impactful technology.

| Name                                                        | Role                        |
|-------------------------------------------------------------|-----------------------------|
| [**Sauel Almonte**](https://www.linkedin.com/in/sauel-almonte/) | (**Lead**) Full-Stack Engineer & AWS Cloud Solutions Architect |
| [**Imran Masud**](https://www.linkedin.com/in/imran-masud-im/) | Backend Engineer (AWS Lambda & Python) |
| [**Ahmet Aygun**](https://www.linkedin.com/in/ahmet-aygun/) | Frontend Developer (UI/UX with AWS Integration) |
| [**Nathnael Girma**](https://www.linkedin.com/in/nathnael-girma/) | Frontend Developer (UI/UX with AWS Integration) |
| [**Michelle Quashie**](https://www.linkedin.com/in/michellequashie/) | AWS Security Architect (IAM & Secrets Manager) |
| [**Jamaal Foster**](https://www.linkedin.com/in/jamaal-foster/) | AWS Security Architect (Policy Enforcement) |

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
