from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class WebmapsModel(db.Model):
    __tablename__ = 'webmaps'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String)
    url = db.Column(db.String(255))

    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

class WebmapsSchema(ma.ModelSchema):
    class Meta:
        model = WebmapsModel