from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class JinbutsudensModel(db.Model):
    __tablename__ = 'jinbutsudens'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    nameYomi = db.Column(db.String(255))
    dateBorn = db.Column(db.String(255))
    dateDeath = db.Column(db.String(255))
    catchWord = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String(255))
    imgUrl = db.Column(db.String(255))

    def __init__(self, name, nameYomi, dateBorn, dateDeath,
                 catchWord, description, url, imgUrl):
        self.name = name
        self.nameYomi = nameYomi
        self.dateBorn = dateBorn
        self.dateDeath = dateDeath
        self.catchWord = catchWord
        self.description = description
        self.url = url
        self.imgUrl = imgUrl

class JinbutsudensSchema(ma.ModelSchema):
    class Meta:
        model = JinbutsudensModel