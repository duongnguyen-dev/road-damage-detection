#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data

# Run script to download dataset
python src/datasets/download_dataset.py --path data/rdd2022

# Check the result
if [ $? -eq 0 ]; then
    echo "Dataset RDD2022 was install successfully to data/rdd2022"
else
    echo "There was an error while installing dataset RDD2022"
    exit 1
fi 