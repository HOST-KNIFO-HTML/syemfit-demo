# auditoria_tipo_coluna.py
import sqlite3

print("📦 Verificando estrutura da tabela 'alunos'...")

conn = sqlite3.connect("syemfit.db")
cursor = conn.cursor()

# Buscar colunas existentes
cursor.execute("PRAGMA table_info(alunos)")
colunas = [col[1] for col in cursor.fetchall()]

adicionados = []
if "tipo" not in colunas:
    cursor.execute("ALTER TABLE alunos ADD COLUMN tipo TEXT")
    adicionados.append("tipo")

if "observacoes" not in colunas:
    cursor.execute("ALTER TABLE alunos ADD COLUMN observacoes TEXT")
    adicionados.append("observacoes")

if "foto" not in colunas:
    cursor.execute("ALTER TABLE alunos ADD COLUMN foto TEXT")
    adicionados.append("foto")

conn.commit()
conn.close()

if adicionados:
    for col in adicionados:
        print(f"🧩 Coluna '{col}' adicionada.")
    print("✅ Tabela 'alunos' atualizada com colunas faltantes.")
else:
    print("✅ Nenhuma alteração necessária. Estrutura completa.")
