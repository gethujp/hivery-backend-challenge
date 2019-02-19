from flask_restplus import fields
from app.api.api import api


dummy_list=api.model('dummy_list', {
    'title': fields.String(required=True, description='Company name'),
})

company_list = api.model('Company', {
    'index': fields.Integer(readOnly=True, description='The unique identifier of a company'),
    'company': fields.String(required=True, description='Company name'),
})

company_model = api.model('Company_model', {
    'index': fields.Integer(readOnly=True, description='The unique identifier of a company'),
    'company': fields.String(required=True, description='Company name'),
})


people_model = api.model('People_model', {
    'index': fields.Integer(readOnly=True, description='The unique identifier of a person'),
    'name': fields.String(readOnly=True, description='Person name'),
    'age': fields.Integer(readOnly=True, description='Age of the person'),
    'email': fields.String(readOnly=True, description='Email of the person'),
    'phone': fields.String(readOnly=True, description='Phone number of the person'),
})

people_model_list = api.model('People List',{'peoples':fields.List(fields.Nested(people_model)),})

fav_food_api_model=api.model('fav_food_api_model', {
    'user_name': fields.String(readOnly=True, description='Person name'),
    'age': fields.Integer(readOnly=True, description='Age of the person'),
    'fruits':fields.List(fields.String(readOnly=True, description='Favourite fruits')),
    'vegetables':fields.List(fields.String(readOnly=True,description='Favourite vegetables')),
})


mutual_friends_model = api.inherit('mutual_friends_model',{
    'person_1':fields.Nested(people_model),
    'person_2':fields.Nested(people_model),                 
    'mutual_friends': fields.List(fields.Nested(people_model))
})