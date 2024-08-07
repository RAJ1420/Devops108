import json
import boto3

sns_client = boto3.client('sns')
sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:YourSNSTopic'

def lambda_handler(event, context):
    # Log the received event
    print("Received event: " + json.dumps(event, indent=2))
    
    # Extract bucket name and object key from the event
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Create a message to be sent
        message = f"Object deleted from bucket: {bucket_name}, key: {object_key}"
        
        # Send a notification via SNS
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject='S3 Object Deletion Notification'
        )
        
        print("Notification sent with response: " + json.dumps(response, indent=2))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent!')
    }