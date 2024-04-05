import aws_cdk as cdk

from cdk.constructs.api import Api
from constructs import Construct

from cdk.config import DEVELOPMENT_US_EAST_2


class ApiStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        Api(self, "Api")


def main():
    app = cdk.App()
    ApiStack(app, "ApiStack", env=DEVELOPMENT_US_EAST_2)
    app.synth()


if __name__ == "__main__":
    main()
