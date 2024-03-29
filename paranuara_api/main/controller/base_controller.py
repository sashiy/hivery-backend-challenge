from paranuara_api.main.utilities.utilities import logging


class BaseController:
    def _create_dict_for_response(self, person_details):
        """
        This method creates and returns dictionary of person with limited and trivial information
        :param person_details: Person JSON with all relevant information
        :return: Person dictionary with trivial infroamtion
        """
        try:
            person_dict = dict()
            person_dict['username'] = person_details['name']
            person_dict['age'] = person_details['age']
            person_dict['address'] = person_details['address']
            person_dict['phone'] = person_details['phone']
            return person_dict
        except Exception as e:
            logging.error(e)
            return dict()
