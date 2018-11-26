from locust import HttpLocust, TaskSet, task
import boto3
import json


class SageMakerConfig:

    def __init__(self):
        # TODO: Configure this before you run
        self.endpointname = "DummyS2"
        self.data = {
            "instances": [
                {
                    "start": "2009-11-01 00:00:00",
                    "target": [4.0, 10.0, "NaN", 100.0, 113.0]

                }
            ],
            "configuration": {
                "num_samples": 50,
                "output_types": ["mean", "quantiles", "samples"],
                "quantiles": ["0.5", "0.9"]
            }
        }


class SageMakerEndpointTastSet(TaskSet):

    @task
    def test_invoke(self):
        config = SageMakerConfig()

        # Start run here
        region = self.client.base_url.split("://")[1].split(".")[2]
        print(self.client.base_url)

        print(region)
        sagemaker_client = boto3.client('sagemaker-runtime', region_name=region, endpoint_url=self.client.base_url)

        response = sagemaker_client.invoke_endpoint(
            EndpointName=config.endpointname,
            Body=json.dumps(config.data).encode(),
            ContentType='application/json',
            Accept='application/json'
        )

        body = response["Body"].read()


class SageMakerEndpointLocust(HttpLocust):
    task_set = SageMakerEndpointTastSet
    min_wait = 5000
    max_wait = 15000
