import logging 
import os

def setup_logger(log_file="logs/json_transformer.log", level=logging.INFO):
    logger = logging.getLogger("json_transformer")
    logger.setLevel(level)

    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.info("json_transformer")
    
    return logger