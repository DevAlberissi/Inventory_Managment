from datetime import datetime
from src.config.data_base import db

class Venda(db.Model):
    __tablename__ = 'vendas'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column('product_id', db.Integer, db.ForeignKey('products.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quantidade = db.Column('quantidade', db.Integer, nullable=False)
    preco_unitario = db.Column('preco_unitario', db.Numeric(10, 2), nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.utcnow)
