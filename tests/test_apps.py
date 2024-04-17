from app import main as prod_app
from app_dev import main as dev_app


def test_prod_app():
    prod_app()


def test_dev_app():
    dev_app()
