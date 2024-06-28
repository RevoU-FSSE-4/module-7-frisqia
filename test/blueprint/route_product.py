from flask import Blueprint
from controllers.product_controller import get_product, create_product, update_product, delete_product
from flask_login import login_required

def login_required_blueprint(bp):
    original_add_url_rule = bp.add_url_rule

    def new_add_url_rule(rule, endpoint=None, view_func=None, **options):
        view_func = login_required(view_func)
        return original_add_url_rule(rule, endpoint, view_func, **options)

    bp.add_url_rule = new_add_url_rule
    return bp

product_bp = Blueprint('product', __name__)
product_bp = login_required_blueprint(product_bp)

product_bp.route('/product', methods=['GET'])(get_product)
product_bp.route('/product', methods=['POST'])(create_product)
product_bp.route('/product/<int:id>', methods=['PUT'])(update_product)
product_bp.route('/product/<int:id>', methods=['DELETE'])(delete_product)