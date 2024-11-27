# import boto3
# import sagemaker
# import pandas as pd

# sess = sagemaker.Session()
# bucket = sess.default_bucket()
# #role = sagemaker.get_execution_role()
# role = "arn:aws:iam::022398263250:role/service-role/SageMaker-MLOpsEngineer"
# region = boto3.Session().region_name



# # Create an S3 client with a specific region
# s3 = boto3.client('s3', region_name='us-east-1')

# # Specify the bucket name
# bucket_name = 'sagemaker-us-east-1-022398263250'

# # List objects within the specified S3 bucket
# response = s3.list_objects_v2(Bucket=bucket_name)

# # Check if the bucket has any contents
# if 'Contents' in response:
#     for obj in response['Contents']:
#         print(obj['Key'])
# else:
#     print(f"No objects found in bucket {bucket_name}.")


# import boto3
# import pandas as pd
# import csv
# import io

# # Initialize a session using boto3
# s3 = boto3.client('s3')

# # Define the S3 bucket and file key
# bucket_name = 'sagemaker-us-east-1-022398263250'
# file_key = 'amazon_reviews_us_Digital_Software_v1_00.tsv'

# # Fetch the file from S3
# response = s3.get_object(Bucket=bucket_name, Key=file_key)

# # Read the file content into a pandas DataFrame
# df = pd.read_csv(
#     io.BytesIO(response['Body'].read()),  # Reading the body of the response
#     delimiter="\t",                       # TSV delimiter
#     quoting=csv.QUOTE_NONE                # Handling quotes
# )

# # Print the shape of the DataFrame to verify
# print(df.head)

# print("Shape of dataframe before splitting {}".format(df.shape))

import boto3
import sagemaker
import pandas as pd
import json

sess = sagemaker.Session()
bucket = sess.default_bucket()
role = "arn:aws:iam::022398263250:role/service-role/AmazonSageMaker-ExecutionRole-20240825T151615"
region = boto3.Session().region_name

sm = boto3.Session().client(service_name="sagemaker", region_name=region)