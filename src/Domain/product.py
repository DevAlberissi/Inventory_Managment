class ProductDomain:
    def __init__(self, id, name, price, quantity, status, seller_id, documentos=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self.seller_id = seller_id
        self.documentos = documentos or []

    def to_dict(self):
        imagens = [d for d in self.documentos if d.get("mime_type", "").startswith("image/")]
        return {
            "id": self.id,
            "name": self.name,
            "price": float(self.price),
            "quantity": self.quantity,
            "status": self.status,
            "seller_id": self.seller_id,
            "imagens": imagens,
            "documentos": self.documentos
        }
