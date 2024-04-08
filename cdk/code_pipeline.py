import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep,
    ManualApprovalStep,
)
from cdk.constructs.api import Api


class ApiStack(cdk.Stack):
    """
    Generic API Stack, but in the future, you may actually use
    different resources in your stack to provision around your API
    construct.
    """

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        Api(self, "Api")


class StagingUsEast2Stage(cdk.Stage):
    """
    Deploys stacks to the Staging US East 2 region.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        ApiStack(self, "ApiStagingStack")


class ProductionUsEast2Stage(cdk.Stage):
    """
    Deploys stacks to the Production US East 2 region.

    While this is similar or the same as the StagingUsEast2Stage,
    we keep them separate to allow addition of unique resources
    depending on the use case.
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        ApiStack(self, "ApiStagingStack")


class CodePipelineStack(cdk.Stack):
    """
    The CodePipelineStack kicks off any time a change has been made
    to the AWS CDK app.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        connection_arn: str,
        repo,
        branch,
        operations_environment: cdk.Environment,
        staging_environment: cdk.Environment,
        production_environment: cdk.Environment,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="RootPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.connection(
                    repo, branch, connection_arn=connection_arn
                ),
                env=dict(
                    # Operations
                    AWS_ACCOUNT_ID_OPERATIONS=operations_environment.account,
                    AWS_PRIMARY_REGION_OPERATIONS=operations_environment.region,
                    AWS_CODESTAR_CONNECTION_ARN=connection_arn,
                    # Staging
                    AWS_ACCOUNT_ID_STAGING=staging_environment.account,
                    AWS_PRIMARY_REGION_STAGING=staging_environment.region,
                    # Production
                    AWS_ACCOUNT_ID_PRODUCTION=production_environment.account,
                    AWS_PRIMARY_REGION_PRODUCTION=production_environment.region,
                ),
                commands=[
                    "npm install -g aws-cdk@2.135",
                    "curl -sSL https://install.python-poetry.org | python3 -",
                    "/root/.local/bin/poetry install",
                    "/root/.local/bin/poetry run cdk synth",
                ],
            ),
            cross_account_keys=True,
        )
        pipeline.add_stage(
            StagingUsEast2Stage(
                self, "staging-us-east-2-stage", env=staging_environment
            )
        )
        pipeline.add_stage(
            ProductionUsEast2Stage(
                self, "production-us-east-2-stage", env=production_environment
            ),
            pre=[ManualApprovalStep("PromoteToProd")],
        )
