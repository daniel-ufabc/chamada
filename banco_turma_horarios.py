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
