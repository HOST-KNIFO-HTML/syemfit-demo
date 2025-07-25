import os
import re

print("📦 SYEMFIT TEMPLATE AUDITOR")
print("────────────────────────────\n")

# Caminhos
main_file = "main.py"
templates_dir = "templates"

# Regex para encontrar @app.route("/...") ou @app.route('/...') com função correspondente
route_pattern = re.compile(r"""@app\.route\(["']/(.+?)["']\)\s+def\s+(\w+)""")

# Rotas encontradas
routes = []

# Lê o main.py
with open(main_file, "r", encoding="utf-8") as f:
    content = f.read()
    matches = route_pattern.findall(content)
    for route, func_name in matches:
        routes.append(func_name)

# Templates existentes
existing_templates = set(f for f in os.listdir(templates_dir) if f.endswith(".html"))
expected_templates = set(f"{r}.html" for r in routes)

# Auditoria
print("🔍 Funções de rota detectadas em main.py:")
for r in routes:
    print(f" → {r}()")

print("\n🗂️ Arquivos HTML esperados em /templates:")
for tpl in expected_templates:
    status = "✅" if tpl in existing_templates else "❌"
    print(f"   {status} {tpl}")

# Resumo
missing = expected_templates - existing_templates
print("\n📊 Resumo:")
print(f"→ {len(existing_templates & expected_templates)} templates OK")
print(f"→ {len(missing)} templates FALTANDO")

if missing:
    print("\n⚠️ Templates faltando:")
    for m in sorted(missing):
        print(f"   - {m}")

print("\n✅ Auditoria concluída.")
