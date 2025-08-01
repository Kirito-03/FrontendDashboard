from flask import Blueprint

confg_sistema = Blueprint('confg_sistema',__name__)

confg_sistema = Blueprint('confg_sistema',__name__,template_folder='../../templates/consiguracion_sistema')

from . import routes
