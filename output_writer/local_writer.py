import os
import json
from config.settings import output_path
from utils.logger import setup_logger

logger = setup_logger()

def write_output(data, filename = "data_transformed.json"):
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    output_file = os.path.join(output_path, filename)
    
    try:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Data written to {output_file}")
    except Exception as e:
        logger.error(f"Transformation failed...Error : {str(e)}")