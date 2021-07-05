from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class WebmapImagesModel(db.Model):
    __tablename__ = 'webmap_images'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    image = db.Column(db.String(255))

    def __init__(self, title, image):
        self.title = title
        self.image = image

class WebmapImagesSchema(ma.ModelSchema):
    class Meta:
        model = WebmapImagesModel