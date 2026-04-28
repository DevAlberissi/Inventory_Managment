from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Controllers.product_controller import ProductController

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('', methods=['POST'])
@jwt_required()
def create_product():
    seller_id = int(get_jwt_identity())
    return ProductController.create_product(seller_id)

@products_bp.route('', methods=['GET'])
@jwt_required()
def list_products():
    seller_id = int(get_jwt_identity())
    return ProductController.list_products(seller_id)

@products_bp.route('/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product(product_id):
    seller_id = int(get_jwt_identity())
    return ProductController.get_product(seller_id, product_id)

@products_bp.route('/<int:product_id>', methods=['PATCH'])
@jwt_required()
def update_product(product_id):
    seller_id = int(get_jwt_identity())
    return ProductController.update_product(seller_id, product_id)

@products_bp.route('/<int:product_id>/deactivate', methods=['PATCH'])
@jwt_required()
def deactivate_product(product_id):
    seller_id = int(get_jwt_identity())
    return ProductController.deactivate_product(seller_id, product_id)
