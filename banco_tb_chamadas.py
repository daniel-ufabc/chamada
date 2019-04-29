import conecta

def cadastraNovaChamada(id_usuario, id_turma, data_chamada):
    chamada = (id_usuario, id_turma, data_chamada)
    query = "INSERT INTO tb_chamadas(id_usuario, id_turma, data_chamada) VALUES (%s, %s, %s)"
    mydb = conecta.conecta()
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





