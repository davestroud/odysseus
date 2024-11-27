terraform {
  backend "s3" {
    bucket = "terraform-dev-state-bucket"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}
