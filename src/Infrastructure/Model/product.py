from src.config.data_base import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Boolean, nullable=False, default=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    documentos = db.relationship('Documento', backref='product', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": float(self.price),
            "quantity": self.quantity,
            "status": self.status,
            "seller_id": self.seller_id
        }
