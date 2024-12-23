terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket-prod"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks-prod"
    encrypt        = true
  }
}
