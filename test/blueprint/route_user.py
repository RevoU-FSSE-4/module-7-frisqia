from flask import Blueprint
from controllers.user_controller import register_user, check_login, user_logout, check_login_jwt

user_bp = Blueprint('users', __name__)

user_bp.route('/register', methods=['POST'])(register_user)
user_bp.route('/login', methods=['POST'])(check_login)
user_bp.route('/loginjwt', methods=['POST'])(check_login_jwt)
user_bp.route('/logout', methods=['GET'])(user_logout)
