import argparse
from src.datasets.utils import download_dataset

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download RDD2022 dataset to specified path")
    parser.add_argument("--dataset", type=str, default="RDD2022", help="Name of the dataset to download")
    parser.add_argument("--path", type=str, required=True, help="Path to save the dataset")
    
    args = parser.parse_args()
    download_dataset(args.dataset, args.path)