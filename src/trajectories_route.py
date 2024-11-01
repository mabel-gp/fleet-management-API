"""Trajectories Endpoint"""
from datetime import datetime 
from flask import Blueprint, jsonify, request
from src.models import Taxi, Trajectory, db


trajectory_blueprint = Blueprint('trajectory_blueprint', __name__) #Crea el blueprint para trajectories

@trajectory_blueprint.route('/trajectories', methods = ['GET'])
def get_trajectories():

    taxiId = request.args.get('taxiId')
    date = request.args.get('date')


    #SC-400 => si el param 'taxi' no es proporcionado
    if taxiId is None:
        return jsonify({'error':'Missing taxiId parameter'}),400
    
    #SC-404 => si el taxi no es encontrado
    taxi = Taxi.query.get(taxiId)
    if taxi is None:
        return jsonify({'error':'taxiId not found'}),404
    
    #SC-400 => si el param 'date' no es proporcionado
    if date is None:
        return jsonify({'error':'Missing date parameter'}),400

    #SC-400 => si el formato de 'date' no es DD-MM-YYYY
    try:
        date_DMY = datetime.strptime(date, '%d-%m-%Y') #Param solo acepta formato DD-MM-YYYY
    except ValueError:
        return jsonify({'error': 'Badly formated date'}),400


    database_query = Trajectory.query.filter(
        Trajectory.taxi_id == taxiId, 
        db.func.date(Trajectory.date) == date_DMY.date()
        )

    trajectories = database_query.all()

    return jsonify([trajectory.to_dictionary() for trajectory in trajectories]),200