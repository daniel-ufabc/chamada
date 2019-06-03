from conecta import conecta
from funcoes_auxiliares import dicionario

def buscaFaltas(id_usuario, id_chamada):
    falta = (id_usuario, id_chamada)
    query = "SELECT * FROM tb_faltas_alunos WHERE id_usuario=%s AND id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, falta)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def marcaFalta(id_usuario, id_chamada, id_turma):
    falta = (id_usuario, id_chamada,id_turma)
    query = "INSERT INTO tb_faltas_alunos(id_usuario, id_chamada, id_turma) values (%s,%s,%s)"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, falta)
    mydb.commit()

def contaFaltas(id_usuario, id_turma):
    aluno = (id_usuario, id_turma)
    query = "SELECT * FROM tb_faltas_alunos WHERE id_usuario=%s AND id_turma = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, aluno)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return len(resposta)

