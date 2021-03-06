from conecta import conecta
from funcoes_auxiliares import dicionario
from banco_tb_coordenadas import deletaCoordendasIdFoto
from banco_tb_fotos import buscaFotoIdChamada, deletaFotoIdFoto
import os


def cadastraNovaChamada(id_usuario, id_turma, data_chamada):
    chamada = (id_usuario, id_turma, data_chamada)
    query = "INSERT INTO tb_chamadas(id_usuario, id_turma, data_chamada) VALUES (%s, %s, %s)"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    mydb.commit()

def excluiChamada(id_chamada):
    chamada = (id_chamada,)
    query = "DELETE FROM tb_turmas WHERE id_turma = %s"
    mydb = conecta.conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    mydb.commit()

def buscaChamada(id_usuario, id_turma, data_chamada):
    chamada = (id_usuario, id_turma, data_chamada)
    query = "SELECT * FROM tb_chamadas WHERE id_usuario=%s AND id_turma=%s AND data_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def renomeiaArquivoId(id_chamada, nome_arquivo):
    chamada = (nome_arquivo ,id_chamada)
    query = "UPDATE tb_chamadas SET nome_arquivo=%s WHERE id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    mydb.commit()

def listaChamadasPendentes(id_usuario):
    query = "SELECT tbt.nome_turma, tbc.id_chamada, tbc.data_chamada FROM tb_chamadas as tbc INNER JOIN tb_turmas as tbt ON tbc.id_turma = tbt.id_turma WHERE tbc.id_usuario = %s AND tbc.id_status = 0"
    chamada = (id_usuario,)
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def publicaChamadaIdChamada(id_chamada):
    chamada = (id_chamada,)
    query = "UPDATE tb_chamadas set id_status=1 WHERE id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    mydb.commit()

def excluiChamadaIdChamada(id_chamada):
    chamada = (id_chamada,)
    info_foto = buscaFotoIdChamada(id_chamada)[0]
    deletaCoordendasIdFoto(info_foto['id_foto'])
    deletaFotoIdFoto(info_foto['id_foto'])
    os.remove('uploads/{}'.format(info_foto['nome_arquivo']))
    query = "DELETE FROM tb_chamadas WHERE id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    mydb.commit()

def listaChamadasAtivas(id_usuario):
    query = "SELECT tbt.nome_turma, tbc.id_chamada, tbc.data_chamada FROM tb_chamadas as tbc INNER JOIN tb_turmas as tbt ON tbc.id_turma = tbt.id_turma WHERE tbc.id_usuario = %s AND tbc.id_status = 1"
    chamada = (id_usuario,)
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def buscaChamadaIdTurma(id_turma):
    chamada = (id_turma,)
    query = "SELECT * FROM tb_chamadas WHERE id_turma=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def buscaChamadaIdChamada(id_chamada):
    chamada = (id_chamada,)
    query = "SELECT * FROM tb_chamadas WHERE id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, chamada)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

