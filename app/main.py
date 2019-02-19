from flask import Flask, Blueprint
from app.api.controller.companies import ns as companies_namespace
from app.api.controller.people import ns as people_namespace
from app.api.api import api
from app.api.db import db
from app.config import config_by_name


class Server(object):

    def __init__(self,config_name):
        self.app = Flask(__name__)
        self.app.config.from_object(config_by_name[config_name])
        blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = api
        self.api.init_app(blueprint)
        self.api.add_namespace(companies_namespace)
        self.api.add_namespace(people_namespace)
        self.app.register_blueprint(blueprint)
        db.init_app(self.app)



    def run(self):
        self.app.run()

server = Server('dev')


if __name__ == '__main__':
    server.run()