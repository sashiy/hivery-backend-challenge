from paranuara_api.main import Config
from paranuara_api.main.utilities.utilities import read_data_from_file, logging


class PeopleService:

    def __init__(self):
        self._list_of_people = read_data_from_file(Config.PEOPLE_JSON)

    def _filter_people_list(self, key, value):
        """
        This method on receiving a key and a value, filters the data in people.json. For example, when key is _id and
        value is 123, this method traverses through entire JSON and extracts all the information where _id is 123
        :param key: Key on which data should be filtered
        :param value: Value for the Key provided
        :return: All matching information as a list
        """
        try:
            if self._list_of_people is not None and len(self._list_of_people) > 0:
                response = [c for c in self._list_of_people if c[key] == value]
                if response is not None and len(response) > 0:
                    return response
                else:
                    return None
            else:
                return None
        except Exception as e:
            logging.error(e)

    def get_person_details(self, person_id):
        """
        This method returns entire information of a person on receiving a person_id which
        is ideally _id in the perople.json
        :param person_id: _id attribute in people.json which is a unique identifier
        :return: Complete information regarding the person
        """
        try:
            person_details = self._filter_people_list('_id', person_id)
            if person_details is not None:
                return person_details[0]
            else:
                return None
        except Exception as e:
            logging.error(e)

    def get_people_in_a_company(self, company_id):
        """
        This method on accepting a valid company_id which is index attribute in companies.json,
        return list of all people who are employees to that particular company
        :param company_id: index of company from companies.json
        :return: List of employees for the given company
        """
        try:
            logging.info('Input {}'.format(company_id))
            company_to_people = self._filter_people_list('company_id', company_id)
            if company_to_people is not None and len(company_to_people) > 0:
                return company_to_people
            else:
                logging.info('Cannot find any people associated with company {}'.format(company_id))
                return None
        except Exception as e:
            logging.error(e)

    def get_common_friend_list(self, p1_details, p2_details):
        """
        This method on accepting details of 2 persons, extracts all the common friends between person 1 & person 2
        :param p1_details: Details of Person 1
        :param p2_details: Details of Person 2
        :return: List of common friends who are alive and having brown eyes
        """
        try:
            friend_list = []
            p1_friend_list = [i['index'] for i in p1_details['friends']]
            p2_friend_list = [i['index'] for i in p2_details['friends']]
            friends_in_common = list(set(p1_friend_list) & set(p2_friend_list))
            if friends_in_common is not None and len(friends_in_common) > 0:
                for person in friends_in_common:
                    person_details = self._filter_people_list('index', person)
                    if person_details is not None and len(person_details) > 0:
                        friend_list.append(person_details[0])
                return self._filter_for_people_alive_with_brown_eyes(friend_list)
            else:
                logging.info(
                    '{} and {} does not have any friends in common'.format(p1_details['name'], p2_details['name']))
                return None
        except Exception as e:
            logging.error(e)

    def _filter_for_people_alive_with_brown_eyes(self, friend_list):
        try:
            if friend_list is not None and len(friend_list) > 0:
                return [i for i in friend_list if
                        i['has_died'] is False and i['eyeColor'].lower() == 'brown']
            else:
                return None
        except Exception as e:
            logging.error(e)

    def person_favourite_food(self, person_details):
        """
        This method on receiving person details, extracts his/her favourite food and distinguishes fruits and
        vegetables from it.
        :param person_details: Person JSON
        :return: List of favourite fruits and list of favourite vegetables
        """
        try:
            if 'favouriteFood' in person_details.keys():
                fav_food = person_details['favouriteFood']
                vegetable_list = self._distinguish_vegetables(fav_food)
                fruits_list = self._distinguish_fruits(fav_food)
                return vegetable_list, fruits_list
            else:
                logging.info('Unable to fetch favourite food for person {}'.format(person_details['_id']))
                return None, None
        except Exception as e:
            logging.error(e)

    def _distinguish_vegetables(self, food_list):
        """
        This method on receiving list of favourite food for a person, distinguishes all the vegetables from it and returns
        them as a list. vegetables.json located in resources directory is used as a reference for this operation
        :param food_list: List of favourite food
        :return: vegetables from the list of favourite food
        """
        try:
            result = []
            vegetable_list_all = read_data_from_file(Config.VEGETABLES_JSON)
            if vegetable_list_all is not None and len(vegetable_list_all) > 0:
                for food in food_list:
                    result = result + [i for i in vegetable_list_all['vegetables'] if i.lower() == food.lower()]
                return result
            else:
                return None
        except Exception as e:
            logging.error(e)
            return None

    def _distinguish_fruits(self, food_list):
        """
        This method on receiving list of favourite food for a person, distinguishes all the fruits from it and returns
        them as a list. fruits.json located in resources directory is used as a reference for this operation
        :param food_list: List of favourite food
        :return: Fruits from the list of favourite food
        """
        try:
            result = []
            fruit_list_all = read_data_from_file(Config.FRUITS_JSON)
            if fruit_list_all is not None and len(fruit_list_all) > 0:
                for food in food_list:
                    result = result + [i for i in fruit_list_all['fruits'] if i.lower() == food.lower()]
                return result
            else:
                return None
        except Exception as e:
            logging.error(e)
            return None
