import pytest
from sagemaker_pipeline.feature_store import create_feature_group
from unittest.mock import MagicMock

def test_create_feature_group():
    # Mock the FeatureGroup to simulate creation
    mock_feature_group = MagicMock()
    mock_feature_group.create.return_value = True

    # Test the feature group creation
    feature_group_name = "TestFeatureGroup"
    record_schema = ["feature1", "feature2", "record_id", "event_time"]
    role_arn = "arn:aws:iam::123456789012:role/test-role"
    s3_uri = "s3://test-bucket/"

    result = create_feature_group(feature_group_name, record_schema, role_arn, s3_uri)
    assert result.name == feature_group_name
