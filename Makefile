-include .env
export $(shell sed 's/=.*//' .env)

bootstrap-dev:
	npx cdk bootstrap --profile ${AWS_PROFILE_DEV} "aws://${AWS_ACCOUNT_ID_DEV}/${AWS_PRIMARY_REGION_DEV}"

bootstrap-operations:
	aws sso login --profile ${AWS_PROFILE_OPERATIONS}
	npx cdk bootstrap --profile ${AWS_PROFILE_OPERATIONS} "aws://${AWS_ACCOUNT_ID_OPERATIONS}/${AWS_PRIMARY_REGION_OPERATIONS}"

bootstrap-staging:
	aws sso login --profile ${AWS_PROFILE_STAGING}
	npx cdk bootstrap --profile ${AWS_PROFILE_STAGING} "aws://${AWS_ACCOUNT_ID_STAGING}/${AWS_PRIMARY_REGION_STAGING}" --cloudformation-execution-policies "arn:aws:iam::aws:policy/AdministratorAccess" --trust ${AWS_ACCOUNT_ID_OPERATIONS}

bootstrap-production:
	aws sso login --profile ${AWS_PROFILE_PRODUCTION}
	npx cdk bootstrap --profile ${AWS_PROFILE_PRODUCTION} "aws://${AWS_ACCOUNT_ID_PRODUCTION}/${AWS_PRIMARY_REGION_PRODUCTION}" --cloudformation-execution-policies "arn:aws:iam::aws:policy/AdministratorAccess" --trust ${AWS_ACCOUNT_ID_OPERATIONS}

install:
	poetry install
	cd api && poetry install

deploy:
	poetry run npx cdk deploy --profile ${AWS_PROFILE_OPERATIONS}

deploy-dev:
	poetry run npx cdk deploy --profile ${AWS_PROFILE_DEV} -a "python app_dev.py"
