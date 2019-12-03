from flask import Blueprint
from flask_restful import Api

automobile_blueprint = Blueprint('automobile', __name__)
automobile_api = Api(automobile_blueprint)

from . import routes
