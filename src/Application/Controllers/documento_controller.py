from flask import request, jsonify, make_response
from src.Application.Service.documento_service import DocumentoService
from src.Application.Service.product_service import ProductService

class DocumentoController:
    @staticmethod
    def _check_product_ownership(product_id, seller_id):
        product, error = ProductService.get_product(product_id, seller_id)
        if error == "not_found":
            return None, make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        if error == "forbidden":
            return None, make_response(jsonify({"erro": "Acesso não autorizado"}), 403)
        return product, None

    @staticmethod
    def upload_documento(seller_id, product_id):
        _, err = DocumentoController._check_product_ownership(product_id, seller_id)
        if err:
            return err

        if 'conteudo' not in request.files:
            return make_response(jsonify({"erro": "Campo 'conteudo' obrigatório"}), 400)

        file = request.files['conteudo']
        if not file or not file.filename:
            return make_response(jsonify({"erro": "Arquivo inválido"}), 400)

        nome_arquivo = file.filename
        mime_type = file.content_type or 'application/octet-stream'
        conteudo = file.read()

        doc = DocumentoService.create_documento(product_id, nome_arquivo, mime_type, conteudo)
        return make_response(jsonify({
            "mensagem": "Documento enviado com sucesso",
            "documento": doc.to_dict()
        }), 201)

    @staticmethod
    def list_documentos(seller_id, product_id):
        _, err = DocumentoController._check_product_ownership(product_id, seller_id)
        if err:
            return err

        docs = DocumentoService.list_documentos(product_id)
        return make_response(jsonify({"documentos": [d.to_dict() for d in docs]}), 200)

    @staticmethod
    def get_documento(seller_id, documento_id):
        doc = DocumentoService.get_documento(documento_id)
        if not doc:
            return make_response(jsonify({"erro": "Documento não encontrado"}), 404)

        _, err = DocumentoController._check_product_ownership(doc.product_id, seller_id)
        if err:
            return err

        response = make_response(doc.conteudo)
        response.headers['Content-Type'] = doc.mime_type
        response.headers['Content-Disposition'] = f'inline; filename="{doc.nome_arquivo}"'
        return response

    @staticmethod
    def delete_documento(seller_id, documento_id):
        doc = DocumentoService.get_documento(documento_id)
        if not doc:
            return make_response(jsonify({"erro": "Documento não encontrado"}), 404)

        _, err = DocumentoController._check_product_ownership(doc.product_id, seller_id)
        if err:
            return err

        DocumentoService.delete_documento(documento_id)
        return make_response(jsonify({"mensagem": "Documento removido com sucesso"}), 200)
