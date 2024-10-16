import os #Para trabajar con las env-var
from flask import Flask
from dotenv import load_dotenv
from src.model import db
from src.route import tx_bp, tj_bp

load_dotenv(dotenv_path = '.env.development.local') #Cargar env-var

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') #Se carga la env-var
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)  #Conecta la instancia SQLALchemy con Flask
app.register_blueprint(tx_bp) #Blueprint Taxis
app.register_blueprint(tj_bp) #Blueprint Trajectories

if __name__ == '__main__':
    app.run(debug=True)
