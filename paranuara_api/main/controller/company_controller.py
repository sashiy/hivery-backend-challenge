from flask_restplus import Namespace, Resource

from paranuara_api.main.controller.base_controller import BaseController
from paranuara_api.main.service import company_service as cs, people_service as ps

api = Namespace('company', description='Get employees from a company')


@api.route('/<company_name>')
@api.param('company_name', 'Company identifier')
class CompanyEmployeeList(Resource, BaseController):
    @api.doc('Retrieve all people of a company')
    def get(self, company_name):
        """
        This method, on accepting a valid company name, looks for the unique identifier of the company from companies.json
        and fetches all the employees of the company by compiling information from people.json
        :param company_name: Name of the company
        :return: List of employees with essential information about each
        """
        response = {}
        company_reference = cs.CompanyService()
        company_id = company_reference.get_company_id(company_name)
        if company_id < 0:
            response['data'] = 'Company with the name {} doesn''t exist. Please try with a valid input'.format(
                company_name)
        else:
            people_reference = ps.PeopleService()
            employee_list = people_reference.get_people_in_a_company(company_id)
            no_of_employees = len(employee_list) if employee_list is not None else 0
            response['# of employees'] = no_of_employees
            response['data'] = []
            if employee_list is not None and no_of_employees > 0:
                for employee in employee_list:
                    response['data'].append(self._create_dict_for_response(employee))
            else:
                response['data'].append('Company does not have any employees!')
        return response
