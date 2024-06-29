from flask import Flask
from dotenv import load_dotenv
from blueprint.review_route import review_bp
from blueprint.user_route import user_bp
from sqlalchemy.orm import sessionmaker
from connectors.mysql_connector import connection


from flask_login import LoginManager
from models.user import User

import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(review_bp)
app.register_blueprint(user_bp)


#save session id
login_manager = LoginManager()
login_manager.init_app(app)


#current_user / get who is user login
@login_manager.user_loader
def load_user(users_id):
     Session = sessionmaker(connection)
     s = Session()
     return s.query(User).get(int(users_id))
     

@app.route('/')
def hello_world():
    return "Hello World"




