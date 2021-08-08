from flask import Flask
from flask_restful import Api
from resources.comidaInt_resource import Comida
from resources.cuadrimotos_resource import Cuadrimotos
from resources.restaurante_resource import Restaurante
from resources.endpoints_resource import All

app = Flask(__name__)
api = Api(app)

api.add_resource(All, "/<string:endpoint>")
api.add_resource(Comida, "/comida/<int:id>")
api.add_resource(Cuadrimotos, "/cuadrimotos/<int:id>")
api.add_resource(Restaurante, "/restaurante/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)