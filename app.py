from autentica_usuario import autenticaUsuario
from funcoes_auxiliares import limpaDicionario, removeEspaco, semanal, nomeArquivo
from banco_tb_usuarios import buscaUsuario
from banco_tb_turmas import listaTurmas, desativaTurma, buscaTurma, ativaTurma
from banco_tb_chamadas import buscaChamada, cadastraNovaChamada, listaChamadasPendentes
from banco_turma_horarios import buscaHorarioTurma
from banco_tb_fotos import cadastraNovafoto, atualizaDimensao, buscaFoto
from banco_tb_coordenadas import detectaFaces
from flask import Flask, render_template, request, redirect, session, flash
from openCV import dimensoesImagem

app = Flask(__name__)
app.secret_key = 'appufabc'

@app.route('/teste')
def testeUI():
    return render_template('index.html')

@app.route('/')
def painel_professor():
    if 'autenticado' in session and session['autenticado']:
        turmas = listaTurmas(session['id_usuario'])
        chamadas_pendentes = listaChamadasPendentes(session['id_usuario'])
        print(turmas)
        return render_template('index.html', lista_de_turmas=turmas, removeEspaco=removeEspaco, buscaHorarioTurma=buscaHorarioTurma, semanal=semanal, chamadas_pendentes=chamadas_pendentes)
    else:
        return redirect('/login')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autentica', methods=['POST'])
def autenticaLogin():
    email = request.form['email']
    senha = request.form['senha']
    if autenticaUsuario(email, senha):
        session['autenticado'] = True
        session['id_usuario'] = buscaUsuario(email,senha)[0]['id_usuario']
        session['id_permissao'] = buscaUsuario(email,senha)[0]['id_permissao']
        return redirect('/')
    else:
        session['autenticado'] = False
        flash('Usuario ou senha invalido(s)')
        return redirect('/login')


@app.route('/logout')
def encerraSessao():
    limpaDicionario(session)
    return redirect('/')

@app.route('/arquivar_turma', methods=['POST'])
def arquivaTurma():
    if 'id_turma_arquivar' in request.form:
        id_turma = request.form['id_turma_arquivar']
        turma = buscaTurma(id_turma)
        desativaTurma(id_turma)
        flash('{} arquivado(a) com sucesso !'.format(turma[0]['nome_turma']))
    return redirect('/')

@app.route('/desarquivar_turma', methods=['POST'])
def desarquivaTurma():
    if 'id_turma_desarquivar' in request.form:
        id_turma = request.form['id_turma_desarquivar']
        turma = buscaTurma(id_turma)
        ativaTurma(id_turma)
        flash('{} desarquivado(a) com sucesso !'.format(turma[0]['nome_turma']))
    return redirect('/')

@app.route('/criar_chamada', methods=['POST'])
def criarChamada():
    data_chamada = request.form['input_data_chamada']
    id_turma = request.form['id_turma']
    id_usuario = session['id_usuario']
    cadastraNovaChamada(id_usuario, id_turma, data_chamada)
    info_chamada = buscaChamada(id_usuario, id_turma, data_chamada)[0]
    nome_arquivo = nomeArquivo(info_chamada['id_chamada'], request.form['nome_arquivo'])
    arquivo = request.files['foto_upload']
    cadastraNovafoto(nome_arquivo, id_usuario)
    arquivo.save('uploads/{}'.format(nome_arquivo))
    dimensoes = dimensoesImagem(nome_arquivo)
    atualizaDimensao(dimensoes['largura'], dimensoes['altura'], nome_arquivo)
    info_foto = buscaFoto(nome_arquivo)[0]
    detectaFaces(nome_arquivo, id_usuario, info_foto['id_foto'])
    return redirect('/')



app.run()