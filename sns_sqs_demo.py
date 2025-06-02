
import boto3
import time

sns = boto3.client('sns')
sqs = boto3.client('sqs')

SNS_TOPIC_ARN = '<your_sns_topic_arn>'
SQS_QUEUE_URL = '<your_sqs_queue_url>'

message = "Hello from boto3!"
response = sns.publish(
    TopicArn=SNS_TOPIC_ARN,
    Message=message,
    Subject='Demo'
)
print(f"Message sent to SNS: {response['MessageId']}")

print("Waiting for message to arrive in SQS...")
time.sleep(5)

msgs = sqs.receive_message(
    QueueUrl=SQS_QUEUE_URL,
    MaxNumberOfMessages=1,
    VisibilityTimeout=30,
    WaitTimeSeconds=1
)

if "Messages" in msgs:
    print("Message received in SQS (in-flight):")
    print(msgs["Messages"][0]["Body"])
else:
    print("No messages found in SQS.")
