"""Users Endpoints"""
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError 
from src.models import db, Users


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

    data_new_user = request.get_json()

    if not 'email' in data_new_user or not 'password' in data_new_user:
        return jsonify({'error':'Bad Request: No email or password provided in body'}), 400

    new_user = Users(
        name=data_new_user['name'],
        email=data_new_user['email'],
        password=data_new_user['password']
    )

    try:

        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email
        }), 201

    except IntegrityError:

        db.session.rollback()

        return jsonify({'error':'Conflict: User with email already exists'}), 409
    

#---Modificar un usuario---#
@users_blueprint.route('/users/<uid>', methods = ['PATCH'])

def modify_user(uid):
    """Modify a user"""

    user = Users.query.get(uid) #Consulta por id

    if not user:
        return jsonify({'error': 'Not Found: User does not exist'}), 404

    data_modify_user = request.get_json(silent=True)

    if not data_modify_user:
        return jsonify({'error': 'Bad Request: No request body'}), 400

    if 'email' in data_modify_user or 'password' in data_modify_user:
        return jsonify({'error': 'Bad Request: Updating email or password is not allowed'}), 400

    if 'name' in data_modify_user:
        user.name = data_modify_user['name']

    db.session.commit()

    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email
    }), 200
    


