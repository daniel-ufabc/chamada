import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "UFABC"
)



mycursor = mydb.cursor()

query = "SELECT * FROM tb_usuarios WHERE email = %s AND senha = %s"
usuario1 = ("prof3@gmail.com", "1234")

mycursor.execute(query, usuario1)

resp = mycursor.fetchall()

for row in resp:
    print(row)