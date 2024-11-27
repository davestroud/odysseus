provider "aws" {
  region = "us-east-1"
}

module "environment" {
  source      = "../modules"
  environment = "prod"
  bucket_name = "sagemaker-prod-your-bucket-name"
}

output "prod_s3_bucket_name" {
  value = module.environment.bucket_name
}

output "prod_role_arn" {
  value = module.environment.role_arn
}
