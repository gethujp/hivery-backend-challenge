from app.api.db import db as mongo
from bson.json_util import dumps
import json
class Companies(object):
    def __init__(self):
        self.companies = mongo.db.companies

    def find_one(self,company_name):
        company_db = self.companies.find_one({'company': str(company_name).upper()})
        print(company_db)
        return company_db

    def list_all(self):
        company_list = json.loads(dumps(self.companies.find()))
        return company_list


class People(object):
    def __init__(self):
        self.people = mongo.db.people


    def find_people_in_company(self,company_id):
        return json.loads(dumps(self.people.find({'company_id': company_id})))

    def find_people_by_name(self,name):
        return self.people.find_one({'name':name})

    def find_mutual_friends(self,person_one,person_two,eye_colour,died_flg):
        mutual_friends_object = [i for i in person_one['friends'] if i in person_two['friends']]
        mutual_friends_indices=[friend_index['index'] for friend_index in mutual_friends_object]
        return json.loads(dumps(self.find_people_list(mutual_friends_indices,eye_colour,died_flg)))


    def find_people_list(self,id_list,eye_colour,died_flg):
        return self.people.find({ "index":{"$in":id_list}, "eyeColor":eye_colour,"has_died":died_flg });

    def find_fav_food(self,person_data):
        total_fruit_list = ['orange', 'apple', 'banana', 'strawberry']
        response = {}
        if person_data is not None:
            fruitlist = []
            vegList = []
            fruitlist.extend(fruit for fruit in person_data['favouriteFood'] if fruit in total_fruit_list)
            vegList.extend(veg for veg in person_data['favouriteFood'] if veg not in total_fruit_list);
            response['fruits'] = fruitlist
            response['vegetables'] = vegList
            response['age']=person_data['age']
            response['user_name'] = person_data['name']
        return response



