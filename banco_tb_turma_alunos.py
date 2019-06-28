from conecta import conecta
from funcoes_auxiliares import dicionario
from banco_tb_usuarios import buscaIdRA
import csv

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

def buscaTurmaAluno(id_usuario, id_turma):
    turma = (id_usuario, id_turma)
    query = "SELECT * FROM tb_turma_alunos WHERE id_usuario = %s AND id_turma= %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def cadastraTurmaAluno(id_usuario, id_turma):
    if len(buscaTurmaAluno(id_usuario, id_turma)) == 0:
        turma = (id_usuario, id_turma)
        query = "INSERT INTO tb_turma_alunos(id_usuario, id_turma) values(%s,%s)"
        mydb = conecta()
        mycursor = mydb.cursor()
        mycursor.execute(query, turma)
        mydb.commit()

def cadastraAlunos(tabela, id_turma):
    for ra in csv.reader(tabela):
        id_usuario = buscaIdRA(ra[0])['id_usuario']
        cadastraTurmaAluno(id_usuario=id_usuario, id_turma=id_turma)


