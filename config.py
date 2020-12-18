import json
import mariadbConnector


class Config:
    def __init__(self):
        #Datenbank
        datenbank = DBConfig()
        self.dbUser = datenbank.user
        self.dbPasswort = datenbank.password
        self.dbHost = datenbank.host
        self.dbPort = datenbank.port
        self.dbDatabase = datenbank.database
        #Bot
        #todo eine gemeinsame DB Abfrage
        self.dbConnection = mariadbConnector.ConnectionToDatabase(DBConfig())
        self.botToken = self.dbConnection.getConfig('Token')
        self.regChannel = int(self.dbConnection.getConfig('regChannel'))
        self.firstRegMsg = int(self.dbConnection.getConfig('firstRegMsg'))
        self.secondRegMsg = int(self.dbConnection.getConfig('secondRegMsg'))


class DBConfig:
    def __init__(self):
        with open("dbConfig") as json_data_file:
            data = json.load(json_data_file)
        self.user = data["user"]
        self.password = data["password"]
        self.host = data["host"]
        self.port = data["port"]
        self.database = data["database"]

