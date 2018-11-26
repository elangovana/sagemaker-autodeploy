# Stress test your SageMaker endpoint

## Pre-requisites

1. Install Python 3.5

2. Setup virtual environment. This example is for bash and OsX
    ```bash
    python -m pip install --user virtualenv
    mkdir ~/virtualenvironment
    python -m virtualenv  ~/virtualenvironment/sagemakerloadatest
    source ~/virtualenvironment/sagemakerloadatest/bin/activate
    ```

## Setup
1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Run Loadtest
1. In the [config.json](config.json), update the config which includes the endpoint name and the data to use for load testing..

1. Kick off loadttest. In this example below, the region is https://runtime.sagemaker.ap-southeast-2.amazonaws.com
    
    ```bash
    locust -f loadtest/stress.py --host=https://runtime.sagemaker.ap-southeast-2.amazonaws.com
    
    ```

