import os
import logging
import json

from paranuara_api.main.config import Config

FORMAT = '%(asctime)-15s %(filename)s:%(lineno)s  %(message)s'
logging.basicConfig(format=FORMAT, filename=os.path.join(Config.LOG_FILE_PATH), level=logging.INFO)


def _check_if_file_exists(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)


def read_data_from_file(file_path):
    try:
        if _check_if_file_exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
            logging.info('File {} does not exist'.format(file_path))
            return None
    except Exception as e:
        logging.error(e)
        return None
