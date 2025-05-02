#!/bin/bash

STACK_PREFIX="unitedrelief"
REGION="us-east-1"
TEMPLATE_DIR="server/aws/infrastructure"

#echo "Deploying S3 Bucket..."
#aws cloudformation deploy \
#  --stack-name "${STACK_PREFIX}-s3" \
#  --template-file "${TEMPLATE_DIR}/s3_bucket.yaml" \
#  --region ${REGION} \
#  --capabilities CAPABILITY_NAMED_IAM

echo "Deploying DynamoDB Tables..."
aws cloudformation deploy \
  --stack-name "${STACK_PREFIX}-dynamodb" \
  --template-file "${TEMPLATE_DIR}/dynamodb_tables.yaml" \
  --region ${REGION} \
  --capabilities CAPABILITY_NAMED_IAM

echo "Deploying Lambda Functions..."
aws cloudformation deploy \
  --stack-name "${STACK_PREFIX}-lambda" \
  --template-file "${TEMPLATE_DIR}/lambda_functions.yaml" \
  --region ${REGION} \
  --capabilities CAPABILITY_NAMED_IAM

echo "Deploying API Gateway..."
aws cloudformation deploy \
  --stack-name "${STACK_PREFIX}-apigateway" \
  --template-file "${TEMPLATE_DIR}/api_gateway.yaml" \
  --region ${REGION} \
  --capabilities CAPABILITY_NAMED_IAM

# Optional: SES
#if [ -f "${TEMPLATE_DIR}/ses_config.yaml" ]; then
#  echo "Deploying SES Configuration..."
#  aws cloudformation deploy \
#    --stack-name "${STACK_PREFIX}-ses" \
#    --template-file "${TEMPLATE_DIR}/ses_config.yaml" \
#    --region ${REGION} \
#    --capabilities CAPABILITY_NAMED_IAM
#fi

echo "✅ All infrastructure stacks deployed."
