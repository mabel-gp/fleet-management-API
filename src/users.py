"""Users Endpoints"""
from flask import Blueprint, jsonify, request
from src.models import Users

#---Lista de Usuarios---#
users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/users', methods = ['GET'])
def users():
    """List users"""
    page = request.args.get('page',default=1)
    limit = request.args.get('limit', default=10)

    # Values no válidos(x or y)
    try:
        page = int(page)
        limit = int(limit)
    except ValueError:
        return jsonify({'error': 'Bad Request: Page or limit is not valid'}), 400
    
    # Values no válidos(negativos)
    if page <1 or limit <1:
        return jsonify({'error': 'Bad Request: Page or limit is not valid'}), 400

    database_query = Users.query.limit(limit).all()

    return jsonify([user.to_dictionary() for user in database_query]), 200


#---Crear un usuario---#
@users_blueprint.route('/users', methods = ['POST'])

def create_user():
    """Create a user"""

    new_user = request.json

    return jsonify(new_user), 201
