import mysql.connector

def conecta():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "UFABC"
    )
    return mydb