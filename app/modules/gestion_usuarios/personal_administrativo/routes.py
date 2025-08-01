from flask import Blueprint,render_template

from app.modules.gestion_academica.matriculacion import ga_matricula

@ga_matricula.route('/gd_matricula')
def confg_sistema():
    return 'sis'