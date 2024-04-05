from apig_wsgi import make_lambda_handler
from src.wsgi import create_app

api_handler = make_lambda_handler(create_app())
