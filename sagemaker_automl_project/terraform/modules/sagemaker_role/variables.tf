variable "environment" {
  description = "Environment name (dev/staging/prod)"
  type        = string
}

variable "bucket_name" {
  description = "Name of the associated S3 bucket"
  type        = string
}
