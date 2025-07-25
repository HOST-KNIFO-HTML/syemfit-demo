from flask import Flask, render_template, request
import os, sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'syemfit_secret_🔥_key'
DB = 'banco.db'

def get_user(username):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        user = get_user(usuario)
        if user and user[2] == senha:
            session['usuario'] = usuario
            return redirect('/dashboard')
        return render_template('login.html', erro='Credenciais inválidas.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/assinaturas')
def assinaturas():
    return render_template('assinaturas.html')

@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html')

@app.route('/acesso')
def acesso():
    return render_template('acesso.html')

@app.route('/agendamentos')
def agendamentos():
    return render_template('agendamentos.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/backup')
def backup():
    return render_template('backup.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html')

@app.route('/integracoes')
def integracoes():
    return render_template('integracoes.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/cadastro_aluno", methods=["GET", "POST"])
def cadastro_aluno():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        telefone = request.form.get("telefone")
        observacoes = request.form.get("observacoes")
        foto = request.files.get("foto")

        if foto and nome:
            filename = nome.replace(" ", "_") + ".jpg"
            caminho_foto = os.path.join("static", "fotos", filename)
            foto.save(caminho_foto)

            conn = sqlite3.connect("syemfit.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO alunos (nome, idade, telefone, observacoes, foto) VALUES (?, ?, ?, ?, ?)",
                           (nome, idade, telefone, observacoes, filename))
            conn.commit()
            conn.close()
            return "✅ Aluno cadastrado com sucesso!"

    return render_template("cadastro_aluno.html")


@app.route('/alunos')
def listar_alunos():
    conn = sqlite3.connect('syemfit.db')
    conn.row_factory = sqlite3.Row
    alunos = conn.execute('SELECT * FROM alunos').fetchall()
    conn.close()
    return render_template('alunos.html', alunos=alunos)


@app.route('/editar_aluno/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    conn = sqlite3.connect('syemfit.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        observacoes = request.form['observacoes']

        if 'foto' in request.files and request.files['foto'].filename != '':
            foto = request.files['foto']
            foto_path = os.path.join('static/fotos', f'{id}_{foto.filename}')
            foto.save(foto_path)
            cursor.execute("UPDATE alunos SET nome=?, idade=?, observacoes=?, foto_path=? WHERE id=?",
                           (nome, idade, observacoes, foto_path, id))
        else:
            cursor.execute("UPDATE alunos SET nome=?, idade=?, observacoes=? WHERE id=?",
                           (nome, idade, observacoes, id))

        conn.commit()
        conn.close()
        return redirect(url_for('alunos'))

    cursor.execute("SELECT * FROM alunos WHERE id=?", (id,))
    aluno = cursor.fetchone()
    conn.close()

    if aluno:
        aluno_dict = {
            'id': aluno[0],
            'nome': aluno[1],
            'idade': aluno[2],
            'observacoes': aluno[3],
            'foto_path': aluno[4]
        }
        return render_template('editar_aluno.html', aluno=aluno_dict)
    else:
        return "Aluno não encontrado", 404
@app.route("/cadastro_geral", methods=["GET", "POST"])
def cadastro_geral():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        contato = request.form["contato"]
        tipo = request.form["tipo"]
        plano = request.form["plano"]
        observacoes = request.form["observacoes"]
        foto = request.files["foto"]
        caminho_foto = os.path.join("static/fotos", foto.filename)
        foto.save(caminho_foto)
        conn = sqlite3.connect("syemfit.db")
        c = conn.cursor()
        c.execute("INSERT INTO alunos (nome, idade, contato, tipo, plano, observacoes, foto) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (nome, idade, contato, tipo, plano, observacoes, caminho_foto))
        conn.commit()
        conn.close()
        return "Cadastro realizado com sucesso!"
    return render_template("cadastro_geral.html")
@app.route('/cadastros')
def listar_cadastros():
    tipo = request.args.get('tipo')
    conn = sqlite3.connect('syemfit.db')
    cursor = conn.cursor()
    if tipo:
        cursor.execute("SELECT * FROM alunos WHERE tipo = ?", (tipo,))
    else:
        cursor.execute("SELECT * FROM alunos")
    cadastros = cursor.fetchall()
    conn.close()
    return render_template('lista_geral.html', cadastros=cadastros)

@app.route("/cadastro/<int:id>")
def visualizar_cadastro(id):
    conn = sqlite3.connect("syemfit.db")
    conn.row_factory = sqlite3.Row
    aluno = conn.execute("SELECT * FROM alunos WHERE id = ?", (id,)).fetchone()
    conn.close()
    if aluno is None:
        return "Cadastro não encontrado", 404
    return render_template("visualizar_cadastro.html", aluno=aluno)
