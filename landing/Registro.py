from flask_restful import Resource
import datetime
from dao import Mongo
import datetime

class RegistroClientes(Resource):

    def get(self, nombre, email, telefono, comentario):
        try:
            collection = Mongo.ConexionMongo().get_db().lg_registro

            datos_cliente = {
                'nombre': nombre,
                'email': email,
                'telefono': telefono,
                'comentario': comentario,
                'estado': 'a',
                'datosServer': str(collection)
                }

        except TypeError:
            print('No es posible el ingreso de datos')

        return datos_cliente