from flask_restful import Resource, reqparse
from logic.cuadrimotos_logic import cuadrimotosLogic


class Cuadrimotos(Resource):
    def __init__(self):
        self.cuadrimotos_put_args = self.createParser()
        self.logic = cuadrimotosLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("codigo", type=str, help="codigo de la cuadrimoto")
        args.add_argument("tamagno", type=str, help="tamagno de la cuadrimoto")
        args.add_argument("precio", type=float, help="precio de la cuadrimoto")
        args.add_argument(
            "horario_abre", type=str, help="horario de apertura de la cuadrimoto"
        )
        args.add_argument(
            "horario_cierre", type=str, help="horario de cierre de la cuadrimoto"
        )
        return args

    def get(self, id):
        result = self.logic.getCuadrimotosById(id)
        return result, 200
