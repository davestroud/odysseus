# sagemaker_pipeline.py

import sagemaker
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.processing import ScriptProcessor
from sagemaker.sklearn import SKLearn
from sagemaker.inputs import TrainingInput
from sagemaker.workflow.parameters import ParameterString, ParameterInteger
import boto3

# Define parameters
region = "us-east-1"
role = "arn:aws:iam::123456789012:role/AmazonSageMaker-ExecutionRole"
sagemaker_session = sagemaker.Session()

bucket = "sagemaker-your-bucket-name"
processing_instance_type = ParameterString(name="ProcessingInstanceType", default_value="ml.m5.xlarge")
training_instance_type = ParameterString(name="TrainingInstanceType", default_value="ml.m5.xlarge")

# Processing Step (e.g., data cleaning)
sklearn_processor = ScriptProcessor(
    image_uri=SKLearn.get_image_uri(region, "0.23-1"),
    role=role,
    instance_type="ml.m5.xlarge",
    instance_count=1,
    command=["python3"],
)

processing_step = ProcessingStep(
    name="DataProcessing",
    processor=sklearn_processor,
    inputs=[sagemaker.processing.ProcessingInput(
        source=f"s3://{bucket}/input_data/",
        destination="/opt/ml/processing/input"
    )],
    outputs=[sagemaker.processing.ProcessingOutput(
        source="/opt/ml/processing/output",
        destination=f"s3://{bucket}/processed_data/"
    )],
    code="processing_script.py"
)

# Training Step (e.g., training a model)
estimator = sagemaker.estimator.Estimator(
    image_uri=sagemaker.image_uris.retrieve("xgboost", region, "1.2-1"),
    role=role,
    instance_count=1,
    instance_type="ml.m5.xlarge",
    output_path=f"s3://{bucket}/model_output/"
)

training_step = TrainingStep(
    name="ModelTraining",
    estimator=estimator,
    inputs={
        "train": TrainingInput(s3_data=f"s3://{bucket}/processed_data/", content_type="text/csv"),
    }
)

# Create Pipeline
pipeline = Pipeline(
    name="MySageMakerPipeline",
    parameters=[processing_instance_type, training_instance_type],
    steps=[processing_step, training_step],
    sagemaker_session=sagemaker_session,
)

# Run the pipeline
if __name__ == "__main__":
    pipeline.upsert(role_arn=role)
    execution = pipeline.start()
    execution.wait()
