from conecta import conecta
from funcoes_auxiliares import dicionario
from banco_tb_coordenadas import mudaStatusCoordenada
from banco_tb_faltas_alunos import contaFaltas

def buscaPresenca(id_usuario, id_chamada):
    presenca = (id_usuario, id_chamada)
    query = "SELECT * FROM tb_presenca_alunos WHERE id_usuario=%s AND id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, presenca)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def marcaPresenca(id_usuario, id_chamada, id_coordenada, id_turma):
    presenca = (id_usuario, id_chamada, id_coordenada, id_turma)
    query = "INSERT INTO tb_presenca_alunos(id_usuario, id_chamada, id_coordenada, id_turma) values (%s, %s, %s, %s)"
    mudaStatusCoordenada(id_coordenada)
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, presenca)
    mydb.commit()


def buscaPresencaIdTurma(id_turma):
    presenca = (id_turma,)
    query = "SELECT * FROM tb_presenca_alunos WHERE id_turma = %s AND"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, presenca)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta


def geraRelatorioProfessor(lista_turmas):
    frequencias = []
    for turma in lista_turmas:
        presencas = buscaPresencaIdTurma(turma['id_turma'])
        frequencia_alunos = {}
        for presenca in presencas:
            if presenca['id_usuario'] not in frequencia_alunos:
                frequencia_alunos[presenca['id_usuario']] = 0
            frequencia_alunos[presenca['id_usuario']] += 1
        dados = {'id_turma': turma['id_turma'], 'nome_turma': turma['nome_turma'], 'frequencia_alunos': frequencia_alunos}
        frequencias.append(dados)
    return frequencias

def contaPresenca(id_usuario, id_turma):
    aluno = (id_usuario, id_turma)
    query = "SELECT * FROM tb_presenca_alunos WHERE id_usuario=%s AND id_turma = %s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, aluno)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return len(resposta)



def geraRelatorioAluno(lista_turmas, id_usuario):
    frequencias = []
    for turma in lista_turmas:
        info = {'turma': turma['nome_turma'], 'presenca': contaPresenca(id_usuario, turma['id_turma']), 'faltas': contaFaltas(id_usuario, turma['id_turma'])}
        frequencias.append(info)
    return frequencias
