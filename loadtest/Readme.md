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
    
2. AWS Credentials

   - In order to get this to work, please ensure that you have configured the aws credentials to have permissions to invoke endpoint. To set up boto3 to work with aws credentials, see see  https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html.
   - The user should have permission to invoke the endpoint. In this example below, the user will have permission to invoke the endpoint named "myendpoint", in region "ap-southeast-2".
   ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "sagamakerinvokeendpoint",
                "Effect": "Allow",
                "Action": "sagemaker:InvokeEndpoint",
                "Resource": "arn:aws:sagemaker:ap-southeast-2:*:endpoint/myendpoint"
            }
        ]
    }
    ```
   
  

## Run Loadtest
1. In the [config.json](config.json), update the config which includes the endpoint name and the data to use for load testing..

1. Kick off loadttest. In this example below, the region is https://runtime.sagemaker.ap-southeast-2.amazonaws.com
    
    ```bash
    locust -f loadtest/stress.py --host=https://runtime.sagemaker.ap-southeast-2.amazonaws.com
    
    ```

