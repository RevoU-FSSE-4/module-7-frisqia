from flask import Blueprint
from controllers.user_controller import register_user, check_login, logout_user

user_bp = Blueprint('users', __name__)

user_bp.route('/register', methods=['POST'])(register_user)
user_bp.route('/login', methods=['POST'])(check_login)
user_bp.route('/logout', methods=['GET'])(logout_user)
