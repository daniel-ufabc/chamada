from conecta import conecta
from funcoes_auxiliares import dicionario

def buscaUsuario(email=None, senha=None):
    parametros = {'email': email, 'senha': senha}
    parametros_validos = {}
    query = "SELECT * FROM tb_usuarios WHERE"
    for chave in parametros:
        if parametros[chave] is not None:
            parametros_validos[chave] = parametros[chave]
            query += " {} = %s AND".format(chave)
    query = query[:-4]
    valores = tuple(parametros_validos.values())
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, valores)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    if len(resposta) == 1:
        return resposta[0]
    else:
        return resposta

def buscaRA(id_usuario):
    usuario = (id_usuario,)
    query = "SELECT RA from tb_usuarios WHERE id_usuario = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, usuario)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta[0]
