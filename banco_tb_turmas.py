from conecta import conecta
from funcoes_auxiliares import dicionario

def criaTurma(id_usuario, nome_turma, campus):
    turma = (id_usuario, nome_turma, campus)
    query = "INSERT INTO tb_turmas(id_usuario, nome_turma, campus) VALUES (%s, %s, %s)"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()
    return True

def ativaTurma(id_turma):
    turma = (id_turma,)
    query = "UPDATE tb_turmas SET id_status = 1 WHERE id_turma = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()
    return True

def desativaTurma(id_turma):
    turma = (id_turma,)
    query = "UPDATE tb_turmas SET id_status = 0 WHERE id_turma = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()
    return True

def listaTurmas(id_usuario):
    usuario = (id_usuario,)
    query = "SELECT * FROM tb_turmas WHERE id_usuario = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, usuario)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def buscaTurma(id_turma):
    turma = (id_turma,)
    query = "SELECT * FROM tb_turmas WHERE id_turma = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def buscaTodasAsTurmas():
    query = "SELECT * FROM tb_turmas WHERE id_status=1"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    turmas = {}
    turmas['nome_turma'] = [turma['nome_turma'] for turma in resposta]
    turmas['id_turma'] = [turma['id_turma'] for turma in resposta]
    return turmas

