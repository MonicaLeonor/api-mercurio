from flask_restful import Resource, reqparse
from logic.endpoints import EndPointsLogic


class All(Resource):
    def __init__(self):
        self.logic = EndPointsLogic()

    def get(self, endpoint):
        result = self.logic.getAll(endpoint)
        return result, 200
