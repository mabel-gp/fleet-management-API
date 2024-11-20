import os #Para trabajar con las env-var
from flask import Flask
from dotenv import load_dotenv
from src.models import db
from src.taxi_route import taxi_blueprint
from src.trajectories_route import trajectory_blueprint
from src.lastposition_route import lastPosition_blueprint
from src.users import users_blueprint
from src.auth_users import auth_users_blueprint

load_dotenv(dotenv_path = '.env.development.local') #Cargar env-var

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') #Se carga la env-var
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['KEY'] = os.getenv('KEY') #Cargar secret key para JWT

db.init_app(app)  #Conecta la instancia SQLALchemy con Flask
app.register_blueprint(taxi_blueprint) #Blueprint Taxis
app.register_blueprint(trajectory_blueprint) #Blueprint Trajectories
app.register_blueprint(lastPosition_blueprint) #Blueprint Trajectories
app.register_blueprint(users_blueprint) #Blueprint Users
app.register_blueprint(auth_users_blueprint) #Blueprint Autentication Users

if __name__ == '__main__':
    app.run(debug=True)
