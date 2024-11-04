"""Users Endpoints"""
from flask import Blueprint, jsonify
from src.models import Users

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/users', methods = ['GET'])
def users():

    database_query = Users.query.all()
    
    return jsonify([user.to_dictionary() for user in database_query]), 200