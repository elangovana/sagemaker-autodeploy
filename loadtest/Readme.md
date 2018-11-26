# Stress test your SageMaker endpoint

## Pre-requisites

1. Install Python 3.5
2. Setup virtual environment..

## Setup
1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Run Loadtest
1. Update the config

1. Kick off loadttest. In this example below, the region is https://runtime.sagemaker.ap-southeast-2.amazonaws.com
    
    ```bash
    locust -f loadtest/stress.py --host=https://runtime.sagemaker.ap-southeast-2.amazonaws.com
    
    ```

