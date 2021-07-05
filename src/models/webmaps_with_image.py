from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class WebmapsWithImageModel(db.Model):
    __tablename__ = 'webmaps_with_image'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    description = db.Column(db.String)
    image = db.Column(db.String(1000))

    def __init__(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image

class WebmapsWithImageSchema(ma.ModelSchema):
    class Meta:
        model = WebmapsWithImageModel