import mysql.connector
from mysql.connector import errorcode

class ConnectionToDatabase:
    def __init__(self,dbConfig):
        self.connection = connectToDatabase(dbConfig)
        self.cursor = self.connection.cursor()

    #fügt User das erste Mal der Datenbank hinzu
    def addUser(self,discordID,displayName,joinTime,jahrgang = None, studiengang = None):
        sql = "INSERT INTO user (discordID,displayName,joinTime,jahrgang,studiengang) VALUES (%s, %s, %s,%s,%s)"
        var = (discordID,displayName,joinTime,jahrgang,studiengang)

        self.cursor.execute(sql, var)
        self.connection.commit()

    #Überprüft, ob User mit der ID einen Datenbankeintrag hat
    def userAlreadyExists(self,discordID):
        sql = 'SELECT Count(id) FROM user WHERE discordID = {}'.format(discordID)

        self.cursor.execute(sql)
        result = self.cursor.fetchall()[0][0]
        return bool(result)

    # löscht User
    def deleteUser(self,discordID):
        sql = 'DELETE FROM user WHERE discordID = {}'.format(discordID)

        self.cursor.execute(sql)
        self.connection.commit()

    # edit User
    def editUser(self,discordID,role = None,jahrgang = None, studiengang = None, name= None,joinTime= None, leaveTime= None):
        sql = "UPDATE user SET "
        #formt String in SQL Syntax
        if not role == None: sql +=  "role = '{}',".format(role)
        if not jahrgang == None: sql += "jahrgang = '{}',".format(jahrgang)
        if not studiengang == None: sql +="studiengang = '{}',".format(studiengang)
        if not name == None:  sql +="displayName ='{}',".format(name)
        if not joinTime == None: sql += "joinTime ='{}',".format(joinTime)
        if not leaveTime == None:sql +=  "leaveTime ='{}',".format(leaveTime)
        sql += "discordID = '{}'".format(discordID)
        sql += " WHERE discordID = {}".format(discordID)

        print(sql)

        self.cursor.execute(sql)
        self.connection.commit()

    def getAllUserEigenschaften(self,discordID):
        sql = "SELECT * FROM user WHERE discordID = {}".format(discordID)

        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        result = {
        'role': result[0][1],
        'discordID': result[0][2],
        'displlayName': result[0][3],
        'joinTime': result[0][4],
        'jahrgang': result[0][5],
        'studiengang': result[0][6]
        }
        return result

    def getUserEigenschaft(self,discordID, eigenschaft):
        sql="SELECT {} FROM user WHERE discordID = {}".format(eigenschaft,discordID)

        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result[0][0]



    def getConfig(self,feld):
        sql = "SELECT wert FROM config WHERE feld = '{}'".format(feld)

        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result[0][0]

def connectToDatabase(dbConfig):
        try:
            connection = mysql.connector.connect(
                user=dbConfig.user,
                password=dbConfig.password,
                host=dbConfig.host,
                port=dbConfig.port,
                database=dbConfig.database
            )
            return connection
            #addUser('6','testuser','2020-01-01 07:24:24')
            #userAlreadyExists(1)
            #editUser(5, studiengang = 'tes',role = 'r' )
            #getAllUserEigenschaften('6')
            #getConfig('Token')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your DB user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)