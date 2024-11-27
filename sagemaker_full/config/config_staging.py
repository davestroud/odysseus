# Staging environment configuration

BUCKET_NAME = "sagemaker-staging-{account-id}"
PREFIX = "sagemaker/autopilot-demo"
REGION = "us-east-1"
ROLE_ARN = "arn:aws:iam::{account-id}:role/service-role/AmazonSageMaker-ExecutionRole-Staging"
DATASET_PATH = "data/amazon_reviews_us_Digital_Software_v1_00.tsv"
TARGET_COLUMN = "star_rating"

# Staging specific configurations
DEBUG = False
LOG_LEVEL = "INFO" 