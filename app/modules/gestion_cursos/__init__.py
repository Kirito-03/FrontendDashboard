from flask import Blueprint
home_db = Blueprint('home_db', __name__)

home_bp = Blueprint('home_bp', __name__, template_folder='../../templates/home')

from . import routes
