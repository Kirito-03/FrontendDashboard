from flask import Blueprint, render_template
from app.modules.auth import auth_db


@auth_db.route('/')  # ¡No repitas 'auth' aquí!
def home():
    return render_template('auth/login.html')