import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

cursorObject = dataBase.cursor()

#Create Database
cursorObject.execute("Create Database dbname")

print("Done")