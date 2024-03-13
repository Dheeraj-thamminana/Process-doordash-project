import json
import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        response = s3.get_object(Bucket=bucket, Key=key)
        
        # Read data into pandas DataFrame
        df = pd.read_json(response['Body'], lines=True)
        
        # Filter records where status is 'delivered'
        delivered_df = df[df['status'] == 'delivered']
        
        # Convert DataFrame to JSON string
        delivered_json = delivered_df.to_json(orient='records', lines=True)
        
        # Write the filtered data to the target S3 bucket
        s3.put_object(Bucket='doordash-target-zn', Key=key, Body=delivered_json)
        
        # Publish a success message to the SNS topic
        sns.publish(TopicArn='arn:aws:sns:region:account-id:doordash-notification', Message='Delivery data processed successfully.', Subject='Delivery Data Processing')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
