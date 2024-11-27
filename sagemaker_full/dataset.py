# dataset.py

from sagemaker.s3 import S3Uploader
from sagemaker.session import Session
from logger import logger
import boto3
import config

sagemaker_session = Session(boto_session=boto3.Session(region_name=config.REGION))

def upload_dataset(dataset_path, bucket, prefix):
    logger.info("Uploading dataset to S3...")
    s3_uri = S3Uploader.upload(
        local_path=dataset_path, 
        desired_s3_uri=f"s3://{bucket}/{prefix}",
        sagemaker_session=sagemaker_session
    )
    logger.info(f"Dataset uploaded to {s3_uri}")
    return s3_uri
