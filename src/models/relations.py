from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

ma = Marshmallow()

class RelationsModel(db.Model):
    __tablename__ = 'relations'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    record_id = db.Column(db.Integer)
    person_name = db.Column(db.String(255))
    person_desc = db.Column(db.String)
    person_img = db.Column(db.String(255))
    record_title = db.Column(db.String(255))
    record_desc = db.Column(db.String)
    record_kind = db.Column(db.Integer)
    record_img = db.Column(db.String(1200))
    relate_words = db.Column(db.String(255))

    def __init__(self, person_id, record_id, person_name, person_desc, person_img,
                record_title, record_desc, record_kind, record_img, relate_words):
        self.person_id = person_id
        self.record_id = record_id
        self.person_name = person_name
        self.person_desc = person_desc
        self.person_img = person_img
        self.record_title = record_title
        self.record_desc = record_desc
        self.record_kind = record_kind
        self.record_img = record_img
        self.relate_words = relate_words
    def __repr__(self):
        return '<person_name %r>' % self.person_name

class RelationsSchema(ma.ModelSchema):
    class Meta:
        model = RelationsModel