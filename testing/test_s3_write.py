import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import boto3
import json
import pytest
from moto import mock_aws
from config import settings
from output_writer.s3_writer import write_s3_file 

"""
def write_s3(bucket_name, key, data):
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(data).encode('utf-8')
    )
"""

@pytest.fixture
def s3_bucket():
    with mock_aws():
        s3_client = boto3.client('s3', region_name='us-east-1')
        s3_client.create_bucket(Bucket='test-bucket')
        settings.bucket_name = 'test-bucket'
        settings.s3_output_path = 'test-folder/' 
        yield s3_client


def test_write_s3(s3_bucket):
    test_data = {'name': 'John Doe', 'age': 30}
    write_s3_file(s3_bucket, test_data)
    
    key = 'test-folder/data_transformed.json'

    response = s3_bucket.get_object(Bucket='test-bucket', Key=key)
    result = json.loads(response['Body'].read().decode('utf-8'))
    
    assert result == test_data

if __name__ == "__main__":
    pytest.main()
