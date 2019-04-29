import autentica_usuario as autentica
import funcoes_auxiliares as func_aux
import banco_tb_usuarios
from flask import Flask, render_template, request, redirect, session, flash


app = Flask(__name__)
app.secret_key = 'appufabc'

@app.route('/')
def painel_professor():
    if 'autenticado' in session and session['autenticado']:
        return render_template('index.html')
    else:
        return redirect('/login')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autentica', methods=['POST',])
def autenticaLogin():
    email = request.form['email']
    senha = request.form['senha']
    if(autentica.autenticaUsuario(email,senha)):
        session['autenticado'] = True
        session['id_usuario'] = banco_tb_usuarios.buscaUsuario(email,senha)[0]['id_usuario']
        session['id_permissao'] = banco_tb_usuarios.buscaUsuario(email,senha)[0]['id_permissao']
        return redirect('/')
    else:
        session['autenticado'] = False
        flash('Usuario ou senha invalido(s)')
        return redirect('/login')


@app.route('/logout')
def encerraSessao():
    func_aux.limpaDicionario(session)
    return redirect('/')

app.run()