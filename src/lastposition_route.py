"""Last Position Endpoint"""
from flask import Blueprint, jsonify
from sqlalchemy import select, func
from src.models import Taxi, Trajectory, db

lastPosition_blueprint = Blueprint('lastPosition_blueprint', __name__)

@lastPosition_blueprint.route('/trajectories/latest', methods = ['GET'])
def get_lastPosition():

    session = db.session() #Interacción con la database
    #Subconsulta 
    sub_query = (
        select(
            Trajectory.taxi_id,
            func.max(Trajectory.date).label('last_date')
        )
        .group_by(Trajectory.taxi_id)
        .subquery()
        )

    # Consulta principal
    main_query = (
        select(
            Trajectory.taxi_id,
            Taxi.plate,
            Trajectory.date,
            Trajectory.latitude,
            Trajectory.longitude
        )
        .join(sub_query, (Trajectory.taxi_id == sub_query.c.taxi_id)&(Trajectory.date == sub_query.c.last_date))
        .join(Taxi, Trajectory.taxi_id == Taxi.id)
        
    )

    last_trajectories = session.execute(main_query).all() # Ejecuta la consulta principal
    #List, contiene el dic
    last_trajc_dict = [
        {
        'taxiId': last_trajectory.taxi_id,
        'plate': last_trajectory.plate,
        'date': last_trajectory.date,
        'latitude': last_trajectory.latitude,
        'longitude': last_trajectory.longitude,
        }
        for last_trajectory in last_trajectories
    ]
    return jsonify(last_trajc_dict), 200




    
