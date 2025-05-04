#!/bin/bash

TOPIC_ARN="arn:aws:sns:us-east-1:650856831762:unitedrelief-submissions-alerts"

emails=(
  "almontesauel@gmail.com"
  "imranmasud222@gmail.com"
  "Jwfoster860@Gmail.com"
  "getanathan898@gmail.com"
  "ahmetaygunn5@gmail.com"
  "Quashie.michelle7@gmail.com"
)

for email in "${emails[@]}"; do
  echo "Subscribing $email..."
  aws sns subscribe \
    --topic-arn "$TOPIC_ARN" \
    --protocol email \
    --notification-endpoint "$email"
done

echo "✅ Subscription requests sent. Ask each admin to confirm via email."
