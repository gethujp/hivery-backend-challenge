import logging

from flask_restplus import Resource,abort
from app.api.models.models import people_model,fav_food_api_model,mutual_friends_model,people_model_list
from app.api.api import api
from app.api.services.service import People,Companies

from werkzeug.exceptions import BadRequest,NotFound



ns = api.namespace('people', description='Operations related to people')

@ns.errorhandler(NotFound)
def handle_not_found(e):
    return {'message': e}, 404


@ns.route('/company/<company_name>')
@api.response(404, 'Person not found.')
class PeopleInCompany(Resource):
    @api.marshal_with(people_model)
    def get(self, company_name):
        """
        Returns all people working in the given company
        """
        company_detail=Companies().find_one(company_name)
        if company_detail:
            response = People().find_people_in_company(company_detail['index'])
            if len(response)>0:
                return response
            else:
                abort(404, "No employees in the company")
        else:
            abort(404,"Requested Company not found")


@ns.route('/person/<person_name>')
@api.response(404, 'Person not found.')
class PersonData(Resource):
    @api.marshal_with(people_model)
    def get(self, person_name):
        """
        Returns the requested person details
        """
        response = People().find_people_by_name(person_name)
        return response

@ns.route('/mutual_friends/<person_1>/<person_2>')
@api.response(404, 'Person not found.')
class PersonMutualFriends(Resource):
    @api.marshal_with(mutual_friends_model)
    def get(self, person_1,person_2):
        """
        Returns Mutual friends data of two people.
        """
        people=People()
        person_1_data = people.find_people_by_name(person_1)
        person_2_data = people.find_people_by_name(person_2)
        if person_1_data and person_2_data:
            response=people.find_mutual_friends(person_1_data,person_2_data,'brown',False)
            return {"person_1":person_1_data,"person_2":person_2_data,"mutual_friends":response}
        elif person_1_data is None and person_2_data is None:
            abort(404,'{} and {} are not citizens of Paranura'.format(person_1,person_2))
        elif person_1_data is None:
            abort(404,'{} is not a citizen of Paranura'.format(person_1))
        else:
            abort(404,'{} is not a citizen of Paranura'.format(person_2))


@ns.route('/fav_food/<person_name>')
@api.response(404, 'Person not found.')
class PersonFavFood(Resource):
    @api.marshal_with(fav_food_api_model)
    def get(self,person_name):
        """
        Returns Favourite food of a person
        """
        people=People()
        person_data = people.find_people_by_name(person_name)
        if person_data:
            response = people.find_fav_food(person_data)
            return response
        else:
            abort(404, '{} is not a citizen of Paranura'.format(person_name))