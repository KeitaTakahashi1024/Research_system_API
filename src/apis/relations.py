from flask_restful import Resource, reqparse, abort
from flask import jsonify
from flask import request
from src.models.relations import RelationsModel, RelationsSchema
from src.database import db

class RelationsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', required=True)
        self.reqparse.add_argument('kind', required=True)
        super(RelationsAPI, self).__init__()

    def post(self):
        results = [];
        args = self.reqparse.parse_args()
        recordId = int(args['id'])
        recordKind = int(args['kind'])

        if (recordKind == 4):
            results = RelationsModel.query.filter(RelationsModel.person_id == recordId)
            jsonData = RelationsSchema(many=True).dump(results)
            return jsonify(jsonData)
        else:
            results = RelationsModel.query.filter(RelationsModel.record_id == recordId,
                                                  RelationsModel.record_kind == recordKind)
            jsonData = RelationsSchema(many=True).dump(results)
            return jsonify(jsonData)
