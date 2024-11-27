# SageMaker Autopilot Pipeline Project

## Overview
This project automates the end-to-end machine learning workflow using **AWS SageMaker**, **Docker**, **GitHub Actions**, and **Terraform**. It provides a complete pipeline for data processing, training, deployment, and prediction, with dedicated **development**, **staging**, and **production** environments. The pipeline uses **SageMaker Autopilot** to automatically build and deploy machine learning models.

The key features include:
- **Multi-Environment Support**: Separate configurations for dev, staging, and prod.
- **Feature Store Integration**: Store processed features in **SageMaker Feature Store** for reuse.
- **CI/CD Automation**: Automated workflows using **GitHub Actions**.
- **Infrastructure as Code (IaC)**: Use **Terraform** to create, manage, and deploy AWS infrastructure.
- **Testing**: Integrated **unit**, **integration**, and **end-to-end tests**.

---

## Project Directory Structure

```
sagemaker_automl_project/
├── config/                  # Environment-specific configurations
│   ├── config_dev.py
│   ├── config_staging.py
│   └── config_prod.py
├── main.py                  # Main orchestration script for pipeline execution
├── Dockerfile               # Docker configuration for containerization
├── requirements.txt         # Python dependencies
├── sagemaker_pipeline/      # Scripts for SageMaker pipeline components
│   ├── sagemaker_pipeline.py
│   ├── processing_script.py
│   ├── feature_store.py
├── step_functions/          # Scripts for AWS Step Functions integration
│   ├── state_machine.json
│   └── state_machine.py
├── tests/                   # Unit, integration, and end-to-end tests
│   ├── unit/
│   │   ├── test_config.py
│   │   └── test_feature_store.py
│   ├── integration/
│   │   ├── test_s3_upload.py
│   │   └── test_pipeline_creation.py
│   └── e2e/
│       └── test_full_workflow.py
├── terraform/               # Infrastructure as Code (Terraform)
│   ├── modules/
│   │   ├── s3_bucket/
│   │   └── sagemaker_role/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── backend.tf
│   ├── staging/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── backend.tf
│   └── prod/
│       ├── main.tf
│       ├── variables.tf
│       └── backend.tf
└── .github/                 # CI/CD workflows for GitHub Actions
    └── workflows/
        ├── ci_cd_dev.yml
        ├── ci_cd_staging.yml
        └── ci_cd_prod.yml
```

---

## Step-by-Step Instructions to Create the Project

### **1. Setting Up the Environment**

#### **Prerequisites**
- AWS Account with permissions for SageMaker, ECS, and ECR.
- Docker installed locally.
- GitHub account with repository created for this project.
- Python 3.9+ and pip installed.
- Terraform installed locally.

#### **Clone the Repository**
Start by cloning this GitHub repository to your local machine:
```sh
git clone https://github.com/your-username/sagemaker-automl-pipeline.git
cd sagemaker-automl-pipeline
```

### **2. Python Environment Setup**

#### **Create and Activate Virtual Environment**
Create and activate a virtual environment:
```sh
python3 -m venv env
source env/bin/activate
```

#### **Install Dependencies**
Install the required Python dependencies:
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### **3. Setting Up AWS Infrastructure Using Terraform**

Terraform is used to create AWS resources for each environment: **dev**, **staging**, and **prod**. The `terraform/` directory is structured to have reusable modules and environment-specific configurations.

#### **Initialize and Apply Terraform**
1. **Navigate to the Environment Directory** (e.g., `dev`):
   ```sh
   cd terraform/dev
   terraform init
   ```
2. **Apply Terraform Configurations**:
   ```sh
   terraform apply
   ```
   - This command will create resources such as an S3 bucket and IAM roles.
   - Follow similar steps for **staging** and **prod** by navigating to their respective directories (`terraform/staging/` and `terraform/prod/`) and running the same commands.

**Note**: The **backend.tf** files store the Terraform state in dedicated S3 buckets for each environment.

### **4. Dockerization**

The project uses Docker to containerize the Python environment, ensuring consistency across deployments.

#### **Build Docker Image**
```sh
docker build -t sagemaker_pipeline_app .
```

#### **Run Docker Container**
```sh
docker run --name sagemaker_pipeline_container -d sagemaker_pipeline_app
```

### **5. Configuring GitHub Actions for CI/CD**

The **GitHub Actions workflows** in `.github/workflows/` automate the **build**, **test**, and **deployment** processes for each environment.

