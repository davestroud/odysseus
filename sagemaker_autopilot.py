import boto3
import sagemaker
from sagemaker import AutoML, AutoMLInput
from sagemaker.session import Session
from sagemaker.s3 import S3Uploader
from sagemaker.predictor import Predictor
from sagemaker.deserializers import JSONDeserializer
from sagemaker.serializers import JSONSerializer

import os
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurable Constants
BUCKET_NAME = "sagemaker-us-east-1-022398263250"
PREFIX = "sagemaker/autopilot-demo"
REGION = "us-east-1"
ROLE_ARN = "arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole"
DATASET_PATH = "/Users/davidstroud/Downloads/amazon_reviews_us_Digital_Software_v1_00.tsv"
TARGET_COLUMN = "star_rating"  # Update this to match your dataset

# AWS Sessions
sagemaker_session = Session(boto_session=boto3.Session(region_name=REGION))
s3_client = boto3.client('s3', region_name=REGION)

# Upload dataset to S3
def upload_dataset(dataset_path, bucket, prefix):
    """
    Upload dataset to S3.
    """
    logger.info("Uploading dataset to S3...")
    s3_uri = S3Uploader.upload(
        local_path=dataset_path, 
        desired_s3_uri=f"s3://{bucket}/{prefix}",
        sagemaker_session=sagemaker_session
    )
    logger.info(f"Dataset uploaded to {s3_uri}")
    return s3_uri


# Create Autopilot Job
def create_automl_job(s3_input_uri, role, output_path):
    """
    Create a SageMaker Autopilot job.
    """
    logger.info("Creating SageMaker Autopilot job...")
    automl = AutoML(
        role=role,
        target_attribute_name=TARGET_COLUMN,
        sagemaker_session=sagemaker_session,
        output_path=output_path
    )
    automl_input = AutoMLInput(
        inputs=s3_input_uri,
        target_attribute_name=TARGET_COLUMN,
        compression="None",
        content_type="text/csv"  # Adjust if using TSV
    )
    automl.fit(automl_input)
    logger.info("SageMaker Autopilot job created successfully.")
    return automl

# Deploy Best Model
def deploy_best_model(automl_job_name):
    """
    Deploy the best model from the AutoML job.
    """
    logger.info("Retrieving the best candidate model...")
    sm_client = boto3.client("sagemaker", region_name=REGION)

    # Describe the AutoML job to get the best candidate
    response = sm_client.describe_auto_ml_job(AutoMLJobName=automl_job_name)
    best_candidate = response["BestCandidate"]

    # Create a model from the best candidate
    model_name = best_candidate["CandidateName"]
    sm_client.create_model(
        ModelName=model_name,
        PrimaryContainer={
            "Image": best_candidate["InferenceContainers"][0]["Image"],
            "ModelDataUrl": best_candidate["InferenceContainers"][0]["ModelDataUrl"],
        },
        ExecutionRoleArn=ROLE_ARN,
    )
    logger.info(f"Best candidate model '{model_name}' created successfully.")

    # Deploy the model
    endpoint_name = f"{model_name}-endpoint"
    sm_client.create_endpoint_config(
        EndpointConfigName=endpoint_name,
        ProductionVariants=[
            {
                "VariantName": "AllTraffic",
                "ModelName": model_name,
                "InstanceType": "ml.m5.large",
                "InitialInstanceCount": 1
            }
        ]
    )
    sm_client.create_endpoint(
        EndpointName=endpoint_name,
        EndpointConfigName=endpoint_name
    )
    logger.info(f"Endpoint '{endpoint_name}' is being created. Waiting for it to be InService...")

    # Wait for endpoint to be InService
    sm_client.get_waiter("endpoint_in_service").wait(EndpointName=endpoint_name)
    logger.info(f"Endpoint '{endpoint_name}' is now InService.")

    # Return the predictor
    predictor = Predictor(
        endpoint_name=endpoint_name,
        sagemaker_session=sagemaker_session,
    )
    predictor.serializer = JSONSerializer()
    predictor.deserializer = JSONDeserializer()
    logger.info("Best model deployed successfully.")
    return predictor

# Prediction Function
def predict(predictor, payload):
    """
    Make a prediction using the deployed model.
    """
    logger.info("Making a prediction...")
    response = predictor.predict(payload)
    logger.info(f"Prediction: {response}")
    return response

# Main Execution
if __name__ == "__main__":
    try:
        # Data Preparation
        logger.info("Starting the SageMaker Autopilot Workflow...")
        s3_dataset_uri = upload_dataset(DATASET_PATH, BUCKET_NAME, PREFIX)

        # Model Training
        output_path = f"s3://{BUCKET_NAME}/{PREFIX}/output"
        automl = create_automl_job(s3_dataset_uri, ROLE_ARN, output_path)

        # Wait for the Autopilot job to complete
        automl_job_name = automl.latest_auto_ml_job.name
        logger.info(f"Waiting for Autopilot job '{automl_job_name}' to complete...")
        sagemaker_session.wait_for_auto_ml_job(automl_job_name)

        # Deployment
        predictor = deploy_best_model(automl_job_name)

        # Prediction Example
        test_payload = {"feature_1": "value1", "feature_2": "value2"}  # Replace with actual feature names
        prediction = predict(predictor, test_payload)
        logger.info(f"Prediction result: {prediction}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
