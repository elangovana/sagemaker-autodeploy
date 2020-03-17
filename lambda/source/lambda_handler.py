import json
import os

import boto3

"""
Lambda function to invoke sagemaker endpoiunt
"""


def lambda_handler(event, context):
    model_name = event["queryStringParameters"]["model_name"]
    request_data = json.loads(event["body"])
    endpoint_name = os.environ['sagemaker_endpoint']

    sagemaker_client = boto3.client('sagemaker-runtime')

    model_type = model_name
    custom_attributes = "tfs-model-name={},tfs-model-version={}".format(model_type, 1)
    response = sagemaker_client.invoke_endpoint(
        EndpointName=endpoint_name,
        Body=json.dumps(request_data).encode(),
        CustomAttributes=custom_attributes,
        ContentType='application/json',
        Accept='application/json'
    )

    body = response["Body"].read()

    response = {"body": body.decode('utf-8')}
    return response
