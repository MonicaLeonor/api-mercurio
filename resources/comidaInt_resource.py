from flask_restful import Resource, reqparse
from logic.comidaInt_logic import comidaIntLogic


class Comida(Resource):
    def __init__(self):
        self.comida_put_args = self.createParser()
        self.logic = comidaIntLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre", type=str, help="nombre de la comida")
        args.add_argument("pais", type=str, help="pais de la comida")
        args.add_argument("precio", type=float, help="precio de la comida")
        return args

    def get(self, id):
        result = self.logic.getComidaById(id)
        return result, 200
