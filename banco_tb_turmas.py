import conecta

def criaTurma(id_usuario, nome_turma, campus):
    turma = (id_usuario, nome_turma, campus)
    query = "INSERT INTO tb_turmas(id_usuario, nome_turma, campus) VALUES (%s, %s, %s)"
    mydb = conecta.conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()
    return True

def ativaTurma(id_turma):
    turma = (id_turma,)
    query = "UPDATE tb_turmas SET id_status = 0 WHERE id_turma = %s"
    mydb = conecta.conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()
    return True

def desativaTurma(id_turma):
    turma = (id_turma,)
    query = "UPDATE tb_turmas SET id_status = 1 WHERE id_turma = %s"
    mydb = conecta.conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, turma)
    mydb.commit()
    return True

criaTurma(1, "Bases Computacionais", "Santo Andre")

