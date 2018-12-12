from flask import Flask
from flask_restful import Resource, Api
from landing import Registro

app = Flask(__name__)
api = Api(app)

api.add_resource(Registro.RegistroClientes, '/<string:nombre>/<string:email>/<string:telefono>/<string:comentario>')

if __name__ == '__main__':
    app.run(host="0.0.0.0")