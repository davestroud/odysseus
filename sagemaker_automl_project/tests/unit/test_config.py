import pytest
import config.config_dev as config_dev
import config.config_staging as config_staging
import config.config_prod as config_prod

# Test Dev Config
def test_dev_config():
    assert config_dev.REGION == "us-east-1"
    assert config_dev.ROLE_ARN.startswith("arn:aws:iam")
    assert "dev" in config_dev.BUCKET_NAME

# Test Staging Config
def test_staging_config():
    assert config_staging.REGION == "us-east-1"
    assert config_staging.ROLE_ARN.startswith("arn:aws:iam")
    assert "staging" in config_staging.BUCKET_NAME

# Test Prod Config
def test_prod_config():
    assert config_prod.REGION == "us-east-1"
    assert config_prod.ROLE_ARN.startswith("arn:aws:iam")
    assert "prod" in config_prod.BUCKET_NAME
