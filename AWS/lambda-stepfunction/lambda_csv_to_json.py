import boto3
import csv
import json
import os
from io import StringIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get S3 bucket and object key from event
    bucket = event['bucket']
    key = event['key']
    
    # Get CSV object from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    csv_data = response['Body'].read().decode('utf-8')
    
    # Read CSV into list of dicts
    csv_reader = csv.DictReader(StringIO(csv_data))
    json_data = [row for row in csv_reader]

    # Optional: Log number of records processed
    print(f"Parsed {len(json_data)} records from CSV")

    return json_data  # To be passed to Step Function's Map state
