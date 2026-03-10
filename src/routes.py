from src.Application.Controllers.user_controller import UserController
from flask import jsonify, make_response

def init_routes(app):
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    

