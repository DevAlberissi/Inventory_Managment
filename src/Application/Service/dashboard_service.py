from src.Infrastructure.Model.venda import Venda
from src.Infrastructure.Model.product import Product
from src.config.data_base import db
from sqlalchemy import func

class DashboardService:
    @staticmethod
    def get_dashboard(seller_id):

        resultados = db.session.query(
            Product.id,
            Product.name,
            Product.quantity.label("estoque"),
            func.coalesce(func.sum(Venda.quantity), 0).label("vendido"),
            func.coalesce(func.sum(Venda.quantity * Venda.price), 0).label("valor_total")
        ).outerjoin(
            Venda, Venda.product_id == Product.id
        ).filter(
            Product.seller_id == seller_id
        ).group_by(
            Product.id
        ).all()

        produtos = [
            {
                "id": r.id,
                "name": r.name,
                "estoque": r.estoque,
                "vendido": int(r.vendido),
                "valor_total": float(r.valor_total)
            }
            for r in resultados
        ]

        return {"produtos": produtos}