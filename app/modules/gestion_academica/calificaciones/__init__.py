from flask import Blueprint

ga_calificaciones = Blueprint('ga_calificaciones',__name__)

ga_calificaciones = Blueprint('ga_calificaciones',__name__,template_folder='../../templates/gestion_academica/calificaciones')

from . import routes
