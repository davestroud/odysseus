# automl_job.py

import boto3
from sagemaker import AutoML, AutoMLInput
from sagemaker.session import Session
from logger import logger
import config

sagemaker_session = Session(boto_session=boto3.Session(region_name=config.REGION))

def create_automl_job(s3_input_uri, role, output_path):
    logger.info("Creating SageMaker Autopilot job...")
    automl = AutoML(
        role=role,
        target_attribute_name=config.TARGET_COLUMN,
        sagemaker_session=sagemaker_session,
        output_path=output_path
    )
    automl_input = AutoMLInput(
        inputs=s3_input_uri,
        target_attribute_name=config.TARGET_COLUMN,
        compression="None",
        content_type="text/csv"  # Adjust if using TSV
    )
    automl.fit(automl_input)
    logger.info("SageMaker Autopilot job created successfully.")
    return automl
