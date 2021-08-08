from core.pyba_logic import PybaLogic


class restaurantesLogic(PybaLogic):
    def init(self):
        super().init()

    # Parámetro get
    def getRestauranteById(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM restaurante where id = '{id}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return {}
