import os

from dotenv import load_dotenv

load_dotenv()

ENV__SECRET_KEY = os.getenv('SECRET_KEY')
ENV__DEBUG = os.getenv('DEBUG')
ENV__ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

ENV__DATABASE_NAME = os.getenv('DATABASE_NAME')
ENV__DATABASE_USER = os.getenv('DATABASE_USER')
ENV__DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
ENV__DATABASE_HOST = os.getenv('DATABASE_HOST')
ENV__DATABASE_PORT = os.getenv('DATABASE_PORT')

ENV__API_BACKEND = os.getenv('API_BACKEND')

ENV__BOT_TOKEN = os.getenv('BOT_TOKEN')