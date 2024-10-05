from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'
    
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    # Ensure 'id' is serialized
    serialize_rules = ('id', 'magnitude', 'location', 'year')

    def __repr__(self):
        return f'<Earthquake {self.id} - {self.location} ({self.year})>'
