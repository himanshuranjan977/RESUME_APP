from os import environ, getcwd, path
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv(path.join(getcwd(), '.env'))

SECRET_KEY = environ.get('SECRET_KEY')

db = SQLAlchemy()
