from flask import Blueprint
from controller.controller_user import chek_test, register_user, user_login, user_logout

user_bp = Blueprint('user_routes', __name__)

user_bp.route('/chek', methods=['GET'])(chek_test)
user_bp.route('/register', methods=['POST'])(register_user)
user_bp.route('/login', methods= ['POST'])(user_login)
# user_bp.route('/loginjwt', methods=['POST'])(user_loginJWT)
user_bp.route('/logout', methods=['POST'])(user_logout)
