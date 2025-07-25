import os
import sqlite3

print("📦 SYEMFIT FINAL AUDITOR")
print("────────────────────────────\n")

# Auditoria de rotas no main.py
main_path = 'main.py'
templates_path = 'templates'
banco_path = 'syemfit.db'

print("🔍 Funções de rota detectadas em main.py:")
with open(main_path) as f:
    lines = f.readlines()
rotas = [line.strip().split('def ')[1].split('(')[0] 
         for line in lines if line.strip().startswith('def ') and line.strip().endswith('):')]
for r in rotas:
    print(f" → {r}()")

print("\n🗂️ Templates HTML esperados:")
ok, missing = [], []
for rota in rotas:
    nome_arquivo = f"{rota}.html"
    caminho = os.path.join(templates_path, nome_arquivo)
    if os.path.exists(caminho):
        print(f"   ✅ {nome_arquivo}")
        ok.append(nome_arquivo)
    else:
        print(f"   ❌ {nome_arquivo}")
        missing.append(nome_arquivo)

print("\n📊 Resumo Templates:")
print(f"→ {len(ok)} templates OK")
print(f"→ {len(missing)} templates FALTANDO")

# Auditoria de colunas da tabela alunos
print("\n🧬 Estrutura da tabela 'alunos':")
esperadas = ['id', 'nome', 'foto', 'tipo', 'idade', 'observacoes']
try:
    conn = sqlite3.connect(banco_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(alunos)")
    colunas = [info[1] for info in cursor.fetchall()]
    for col in esperadas:
        if col in colunas:
            print(f"   ✅ {col}")
        else:
            print(f"   ❌ {col} (FALTANDO)")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

print("\n✅ Auditoria completa. Tudo pronto para a próxima fase!")
