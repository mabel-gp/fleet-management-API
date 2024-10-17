from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #Crea instancia SQLAlchemy

class Taxi(db.Model):
    """Modelo-Taxis"""
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
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
            'taxiId': self.taxi_id,
            'date':self.date,
            'latitude':self.latitude,
            'longitude':self.longitude
        }
