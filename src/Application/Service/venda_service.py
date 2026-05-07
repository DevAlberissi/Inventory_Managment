from src.Domain.venda import VendaDomain
from src.Infrastructure.Model.venda import Venda
from src.Infrastructure.Model.product import Product
from src.Infrastructure.Model.user import User
from src.config.data_base import db

class VendaService:
    @staticmethod
    def create_venda(seller_id, produto_id, quantidade):
        seller = User.query.get(seller_id)
        if not seller or not seller.status:
            return None, "seller_inactive"

        product = Product.query.get(produto_id)
        if not product:
            return None, "not_found"
        if product.seller_id != seller_id:
            return None, "forbidden"
        if not product.status:
            return None, "product_inactive"
        if quantidade > product.quantity:
            return None, "insufficient_stock"

        product.quantity -= quantidade

        venda = Venda(
            produto_id=produto_id,
            seller_id=seller_id,
            quantidade=quantidade,
            preco_unitario=product.price
        )
        db.session.add(venda)
        db.session.commit()
        return VendaDomain(venda.id, venda.produto_id, venda.seller_id, venda.quantidade, venda.preco_unitario, venda.created_at), None

    @staticmethod
    def list_vendas(seller_id):
        vendas = Venda.query.filter_by(seller_id=seller_id).all()
        result = []
        for v in vendas:
            product = Product.query.get(v.produto_id)
            produto_dict = None
            if product:
                produto_dict = {
                    "id": product.id,
                    "name": product.name,
                    "imagens": [doc.to_dict() for doc in product.documentos]
                }
            result.append(VendaDomain(v.id, v.produto_id, v.seller_id, v.quantidade, v.preco_unitario, v.created_at, produto=produto_dict))
        return result

    @staticmethod
    def get_venda(venda_id, seller_id):
        venda = Venda.query.get(venda_id)
        if not venda:
            return None, "not_found"
        if venda.seller_id != seller_id:
            return None, "forbidden"
        return VendaDomain(venda.id, venda.produto_id, venda.seller_id, venda.quantidade, venda.preco_unitario, venda.created_at), None

    @staticmethod
    def delete_venda(venda_id, seller_id):
        venda = Venda.query.get(venda_id)
        if not venda:
            return False, "not_found"
        if venda.seller_id != seller_id:
            return False, "forbidden"

        product = Product.query.get(venda.produto_id)
        if product:
            product.quantity += venda.quantidade

        db.session.delete(venda)
        db.session.commit()
        return True, None
