from conecta import conecta
from funcoes_auxiliares import dicionario


def buscaHorarioTurma(id_turma):
    turma = (id_turma,)
    query = "SELECT tds.dia_da_semana, tth.id_dia_semanal, tth.horario FROM tb_turma_horarios as tth LEFT join tb_dia_semanal as tds ON tth.id_dia_semanal = tds.id_dia_semanal WHERE id_turma = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def buscaHorarioCompleto(id_turma, id_dia_semanal, horario):
    turma = (id_turma, id_dia_semanal, horario)
    query = "SELECT * FROM tb_turma_horarios WHERE id_turma=%s AND id_dia_semanal=%s AND horario=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def excluirHorario(id_turma, id_dia_semanal, horario):
    turma = (id_turma, id_dia_semanal, horario)
    query = "DELETE FROM tb_turma_horarios WHERE id_turma=%s AND id_dia_semanal=%s AND horario=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()


def adicionaHorario(id_turma, id_dia_semanal, horario):
    if len(buscaHorarioCompleto(id_turma, id_dia_semanal, horario)) == 0:
        turma = (id_turma, id_dia_semanal, horario)
        query = "INSERT INTO tb_turma_horarios(id_turma, id_dia_semanal, horario) VALUES (%s, %s, %s)"
        mydb = conecta()
        mycursor = mydb.cursor()
        mycursor.execute(query, turma)
        mydb.commit()

