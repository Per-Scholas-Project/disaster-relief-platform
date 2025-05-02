#!/bin/bash

# === PATH CONFIGURATION ===
ROOT_DIR="aws/lambda_functions"
DEPLOY_DIR="aws/deployment"
BUILD_DIR="${DEPLOY_DIR}/lambda_build"

RELIEF_FUNC_NAME="SubmitReliefRequest"
VOLUNTEER_FUNC_NAME="SubmitVolunteerForm"

# === CLEAN PREVIOUS BUILD ===
rm -rf server/${BUILD_DIR}
mkdir -p server/${BUILD_DIR}

# === INSTALL DEPENDENCIES INTO BUILD DIR ===
python3 -m pip install -r server/requirements.txt -t server/${BUILD_DIR}/

# === PACKAGE RELIEF REQUEST FUNCTION ===
cp server/${ROOT_DIR}/relief_request.py server/${BUILD_DIR}/
cp server/${ROOT_DIR}/s3_service.py server/${BUILD_DIR}/
cp server/${ROOT_DIR}/dynamodb_service.py server/${BUILD_DIR}/
cp server/${ROOT_DIR}/__init__.py server/${BUILD_DIR}/

cd server/${BUILD_DIR} || exit 1
zip -r ../relief_request.zip .
rm relief_request.py s3_service.py dynamodb_service.py __init__.py
cd - > /dev/null || exit 1

# === PACKAGE VOLUNTEER FORM FUNCTION ===
cp server/${ROOT_DIR}/volunteer_form.py server/${BUILD_DIR}/
cd server/${BUILD_DIR} || exit 1
zip -r ../volunteer_form.zip .
rm volunteer_form.py
cd - > /dev/null || exit 1

# === CLEANUP TEMP FOLDER ===
rm -rf server/${BUILD_DIR}

# === DEPLOY ZIP FILES TO LAMBDA ===
aws lambda update-function-code \
  --function-name ${RELIEF_FUNC_NAME} \
  --zip-file fileb://server/${DEPLOY_DIR}/relief_request.zip

aws lambda update-function-code \
  --function-name ${VOLUNTEER_FUNC_NAME} \
  --zip-file fileb://server/${DEPLOY_DIR}/volunteer_form.zip

echo "✅ Lambda functions deployed successfully."
