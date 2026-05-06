from flask import request, jsonify, make_response
from src.Application.Service.venda_service import VendaService

class VendaController:
    @staticmethod
    def register_venda(seller_id, product_id):
        quantity = request.form.get('quantity')
        
        if not quantity:
            return make_response(jsonify({"erro": "Campo obrigatório: quantity"}), 400)
        
        try:
            quantity = int(quantity)
        except ValueError:
            return make_response(jsonify({"erro": "quantity deve ser um numero inteiro"}), 400)
        
        venda, error = VendaService.register_venda(seller_id, product_id, quantity)
        
        if error == "not_found":
            return make_response(jsonify({"erro": "Produto não encontrado ou inativo"}), 404)

        if error == "forbidden":
            return make_response(jsonify({"erro": "Seller inativo"}), 403)

        if error == "stock":
            return make_response(jsonify({"erro": "Estoque insuficiente"}), 400)

        return make_response(jsonify({
            "mensagem": "Venda realizada com sucesso",
            "produto": venda.to_dict()
        }), 201)
    

    @staticmethod
    def list_venda(seller_id):
        vendas = VendaService.list_venda(seller_id)
        return make_response(jsonify({
            "vendas": [v.to_dict() for v in vendas]
            }), 200)

    @staticmethod
    def get_venda(seller_id, venda_id):
        venda, error = VendaService.get_venda(seller_id, venda_id)
        if error == "not_found":
            return make_response(jsonify({"erro": "Venda não encontrada"}), 404)
        if error == "forbidden":
            return make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        return make_response(jsonify({"venda": venda.to_dict()}), 200)
    
