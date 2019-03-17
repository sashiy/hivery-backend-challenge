import unittest
import json
from flask_testing import TestCase

from manage import application


class APITestCase(TestCase):
    def create_app(self):
        application.config.from_object('paranuara_api.main.config.Config')
        return application

    def test_index(self):
        tester = application.test_client(self)
        res = tester.get('/')
        self.assertEqual(res.status_code, 200)

    def test_company_to_employees_not_exist(self):
        tester = application.test_client(self)
        res = tester.get('company/test')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['data'], 'Company with the name test doesnt exist. Please try with a valid input')

    def test_company_to_employees_exist(self):
        tester = application.test_client(self)
        res = tester.get('company/JAMNATION')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['# of employees'], 11)

    def test_company_to_employees_no_employee(self):
        tester = application.test_client(self)
        res = tester.get('company/NETBOOK')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['# of employees'], 0)

    def test_person_existence_true(self):
        tester = application.test_client(self)
        res = tester.get('people/595eeb9b31d3539d270d1428')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['username'], 'Rhodes Boone')

    def test_person_existence_false(self):
        tester = application.test_client(self)
        res = tester.get('people/sample')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['data'], 'Error: User doesn''t exist. Please try with valid input.')

    def test_person_favourite_food_fruits_and_vegetables(self):
        tester = application.test_client(self)
        res = tester.get('people/595eeb9c5e4cf3e274cdf3d3')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['username'], 'Esther Benson')
        self.assertCountEqual(data['fruits'], ["orange", "banana", "apple"])
        self.assertCountEqual(data['vegetables'], ["celery"])

    def test_person_favourite_food_fruits(self):
        tester = application.test_client(self)
        res = tester.get('people/595eeb9b309724177239a445')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['username'], 'Mindy Beasley')
        self.assertCountEqual(data['fruits'], ["orange", "banana", "apple", "strawberry"])
        self.assertCountEqual(data['vegetables'], [])

    def test_common_friends_invalid_input(self):
        tester = application.test_client(self)
        res = tester.get('people/595eeb9b309724177239a445/595eeb9b309724177239a445')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['data'],
                         'Error 595eeb9b309724177239a445 and 595eeb9b309724177239a445 are same, please provide different user identifiers')

    def test_common_friends_valid(self):
        tester = application.test_client(self)
        res = tester.get('people/595eeb9b309724177239a445/595eeb9b82a0056a415c44aa')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['person_1']['username'], 'Mindy Beasley')
        self.assertEqual(data['person_2']['username'], 'Lindsay Harrington')
        self.assertEqual(data['friends_in_common'][0]['username'], 'Decker Mckenzie')


if __name__ == '__main__':
    unittest.main()
