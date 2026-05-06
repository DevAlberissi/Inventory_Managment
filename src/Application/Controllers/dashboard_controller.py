from flask import request, jsonify, make_response
from src.Application.Service.dashboard_service import DashboardService

class DashboardController:
    @staticmethod
    def get_dashboard(seller_id):
        data = DashboardService.get_dashboard(seller_id)
        return jsonify(data)
    