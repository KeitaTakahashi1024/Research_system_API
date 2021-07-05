from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class PlacesModel(db.Model):
    __tablename__ = 'places'

    name = db.Column(db.String(255), primary_key=True)
    place = db.Column(db.String(255), primary_key=True)

    def __init__(self, name, place):
        self.name = name
        self.place = place

class  PlacesSchema(ma.ModelSchema):
    class Meta:
        model = PlacesModel