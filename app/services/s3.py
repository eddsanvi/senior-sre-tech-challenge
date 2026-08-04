import boto3

from app.config.settings import (
    AWS_REGION,
    AWS_ENDPOINT_URL,
    S3_BUCKET
)

s3_client = boto3.client(
    "s3",
    endpoint_url=AWS_ENDPOINT_URL,
    region_name=AWS_REGION,
    aws_access_key_id="test",
    aws_secret_access_key="test"
)


def upload_avatar(file):

    s3_client.upload_fileobj(
        file.file,
        S3_BUCKET,
        file.filename
    )

    return (
        f"{AWS_ENDPOINT_URL}/{S3_BUCKET}/{file.filename}"
    )