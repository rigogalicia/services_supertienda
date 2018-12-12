from pymongo import MongoClient

class ConexionMongo():

    def __init__(self):
        __client = None
        __db = None

    def get_client(self):
        try:
            self.__client = MongoClient('localhost', 27017)
        except:
            print('No es posible conectarse a la base de datos')
        return self.__client
    

    def get_db(self):
        try:
            self.__db = self.get_client().supertienda
        except:
            print('No es posible crear la base de datos supertienda')
        return self.__db