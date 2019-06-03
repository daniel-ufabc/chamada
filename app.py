from autentica_usuario import autenticaUsuario
from funcoes_auxiliares import limpaDicionario, removeEspaco, semanal, nomeArquivo, ordenaChamadas
from banco_tb_usuarios import buscaUsuario, buscaRA
from banco_tb_turmas import listaTurmas, desativaTurma, buscaTurma, ativaTurma, criaTurma, buscaTodasAsTurmas
from banco_tb_chamadas import buscaChamada, cadastraNovaChamada, listaChamadasPendentes, publicaChamadaIdChamada, excluiChamadaIdChamada, listaChamadasAtivas, buscaChamadaIdTurma, buscaChamadaIdChamada
from banco_turma_horarios import buscaHorarioTurma, excluirHorario, adicionaHorario
from banco_tb_fotos import cadastraNovafoto, atualizaDimensao, buscaFoto, buscaFotoIdChamada
from banco_tb_coordenadas import detectaFaces, buscaFacesIdFoto, cadastraCoordenada, deletaCoordendasIdFoto, buscaCoordenadaAtiva
from flask import Flask, render_template, request, redirect, session, flash, send_from_directory
from openCV import dimensoesImagem
from banco_tb_turma_alunos import listaTurmasAluno, excluiTurmaAluno, cadastraTurmaAluno
from banco_tb_presenca_alunos import buscaPresenca, marcaPresenca, geraRelatorioProfessor, geraRelatorioAluno
from banco_tb_faltas_alunos import buscaFaltas, marcaFalta
import json

app = Flask(__name__)
app.secret_key = 'appufabc'

@app.route('/teste')
def testeUI():
    return render_template('index.html')

@app.route('/')
def painel():
    if 'autenticado' in session and session['autenticado']:
        if session['id_permissao'] == 1:
            turmas = listaTurmas(session['id_usuario'])
            chamadas_pendentes = listaChamadasPendentes(session['id_usuario'])
            chamadas_ativas = listaChamadasAtivas(session['id_usuario'])
            chamadas_ativas.sort(key=ordenaChamadas, reverse=True)
            horario_turmas = []
            for turma in turmas:
                if turma['id_status'] == 1:
                    horarios = buscaHorarioTurma(turma['id_turma'])
                    for horario in horarios:
                        h = {'nome': turma['nome_turma'], 'dia_semanal': horario['id_dia_semanal'], 'horario': horario['horario'] }
                        horario_turmas.append(h)
            return render_template('index.html', lista_de_turmas=turmas, removeEspaco=removeEspaco, buscaHorarioTurma=buscaHorarioTurma, semanal=semanal, chamadas_pendentes=chamadas_pendentes, chamadas_ativas=chamadas_ativas, buscaFacesIdFoto=buscaFacesIdFoto, buscaCoordenadaAtiva=buscaCoordenadaAtiva, buscaFotoIdChamada=buscaFotoIdChamada, len=len, horario_turmas=horario_turmas)
        if session['id_permissao'] == 0:
            turmas = listaTurmasAluno(session['id_usuario'])
            todas_turmas = buscaTodasAsTurmas()
            chamadas_pendentes = []
            chamadas_ativas_presente = []
            chamadas_ativas_ausente = []
            for turma in turmas:
                for chamada in buscaChamadaIdTurma(turma['id_turma']):
                    if buscaPresenca(session['id_usuario'], chamada['id_chamada']):
                        chamadas_ativas_presente.append(chamada)
                    elif buscaFaltas(session['id_usuario'], chamada['id_chamada']):
                        chamadas_ativas_ausente.append(chamada)
                    elif chamada['id_status'] == 1:
                        chamadas_pendentes.append(chamada)
            chamadas_ativas_presente.sort(key=ordenaChamadas)
            chamadas_ativas_ausente.sort(key=ordenaChamadas)
            return render_template('index2.html', len=len, lista_de_turmas=turmas, buscaTurma=buscaTurma, chamadas_pendentes=chamadas_pendentes, chamadas_ativas_presente=chamadas_ativas_presente , chamadas_ativas_ausente=chamadas_ativas_ausente, todas_turmas=todas_turmas)
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
        session['id_usuario'] = buscaUsuario(email=email, senha=senha)['id_usuario']
        session['id_permissao'] = buscaUsuario(email=email, senha=senha)['id_permissao']
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
    if not buscaChamada(id_usuario, id_turma, data_chamada):
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
    else:
        flash('Chamada ja existe')
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
    info_chamada = buscaChamadaIdChamada(info_foto['id_chamada'])[0]
    nome_arquivo = info_foto['nome_arquivo']
    coordenadas_faces = buscaFacesIdFoto(info_foto['id_foto'])
    return render_template('marcar_presenca.html', nome_arquivo=nome_arquivo, info_foto=info_foto, faces=coordenadas_faces, id_chamada=id_chamada, id_turma=info_chamada['id_turma'])

