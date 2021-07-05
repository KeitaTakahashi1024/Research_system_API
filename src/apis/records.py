from flask_restful import Resource, reqparse, abort
from flask import jsonify
from flask import request
from sqlalchemy import or_
from src.models.jinbutsudens import JinbutsudensModel, JinbutsudensSchema
from src.models.shishis import ShishisModel, ShishisSchema
from src.models.digitals import DigitalsModel, DigitalsSchema
from src.models.webmaps_with_image import WebmapsWithImageModel, WebmapsWithImageSchema
from src.database import db


class RecordsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('keyword', required=True)
        self.reqparse.add_argument('jinbutsu', required=True)
        self.reqparse.add_argument('shishi', required=True)
        self.reqparse.add_argument('digital', required=True)
        self.reqparse.add_argument('webmap', required=True)
        super(RecordsAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        keyword = args['keyword']
        use_jinbutsu = args['jinbutsu']
        use_shishi = args['shishi']
        use_digital = args['digital']
        use_webmap = args['webmap']

        allJson = []
        if (use_shishi == "true"):
            results = ShishisModel.query.filter(
                                                or_(ShishisModel.paragraph_title.like(f'%{keyword}%'),
                                                    ShishisModel.paragraph_body.like(f'%{keyword}%')
                                                   )
            )
            jsonData = ShishisSchema(many=True).dump(results)
            for json in jsonData:
                allJson.append({
                    'id': json['id'],
                    'title': json['paragraph_title'],
                    'description': json['paragraph_body'],
                    'img': json['image_url'],
                    'kind': 1
                })
        if (use_webmap == "true"):
            results = WebmapsWithImageModel.query.filter(
                                                        or_(WebmapsWithImageModel.title.like(f'%{keyword}%'),
                                                        WebmapsWithImageModel.description.like(f'%{keyword}%')
                                                           )
            )
            jsonData = WebmapsWithImageSchema(many=True).dump(results)
            for json in jsonData:
                allJson.append({
                    'id': json['id'],
                    'title': json['title'],
                    'description': json['description'],
                    'img': json['image'],
                    'kind': 2
                })
        if (use_digital == "true"):
            results = DigitalsModel.query.filter(
                                                or_(DigitalsModel.title.like(f'%{keyword}%'),
                                                    DigitalsModel.contents.like(f'%{keyword}%')
                                                    )
            )
            jsonData = DigitalsSchema(many=True).dump(results)
            for json in jsonData:
                allJson.append({
                    'id': json['id'],
                    'title': json['title'],
                    'description': json['contents'],
                    'img': json['img_url'],
                    'kind': 3
                })
        if (use_jinbutsu == "true"):
            results = JinbutsudensModel.query.filter(
                                                    or_(JinbutsudensModel.name.like(f'%{keyword}%'),
                                                        JinbutsudensModel.description.like(f'%{keyword}%')
                                                        )
            )
            jsonData = JinbutsudensSchema(many=True).dump(results)
            for json in jsonData:
                allJson.append({
                    'id': json['id'],
                    'title': json['name'],
                    'description': json['description'],
                    'img': json['imgUrl'],
                    'kind': 4
                })
        return jsonify(allJson)