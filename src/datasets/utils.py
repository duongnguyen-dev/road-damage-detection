import os
import dataset_tools as dtools
from loguru import logger

def download_dataset(dataset_name: str, dataset_path: str):
    if not os.path.exists(dataset_path):
        logger.info(f"The provided path {dataset_path} does not exist. Creating directory {dataset_path}")
        os.makedirs(dataset_path) 

    try:  
        logger.info(f"Downloading dataset {dataset_name} to {dataset_path}")
        dtools.download_dataset(dataset_name, dataset_path) 
        logger.info(f"Dataset {dataset_name} downloaded successfully to {dataset_path}")
    except Exception as e:
        logger.error(f"Error downloading dataset {dataset_name} to {dataset_path}: {e}")
        raise e