from flask import Blueprint
from controller.controller_review import get_test, fetch_review ,search_review_data

review_bp = Blueprint('reviews_routes', __name__)

review_bp.route('/test', methods=['GET'])(get_test)
review_bp.route('/reviews', methods=['GET'])(fetch_review)
review_bp.route('/searchreview', methods=['GET'])(search_review_data)