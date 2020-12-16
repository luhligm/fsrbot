import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'MariaDB10!',
  'host': 'uhligs.synology.me',
  'port': 3307,
  'database': 'fsrbot'
}

try:
  connection = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  connection.close()


cursor = connection.cursor()


# bekommt Configdaten aus der Datenbank
def getConfig(arg):
  sql = "SELECT "+arg+" FROM USER WHERE  ID=1"

  cursor.execute(sql)

  myresult = cursor.fetchall()
  return myresult[1]

# Userabfrage aus der Datenbank anhand der ID
def getUser(id):
  sql = "SELECT * FROM USER WHERE  discordID='" + id + "'"
  cursor.execute(sql)
  myresult = cursor.fetchall()
  return {'role': myresult['role'],'isRegSG':myresult['isRegSG'],'isRegJG':myresult['isRegJG']}

def addUser(userData):
    sql = "INSERT INTO USER (discordID,displayName,joinTime,role,isRegSG,isRegJG) VALUES (%s, %s, %s, %s, %s, %s)"
    var = (userData['_id'], userData['displayName'], userData['joinTime'], userData['role'], userData['isRegSG'], userData['isRegJG'])
    cursor.execute(sql, var)


def editUser(id, data, new):
  sql = "UPDATE USER SET "+data+" = '"+new+"' WHERE discordID='"+id+"'"

  cursor.execute(sql)

  connection.commit()


# Überprüft, ob User mit der ID einen Datenbankeintrag hat
def alreadyExists(id):
  sql = "SELECT * FROM USER WHERE  discordID='"+id+"'"

  cursor.execute(sql)

  myresult = cursor.fetchall()
  return bool(myresult)

# redundant mit alreadyExists(id)?
#def alreadyRegistered(id):
   # query = {"_id": {"$eq": int(id)}}
    #return bool(collection.find_one(query))
