import os

print("📦 Iniciando criação da rota de edição de aluno...")

# 1. Criar o template editar_aluno.html
template_path = "templates/editar_aluno.html"
os.makedirs("templates", exist_ok=True)

if not os.path.exists(template_path):
    with open(template_path, "w") as f:
        f.write('''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Editar Aluno</title>
</head>
<body>
    <h1>Editar Aluno</h1>
    <form action="{{ url_for('editar_aluno', id=aluno.id) }}" method="post" enctype="multipart/form-data">
        Nome: <input type="text" name="nome" value="{{ aluno.nome }}"><br>
        Idade: <input type="number" name="idade" value="{{ aluno.idade }}"><br>
        Observações: <textarea name="observacoes">{{ aluno.observacoes }}</textarea><br>
        Atualizar Foto: <input type="file" name="foto"><br>
        <input type="submit" value="Salvar">
    </form>
</body>
</html>
''')
    print(f"✅ Template criado: {template_path}")
else:
    print("✅ Template já existe.")

# 2. Adicionar rota ao main.py
main_py = "main.py"
with open(main_py, "r") as f:
    conteudo = f.read()

if "def editar_aluno(" not in conteudo:
    with open(main_py, "a") as f:
        f.write('''

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
''')
    print("✅ Rota '/editar_aluno/<id>' adicionada ao main.py")
else:
    print("✅ Rota já existe no main.py")

print("✅ Patch finalizado. Reinicie o servidor e acesse /editar_aluno/<id> para testar.")
