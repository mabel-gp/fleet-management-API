""""Authentication Users Endpoint"""
from flask import Blueprint


auth_users_blueprint = Blueprint('auth_users_blueprint', __name__)

@auth_users_blueprint.route('/auth/login', methods = ['POST'])
def auth_users():
    """Authentication Users"""