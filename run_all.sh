#!/bin/bash
# Run all API scripts with debugging information

source venv/bin/activate

echo "Loading environment variables..."
export $(grep -v '^#' .env | xargs)

echo "Running API 1 script..."
python api1/api1_integration.py
echo "Finished running API 1 script."

echo "Running API 2 script..."
python api2/api2_integration.py
echo "Finished running API 2 script."

deactivate
