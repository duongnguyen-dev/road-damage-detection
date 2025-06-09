#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Create data directory if it doesn't exist
mkdir -p "$PROJECT_ROOT/data"

# Run script to download dataset
python "$PROJECT_ROOT/src/datasets/download_dataset.py" --path "$PROJECT_ROOT/data/rdd2022"

# Check the result
if [ $? -eq 0 ]; then
    echo "Dataset RDD2022 was install successfully to $PROJECT_ROOT/data/rdd2022"
else
    echo "There was an error while installing dataset RDD2022"
    exit 1
fi 