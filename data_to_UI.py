import boto3
import json

# Create an SQS client
sqs = boto3.client('sqs')

# Get the queue URL (replace with your actual queue URL)
queue_url = 'https://sqs.ap-south-1.amazonaws.com/730335673331/project-queue'

# Create your message data (can be anything serializable to JSON)
message_data = {
    'product_id': 1,
    'product_name': "whiteboard",
    'quantity': 10,
    'price': 100,
    'discount': 20,
    'category': 'education',
    'retailStock': "sdd"
}

# Send the message
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(message_data)
)

# Print the unique message ID
print(response['MessageId'])
