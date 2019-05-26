from conecta import conecta
from funcoes_auxiliares import dicionario

def listaTurmasAluno(id_usuario):
    usuario = (id_usuario,)
    query = "SELECT * FROM tb_turma_alunos WHERE id_usuario = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, usuario)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def excluiTurmaAluno(id_usuario, id_turma):
    turma = (id_usuario, id_turma)
    query = "DELETE FROM tb_turma_alunos WHERE id_usuario = %s AND id_turma= %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()

