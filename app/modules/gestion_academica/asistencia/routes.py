from flask import Blueprint,render_template

from app.modules.gestion_academica.asistencia import ga_asistencia

@ga_asistencia.route('/ga_asistencia')
def confg_sistema():
    return 'sis'