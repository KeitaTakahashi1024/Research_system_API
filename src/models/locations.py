from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class LocationsModel(db.Model):
    __tablename__ = 'locations'

    place = db.Column(db.String(255), primary_key=True)
    lat = db.Column(db.String(255))
    lon = db.Column(db.String(255))

    def __init__(self, place, lat, lon):
        self.place = place
        self.lat = lat
        self.lon = lon

class  LocationsSchema(ma.ModelSchema):
    class Meta:
        model = LocationsModel