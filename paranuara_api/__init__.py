from flask_restplus import Api
from flask import Blueprint

from paranuara_api.main.controller.company_controller import api as company_ns
from paranuara_api.main.controller.people_controller import api as people_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Paranuara API for company and people',
          version='1.0',
          description='Exposed endpoints to fetch information regarding Paranuara''s companies and its people'
          )

"""
Its required to add all the namespaces defined in any controller inside the application, 
this acts like a hook between flask server and the browser
"""
api.add_namespace(company_ns, path='/company')
api.add_namespace(people_ns, path='/people')
