from conecta import conecta
from funcoes_auxiliares import dicionario

def buscaUsuario(email, senha):
    login = (email, senha)
    query = "SELECT * FROM tb_usuarios WHERE email=%s AND senha=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, login)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta
