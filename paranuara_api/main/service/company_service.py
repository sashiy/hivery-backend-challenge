from paranuara_api.main import Config
from paranuara_api.main.utilities.utilities import read_data_from_file, logging


class CompanyService:

    def __init__(self):
        self._list_of_companies = read_data_from_file(Config.COMPANIES_JSON)

    def _check_if_company_exists(self, company_name):
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
        try:
            company_details = self._check_if_company_exists(company_name)
            if company_details is not None:
                return company_details['index']
            else:
                return -1
        except Exception as e:
            logging.error(e)
