from typing import Dict
import os


class Config:
    SECRET_KEY: str = os.getenv('SECRET_KEY') or 'default'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.getenv('DB_URL_DEV')
        or 'postgresql+psycopg2://postgres:{password}@localhost/nextlin_dev'
        .format(password=os.getenv('DB_PASS_DEV') or '')
    )


class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.getenv('DB_URL_TEST')
        or 'postgresql+psycopg2://postgres:{password}@localhost/nextlin_test'
        .format(password=os.getenv('DB_PASS_TEST') or '')
    )


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        os.getenv('DB_URL_PROD')
        or 'postgresql+psycopg2://postgres:{password}@localhost/nextlin_test'
        .format(password=os.getenv('DB_PASS_PROD') or '')
    )


config: Dict[str, type] = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
