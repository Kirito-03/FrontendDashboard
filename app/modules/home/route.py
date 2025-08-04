from . import home_bp
from flask import render_template
@home_bp.route('/')
def index():
    return render_template("home/base.html")