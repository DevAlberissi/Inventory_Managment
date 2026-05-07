class VendaDomain:
    def __init__(self, id, produto_id, seller_id, quantidade, preco_unitario, created_at, produto=None):
        self.id = id
        self.produto_id = produto_id
        self.seller_id = seller_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.created_at = created_at
        self.produto = produto

    def to_dict(self):
        data = {
            "id": self.id,
            "produto_id": self.produto_id,
            "seller_id": self.seller_id,
            "quantidade": self.quantidade,
            "preco_unitario": float(self.preco_unitario),
            "created_at": self.created_at.isoformat()
        }
        if self.produto is not None:
            data["produto"] = self.produto
        return data
