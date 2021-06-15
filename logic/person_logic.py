from core.pyba_logic import PybaLogic


class PersonLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getAllPerson(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM person;"
        results = database.executeQuery(sql)
        return results
