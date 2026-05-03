from src.Domain.documento import DocumentoDomain
from src.Infrastructure.Model.documento import Documento
from src.config.data_base import db

class DocumentoService:
    @staticmethod
    def create_documento(product_id, nome_arquivo, mime_type, conteudo):
        doc = Documento(
            product_id=product_id,
            nome_arquivo=nome_arquivo,
            mime_type=mime_type,
            conteudo=conteudo,
        )
        db.session.add(doc)
        db.session.commit()
        return DocumentoDomain(doc.id, doc.product_id, doc.nome_arquivo, doc.mime_type)

    @staticmethod
    def list_documentos(product_id):
        docs = Documento.query.filter_by(product_id=product_id).all()
        return [DocumentoDomain(d.id, d.product_id, d.nome_arquivo, d.mime_type) for d in docs]

    @staticmethod
    def get_documento(documento_id):
        doc = Documento.query.get(documento_id)
        if not doc:
            return None
        return DocumentoDomain(doc.id, doc.product_id, doc.nome_arquivo, doc.mime_type, doc.conteudo)

    @staticmethod
    def delete_documento(documento_id):
        doc = Documento.query.get(documento_id)
        if not doc:
            return False
        db.session.delete(doc)
        db.session.commit()
        return True
