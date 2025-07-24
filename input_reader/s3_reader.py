import boto3
import json
from config import settings
from utils.logger import setup_logger
from botocore.exceptions import ClientError

logger = setup_logger()

def read_s3_file(s3):
    data_list = []
    
    """
    response = s3.get_object(Bucket=bucket_name, Key=key)
    data = response['Body'].read()
    """
    
    try:
        response = s3.list_objects_v2(Bucket=settings.bucket_name, Prefix=settings.s3_input_path)
        
    except ClientError as e:
        logger.error(f"Failed to list objects in bucket '{settings.bucket_name}':{e}")
        return []
    
    except Exception as e:
        logger.error(f"Unexpected error during operation:{e}")
        return []
    
    for filename in response.get('Contents', []):
        key = filename['Key']
        
        if key.endswith('.json'):
            
            try:
                s3_file = s3.get_object(Bucket=settings.bucket_name, Key=key)
                data = s3_file['Body'].read()
                data_content = json.loads(data.decode('utf-8'))
                data_list.append(data_content)
            except ClientError as e:
                logger.error(f"Failed to read s3 file '{key}':{e}")
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON file '{key}':{e}")
            except Exception as e:
                logger.error(f"Unexpected error in file '{key}':{e}")
    
    return data_list
