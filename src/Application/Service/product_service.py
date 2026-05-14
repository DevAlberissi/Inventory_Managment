from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class ProductService:
    @staticmethod
    def create_product(seller_id, name, price, quantity, status):
        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            status=status,
            seller_id=seller_id
        )
        db.session.add(product)
        db.session.commit()
        return ProductDomain(product.id, product.name, product.price, product.quantity, product.status, product.seller_id)

    @staticmethod
    def _docs_from_product(product):
        return [
            {
                "id": d.id,
                "nome_arquivo": d.nome_arquivo,
                "mime_type": d.mime_type,
                "url": f"/documentos/{d.id}"
            }
            for d in product.documentos
        ]

    @staticmethod
    def list_products(seller_id):
        products = Product.query.filter_by(seller_id=seller_id).all()
        return [
            ProductDomain(p.id, p.name, p.price, p.quantity, p.status, p.seller_id, ProductService._docs_from_product(p))
            for p in products
        ]

    @staticmethod
    def get_product(product_id, seller_id):
        product = Product.query.get(product_id)
        if not product:
            return None, "not_found"
        if product.seller_id != seller_id:
            return None, "forbidden"
        return ProductDomain(product.id, product.name, product.price, product.quantity, product.status, product.seller_id, ProductService._docs_from_product(product)), None

    @staticmethod
    def update_product(product_id, seller_id, data):
        product = Product.query.get(product_id)
        if not product:
            return None, "not_found"
        if product.seller_id != seller_id:
            return None, "forbidden"

        for campo in ["name", "price", "quantity", "status"]:
            if campo in data:
                setattr(product, campo, data[campo])

        db.session.commit()
        return ProductDomain(product.id, product.name, product.price, product.quantity, product.status, product.seller_id, ProductService._docs_from_product(product)), None

    @staticmethod
    def deactivate_product(product_id, seller_id):
        product = Product.query.get(product_id)
        if not product:
            return False, "not_found"
        if product.seller_id != seller_id:
            return False, "forbidden"

        product.status = False
        db.session.commit()
        return True, None

    @staticmethod
    def activate_product(product_id, seller_id):
        product = Product.query.get(product_id)
        if not product:
            return False, "not_found"
        if product.seller_id != seller_id:
            return False, "forbidden"

        product.status = True
        db.session.commit()
        return True, None
