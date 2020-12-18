import mariadbConnector
import datetime
from config import DBConfig

class User:

    def __init__(self, discordID,name,role = None,jahrgang = None, studiengang = None):
        self.discordID = discordID
        # db connection
        # todo db connection an einem anderen Ort aufbauen
        self.dbConnection = mariadbConnector.ConnectionToDatabase(DBConfig())
        # wenn User schon in der DB vorhanden ist
        # todo einzelne Datenbankabfragen zusammenlegen
        if self.userAlreadyExists():
            print('User existiert schon')
            self.name = self.getName()
            self.role = self.getRole()
            self.jahrgang = self.getJahrgang()
            self.studiengang = self.getStudiengang()
            self.joinTime = self.getJoinTime()
            self.leaveTime = self.getLeaveTime()

        # wenn User noch nicht in der Datebank vorhanden ist wird er angelegt
        else:
            print('User existiert noch nicht')
            self.name = name
            self.joinTime = datetime.datetime.now()
            self.role = role
            self.jahrgang = jahrgang
            self.studiengang = studiengang
            self.leaveTime = None
            self.addUserToDatabase()






    def setName(self,name):
        self.name = name
        self.dbConnection.editUser(self.discordID,name=name)

    def getName(self):
        return self.dbConnection.getUserEigenschaft(self.discordID,'displayname')

    def setRole(self,role):
        self.role = role
        self.dbConnection.editUser(self.discordID, role=role)

    def getRole(self):
        return self.dbConnection.getUserEigenschaft(self.discordID, 'role')

    def setLeaveTime(self):
        self.leaveTime = datetime.datetime.now()
        self.dbConnection.editUser(self.discordID, leaveTime=self.leaveTime)

    def getLeaveTime(self):
        return self.dbConnection.getUserEigenschaft(self.discordID, 'leaveTime')

    def setJoinTime(self):
        self.joinTime = datetime.datetime.now()
        self.dbConnection.editUser(self.discordID, joinTime=self.joinTime)

    def getJoinTime(self):
        return self.dbConnection.getUserEigenschaft(self.discordID, 'joinTime')

    def setStudiengang(self,studiengang):
        self.studiengang = studiengang
        self.dbConnection.editUser(self.discordID,studiengang=studiengang)

    def getStudiengang(self):
        return self.dbConnection.getUserEigenschaft(self.discordID,'studiengang')

    def setJahrgang(self,jahrgang):
        self.jahrgang = jahrgang
        self.dbConnection.editUser(self.discordID, jahrgang=int(jahrgang))

    def getJahrgang(self):
        return self.dbConnection.getUserEigenschaft(self.discordID,'jahrgang')

    def addUserToDatabase(self):
        self.dbConnection.addUser(self.discordID, self.name, self.joinTime,self.jahrgang,self.studiengang)

    def userAlreadyExists(self):
        return self.dbConnection.userAlreadyExists(self.discordID)

    def delUser(self):
        self.dbConnection.deleteUser(self, self.discordID)