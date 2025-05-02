#!/bin/bash

# === CONFIGURATION ===
STACK_PREFIX="unitedrelief"
REGION="us-east-1"

# === DEPLOY S3 BUCKET ===
echo "🚀 Deploying S3 Bucket..."
aws cloudformation deploy \
  --stack-name "${STACK_PREFIX}-s3" \
  --template-file s3_bucket.yaml \
  --region ${REGION} \
  --capabilities CAPABILITY_NAMED_IAM

# === DEPLOY DynamoDB Tables ===
echo "📦 Deploying DynamoDB Tables..."
aws cloudformation deploy \
  --stack-name "${STACK_PREFIX}-dynamodb" \
  --template-file dynamodb_tables.yaml \
  --region ${REGION} \
  --capabilities CAPABILITY_NAMED_IAM

# === DEPLOY Lambda Functions and IAM Roles ===
echo "🧠 Deploying Lambda Functions..."
aws cloudformation deploy \
  --stack-name "${STACK_PREFIX}-lambda" \
  --template-file lambda_functions.yaml \
  --region ${REGION} \
  --capabilities CAPABILITY_NAMED_IAM

# === DEPLOY API Gateway ===
echo "🌐 Deploying API Gateway..."
aws cloudformation deploy \
  --stack-name "${STACK_PREFIX}-apigateway" \
  --template-file api_gateway.yaml \
  --region ${REGION} \
  --capabilities CAPABILITY_NAMED_IAM

echo "✅ All stacks deployed successfully!"
