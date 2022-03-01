from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary


app = Flask(__name__)
app.secret_key = '%*&&*GJVGHHFCHGFYRT^%$^%^*&(&^I&%%*^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/labsaledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 4

db = SQLAlchemy(app = app)

cloudinary.config(
    cloud_name = 'ou-hcm',
    api_key = '437197794832588',
    api_secret = 'ZC-PQCgqI44E5UEKy7o8FhMtKmY'
)

login = LoginManager(app = app)