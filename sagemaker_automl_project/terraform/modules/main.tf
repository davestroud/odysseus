# Create a base module with common configurations
variable "environment" {
  type = string
}

variable "bucket_name" {
  type = string
}

module "s3_bucket" {
  source      = "./s3_bucket"
  bucket_name = var.bucket_name
  environment = var.environment
}

module "sagemaker_role" {
  source      = "./sagemaker_role"
  bucket_name = module.s3_bucket.bucket_name
  environment = var.environment
}

output "bucket_name" {
  value = module.s3_bucket.bucket_name
}

output "role_arn" {
  value = module.sagemaker_role.role_arn
}

# Common resource definitions 