#!/bin/bash

set -e  # Exit on any command error
set -u  # Exit if any variable is undefined

# === Config ===
LAMBDA_NAME="SubmitReliefRequest"
SRC_FILE="aws/lambda_functions/relief_request.py"
BUILD_DIR="aws/lambda_functions/build/relief_request"
ZIP_PATH="$(pwd)/aws/deployment/relief_request.zip"  # Absolute path is safer
REGION="us-east-1"

echo "📦 Cleaning previous build..."
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "📥 Installing dependencies..."
pip install requests_toolbelt -t "$BUILD_DIR"

echo "📂 Copying source file..."
cp "$SRC_FILE" "$BUILD_DIR/"

echo "🗜️ Packaging Lambda function..."
cd "$BUILD_DIR"
zip -r "$ZIP_PATH" .  # FIX: Use absolute ZIP_PATH to avoid zip path issues
cd - > /dev/null

echo "🚀 Updating Lambda function in AWS..."
aws lambda update-function-code \
  --function-name "$LAMBDA_NAME" \
  --zip-file "fileb://$ZIP_PATH" \
  --region "$REGION"

echo "✅ ReliefRequest Lambda deployment complete."
