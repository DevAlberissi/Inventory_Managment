from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class ProductService:
    @staticmethod
    def create_product(seller_id, name, price, quantity, status, image_url):
        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            status=status,
            image_url=image_url,
            seller_id=seller_id
        )
        db.session.add(product)
        db.session.commit()
        return ProductDomain(product.id, product.name, product.price, product.quantity, product.status, product.image_url, product.seller_id)

    @staticmethod
    def list_products(seller_id):
        products = Product.query.filter_by(seller_id=seller_id).all()
        return [ProductDomain(p.id, p.name, p.price, p.quantity, p.status, p.image_url, p.seller_id) for p in products]

    @staticmethod
    def get_product(product_id, seller_id):
        product = Product.query.get(product_id)
        if not product:
            return None, "not_found"
        if product.seller_id != seller_id:
            return None, "forbidden"
        return ProductDomain(product.id, product.name, product.price, product.quantity, product.status, product.image_url, product.seller_id), None

    @staticmethod
    def update_product(product_id, seller_id, data, image_url=None):
        product = Product.query.get(product_id)
        if not product:
            return None, "not_found"
        if product.seller_id != seller_id:
            return None, "forbidden"

        campos = ["name", "price", "quantity", "status"]
        for campo in campos:
            if campo in data:
                setattr(product, campo, data[campo])

        if image_url is not None:
            product.image_url = image_url

        db.session.commit()
        return ProductDomain(product.id, product.name, product.price, product.quantity, product.status, product.image_url, product.seller_id), None

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
