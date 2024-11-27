#!/bin/bash

# Create main project directory structure
mkdir -p sagemaker_automl_project/{config,sagemaker_pipeline,step_functions,tests/{unit,integration,e2e},terraform/{modules/{s3_bucket,sagemaker_role},dev,staging,prod},.github/workflows}

# Create config files
touch sagemaker_automl_project/config/{config_dev.py,config_staging.py,config_prod.py}

# Create main application files
touch sagemaker_automl_project/{main.py,Dockerfile,requirements.txt}

# Create SageMaker pipeline files
touch sagemaker_automl_project/sagemaker_pipeline/{sagemaker_pipeline.py,processing_script.py,feature_store.py}

# Create Step Functions files
touch sagemaker_automl_project/step_functions/{state_machine.json,state_machine.py}

# Create test files
touch sagemaker_automl_project/tests/unit/{test_config.py,test_feature_store.py}
touch sagemaker_automl_project/tests/integration/{test_s3_upload.py,test_pipeline_creation.py}
touch sagemaker_automl_project/tests/e2e/test_full_workflow.py

# Create Terraform files
touch sagemaker_automl_project/terraform/dev/main.tf
touch sagemaker_automl_project/terraform/staging/main.tf
touch sagemaker_automl_project/terraform/prod/main.tf

# Create GitHub workflow files
touch sagemaker_automl_project/.github/workflows/{ci_cd_dev.yml,ci_cd_staging.yml,ci_cd_prod.yml}

# Create README
touch sagemaker_automl_project/README.md 