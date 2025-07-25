# patch_cadastro_geral.py
import os

print("📦 Iniciando criação automática da rota de cadastro geral...")

TEMPLATE = "templates/cadastro_geral.html"
STATIC_DIR = "static/fotos"
MAIN_PY = "main.py"

# HTML Template
html = '''<!DOCTYPE html>
<html>
<head>
    <title>Cadastro Geral</title>
</head>
<body>
    <h1>Cadastro Geral</h1>
    <form method="post" enctype="multipart/form-data">
        <label>Nome:</label><input type="text" name="nome"><br>
        <label>Idade:</label><input type="number" name="idade"><br>
        <label>Contato:</label><input type="text" name="contato"><br>
        <label>Tipo:</label>
        <select name="tipo">
            <option value="aluno">Aluno</option>
            <option value="profissional">Profissional</option>
            <option value="socio">Sócio</option>
        </select><br>
        <label>Plano:</label><input type="text" name="plano"><br>
        <label>Observações:</label><textarea name="observacoes"></textarea><br>
        <label>Foto:</label><input type="file" name="foto"><br>
        <input type="submit" value="Cadastrar">
    </form>
</body>
</html>'''

# Criar template
os.makedirs("templates", exist_ok=True)
with open(TEMPLATE, "w") as f:
    f.write(html)
print(f"✅ Template criado: {TEMPLATE}")

# Garantir pasta de fotos
os.makedirs(STATIC_DIR, exist_ok=True)
print(f"📁 Diretório garantido: {STATIC_DIR}")

# Adicionar rota no main.py
with open(MAIN_PY, "r") as f:
    content = f.read()

if "def cadastro_geral()" not in content:
    rota = '''
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
'''
    # Import necessário
    imports = "\nfrom flask import Flask, render_template, request\nimport os, sqlite3"
    if imports not in content:
        content = imports + "\n" + content

    # Inserir no final
    with open(MAIN_PY, "w") as f:
        f.write(content.strip() + "\n" + rota.strip())

    print("✅ Rota '/cadastro_geral' adicionada ao main.py")
else:
    print("ℹ️ Rota já existente.")

print("✅ Patch finalizado. Reinicie o servidor e acesse /cadastro_geral para testar.")
