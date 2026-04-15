from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def get_Anni(self):
        return DAO.get_Anni()

    def get_Brand(self):
        return DAO.get_Brand()

    def get_Retail(self):
        return DAO.get_Retail()