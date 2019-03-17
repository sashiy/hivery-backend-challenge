import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    COMPANIES_JSON = os.path.join(basedir, 'resources', 'companies.json')
    PEOPLE_JSON = os.path.join(basedir, 'resources', 'people.json')
    FRUITS_JSON = os.path.join(basedir, 'resources', 'fruits.json')
    VEGETABLES_JSON = os.path.join(basedir, 'resources', 'vegetables.json')
    LOG_FILE_PATH= os.path.join(basedir, 'logs', 'paranuara_api.log')
