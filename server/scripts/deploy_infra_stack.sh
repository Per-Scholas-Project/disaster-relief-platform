#!/bin/bash

set -e  # Exit on any error
set -u  # Treat unset variables as errors

# === Config ===
STACK_PREFIX="unitedrelief"
TEMPLATE_DIR="aws/infrastructure"
CODE_BUCKET="unitedrelief-submissions"

echo "🚀 Deploying UnitedRelief infrastructure stacks..."

# === S3 Bucket ===
echo "📦 Deploying S3 bucket..."
aws cloudformation deploy \
  --stack-name ${STACK_PREFIX}-s3 \
  --template-file ${TEMPLATE_DIR}/s3_bucket.yaml \
  --capabilities CAPABILITY_NAMED_IAM

# === DynamoDB Tables ===
echo "🗃️ Deploying DynamoDB tables..."
aws cloudformation deploy \
  --stack-name ${STACK_PREFIX}-dynamodb \
  --template-file ${TEMPLATE_DIR}/dynamodb_tables.yaml \
  --capabilities CAPABILITY_NAMED_IAM

# === IAM Role for Lambda ===
echo "🔐 Deploying IAM role..."
aws cloudformation deploy \
  --stack-name ${STACK_PREFIX}-iam-role \
  --template-file ${TEMPLATE_DIR}/iam_lambda_role.yaml \
  --capabilities CAPABILITY_NAMED_IAM

# === Lambda Functions ===
echo "🧠 Deploying Lambda functions..."
aws cloudformation deploy \
  --stack-name ${STACK_PREFIX}-lambda \
  --template-file ${TEMPLATE_DIR}/lambda_functions.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides CodeBucket=${CODE_BUCKET}

# === API Gateway ===
echo "🌐 Deploying API Gateway..."
aws cloudformation deploy \
  --stack-name ${STACK_PREFIX}-apigateway \
  --template-file ${TEMPLATE_DIR}/api_gateway.yaml \
  --capabilities CAPABILITY_NAMED_IAM

# === Presigned URL Lambda ===
echo "🔑 Deploying Presigned URL Lambda..."
aws cloudformation deploy \
  --stack-name ${STACK_PREFIX}-presigned-url \
  --template-file ${TEMPLATE_DIR}/lambda_generate_presigned_url.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides CodeBucket=${CODE_BUCKET}

echo "✅ All UnitedRelief infrastructure stacks deployed successfully."
