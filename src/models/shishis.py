from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class ShishisModel(db.Model):
    __tablename__ = 'hakodateshishi'

    id = db.Column(db.Integer, primary_key=True)
    paragraph_title = db.Column(db.String)
    paragraph_body = db.Column(db.String)
    url = db.Column(db.String(255))
    image_url = db.Column(db.String(1200))

    def __init__(self, paragraph_title, paragraph_body, url, image_url):
        self.paragraph_title = paragraph_title
        self.paragraph_body = paragraph_body
        self.url = url
        self.image_url = image_url

class ShishisSchema(ma.ModelSchema):
    class Meta:
        model = ShishisModel