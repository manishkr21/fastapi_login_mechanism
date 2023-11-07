import mysql.connector as sql

# connect to database
def connectDB():
    connection = sql.connect(host='localhost', database='gujarati_gov', user='cpgrams', password='rajnath')
    return connection

# close database
def closeDB(connection):
    connection.close()