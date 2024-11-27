# sagemaker_pipeline/feature_store.py

import time
import boto3
import sagemaker
from sagemaker.feature_store.feature_group import FeatureGroup
from sagemaker.session import Session
from logger import logger
import config

# Initialize SageMaker session and Feature Store client
region = config.REGION
sagemaker_session = Session(boto_session=boto3.Session(region_name=region))
featurestore_client = boto3.client("sagemaker-featurestore-runtime", region_name=region)

# Function to create a Feature Group
def create_feature_group(feature_group_name, record_schema, role_arn, s3_uri):
    feature_group = FeatureGroup(name=feature_group_name, sagemaker_session=sagemaker_session)

    # Define Feature Group schema and configuration
    feature_group.create(
        s3_uri=s3_uri,
        record_identifier_name="record_id",  # Unique identifier for each record
        event_time_feature_name="event_time",  # Timestamp feature
        role_arn=role_arn,
        enable_online_store=True,
        description="Feature group for storing processed features for ML",
    )
    logger.info(f"Feature Group '{feature_group_name}' created successfully.")

    # Wait until the feature group is in 'Created' state
    while feature_group.describe().get("FeatureGroupStatus") != "Created":
        logger.info("Waiting for Feature Group to be created...")
        time.sleep(5)
    
    return feature_group

# Function to ingest data into Feature Group
def ingest_data_to_feature_group(feature_group, data_frame):
    feature_group.ingest(data_frame, max_workers=3, wait=True)
    logger.info(f"Data ingested into Feature Group '{feature_group.name}' successfully.")
