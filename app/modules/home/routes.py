from flask import Blueprint,render_template
from app.modules.home import home_db

@home_db.route('/inicio')
def inicio():
    return render_template('home/inicio.html')