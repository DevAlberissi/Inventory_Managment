class VendaDomain:
    def __init__(self, id, quantity, price):
        self.id = id
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "price": self.price,
        }
