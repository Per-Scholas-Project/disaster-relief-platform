#!/bin/bash

set -e  # Exit on error
set -u  # Exit if variable is undefined

# === Config ===
LAMBDA_NAME="SubmitVolunteerForm"
SRC_FILE="aws/lambda_functions/volunteer_form.py"
BUILD_DIR="aws/lambda_functions/build/volunteer_form"
ZIP_PATH="aws/deployment/volunteer_form.zip"
REGION="us-east-1"

echo "📦 Cleaning previous build..."
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "📂 Copying source file..."
cp "$SRC_FILE" "$BUILD_DIR/"

echo "🗜️ Packaging Lambda function..."
cd "$BUILD_DIR"
zip -r "../../../deployment/volunteer_form.zip" .
cd - > /dev/null

echo "🚀 Updating Lambda function in AWS..."
aws lambda update-function-code \
  --function-name "$LAMBDA_NAME" \
  --zip-file "fileb://$ZIP_PATH" \
  --region "$REGION"

echo "✅ VolunteerForm Lambda deployment complete."
