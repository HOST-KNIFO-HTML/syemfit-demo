import sqlite3
from datetime import datetime

db_path = "syemfit.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("📦 Criando tabela alunos...")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT,
    telefone TEXT,
    nascimento TEXT,
    genero TEXT,
    objetivo TEXT,
    foto TEXT,
    data_cadastro TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()
print("✅ Tabela 'alunos' criada com sucesso!")
