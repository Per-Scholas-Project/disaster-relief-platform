#!/bin/bash

set -e  # Exit on any command error
set -u  # Exit if any variable is undefined

# === Config ===
LAMBDA_NAME="GeneratePreSignedUrl"  # ✅ FIXED: Match CloudFormation name exactly
SRC_FILE="aws/lambda_functions/generate_presigned_url.py"
BUILD_DIR="aws/lambda_functions/build/generate_presigned_url"
ZIP_PATH="$(pwd)/aws/deployment/generate_presigned_url.zip"  # Absolute path is safer
REGION="us-east-1"

echo "📦 Cleaning previous build..."
rm -rf "$BUILD_DIR" "$ZIP_PATH"
mkdir -p "$BUILD_DIR"

echo "📂 Copying Lambda source..."
cp "$SRC_FILE" "$BUILD_DIR/"

echo "🗜️ Packaging Lambda ZIP..."
cd "$BUILD_DIR"
zip -r "$ZIP_PATH" .
cd - > /dev/null

echo "🚀 Uploading ZIP to Lambda..."
aws lambda update-function-code \
  --function-name "$LAMBDA_NAME" \
  --zip-file "fileb://$ZIP_PATH" \
  --region "$REGION"

echo "✅ GeneratePreSignedUrl Lambda deployment complete."