@app.route('/marcar_chamada', methods=['POST'])
def marcaChamada():
    id_coordenada = request.form['id_coordenada']
    id_usuario = session['id_usuario']
    id_chamada = request.form['id_chamada']
    id_turma = request.form['id_turma']
    marcaPresenca(id_usuario, id_chamada, id_coordenada, id_turma)
    return redirect('/')

@app.route('/relatorio_profesor')
def relatorioProfessor():
    lista_turmas = listaTurmas(session['id_usuario'])
    lista_turmas = [turma for turma in lista_turmas if turma['id_status'] == 1]
    frequencias = geraRelatorioProfessor(lista_turmas)
    return render_template('relatorio_professor.html', frequencias=frequencias, buscaRA=buscaRA)

@app.route('/detalhes_chamada', methods=['POST'])
def detalhesChamada():
    id_chamada = request.form['id_chamada']
    info_foto = buscaFotoIdChamada(id_chamada)[0]
    nome_arquivo = info_foto['nome_arquivo']
    coordenadas_faces = buscaFacesIdFoto(info_foto['id_foto'])
    return render_template('info_chamada_professor.html', nome_arquivo=nome_arquivo, faces=coordenadas_faces, info_foto=info_foto)

@app.route('/editar_dados_turma', methods=['POST'])
def editarDadosTurma():
    id_turma = ""
    if 'comando' in request.form:
        if request.form['comando'] == 'excluir':
            id_turma = request.form['id_turma']
            id_dia_semanal = request.form['id_dia_semanal']
            horario = request.form['horario']
            excluirHorario(id_turma, id_dia_semanal, horario)
        if request.form['comando'] == 'adicionar':
            id_turma = request.form['id_turma']
            id_dia_semanal = request.form['id_dia_semanal']
            horario = request.form['horario']
            adicionaHorario(id_turma, id_dia_semanal, horario)
        id_turma = request.form['id_turma']
    else:
        id_turma = request.form['id_turma_editar']
    turma = buscaTurma(id_turma)[0]
    horarios = buscaHorarioTurma(id_turma)
    return render_template('editar_dados_turma.html', horarios=horarios, turma=turma, semanal=semanal)

@app.route('/cadastar_nova_turma', methods=['POST'])
def criaNovaTurma():
    id_usuario = session['id_usuario']
    campus = request.form['campus']
    nome_turma = request.form['nome_turma']
    criaTurma(id_usuario, nome_turma, campus)
    return redirect('/')

@app.route('/cadastra_nova_turma_aluno', methods=['POST'])
def cadastraNovaTurmaAluno():
    id_usuario = session['id_usuario']
    id_turma = request.form['id_turma']
    cadastraTurmaAluno(id_usuario, id_turma)
    return redirect('/')

@app.route('/relatorio_aluno')
def relatorioAluno():
    id_usuario = session['id_usuario']
    turmas = listaTurmasAluno(id_usuario)
    turmas = [buscaTurma(turma['id_turma'])[0] for turma in turmas]
    frequencias = geraRelatorioAluno(turmas, id_usuario)
    return render_template('relatorio_aluno.html', frequencias=frequencias)

@app.route('/marcar_falta', methods=['POST'])
def marcarFaltaAluno():
    id_usuario = session['id_usuario']
    id_turma = request.form['id_turma']
    id_chamada = request.form['id_chamada']
    marcaFalta(id_usuario, id_chamada,id_turma)
    return redirect('/')

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

app.run()