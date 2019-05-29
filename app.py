from autentica_usuario import autenticaUsuario
from funcoes_auxiliares import limpaDicionario, removeEspaco, semanal, nomeArquivo
from banco_tb_usuarios import buscaUsuario
from banco_tb_turmas import listaTurmas, desativaTurma, buscaTurma, ativaTurma
from banco_tb_chamadas import buscaChamada, cadastraNovaChamada, listaChamadasPendentes, publicaChamadaIdChamada, excluiChamadaIdChamada, listaChamadasAtivas, buscaChamadaIdTurma
from banco_turma_horarios import buscaHorarioTurma
from banco_tb_fotos import cadastraNovafoto, atualizaDimensao, buscaFoto, buscaFotoIdChamada
from banco_tb_coordenadas import detectaFaces, buscaFacesIdFoto, cadastraCoordenada, deletaCoordendasIdFoto, buscaCoordenadaAtiva
from flask import Flask, render_template, request, redirect, session, flash, send_from_directory
from openCV import dimensoesImagem
from banco_tb_turma_alunos import listaTurmasAluno, excluiTurmaAluno
from banco_tb_presenca_alunos import buscaPresenca, marcaPresenca
import json

app = Flask(__name__)
app.secret_key = 'appufabc'

@app.route('/teste')
def testeUI():
    return render_template('index.html')

@app.route('/')
def painel_professor():
    if 'autenticado' in session and session['autenticado']:
        if session['id_permissao'] == 1:
            turmas = listaTurmas(session['id_usuario'])
            chamadas_pendentes = listaChamadasPendentes(session['id_usuario'])
            chamadas_ativas = listaChamadasAtivas(session['id_usuario'])
            horario_turmas = []
            for turma in turmas:
                if turma['id_status'] == 1:
                    horarios = buscaHorarioTurma(turma['id_turma'])
                    for horario in horarios:
                        h = {'nome': turma['nome_turma'], 'dia_semanal': horario['id_dia_semanal'], 'horario': horario['horario'] }
                        horario_turmas.append(h)
            print(horario_turmas)
            return render_template('index.html', lista_de_turmas=turmas, removeEspaco=removeEspaco, buscaHorarioTurma=buscaHorarioTurma, semanal=semanal, chamadas_pendentes=chamadas_pendentes, chamadas_ativas=chamadas_ativas, buscaFacesIdFoto=buscaFacesIdFoto, buscaCoordenadaAtiva=buscaCoordenadaAtiva, buscaFotoIdChamada=buscaFotoIdChamada, len=len, horario_turmas=horario_turmas)
        if session['id_permissao'] == 0:
            turmas = listaTurmasAluno(session['id_usuario'])
            chamadas_pendentes = []
            chamadas_ativas = []
            for turma in turmas:
                for chamada in buscaChamadaIdTurma(turma['id_turma']):
                    if buscaPresenca(session['id_usuario'], chamada['id_chamada']):
                        chamadas_ativas.append(chamada)
                    else:
                        chamadas_pendentes.append(chamada)
            return render_template('index2.html', lista_de_turmas=turmas, buscaTurma=buscaTurma, chamadas_pendentes=chamadas_pendentes, chamadas_ativas=chamadas_ativas)
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
    cadastraNovafoto(nome_arquivo, id_usuario, info_chamada['id_chamada'])
    arquivo.save('uploads/{}'.format(nome_arquivo))
    dimensoes = dimensoesImagem(nome_arquivo)
    atualizaDimensao(dimensoes['largura'], dimensoes['altura'], nome_arquivo)
    info_foto = buscaFoto(nome_arquivo)[0]
    detectaFaces(nome_arquivo, id_usuario, info_foto['id_foto'])
    return redirect('/')

@app.route('/chamada', methods=['POST'])
def confirmaChamada():
    id_chamada = request.form['id_chamada']
    info_foto = buscaFotoIdChamada(id_chamada)[0]
    nome_arquivo = info_foto['nome_arquivo']
    coordenadas_faces = buscaFacesIdFoto(info_foto['id_foto'])
    return render_template('chamada.html', nome_arquivo=nome_arquivo, faces=coordenadas_faces, info_foto=info_foto)

@app.route('/publicar_chamada', methods=['POST'])
def publicaChamada():
    coordenadas = request.form['coordenadas']
    id_foto = request.form['id_foto']
    id_chamada = request.form['id_chamada']
    coordenadas = json.loads(coordenadas)
    deletaCoordendasIdFoto(id_foto)
    for c in coordenadas:
        cadastraCoordenada(c['x'], c['y'], c['w'], c['h'], session['id_usuario'], id_foto)
    publicaChamadaIdChamada(id_chamada)
    return redirect('/')

@app.route('/excluir_chamada', methods=['POST'])
def excluirChamada():
    id_chamada = request.form['id_chamada']
    excluiChamadaIdChamada(id_chamada)
    return redirect('/')

@app.route('/remover_turma_aluno', methods=['POST'])
def removeTurmaAluno():
    id_usuario = session['id_usuario']
    id_turma = request.form['id_turma']
    excluiTurmaAluno(id_usuario, id_turma)
    return redirect('/')

@app.route('/marcar_presenca', methods=['POST'])
def marcarPresenca():
    id_chamada = request.form['id_chamada']
    info_foto = buscaFotoIdChamada(id_chamada)[0]
    nome_arquivo = info_foto['nome_arquivo']
    coordenadas_faces = buscaFacesIdFoto(info_foto['id_foto'])
    return render_template('marcar_presenca.html', nome_arquivo=nome_arquivo, info_foto=info_foto, faces=coordenadas_faces, id_chamada=id_chamada)

@app.route('/marcar_chamada', methods=['POST'])
def marcaChamda():
    id_coordenada = request.form['id_coordenada']
    id_usuario = session['id_usuario']
    id_chamada = request.form['id_chamada']
    marcaPresenca(id_usuario, id_chamada, id_coordenada)
    return redirect('/')


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

app.run()