#### **Set Up GitHub Secrets**
- Go to your GitHub repository and navigate to **Settings** > **Secrets and Variables** > **Actions**.
- Add the following secrets:
  - **`AWS_ACCESS_KEY_ID`**
  - **`AWS_SECRET_ACCESS_KEY`**
  - **`AWS_ACCOUNT_ID`**
  - **`DOCKER_USERNAME`** and **`DOCKER_PASSWORD`**

These secrets are used by the workflows to authenticate with AWS and Docker Hub.

### **6. Running GitHub Actions Workflows**

The workflows are structured to handle different environments:

- **Development (`ci_cd_dev.yml`)**:
  - Runs unit and integration tests.
  - Builds and pushes a Docker image to Docker Hub.

- **Staging (`ci_cd_staging.yml`)**:
  - Deploys the container to an **AWS ECS** staging cluster for validation.

- **Production (`ci_cd_prod.yml`)**:
  - Deploys the final version to the **production ECS cluster**.

Workflows are automatically triggered when code is pushed to the respective branch (e.g., `dev`, `staging`, `main`).

### **7. Testing the Project**

Testing is crucial for ensuring that the project runs smoothly.

#### **Run Unit Tests**
To run the unit tests locally:
```sh
pytest tests/unit/
```

#### **Run Integration Tests**
To run integration tests:
```sh
pytest tests/integration/
```

#### **Run End-to-End Tests**
To validate the entire workflow, run:
```sh
pytest tests/e2e/
```

### **8. Running the Project**

The `main.py` file is the entry point for running the complete workflow, from uploading the dataset to deploying the model. Make sure you set the **`ENV`** variable appropriately:

#### **Run with the Development Configuration**
```sh
export ENV=dev
python main.py
```

### **Explanation of Key Files and Folders**

- **`config/`**: Contains configuration files specific to **dev**, **staging**, and **prod**. These define parameters like **S3 bucket names**, **instance types**, and **IAM roles**.
  
- **`main.py`**: The core script that orchestrates data upload, feature ingestion, pipeline creation, and model deployment using the environment-specific configuration.

- **`Dockerfile`**: Defines the steps to containerize the application, including copying the project and installing the dependencies.

- **`sagemaker_pipeline/`**:
  - **`sagemaker_pipeline.py`**: Defines the SageMaker pipeline using the **SageMaker SDK**.
  - **`processing_script.py`**: Handles the data preprocessing step before training.
  - **`feature_store.py`**: Manages the creation of **Feature Groups** in **SageMaker Feature Store**.

- **`terraform/`**: Provides infrastructure management via **Terraform**.
  - **`modules/`**: Reusable Terraform modules for S3 buckets and IAM roles.
  - **`dev/`, `staging/`, `prod/`**: Environment-specific configurations for deploying infrastructure in AWS.

- **`tests/`**:
  - **`unit/`**: Tests for individual components like configuration values and feature store functions.
  - **`integration/`**: Tests for interactions with AWS resources (e.g., uploading to S3, creating SageMaker pipelines).
  - **`e2e/`**: Runs the entire workflow from start to finish to validate all components.

- **`.github/workflows/`**: Contains GitHub Actions workflows for **CI/CD** to automate testing, building, and deploying across environments.
  - **`ci_cd_dev.yml`**: Triggers on pushes to the `dev` branch.
  - **`ci_cd_staging.yml`**: Triggers on pushes to the `staging` branch.
  - **`ci_cd_prod.yml`**: Triggers on pushes to the `main` branch.

### **Creating the Infrastructure Manually**

If you're not using Terraform for setting up the infrastructure, you'll need to:

1. **Create an S3 Bucket** for each environment for storing raw data and model artifacts.
2. **Create IAM Roles** for SageMaker with sufficient permissions to access S3 and other AWS resources.
3. **Create an ECS Cluster** for staging and production environments to deploy the Dockerized container.

### **Tips for Success**

- **Branching Strategy**: Use branches like **dev**, **staging**, and **main** for different stages of development.
- **Testing Before Deployment**: Ensure that all tests pass before deploying to staging or production.
- **Logging and Monitoring**: Set up **CloudWatch Logs** and alarms to monitor the status of your pipelines and deployments.
- **Security Best Practices**: Store sensitive information in AWS **Secrets Manager** or **GitHub Secrets**.

---

### **Conclusion**

This project provides an end-to-end ML pipeline setup that leverages AWS services, containerization, CI/CD automation, and Infrastructure as Code, which makes it highly scalable, maintainable, and production-ready.

By following the detailed instructions above, you can recreate, extend, and adapt this project for your specific machine learning needs, ensuring that all components—from data ingestion to deployment—are automated and properly tested across environments.

Feel free to reach out via GitHub Issues if you have questions, run into issues, or have suggestions to improve this project further. Happy coding and automating your ML workf