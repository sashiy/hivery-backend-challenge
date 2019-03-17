from flask_restplus import Namespace, Resource

from paranuara_api.main.controller.base_controller import BaseController, logging
from paranuara_api.main.service import people_service as ps

api = Namespace('people', description='Get information regarding people')


@api.route('/<person_id>')
@api.param('person_id', 'Person identifier')
class PersonFavouriteFood(Resource, BaseController):
    @api.doc('Retrieve all people of a company')
    def get(self, person_id):
        """
        This method acts as a main serving point for the Persons favourite food API, after receiving person_id as a input,
        it fetches all the relevant information regarding the person and returns what is essential
        :param person_id: unique identifier of the person (_id attribute in people.json)
        :return: Essential information of person like, name, age, favourite fruits and favourite vegetables
        """
        response = {}
        person_ref = ps.PeopleService()
        person_details = person_ref.get_person_details(person_id)
        if person_details is not None and person_details['_id'] is not '':
            vegetables, fruits = person_ref.person_favourite_food(person_details)
            response['username'] = person_details['name']
            response['age'] = person_details['age']
            response['fruits'] = list(set(fruits)) if fruits is not None and len(fruits) > 0 else []
            response['vegetables'] = list(set(vegetables)) if vegetables is not None and len(vegetables) > 0 else []
            return response
        else:
            return {'data': 'Error: User doesn''t exist. Please try with valid input.'}


@api.route('/<person_1_id>/<person_2_id>')
@api.param('person_1_id', 'Person 1 identifier')
@api.param('person_2_id', 'Person 2 identifier')
class PeopleCommonFriends(Resource, BaseController):
    @api.doc('Retrieve common friends between two people')
    def get(self, person_1_id, person_2_id):
        """
        This method, on receiving two valid identifiers of two people, complies the friends list fo figure out list of common friends who
        are still alive and have brown eyes and return essential information regarding each
        :param person_1_id: unique identifier of the person 1(_id attribute in people.json)
        :param person_2_id: unique identifier of the person 2(_id attribute in people.json)
        :return: Essential information of person 1 &2 including all the common friends
        """
        response = {}
        if person_1_id != person_2_id:
            person_ref = ps.PeopleService()
            p1_details = person_ref.get_person_details(person_1_id)
            p2_details = person_ref.get_person_details(person_2_id)
            if p1_details is not None and p2_details is not None:
                response['person_1'] = self._create_dict_for_response(p1_details)
                response['person_2'] = self._create_dict_for_response(p2_details)
                common_friends = person_ref.get_common_friend_list(p1_details, p2_details)
                if common_friends is not None and len(common_friends) > 0:
                    response['friends_in_common'] = []
                    for friend in common_friends:
                        response['friends_in_common'].append(self._create_dict_for_response(friend))
                    return response
                else:
                    message = {'data': 'Error: There are no common friends between these people!'}
                    logging.info(message)
                    return message
            else:
                message = {'data': 'Error: Either {} or {} people does not exist'.format(person_1_id, person_2_id)}
                logging.info(message)
                return message
        else:
            message = {'data': 'Error {} and {} are same, please provide different user identifiers'.format(person_1_id,
                                                                                                            person_2_id)}
            logging.info(message)
            return message
