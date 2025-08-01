from flask import Blueprint

ga_matricula = Blueprint('ga_matricula',__name__)

ga_matricula = Blueprint('ga_matricula',__name__,template_folder='../../templates/gestion_academica/matriculacion')

from . import routes
