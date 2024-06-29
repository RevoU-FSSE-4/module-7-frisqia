from flask import Flask
from dotenv import load_dotenv
# from models.review import Review
# from models.product import Product
# from models.user import User

from blueprint.review_route import review_bp
# from connectors.mysql_connector import connection
# from flask_login import LoginManager
# from flask_jwt_extended import JWTManager

# from sqlalchemy import text, select
# from sqlalchemy.orm import sessionmaker
# import os

load_dotenv()

app = Flask(__name__)

# app.config['SECRET_KEY']= os.getenv('SECRET_KEY')

app.register_blueprint(review_bp)
# app.register_blueprint()

# jwt = JWTManager(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

# @login_manager.user_loader
# def load_user(user_id):
#     from models.user import User
#     return User.query.get(user_id)

@app.route('/')
def hello_world():
    return "Hello World"




