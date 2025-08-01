from flask import Blueprint,render_template

from app.modules.configuracion_sistema import confg_sistema

@confg_sistema.route('/confg_sistema')
def confg_sistema():
    return 'sis'