terraform {
  backend "s3" {
    bucket = "terraform-staging-state-bucket"
    key    = "staging/terraform.tfstate"
    region = "us-east-1"
  }
}
