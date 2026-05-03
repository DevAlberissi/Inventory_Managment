class DocumentoDomain:
    def __init__(self, id, product_id, nome_arquivo, mime_type, conteudo=None):
        self.id = id
        self.product_id = product_id
        self.nome_arquivo = nome_arquivo
        self.mime_type = mime_type
        self.conteudo = conteudo

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "nome_arquivo": self.nome_arquivo,
            "mime_type": self.mime_type,
        }
