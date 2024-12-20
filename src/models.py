from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #Crea instancia SQLAlchemy

class Taxi(db.Model):
    """Modelo-Taxis"""
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String, nullable=False)
    trajectories = db.relationship('Trajectory', backref='taxi') #Relación uno a muchos

    def to_dictionary(self):
        return{
            'id': self.id,
            'plate': self.plate
        }

class Trajectory(db.Model):
    """Modelo-Trajectories"""
    __tablename__ = 'trajectories'

    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, db.ForeignKey('taxis.id'),nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def to_dictionary(self):
        return{
            'id': self.id,
            'plate': self.taxi.plate,
            'taxiId': self.taxi_id,
            'date':self.date,
            'latitude':self.latitude,
            'longitude':self.longitude
        }

class Users(db.Model):
    """Modelo-Users"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def to_dictionary(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }