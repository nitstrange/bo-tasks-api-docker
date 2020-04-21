# services/users/project/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

os.environ['DATABASE_URL'] = 'sqlite:////' + os.path.join(basedir, 'task.db')
os.environ['DATABASE_TEST_URL'] = 'sqlite:////' + os.path.join(basedir,'task_test.db')


class BaseConfig: 
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # new

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')  # new


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # new