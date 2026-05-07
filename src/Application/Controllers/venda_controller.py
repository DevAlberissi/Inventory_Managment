from flask import request, jsonify, make_response
from src.Application.Service.venda_service import VendaService

class VendaController:
    @staticmethod
    def create_venda(seller_id):
        body = request.get_json()
        if not body:
            return make_response(jsonify({"erro": "Body JSON obrigatório"}), 400)

        produto_id = body.get('produto_id')
        quantidade = body.get('quantidade')

        if produto_id is None or quantidade is None:
            return make_response(jsonify({"erro": "Campos obrigatórios: produto_id, quantidade"}), 400)

        try:
            produto_id = int(produto_id)
            quantidade = int(quantidade)
        except (ValueError, TypeError):
            return make_response(jsonify({"erro": "produto_id e quantidade devem ser inteiros"}), 400)

        if quantidade <= 0:
            return make_response(jsonify({"erro": "quantidade deve ser maior que zero"}), 400)

        venda, error = VendaService.create_venda(seller_id, produto_id, quantidade)
        if error == "seller_inactive":
            return make_response(jsonify({"erro": "Seller inativo. Ative sua conta para realizar vendas"}), 403)
        if error == "not_found":
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        if error == "forbidden":
            return make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        if error == "product_inactive":
            return make_response(jsonify({"erro": "Produto inativado. Não é possível vendê-lo"}), 403)
        if error == "insufficient_stock":
            return make_response(jsonify({"erro": "Estoque insuficiente para a quantidade solicitada"}), 422)

        return make_response(jsonify({
            "mensagem": "Venda registrada com sucesso",
            "venda": venda.to_dict()
        }), 201)

    @staticmethod
    def list_vendas(seller_id):
        vendas = VendaService.list_vendas(seller_id)
        return make_response(jsonify({
            "vendas": [v.to_dict() for v in vendas]
        }), 200)

    @staticmethod
    def get_venda(seller_id, venda_id):
        venda, error = VendaService.get_venda(venda_id, seller_id)
        if error == "not_found":
            return make_response(jsonify({"erro": "Venda não encontrada"}), 404)
        if error == "forbidden":
            return make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        return make_response(jsonify({"venda": venda.to_dict()}), 200)

    @staticmethod
    def delete_venda(seller_id, venda_id):
        success, error = VendaService.delete_venda(venda_id, seller_id)
        if error == "not_found":
            return make_response(jsonify({"erro": "Venda não encontrada"}), 404)
        if error == "forbidden":
            return make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        return make_response(jsonify({"mensagem": "Venda cancelada com sucesso"}), 200)
