from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Controllers.dashboard_controller import DashboardController

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboards')

@dashboard_bp.route("", methods=['GET'])
@jwt_required()
def relatorio_dashboard():
    seller_id = int(get_jwt_identity())
    return DashboardController.get_dashboard(seller_id)
