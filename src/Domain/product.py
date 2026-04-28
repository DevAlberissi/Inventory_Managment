class ProductDomain:
    def __init__(self, id, name, price, quantity, status, image_url, seller_id):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self.image_url = image_url
        self.seller_id = seller_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": float(self.price),
            "quantity": self.quantity,
            "status": self.status,
            "image_url": self.image_url,
            "seller_id": self.seller_id
        }
