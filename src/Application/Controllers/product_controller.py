from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService

class ProductController:
    @staticmethod
    def create_product(seller_id):
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity', 0)
        status_raw = request.form.get('status', 'true')

        if not name or price is None:
            return make_response(jsonify({"erro": "Campos obrigatórios: name, price"}), 400)

        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            return make_response(jsonify({"erro": "price e quantity devem ser numéricos"}), 400)

        status = status_raw.lower() != 'false'

        product = ProductService.create_product(seller_id, name, price, quantity, status)
        return make_response(jsonify({
            "mensagem": "Produto cadastrado com sucesso",
            "produto": product.to_dict()
        }), 201)

    @staticmethod
    def list_products(seller_id):
        products = ProductService.list_products(seller_id)
        return make_response(jsonify({
            "produtos": [p.to_dict() for p in products]
        }), 200)

    @staticmethod
    def get_product(seller_id, product_id):
        product, error = ProductService.get_product(product_id, seller_id)
        if error == "not_found":
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        if error == "forbidden":
            return make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        return make_response(jsonify({"produto": product.to_dict()}), 200)

    @staticmethod
    def update_product(seller_id, product_id):
        data = {}
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        status_raw = request.form.get('status')

        if name is not None:
            data['name'] = name
        if price is not None:
            try:
                data['price'] = float(price)
            except ValueError:
                return make_response(jsonify({"erro": "price deve ser numérico"}), 400)
        if quantity is not None:
            try:
                data['quantity'] = int(quantity)
            except ValueError:
                return make_response(jsonify({"erro": "quantity deve ser numérico"}), 400)
        if status_raw is not None:
            data['status'] = status_raw.lower() != 'false'

        product, error = ProductService.update_product(product_id, seller_id, data)
        if error == "not_found":
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        if error == "forbidden":
            return make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        return make_response(jsonify({
            "mensagem": "Produto atualizado com sucesso",
            "produto": product.to_dict()
        }), 200)

    @staticmethod
    def deactivate_product(seller_id, product_id):
        success, error = ProductService.deactivate_product(product_id, seller_id)
        if error == "not_found":
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        if error == "forbidden":
            return make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        return make_response(jsonify({"mensagem": "Produto inativado com sucesso"}), 200)
