from flask_restful import Resource, reqparse, abort
from flask import jsonify
from flask import request
from sqlalchemy import or_, join
from src.models.jinbutu import JinbutudensModel, JinbutudensSchema
from src.models.locations import LocationsModel, LocationsSchema
from src.models.places import PlacesModel, PlacesSchema
from src.models.shishis import ShishisModel, ShishisSchema
from src.models.digitals import DigitalsModel, DigitalsSchema
from src.models.webmaps_with_image import WebmapsWithImageModel, WebmapsWithImageSchema
from src.database import db

class LocationsAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('keyword', required=True)
        self.reqparse.add_argument('jinbutsu', required=True)
        self.reqparse.add_argument('shishi', required=True)
        self.reqparse.add_argument('digital', required=True)
        self.reqparse.add_argument('webmap', required=True)
        super(LocationsAPI, self).__init__()

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
                list = []
                allJson.append({
                    'title': json['paragraph_title'],
                    'description': json['paragraph_body'],
                    'img': json['image_url'],
                    'kind': 1,
                    'places':list
                })
        if (use_webmap == "true"):
            results = WebmapsWithImageModel.query.filter(
                                                        or_(WebmapsWithImageModel.title.like(f'%{keyword}%'),
                                                        WebmapsWithImageModel.description.like(f'%{keyword}%')
                                                           )
            )
            jsonData = WebmapsWithImageSchema(many=True).dump(results)
            for json in jsonData:
                list = []
                allJson.append({
                    'title': json['title'],
                    'description': json['description'],
                    'img': json['image'],
                    'kind': 2,
                    'places': list
                })
        if (use_digital == "true"):
            results = DigitalsModel.query.filter(
                                                or_(DigitalsModel.title.like(f'%{keyword}%'),
                                                    DigitalsModel.contents.like(f'%{keyword}%')
                                                    )
            )
            jsonData = DigitalsSchema(many=True).dump(results)
            for json in jsonData:
                list = []
                allJson.append({
                    'title': json['title'],
                    'description': json['contents'],
                    'img': json['img_url'],
                    'kind': 3,
                    'places':list
                })
        if (use_jinbutsu == "true"):
            results = JinbutudensModel.query.filter(
                                                    or_(JinbutudensModel.name.like(f'%{keyword}%'),
                                                        JinbutudensModel.description.like(f'%{keyword}%')
                                                        )
            )
            jsonData = JinbutudensSchema(many=True).dump(results)
            for json in jsonData:
                list = []
                name = json['name'].strip("\n")
                places = db.session.query(PlacesModel.name, PlacesModel.place, LocationsModel.lat, LocationsModel.lon).join(LocationsModel, PlacesModel.place == LocationsModel.place).filter(PlacesModel.name == name).all()

                if len(places) != 0 :
                    for place in places :
                        print(place[0],name)
                        list.append({
                            'id': place[0],
                            'lat': place[2],
                            'lng': place[3],
                            'name': place[0] + "_" +place[1],
                            'icon':'',
                            'selected_icon': ''
                        })
                
                allJson.append({
                    'title': json['name'],
                    'description': json['description'],
                    'img': json['imageUrl'],
                    'kind': 4,
                    'places': list
                })
                
            print(count)

        return jsonify(allJson)