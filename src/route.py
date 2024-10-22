"""Taxis endpoint"""
from flask import Blueprint, jsonify, request
from src.models import Taxi, Trajectory
from datetime import datetime 
from src.models import db

taxi_blueprint = Blueprint('taxi_blueprint', __name__)#Crea el blueprint para taxis

#Endpoint: responde a la petición 'GET'
@taxi_blueprint.route('/taxis', methods = ['GET'])
def get_taxis():
    #Params de consulta de la solicitud HTTP
    plate = request.args.get('plate')
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    if page < 1 or limit < 1:
        return jsonify({'error': 'Bad Request: Page or limit is not valid'}), 400

    database_query = Taxi.query #Realiza consulta en la tabla Taxis

    if plate:
        filtered_query = database_query.filter(Taxi.plate.like('%'+plate+'%'))
    else:
        filtered_query = database_query

    taxis = filtered_query.paginate(page=page, per_page=limit) #Paginar los resultados  
        
    return jsonify([taxi.to_dictionary() for taxi in taxis]), 200


"""Trajectories Endpoint"""
trajectory_blueprint = Blueprint('trajectory_blueprint', __name__) #Crea el blueprint para trajectories

@trajectory_blueprint.route('/trajectories', methods = ['GET'])
def get_trajectories():

    taxiId = request.args.get('taxiId')
    date = request.args.get('date')

    date_DMY = datetime.strptime(date, '%d-%m-%Y') #Param solo acepta formato DD-MM-YYYY

    database_query = Trajectory.query.filter(
        Trajectory.taxi_id == taxiId, 
        db.func.date(Trajectory.date) == date_DMY.date()
        )

    trajectories = database_query.all()

    return jsonify([trajectory.to_dictionary() for trajectory in trajectories]),200