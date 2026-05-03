from src.config.data_base import db

class Documento(db.Model):
    __tablename__ = 'documentos'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    nome_arquivo = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.LargeBinary(length=16777215), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "nome_arquivo": self.nome_arquivo,
            "mime_type": self.mime_type,
        }
