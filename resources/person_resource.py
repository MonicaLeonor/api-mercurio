from flask_restful import Resource
from logic.person_logic import PersonLogic


class Person(Resource):
    def get(self):
        logic = PersonLogic()
        result = logic.getAllPerson()
        return result