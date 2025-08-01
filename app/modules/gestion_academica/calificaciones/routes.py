from flask import Blueprint,render_template

from app.modules.gestion_academica.calificaciones import ga_calificaciones

@ga_calificaciones.route('/ga_calififcaciones')
def confg_sistema():
    return 'sis'