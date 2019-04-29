import conecta
import funcoes_auxiliares as func_aux

def buscaUsuario(email, senha):
    login = (email, senha)
    query = "SELECT * FROM tb_usuarios WHERE email=%s AND senha=%s"
    mydb = conecta.conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, login)
    resposta = func_aux.dicionario(mycursor.description, mycursor.fetchall())
    return resposta
