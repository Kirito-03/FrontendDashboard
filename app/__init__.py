from flask import Flask

def create_app():

    app = Flask(__name__)

    with app.app_context():
        from .modules.home import home_db
        from.modules.auth import auth_db

        from.modules.configuracion_sistema import confg_sistema

        from .modules.gestion_usuarios.estudiantes import gu_estudiantes

        app.register_blueprint(home_db)
        app.register_blueprint(auth_db)
        app.register_blueprint(confg_sistema)
        app.register_blueprint(gu_estudiantes)

    print("Rutas registradas:",app.url_map)
    return app
