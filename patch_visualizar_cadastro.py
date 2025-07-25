import os
from pathlib import Path

print("📦 Criando rota de visualização detalhada por cadastro...")

project_path = Path(__file__).resolve().parent
main_file = project_path / "main.py"
template_dir = project_path / "templates"
template_dir.mkdir(exist_ok=True)

template_file = template_dir / "visualizar_cadastro.html"

html_content = """\
<!DOCTYPE html>
<html>
<head>
    <title>Visualizar Cadastro</title>
</head>
<body>
    <h1>Ficha de Cadastro: {{ aluno.nome }}</h1>
    <img src="{{ url_for('static', filename='fotos/' + aluno.foto) }}" width="200" alt="Foto do Aluno"><br>
    <p><strong>ID:</strong> {{ aluno.id }}</p>
    <p><strong>Tipo:</strong> {{ aluno.tipo }}</p>
    <p><strong>Idade:</strong> {{ aluno.idade }}</p>
    <p><strong>Observações:</strong> {{ aluno.observacoes }}</p>
    <a href="/cadastros">← Voltar para a lista</a>
</body>
</html>
"""

with open(template_file, "w") as f:
    f.write(html_content)
print(f"✅ Template criado: {template_file.relative_to(project_path)}")

rota = """
@app.route("/cadastro/<int:id>")
def visualizar_cadastro(id):
    conn = sqlite3.connect("syemfit.db")
    conn.row_factory = sqlite3.Row
    aluno = conn.execute("SELECT * FROM alunos WHERE id = ?", (id,)).fetchone()
    conn.close()
    if aluno is None:
        return "Cadastro não encontrado", 404
    return render_template("visualizar_cadastro.html", aluno=aluno)
"""

with open(main_file, "r") as f:
    conteudo = f.read()

if "def visualizar_cadastro" not in conteudo:
    with open(main_file, "a") as f:
        f.write("\n" + rota.strip() + "\n")
    print("✅ Rota '/cadastro/<id>' adicionada ao main.py")
else:
    print("⚠️ Rota já existia, nenhum código duplicado inserido.")

print("✅ Patch finalizado. Reinicie o servidor e acesse /cadastro/<id> para testar.")
