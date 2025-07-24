import os
import json
from config.settings import input_path
from utils.logger import setup_logger


logger = setup_logger()

def read_file():
    
    data_list = []
    
    if not os.path.exists(input_path):
        logger.error(f"Input folder {input_path} not found")
        return data_list
        
    for filename in os.listdir(input_path):
        if filename.endswith(".json"):
            file_path = os.path.join(input_path, filename)
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    data_list.append(data)
                    logger.info(f"{filename} file is read")
            except FileNotFoundError:
                logger.error(f"{filename} file is not found")
            except json.JSONDecodeError:
                logger.error(f"{filename} is invalid json file")
            except PermissionError:
                logger.error(f"{filename} has no permission")
            except Exception as e:
                logger.error(f"unexcepted error in the file {filename} : {str(e)}")
    return data_list
                    