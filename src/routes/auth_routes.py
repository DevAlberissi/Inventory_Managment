from flask import Blueprint
from src.Application.Controllers.user_controller import UserController

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login_user():
    return UserController.login_user()
