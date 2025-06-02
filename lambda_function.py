
import json

def lambda_handler(event, context):
    for record in event['Records']:
        print("Received message from SQS:", record['body'])
    return {"statusCode": 200}
