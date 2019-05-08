from autentica_usuario import autenticaUsuario
from funcoes_auxiliares import limpaDicionario, removeEspaco, semanal
from banco_tb_usuarios import buscaUsuario
from banco_tb_turmas import listaTurmas
from banco_turma_horarios import buscaHorarioTurma
from flask import Flask, render_template, request, redirect, session, flash


app = Flask(__name__)
app.secret_key = 'appufabc'

@app.route('/')
def painel_professor():
    if 'autenticado' in session and session['autenticado']:
        turmas = listaTurmas(session['id_usuario'])
        print(turmas)
        return render_template('index.html', lista_de_turmas=turmas, removeEspaco=removeEspaco, buscaHorarioTurma=buscaHorarioTurma, semanal=semanal)
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

app.run()