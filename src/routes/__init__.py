from src.routes.auth_routes import auth_bp
from src.routes.user_routes import user_bp
from src.routes.product_routes import products_bp
from src.routes.documento_routes import documentos_bp
from src.routes.venda_routes import venda_bp

def init_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(documentos_bp)
    app.register_blueprint(venda_bp)
