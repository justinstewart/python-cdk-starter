from pathlib import Path

from aws_cdk import aws_lambda as lambda_
from constructs import Construct


class Api(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Lambda Function
        directory = Path(__file__).parent.parent.parent / "api"
        docker_image_code = lambda_.DockerImageCode.from_image_asset(
            directory=str(directory), cmd=["src.handlers.api_handler"]
        )
        self.lambda_function = lambda_.DockerImageFunction(
            self, "ApiLambdaFunction", code=docker_image_code
        )
        self.lambda_function.add_function_url(
            auth_type=lambda_.FunctionUrlAuthType.NONE
        )
