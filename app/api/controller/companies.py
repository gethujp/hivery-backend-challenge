import logging

from flask import request
from flask_restplus import Resource,abort
from app.api.models.models import company_model,company_list,dummy_list
from app.api.api import api
from app.api.db import db as mongo
from app.api.services.service import Companies,People

from werkzeug.exceptions import BadRequest,NotFound




log = logging.getLogger(__name__)

company_db = [{"id":0,"title":"chumma"},
              {"id":4,"title":"Jp company"}]
ns = api.namespace('companies', description='Operations related to companies')

@ns.errorhandler(NotFound)
def handle_not_found(e):
    
    return {'message': e}, 404

@ns.route('/list')
class CompanyList(Resource):

    @api.marshal_list_with(company_model)
    def get(self):
        """
        Returns list of Companies.
        """
        try:
            response = Companies().list_all()
            return response
        except Exception as e:
            print e
        #return company_db;

@ns.route('/<name>')
@ns.response(200,'Success')
@ns.response(404,'Company not found')
@ns.response(400,'Bad request')
class CompanyItem(Resource):
    @api.marshal_with(company_model)
    def get(self, name):
        """
        Returns a matching company
        """
        print name
        response = Companies().find_one(name)

        if not response:
            abort(404,'Requested Company not found')
        else:
            return response
