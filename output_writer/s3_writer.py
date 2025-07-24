import boto3
import json
from config import settings
from utils.logger import setup_logger
from botocore.exceptions import ClientError

logger = setup_logger()

def write_s3_file(s3,data):
    
    try:
        json_string = json.dumps(data, indent=4) 
    except (TypeError, ValueError) as e:
        logger.error(f"Failed to formate data to json:{e}")
        return ""
    
    try:
        s3.put_object(
            Bucket=settings.bucket_name,
            Key=f"{settings.s3_output_path}data_transformed.json",
            Body=json_string,
        )
        logger.info(f"Data written to {settings.s3_output_path}data_transformed.json")
    except ClientError as e:
        logger.error(f"Failed to write to s3...:{e}")
    except Exception as e:
        logger.error(f"Unexpected error during writing to s3...:{e}")
        
