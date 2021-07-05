from flask import Flask, jsonify
from flask_restful import Api
from src.database import init_db
from src.apis.relations import RelationsAPI
from src.apis.records import RecordsAPI
from src.apis.locations import LocationsAPI
import src.models
from flask_cors import CORS

def create_app():
  app = Flask(__name__)
  app.config['JSON_AS_ASCII'] = False
  app.config.from_object('src.config.Config')

  init_db(app)

  api = Api(app)
  api.add_resource(RelationsAPI, '/relations')
  api.add_resource(RecordsAPI, '/records')
  api.add_resource(LocationsAPI, '/locations')

  CORS(app)
  return app

app = create_app()