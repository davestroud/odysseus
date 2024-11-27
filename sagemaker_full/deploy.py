# deploy.py

import boto3
from sagemaker.predictor import Predictor
from sagemaker.deserializers import JSONDeserializer
from sagemaker.serializers import JSONSerializer
from logger import logger
import config

def deploy_best_model(automl_job_name, sagemaker_session):
    logger.info("Retrieving the best candidate model...")
    sm_client = boto3.client("sagemaker", region_name=config.REGION)

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
        ExecutionRoleArn=config.ROLE_ARN,
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
