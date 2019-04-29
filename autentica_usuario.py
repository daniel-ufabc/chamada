import banco_tb_usuarios

def autenticaUsuario(email, senha):
    resposta = banco_tb_usuarios.buscaUsuario(email,senha)
    if len(resposta) == 1:
        return True
    else:
        return False