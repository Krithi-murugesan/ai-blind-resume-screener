import boto3
from langchain_aws import ChatBedrock

def get_bedrock_llm():
    """Returns the cost-effective Claude 3 Haiku model."""
    return ChatBedrock(
        model_id="anthropic.claude-3-haiku-20240307-v1:0",
        model_kwargs={"temperature": 0},
        region_name="us-east-1"
    )

def save_to_dynamodb(table_name, item):
    """Saves the screening report to DynamoDB."""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    return table.put_item(Item=item)
