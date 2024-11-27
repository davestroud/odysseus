# main.py

from logger import logger
from dataset import upload_dataset
from automl_job import create_automl_job
from deploy import deploy_best_model
from predict import predict
from sagemaker_pipeline.sagemaker_pipeline import pipeline
from sagemaker_pipeline.feature_store import create_feature_group, ingest_data_to_feature_group
import config
import pandas as pd
from sagemaker.session import Session
import boto3

# Initialize SageMaker Session
region = config.REGION
sagemaker_session = Session(boto_session=boto3.Session(region_name=region))

if __name__ == "__main__":
    try:
        # Data Preparation: Upload Dataset to S3
        logger.info("Starting the SageMaker Autopilot Workflow with Feature Store...")
        s3_dataset_uri = upload_dataset(config.DATASET_PATH, config.BUCKET_NAME, config.PREFIX)

        # Create Feature Group and Ingest Data
        df = pd.read_csv(config.DATASET_PATH)  # Load the dataset into a DataFrame

        # Add record identifier and event timestamp columns
        df[config.RECORD_IDENTIFIER_NAME] = df.index
        df[config.EVENT_TIME_FEATURE_NAME] = pd.to_datetime('now').isoformat()

        # Create Feature Group
        feature_group = create_feature_group(
            feature_group_name=config.FEATURE_GROUP_NAME,
            record_schema=df.columns.tolist(),
            role_arn=config.ROLE_ARN,
            s3_uri=config.S3_URI_FEATURE_STORE
        )

        # Ingest the Data into Feature Store
        ingest_data_to_feature_group(feature_group, df)

        # Create and Run the SageMaker Pipeline
        pipeline.upsert(role_arn=config.ROLE_ARN)
        execution = pipeline.start()
        execution.wait()  # Wait until the pipeline is complete

        # Deployment: Deploy the Best Model from AutoML
        automl_job_name = execution.describe()["PipelineExecutionDisplayName"]
        predictor = deploy_best_model(automl_job_name, sagemaker_session)

        # Make a Prediction
        test_payload = {"feature_1": "value1", "feature_2": "value2"}  # Replace with actual feature names
        prediction = predict(predictor, test_payload)
        logger.info(f"Prediction result: {prediction}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
