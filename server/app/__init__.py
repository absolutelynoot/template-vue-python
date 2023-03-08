from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ
# from dotenv import load_dotenv

# load_dotenv()

# user = environ.get('user') or "placeholderuser"
# password = environ.get('password') or "placeholderpassword"

# DB_HOSTNAME = environ.get('DB_HOSTNAME')
# DB_USERNAME = environ.get('DB_USERNAME')
# DB_PASSWORD = environ.get('DB_PASSWORD')
# DB_NAME = environ.get('DB_NAME')

app = Flask(__name__)

CORS(app)

from .hdb import *