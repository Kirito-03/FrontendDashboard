from flask import Blueprint

ga_asistencia = Blueprint('ga_asistencia',__name__)

ga_asistencia = Blueprint('ga_asistencia',__name__,template_folder='../../templates/gestion_academica/asistencia')

from . import routes
