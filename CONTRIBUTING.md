# Contributing

## Getting Started
The following are required to run this project:

- [Python 3.10+]](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)
- [Node.js 18.x](https://nodejs.org/en/download/)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)

Installing dependencies:

```bash
poetry install
```

Provide docker with permissions to access public ECR repositories:

```bash
aws ecr-public --profile YOUR_PROFILE_NAME get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```
