provider "aws" {
  region = "us-east-1"
}

module "s3_bucket" {
  source      = "../modules/s3_bucket"
  bucket_name = "sagemaker-staging-your-bucket-name"
  environment = "staging"
}

module "sagemaker_role" {
  source      = "../modules/sagemaker_role"
  bucket_name = module.s3_bucket.bucket_name
  environment = "staging"
}

output "staging_s3_bucket_name" {
  value = module.s3_bucket.bucket_name
}

output "staging_role_arn" {
  value = module.sagemaker_role.role_arn
}
