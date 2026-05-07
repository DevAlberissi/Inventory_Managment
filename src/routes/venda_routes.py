from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Controllers.venda_controller import VendaController

vendas_bp = Blueprint('vendas', __name__, url_prefix='/vendas')

@vendas_bp.route('', methods=['POST'])
@jwt_required()
def create_venda():
    seller_id = int(get_jwt_identity())
    return VendaController.create_venda(seller_id)

@vendas_bp.route('', methods=['GET'])
@jwt_required()
def list_vendas():
    seller_id = int(get_jwt_identity())
    return VendaController.list_vendas(seller_id)

@vendas_bp.route('/<int:venda_id>', methods=['GET'])
@jwt_required()
def get_venda(venda_id):
    seller_id = int(get_jwt_identity())
    return VendaController.get_venda(seller_id, venda_id)

@vendas_bp.route('/<int:venda_id>', methods=['DELETE'])
@jwt_required()
def delete_venda(venda_id):
    seller_id = int(get_jwt_identity())
    return VendaController.delete_venda(seller_id, venda_id)
