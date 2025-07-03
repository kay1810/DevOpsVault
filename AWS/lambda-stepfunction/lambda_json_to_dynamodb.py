import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    print(f"Inserting item: {event}")
    
    try:
        table.put_item(Item=event)
        return {
            'statusCode': 200,
            'body': f"Successfully inserted item with id: {event.get('id')}"
        }
    except Exception as e:
        print(f"Error inserting item: {e}")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
