import os
from enum import Enum

import aws_cdk as cdk


class Regions(Enum):
    US_EAST_2 = "us-east-2"

# Source
REPO = os.getenv("REPO")

# CodeStar Connections
CODESTAR_CONNECTION_ARN = os.getenv("AWS_CODESTAR_CONNECTION_ARN")

# Environments
DEVELOPMENT_US_EAST_2 = cdk.Environment(
    account=os.getenv("AWS_ACCOUNT_ID_DEV"), region=Regions.US_EAST_2.value
)
OPERATIONS_US_EAST_2 = cdk.Environment(
    account=os.getenv("AWS_ACCOUNT_ID_OPERATIONS"), region=Regions.US_EAST_2.value
)
PRODUCTION_US_EAST_2 = cdk.Environment(
    account=os.getenv("AWS_ACCOUNT_ID_PRODUCTION"), region=Regions.US_EAST_2.value
)
STAGING_US_EAST_2 = cdk.Environment(
    account=os.getenv("AWS_ACCOUNT_ID_STAGING"), region=Regions.US_EAST_2.value
)
