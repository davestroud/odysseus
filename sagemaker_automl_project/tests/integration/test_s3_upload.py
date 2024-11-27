import pytest
from moto import mock_s3
import boto3
from dataset import upload_dataset

@mock_s3
def test_upload_to_s3():
    # Mock S3
    bucket_name = "test-bucket"
    prefix = "test-prefix"
    s3 = boto3.client('s3', region_name="us-east-1")
    s3.create_bucket(Bucket=bucket_name)

    # Write sample data to temporary CSV file
    dataset_path = "/tmp/test_data.csv"
    with open(dataset_path, "w") as f:
        f.write("column1,column2\n1,2\n3,4")

    # Upload dataset and assert the output URI
    s3_uri = upload_dataset(dataset_path, bucket_name, prefix)
    assert s3_uri == f"s3://{bucket_name}/{prefix}/test_data.csv"

    # Verify the data in S3
    obj = s3.get_object(Bucket=bucket_name, Key=f"{prefix}/test_data.csv")
    content = obj['Body'].read().decode('utf-8')
    assert "column1,column2\n1,2\n3,4" in content
