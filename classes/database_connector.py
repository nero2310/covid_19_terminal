import pymongo

from pymongo import errors


class SaveDataToMongo:
    """
    Initialize connection and save data to mongoDB
    """

    def __init__(self):  # toDO check if connection is valid
        self.colection = None


    def init_connection(self):
        """
        Initialize connection to mongodb
        :return:
        True if connection succeed
        False if connection didn't succeed
        """
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = client["covid_19_db"]
            self.colection = mydb["test"]
        except pymongo.errors.ConnectionFailure:
            return False
        except pymongo.errors.ServerSelectionTimeoutError:
            return False
        return True


    def insert_data(self, data: dict):
        """
        Method send data to mongodb
        If data is dict
        Else raise TypeError
        :param self:
        :param data:dict:
        :return:
        True if data was insert into db
        """
        try:
            if isinstance(data, dict):
                self.colection.insert_one(data)
            elif isinstance(data[0], dict):
                self.colection.insert_one(data[0])
            else:
                raise TypeError
        except pymongo.errors.ServerSelectionTimeoutError:
            print("Can't connect to server")
            return False
        return True
