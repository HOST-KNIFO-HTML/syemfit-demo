import os

print("📦 Iniciando criação da rota de listagem de alunos...")

# 1. Cria template alunos.html se não existir
template_path = "templates/alunos.html"
if not os.path.exists(template_path):
    with open(template_path, "w") as f:
        f.write("""{% extends 'base.html' %}
{% block content %}
<h2>Lista de Alunos</h2>
<table border="1" cellpadding="6">
  <tr>
    <th>Foto</th>
    <th>Nome</th>
    <th>Idade</th>
    <th>Telefone</th>
    <th>Observações</th>
  </tr>
  {% for aluno in alunos %}
  <tr>
    <td>
      {% if aluno.foto %}
        <img src="{{ url_for('static', filename='fotos/' + aluno.foto) }}" width="100">
      {% else %}
        -
      {% endif %}
    </td>
    <td>{{ aluno.nome }}</td>
    <td>{{ aluno.idade }}</td>
    <td>{{ aluno.telefone }}</td>
    <td>{{ aluno.observacoes }}</td>
  </tr>
  {% endfor %}
</table>
{% endblock %}
""")
    print("✅ Template criado: templates/alunos.html")
else:
    print("✅ Template já existe: templates/alunos.html")

# 2. Adiciona rota ao main.py
main_file = "main.py"
with open(main_file, "r") as f:
    conteudo = f.read()

if "def listar_alunos()" not in conteudo:
    nova_rota = """

@app.route('/alunos')
def listar_alunos():
    conn = sqlite3.connect('syemfit.db')
    conn.row_factory = sqlite3.Row
    alunos = conn.execute('SELECT * FROM alunos').fetchall()
    conn.close()
    return render_template('alunos.html', alunos=alunos)
"""
    import_re = "from flask import"
    sqlite3_re = "import sqlite3"
    if import_re in conteudo and sqlite3_re not in conteudo:
        conteudo = conteudo.replace(import_re, import_re + ", render_template")
        conteudo = "import sqlite3\n" + conteudo
    conteudo += nova_rota
    with open(main_file, "w") as f:
        f.write(conteudo)
    print("✅ Rota '/alunos' adicionada ao main.py")
else:
    print("✅ Rota '/alunos' já existia")

print("✅ Patch concluído. Reinicie o servidor e acesse /alunos para ver a lista.")
