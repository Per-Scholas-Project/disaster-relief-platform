import json
import logging
from service import Service

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Instantiate the service
aid_service = Service()

def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")

        http_method = event.get("httpMethod")
        if not http_method:
            logger.error("HTTP method is missing in the request")
            return format_response(400, {"message": "HTTP method is required"})

        body = event.get("body", "{}")
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                logger.error("Invalid JSON in request body")
                return format_response(400, {"message": "Invalid JSON in request body"})

        # Route based on method
        if http_method == "POST":
            logger.info("Processing POST request")
            response = aid_service.submit_aid_request(body)
            return format_response(response["statusCode"], response)

        elif http_method == "GET":
            logger.info("Processing GET request")
            response = aid_service.get_all_requests()
            return format_response(response["statusCode"], response)

        else:
            logger.warning(f"Unsupported HTTP method: {http_method}")
            return format_response(405, {"message": f"Method {http_method} not allowed"})

    except Exception as e:
        logger.exception("An unexpected error occurred")
        return format_response(500, {"message": "Internal server error", "error": str(e)})

def format_response(status_code, body):
    return {
        "statusCode": status_code,
        "body": json.dumps(body) if isinstance(body, dict) else body,
        "headers": {"Content-Type": "application/json"}
    }
