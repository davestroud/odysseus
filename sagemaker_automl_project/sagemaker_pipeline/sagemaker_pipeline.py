# sagemaker_pipeline/sagemaker_pipeline.py

from sagemaker.feature_store.inputs import FeatureStoreInput
from sagemaker.estimator import Estimator
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from logger import logger
import config

# Initialize Feature Store
feature_group_name = "MyFeatureGroup"

# Use Feature Store Input for Training
training_step = TrainingStep(
    name="ModelTraining",
    estimator=estimator,
    inputs={
        "train": FeatureStoreInput(feature_group_name=feature_group_name)
    }
)

# Create and define the SageMaker Pipeline
pipeline = Pipeline(
    name="MySageMakerPipelineWithFeatureStore",
    parameters=[processing_instance_type, training_instance_type],
    steps=[processing_step, training_step],
    sagemaker_session=sagemaker_session,
)
