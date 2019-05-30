from banco_tb_usuarios import buscaUsuario

def autenticaUsuario(email, senha):
    if buscaUsuario(email=email, senha=senha):
        return True
    return False
