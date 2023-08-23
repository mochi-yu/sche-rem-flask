import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = (join(dirname(__file__),  '../.env'))
load_dotenv(dotenv_path)

MYSQL_ROOT_PASSWORD=os.environ.get("MYSQL_ROOT_PASSWORD")
MYSQL_DATABASE=os.environ.get("MYSQL_DATABASE")
MYSQL_USER=os.environ.get("MYSQL_USER")
MYSQL_PASSWORD=os.environ.get("MYSQL_PASSWORD")
MYSQL_HOST=os.environ.get("MYSQL_HOST")
GMAIL_ADDRESS=os.environ.get("GMAIL_ADDRESS")
GMAIL_APP_PASS=os.environ.get("GMAIL_APP_PASS")