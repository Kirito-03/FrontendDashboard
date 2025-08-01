from flask import Blueprint,render_template

from app.modules.gestion_usuarios.estudiantes import gu_estudiantes

@gu_estudiantes.route('/guestudiantes')
def estudiantes():
    return render_template('gestion_usuarios/estudiantes/estudiante.html')