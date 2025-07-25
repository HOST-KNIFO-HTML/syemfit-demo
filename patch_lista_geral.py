import os

print("📦 Criando rota de listagem geral filtrável por tipo...")

TEMPLATE = '''<!DOCTYPE html>
<html>
<head><title>Listagem Geral</title></head>
<body style="background-color: black; color: white;">
    <h1>Lista Geral</h1>
    <form method="get" action="/cadastros">
        <label for="tipo">Filtrar por tipo:</label>
        <select name="tipo">
            <option value="">Todos</option>
            <option value="aluno">Aluno</option>
            <option value="profissional">Profissional</option>
            <option value="sócio">Sócio</option>
        </select>
        <input type="submit" value="Filtrar">
    </form>
    <ul>
        {% for item in cadastros %}
            <li>{{ item[1] }} - {{ item[5] }}</li>
        {% endfor %}
    </ul>
</body>
</html>'''

os.makedirs("templates", exist_ok=True)
with open("templates/lista_geral.html", "w") as f:
    f.write(TEMPLATE)
print("✅ Template criado: templates/lista_geral.html")

ROTA = '''
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
'''

with open("main.py", "r") as f:
    codigo = f.read()

if "def listar_cadastros():" not in codigo:
    with open("main.py", "a") as f:
        f.write(ROTA)
    print("✅ Rota '/cadastros' adicionada ao main.py")
else:
    print("⚠️ Rota já existente no main.py")

print("✅ Patch finalizado. Reinicie o servidor e acesse /cadastros para testar.")
