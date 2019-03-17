from paranuara_api.main import Config
from paranuara_api.main.utilities.utilities import read_data_from_file, logging


class CompanyService:

    def __init__(self):
        self._list_of_companies = read_data_from_file(Config.COMPANIES_JSON)

    def _check_if_company_exists(self, company_name):
        """
        This private method accepts the name of a company as an argument and checks whether
        that company is present in the companies.json file or not. If present all the information available is returned
        as a JSON, else None
        :param company_name: Name of a company
        :return: Company JSON if valid or None
        """
        try:
            logging.info('In method _check_if_company_exists. Input {}'.format(company_name))
            if self._list_of_companies is not None and len(self._list_of_companies) > 0:
                response = [c for c in self._list_of_companies if company_name.upper() == c['company'].upper()]
                if response is not None and len(response) > 0:
                    return response[0]
                else:
                    return None
            else:
                return None
        except Exception as e:
            logging.error(str(e))

    def get_company_id(self, company_name):
        """
        This method returns index of the company which is a unique identifier for the given company name
        :param company_name: Name of the company
        :return: Index or the unique identifier of the company
        """
        try:
            company_details = self._check_if_company_exists(company_name)
            if company_details is not None:
                return company_details['index']
            else:
                return -1
        except Exception as e:
            logging.error(e)
