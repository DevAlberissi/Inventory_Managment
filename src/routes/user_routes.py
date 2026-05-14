from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Controllers.user_controller import UserController

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('', methods=['POST'])
def register_user():
    return UserController.register_user()

@user_bp.route('/activate', methods=['PATCH'])
def activate_user():
    return UserController.activate_user()

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user_id = int(get_jwt_identity())
    return UserController.get_me(user_id)

@user_bp.route('/me', methods=['PATCH'])
@jwt_required()
def update_user():
    user_id = int(get_jwt_identity())
    return UserController.update_user(user_id)
