# sns-sqs-lambda-demo
A demo using AWS SNS, SQS, and Lambda with Terraform

# SNS → SQS → Lambda Integration Demo

This project demonstrates a simple AWS event-driven architecture using **Amazon SNS**, **Amazon SQS**, and **AWS Lambda**, with optional **Terraform** infrastructure as code for setup.

---

## 📁 Project Structure

| File                | Description |
|---------------------|-------------|
| `lambda_function.py` | AWS Lambda function that is triggered by messages in the SQS queue. It logs the message body. |
| `sns_sqs_demo.py`    | Python script using `boto3` to publish a message to SNS and poll for it in SQS. |
| `main.tf`            | Terraform configuration to create and wire up SNS Topic, SQS Queue, and a Lambda trigger. |

---

## 🧠 How It Works

1. **SNS Topic** receives a published message.
2. **SNS** fan-outs the message to the subscribed **SQS Queue**.
3. **Lambda Function** is configured with an SQS trigger and processes incoming messages.

---

## 🚀 Setup Guide

### ✅ Prerequisites

- AWS account and CLI access
- Python 3.x
- `boto3` (`pip install boto3`)
- Terraform (`https://terraform.io`)
- Proper AWS IAM permissions to create and manage SNS, SQS, Lambda

---

## 🛠️ Usage

### 1. Deploy Infrastructure (Optional - with Terraform)

```bash
terraform init
terraform apply
This will provision:

SNS Topic
SQS Queue
Lambda Function with IAM Role
SNS-to-SQS subscription
SQS trigger for Lambda

⚠️ Replace placeholders (e.g., <your_sns_topic_arn>) in main.tf before applying.

2. Run the Publisher Script
In sns_sqs_demo.py, replace:

python
SNS_TOPIC_ARN = '<your_sns_topic_arn>'
SQS_QUEUE_URL = '<your_sqs_queue_url>'
Then run:

bash
python sns_sqs_demo.py
You should see logs like:

text
Message sent to SNS: <message-id>
Waiting for message to arrive in SQS...
Message received in SQS (in-flight):
Hello from boto3!
3. Lambda Function
The function is defined in lambda_function.py:

python
def lambda_handler(event, context):
    for record in event['Records']:
        print("Received message from SQS:", record['body'])
It prints incoming message bodies from the SQS queue.

📌 Notes
Messages not successfully processed by Lambda are automatically retried.
Terraform can be extended to include Dead Letter Queues, alarms, or environment variables.
Make sure the Lambda role has permissions to read from SQS and write logs to CloudWatch.

📄 License
MIT License – use freely, modify responsibly.

🙌 Author
Created by Zeeshan Shah Syed LinkedIn: https://www.linkedin.com/in/syed-s-2a3638264/ | Zeeshanshahsyed14@gmail.com
For demo/testing/development purposes only.
