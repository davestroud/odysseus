import pytest
from moto import mock_sagemaker
import boto3
from sagemaker_pipeline.sagemaker_pipeline import pipeline
from config.config_dev import ROLE_ARN

@mock_sagemaker
def test_pipeline_creation():
    # Mock SageMaker client
    mock_client = boto3.client('sagemaker', region_name="us-east-1")

    # Test creating/upserting pipeline
    response = pipeline.upsert(role_arn=ROLE_ARN)
    assert response["PipelineArn"].startswith("arn:aws:sagemaker")
