from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class DigitalsModel(db.Model):
    __tablename__ = 'digitals_distinct'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    contents = db.Column(db.String)
    url = db.Column(db.String(255))
    img_url = db.Column(db.String(255))

    def __init__(self, title, contents, url, img_url):
        self.title = title
        self.contents = contents
        self.url = url
        self.img_url = img_url

class DigitalsSchema(ma.ModelSchema):
    class Meta:
        model = DigitalsModel