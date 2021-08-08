from core.pyba_logic import PybaLogic


class comidaIntLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # Parámetro get
    def getComidaById(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM comida where id = '{id}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return {}

    # Parámetro post
    def getAllComidas(self, pais):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM `comida`;"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []
