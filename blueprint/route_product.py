from flask import Blueprint
from controllers.product import get_product, create_product, update_product, delete_product

product_bp = Blueprint('product', __name__)

product_bp.route('/product', methods=['GET'])(get_product)
# product_bp.route('/product/<int:id>', methods=['GET'])(create_product)
product_bp.route('/product', methods=['POST'])(create_product)
product_bp.route('/product/<int:id>', methods=['PUT'])(update_product)
product_bp.route('/product/<int:id>', methods=['DELETE'])(delete_product)