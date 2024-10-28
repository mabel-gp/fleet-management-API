"""Last Position Endpoint"""
from flask import Blueprint, jsonify
from sqlalchemy import desc
from src.models import Trajectory

lastPosition_blueprint = Blueprint('lastPosition_blueprint', __name__)

@lastPosition_blueprint.route('/trajectories/latest', methods = ['GET'])
def get_lastPosition():

    #Consulta: último trayectoria de la tabla trajectories
    database_query = Trajectory.query.order_by(
        desc(Trajectory.date)
        ).first()

    dict_latest_trajectory = {
        'taxiId': database_query.taxi_id,
        'date': database_query.date,
        'latitude': database_query.latitude,
        'longitude': database_query.longitude,
    }
    return jsonify(dict_latest_trajectory), 200




    
