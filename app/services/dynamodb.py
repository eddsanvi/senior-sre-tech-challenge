import boto3

from app.config.settings import (
    AWS_REGION,
    AWS_ENDPOINT_URL,
    DYNAMODB_TABLE
)

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=AWS_ENDPOINT_URL,
    region_name=AWS_REGION,
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

table = dynamodb.Table(DYNAMODB_TABLE)


def save_user(user):

    table.put_item(Item=user)


def get_users():

    response = table.scan()

    return response.get("Items", [])