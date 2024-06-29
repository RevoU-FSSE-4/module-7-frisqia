from flask import Flask
from dotenv import load_dotenv
from connectors.mysql_connector import connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, select
from models.product import Product
from models.user import User
from blueprint.route_product import product_bp
from blueprint.route_user import user_bp
import os

from flask_login import LoginManager
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY']= os.getenv('SECRET_KEY')
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)

#JSON Web Token
jwt = JWTManager(app)

# agar bisa melihat ada yg login atau tidak
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    Session = sessionmaker(connection)
    s = Session()
    return s.query(User).get(int(user_id))

@app.route("/")
def hello_world():
    return"hello world"