import os
import requests
import zipfile
import io
from loguru import logger

country_link = {
    "japan": "https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Japan.zip",
    "india": "https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_India.zip",
    "czech": "https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Czech.zip",
    "norway": "https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Norway.zip",
    "usa": "https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_United_States.zip",
    "china_motorbike": "https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_China_MotorBike.zip",
    "china_drone": "https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_China_Drone.zip" 
}

def download_dataset(dataset_name: str, country_name: str, dataset_path: str):
    if not os.path.exists(dataset_path):
        logger.info(f"The provided path {dataset_path} does not exist. Creating directory {dataset_path}.")
        os.makedirs(dataset_path) 

    try:  
        logger.info(f"Downloading dataset {dataset_name} {country_name} to {dataset_path}.")
        r = requests.get(country_link[country_name])
        if r.status_code == 200:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(dataset_path)
            logger.info(f"Dataset {dataset_name} {country_name} was downloaded successfully to {dataset_path}.")
        else:
            logger.error(f"Error while downloading dataset {dataset_name} {country_name} to {dataset_path}: {r.status_code}.")
    except Exception as e:
        logger.error(f"Error while downloading dataset {dataset_name} {country_name} to {dataset_path}: {e}.")
        raise e