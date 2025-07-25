import sqlite3

print("📦 Verificando estrutura da tabela 'alunos'...")

conn = sqlite3.connect('syemfit.db')
cursor = conn.cursor()

# Cria tabela caso não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    telefone TEXT,
    observacoes TEXT
);
""")

# Lista de colunas esperadas
colunas_necessarias = {
    'nome': 'TEXT',
    'idade': 'INTEGER',
    'telefone': 'TEXT',
    'observacoes': 'TEXT',
    'foto': 'TEXT'
}

# Recupera colunas atuais
cursor.execute("PRAGMA table_info(alunos);")
colunas_atuais = {col[1]: col[2] for col in cursor.fetchall()}

# Verifica e adiciona colunas ausentes
for coluna, tipo in colunas_necessarias.items():
    if coluna not in colunas_atuais:
        cursor.execute(f"ALTER TABLE alunos ADD COLUMN {coluna} {tipo};")
        print(f"🧩 Coluna '{coluna}' adicionada.")

if all(c in colunas_atuais for c in colunas_necessarias):
    print("✅ Tabela 'alunos' já estava completa.")
else:
    print("✅ Tabela 'alunos' atualizada com colunas faltantes.")

conn.commit()
conn.close()
