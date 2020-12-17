import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'MariaDB10!',
  'host': '192.168.178.23',
  'port': 3307,
  'database': 'fsrbot'
}


#fügt User das erste Mal der Datenbank hinzu
def addUser(discordID,displayName,joinTime):
    sql = "INSERT INTO user (discordID,displayName,joinTime) VALUES (%s, %s, %s)"
    var = (discordID,displayName,joinTime)

    cursor.execute(sql, var)
    connection.commit()

#Überprüft, ob User mit der ID einen Datenbankeintrag hat
def userAlreadyExists(discordID):
    sql = 'SELECT Count(id) FROM user WHERE discordID = {}'.format(discordID)

    cursor.execute(sql)
    result = cursor.fetchall()[0][0]
    return bool(result)

# löscht User
def deleteUser(discordID):
    sql = 'DELETE FROM user WHERE discordID = {}'.format(discordID)

    cursor.execute(sql)
    connection.commit()

# edit User
def editUser(discordID,role = 'NULL',jahrgang = 'NULL', studiengang = 'NULL'):
    #formt String in SQL Syntax
    if not role == 'NULL': role = "'{}'".format(role)
    if not jahrgang == 'NULL': jahrgang = "'{}'".format(jahrgang)
    if not studiengang == 'NULL': studiengang = "'{}'".format(studiengang)

    sql = "UPDATE user SET " \
          "role = (CASE WHEN role IS NULL THEN {} ELSE role END)," \
          "jahrgang = (CASE WHEN jahrgang IS NULL THEN {} ELSE jahrgang END)," \
          "studiengang = (CASE WHEN studiengang IS NULL THEN {} ELSE studiengang END) " \
          "WHERE discordID = {}"\
        .format(role,jahrgang,studiengang, discordID)

    cursor.execute(sql)
    connection.commit()
def getAllUserEigenschaften(discordID):
    sql = "SELECT * FROM user WHERE discordID = {}".format(discordID)

    cursor.execute(sql)
    result = cursor.fetchall()

    result = {
        'role': result[0][1],
        'discordID': result[0][2],
        'displlayName': result[0][3],
        'joinTime': result[0][4],
        'jahrgang': result[0][5],
        'studiengang': result[0][6]
    }
    return result

def getConfig(feld):
    sql = "SELECT {} FROM config WHERE ID = 1".format(feld)

    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]


try:
  connection = mysql.connector.connect(**config)
  cursor = connection.cursor()
  #addUser('6','testuser','2020-01-01 07:24:24')
  #userAlreadyExists(1)
  #editUser(5, studiengang = 'tes',role = 'r' )
  #getAllUserEigenschaften('6')
  #getConfig('Token')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    pass
  #connection.close()
