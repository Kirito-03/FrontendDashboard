from flask import Blueprint

gu_estudiantes = Blueprint('gu_estudiante',__name__)

gu_estudiantes = Blueprint('gu_estudiante',__name__,template_folder='../../templates/gestion_usuarios/estudiantes')

from . import routes
