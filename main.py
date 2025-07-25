import boto3
from utils.logger import setup_logger
from input_reader.local_reader import read_file
from output_writer.local_writer import write_output
from input_reader.s3_reader import read_s3_file
from output_writer.s3_writer import write_s3_file
from transformer.data_transformer import transform_all

logger = setup_logger()
s3 = boto3.client('s3', region_name='ap-south-1')

x = input("Enter whether data is from 'local' or 's3' bucket: ").strip().lower()

logger.info("Transformation started")

match x:
    case "local":
        logger.info("Reading the file from local...")
        data = read_file()
        logger.info("Transforming data...")
        transformed_data = transform_all(data)
        logger.info("Writing transformed data locally...")
        write_output(transformed_data)

    case "s3":
        logger.info("Reading the file from S3...")
        data = read_s3_file(s3)
        logger.info("Transforming data...")
        transformed_data = transform_all(data)
        logger.info("Writing transformed data to S3...")
        write_s3_file(s3, transformed_data)

    case _:
        logger.error("Invalid option. Please enter 'local' or 's3'.")

    

"""
#create a bucket
response = s3_client.create_bucket(
    Bucket='json-data-transformer',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket created successfully:", response)


#upload the json file

bucket_name = 'json-data-transformer'
local_file_path = './input_data/alice.json'

s3_key = 'input_data/sample_input.json'

try:
    
    s3_client.upload_file(local_file_path, bucket_name, s3_key)
    print(f"File uploaded to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(f"Upload failed: {str(e)}")

"""