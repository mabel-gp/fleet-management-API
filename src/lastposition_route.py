"""Last Position Endpoint"""
from flask import Blueprint, request

lastPosition_blueprint = Blueprint('lastPosition_blueprint', __name__)

@lastPosition_blueprint.route('/trajectories/latest', methods = ['GET'])
def get_lastPosition():

    #En construcción
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

