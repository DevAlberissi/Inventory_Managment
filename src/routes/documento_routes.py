from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Controllers.documento_controller import DocumentoController

documentos_bp = Blueprint('documentos', __name__)

@documentos_bp.route('/products/<int:product_id>/documentos', methods=['POST'])
@jwt_required()
def upload_documento(product_id):
    seller_id = int(get_jwt_identity())
    return DocumentoController.upload_documento(seller_id, product_id)

@documentos_bp.route('/products/<int:product_id>/documentos', methods=['GET'])
@jwt_required()
def list_documentos(product_id):
    seller_id = int(get_jwt_identity())
    return DocumentoController.list_documentos(seller_id, product_id)

@documentos_bp.route('/documentos/<int:documento_id>', methods=['GET'])
@jwt_required()
def get_documento(documento_id):
    seller_id = int(get_jwt_identity())
    return DocumentoController.get_documento(seller_id, documento_id)

@documentos_bp.route('/documentos/<int:documento_id>', methods=['DELETE'])
@jwt_required()
def delete_documento(documento_id):
    seller_id = int(get_jwt_identity())
    return DocumentoController.delete_documento(seller_id, documento_id)
