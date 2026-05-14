from src.Infrastructure.Model.venda import Venda
from src.Infrastructure.Model.product import Product
from src.config.data_base import db
from sqlalchemy import func

class DashboardService:
    @staticmethod
    def get_dashboard(seller_id):
        total_produtos = db.session.query(func.count(Product.id)).filter(
            Product.seller_id == seller_id,
            Product.status == True
        ).scalar() or 0

        produtos_ativos = db.session.query(func.count(Product.id)).filter(
            Product.seller_id == seller_id,
            Product.status == True
        ).scalar() or 0

        estoque_baixo = db.session.query(func.count(Product.id)).filter(
            Product.seller_id == seller_id,
            Product.status == True,
            Product.quantity < 5
        ).scalar() or 0

        valor_estoque = db.session.query(
            func.coalesce(func.sum(Product.price * Product.quantity), 0)
        ).filter(
            Product.seller_id == seller_id,
            Product.status == True
        ).scalar() or 0

        vendas_stats = db.session.query(
            func.coalesce(func.sum(Venda.quantidade * Venda.preco_unitario), 0).label("total_vendido"),
            func.coalesce(func.avg(Venda.quantidade * Venda.preco_unitario), 0).label("ticket_medio"),
            func.coalesce(func.sum(Venda.quantidade), 0).label("unidades_vendidas"),
            func.count(Venda.id).label("num_vendas")
        ).filter(
            Venda.seller_id == seller_id
        ).first()

        ultimas_vendas_rows = db.session.query(
            Venda, Product.name.label("produto_nome")
        ).join(
            Product, Venda.produto_id == Product.id
        ).filter(
            Venda.seller_id == seller_id
        ).order_by(
            Venda.created_at.desc()
        ).limit(6).all()

        ultimas_vendas = [
            {
                "id": row.Venda.id,
                "produto_id": row.Venda.produto_id,
                "produto_nome": row.produto_nome,
                "quantidade": row.Venda.quantidade,
                "preco_unitario": float(row.Venda.preco_unitario),
                "total": float(row.Venda.quantidade * row.Venda.preco_unitario),
                "created_at": row.Venda.created_at.isoformat()
            }
            for row in ultimas_vendas_rows
        ]

        return {
            "total_produtos": total_produtos or 0,
            "produtos_ativos": produtos_ativos or 0,
            "estoque_baixo": estoque_baixo or 0,
            "valor_estoque": float(valor_estoque or 0),
            "resumo_vendas": {
                "total_vendido": float(vendas_stats.total_vendido) if vendas_stats else 0.0,
                "ticket_medio": float(vendas_stats.ticket_medio) if vendas_stats else 0.0,
                "unidades_vendidas": int(vendas_stats.unidades_vendidas) if vendas_stats else 0,
                "num_vendas": int(vendas_stats.num_vendas) if vendas_stats else 0
            },
            "ultimas_vendas": ultimas_vendas
        }
