from src.Infrastructure.Model.product import Product
from src.Infrastructure.Model.user import User
from src.Domain.venda import VendaDomain
from src.Infrastructure.Model.venda import Venda
from src.config.data_base import db

class VendaService:
    @staticmethod
    def register_venda(seller_id, product_id, quantity):
        product = Product.query.get(product_id)
        seller = User.query.get(seller_id)

        if not product or not product.status:
            return None, "not_found"

        if not seller or not seller.status:
            return None, "forbidden"

        if quantity > product.quantity:
            return None, "stock"
        
        price = product.price
        product.quantity -= quantity

        venda = Venda(
            seller_id=seller_id,
            product_id=product_id,
            quantity=quantity,
            price=price
        )

        db.session.add(venda)
        db.session.commit()
        return VendaDomain(venda.id, venda.quantity, venda.price), None
    
    @staticmethod
    def list_venda(seller_id):
        vendas = Venda.query.filter_by(seller_id=seller_id).all()
        return [VendaDomain(v.id, v.quantity, v.price) for v in vendas]


    @staticmethod
    def get_venda(seller_id, venda_id):
        venda = Venda.query.get(venda_id)

        if not venda:
            return None, "not_found"
        
        if venda.seller_id != seller_id:
            return None, "forbidden"
        
        return VendaDomain(venda.id, venda.quantity, venda.price), None
