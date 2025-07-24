import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import boto3
import json                     
import pytest
from moto import mock_aws
from input_reader.s3_reader import read_s3_file
from config import settings

"""
def read_s3(bucket_name, key):
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket_name, Key=key)
    return json.loads(response['Body'].read().decode('utf-8'))
"""

@pytest.fixture #prepares a test environment mock_aws : fake all aws service
def s3_bucket():
    with mock_aws():             
        s3_client = boto3.client('s3', region_name='us-east-1')
        s3_client.create_bucket(Bucket='test-bucket')
        settings.bucket_name = 'test-bucket'
        settings.s3_input_path = ""
        
        yield s3_client

def test_s3(s3_bucket):
    
    test_json_data = {'name': 'John Doe', 'age': 30}
    s3_bucket.put_object(
        Bucket='test-bucket',
        Key='test-file.json',
        Body=json.dumps(test_json_data).encode('utf-8')
    )


    result = read_s3_file(s3_bucket)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == test_json_data

if __name__ == "__main__":
    pytest.main()
    