import os

print("📦 Iniciando criação automática da rota de cadastro de aluno...")

# 1. Criar template cadastro_aluno.html
TEMPLATE_HTML = '''{% extends "base.html" %}
{% block content %}
<h2>Cadastro de Aluno</h2>
<form action="/cadastro_aluno" method="POST" enctype="multipart/form-data">
    <label>Nome:</label><br>
    <input type="text" name="nome" required><br><br>

    <label>Idade:</label><br>
    <input type="number" name="idade"><br><br>

    <label>Telefone:</label><br>
    <input type="text" name="telefone"><br><br>

    <label>Observações:</label><br>
    <textarea name="observacoes"></textarea><br><br>

    <label>Foto:</label><br>
    <input type="file" name="foto" accept="image/*"><br><br>

    <input type="submit" value="Cadastrar">
</form>
{% endblock %}
'''

template_path = 'templates/cadastro_aluno.html'
if not os.path.exists(template_path):
    with open(template_path, 'w') as f:
        f.write(TEMPLATE_HTML)
    print(f"✅ Template criado: {template_path}")
else:
    print(f"✅ Template já existe: {template_path}")

# 2. Criar pasta static/fotos se não existir
fotos_dir = 'static/fotos'
os.makedirs(fotos_dir, exist_ok=True)
print(f"📁 Diretório garantido: {fotos_dir}")

# 3. Adicionar rota no main.py
ROTA_PY = '''
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
'''

main_path = 'main.py'
with open(main_path, 'r') as f:
    lines = f.readlines()

if "def cadastro_aluno():" not in "".join(lines):
    insert_point = 0
    for i, line in enumerate(lines):
        if "from flask" in line:
            insert_point = i + 1
            break
    if "import sqlite3" not in "".join(lines):
        lines.insert(insert_point, "import sqlite3\n")
    if "import os" not in "".join(lines):
        lines.insert(insert_point, "import os\n")

    for i, line in enumerate(lines):
        if "app = Flask" in line:
            insert_point = i + 1
            break

    lines.append("\n" + ROTA_PY.strip() + "\n")

    with open(main_path, 'w') as f:
        f.writelines(lines)
    print("✅ Rota adicionada ao main.py")
else:
    print("⚠️ Rota já existe em main.py")

print("✅ Patch finalizado. Reinicie o servidor e acesse /cadastro_aluno para testar.")
