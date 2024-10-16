from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #Crea instancia SQLAlchemy

class Taxi(db.Model):
    """Modelo-Tabla Taxis"""
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)

    def dictionary(self):
        return{
            'id': self.id,
            'plate': self.plate
        }

class Trajectory(db.Model):
    """Modelo-Tabla Trajectories"""
    __tablename__ = 'trajectories'

    id = db.Column(db.Integer, primary_key=True)
    taxiId = db.Column(db.Integer, db.ForeignKey('taxis.id'),nullable=False)
    date = db.Column(db.TIMESTAMP, nullable=False)
    latitude = db.Column(db.DOUBLE_PRECISION, nullable=False)
    longitude = db.Column(db.DOUBLE_PRECISION, nullable=False)

    def dictionary(self):
        return{
            'id': self.id,
            'taxiId': self.taxiId,
            'date':self.date,
            'latitude':self.latitude,
            'longitude':self.longitude
        }
