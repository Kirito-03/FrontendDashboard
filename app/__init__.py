from .route import blueprin #importo del directori actual el b
from flask import Flask
# Inicializcion de la aplicacion
def create_app():
    app=Flask(__name__)
    app.register_blueprint(blueprin[0])   #registro el bluprint de acuerdo all array-indice
    # app.register_blueprint(blueprin[0])   #registro el bluprint de acuerdo all array-indice
    # app.register_blueprint(blueprin[0])   #registro el bluprint de acuerdo all array-indice
    # app.register_blueprint(blueprin[0])   #registro el bluprint de acuerdo all array-indice
    # app.register_blueprint(blueprin[0])   #registro el bluprint de acuerdo all array-indice
    # app.register_blueprint(blueprin[0])   #registro el bluprint de acuerdo all array-indice
    # app.register_blueprint(blueprin[0])   #registro el bluprint de acuerdo all array-indice
    return app
    