import aws_cdk as cdk

from cdk.config import (
    CODESTAR_CONNECTION_ARN,
    OPERATIONS_US_EAST_2,
    STAGING_US_EAST_2,
    PRODUCTION_US_EAST_2,
)
from cdk.code_pipeline import CodePipelineStack


def main():
    app = cdk.App()
    CodePipelineStack(
        app,
        "CodePipeline",
        connection_arn=CODESTAR_CONNECTION_ARN,
        env=OPERATIONS_US_EAST_2,
        operations_environment=OPERATIONS_US_EAST_2,
        staging_environment=STAGING_US_EAST_2,
        production_environment=PRODUCTION_US_EAST_2,
        repo="justinstewart/breakable-toys",
        branch="main",
    )
    app.synth()


if __name__ == "__main__":
    main()
