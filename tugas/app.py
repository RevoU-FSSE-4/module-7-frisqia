from flask import Flask

from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)

app.config['SECRET_KEY']= os.getenv('SECRET_KEY')

app.register_blueprint()
app.register_blueprint()

jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"