from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Controllers.venda_controller import VendaController

venda_bp = Blueprint('vendas', __name__, url_prefix='/venda')

@venda_bp.route("/<int:product_id>", methods=["POST"])
@jwt_required()
def register_venda(product_id):
    seller_id = int(get_jwt_identity())
    return VendaController.register_venda(seller_id, product_id)

@venda_bp.route("", methods=["GET"])
@jwt_required()
def list_venda():
    seller_id = int(get_jwt_identity())
    return VendaController.list_venda(seller_id)

@venda_bp.route("/<int:venda_id>", methods=["GET"])
@jwt_required()
def get_venda(venda_id):
    seller_id = int(get_jwt_identity())
    return VendaController.get_venda(seller_id, venda_id)