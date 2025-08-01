from flask import Blueprint
auth_db = Blueprint('auth_db', __name__)

auth_bp = Blueprint('auth_bp', __name__, template_folder='../../templates/auth')

from . import routes