# sagemaker_pipeline/processing_script.py

import pandas as pd
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    # Load data
    df = pd.read_csv(f"{args.input}/raw_data.csv")
    
    # Preprocessing logic here (cleaning, feature engineering, etc.)
    processed_df = df.copy()  # Replace with actual processing code

    # Define the record identifier and event timestamp
    processed_df['record_id'] = processed_df.index  # Unique identifier for each row
    processed_df['event_time'] = pd.to_datetime('now').isoformat()  # Event timestamp

    # Save to output
    processed_df.to_csv(f"{args.output}/processed_data.csv", index=False)
    
    # Send data to Feature Store
    from feature_store import create_feature_group, ingest_data_to_feature_group
    feature_group_name = "MyFeatureGroup"
    role_arn = "arn:aws:iam::123456789012:role/AmazonSageMaker-ExecutionRole"

    # Create Feature Group and ingest data
    feature_group = create_feature_group(feature_group_name, processed_df.columns.tolist(), role_arn, "s3://your-sagemaker-bucket/feature-store/")
    ingest_data_to_feature_group(feature_group, processed_df)
