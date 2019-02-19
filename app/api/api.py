import logging
import traceback

from flask_restplus import Api
from werkzeug.exceptions import  NotFound

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Hivery Api',
          description='List of API for getting the details of companies and people in Paranura')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    return {'message': message}, 500



