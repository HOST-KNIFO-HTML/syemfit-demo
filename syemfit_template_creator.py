import os

print("🛠️ SYEMFIT TEMPLATE CREATOR")
print("────────────────────────────\n")

# Templates faltando (você pode importar do outro script, mas aqui é fixo para executar direto)
missing_templates = ["logout.html"]

template_dir = "templates"

# Conteúdo base
template_base = lambda name: f"""{{% extends "base.html" %}}

{{% block content %}}
    <h1>{name.replace(".html", "").capitalize()}</h1>
    <p>Este é o template <strong>{name}</strong>.</p>
{{% endblock %}}
"""

for tpl in missing_templates:
    path = os.path.join(template_dir, tpl)
    if os.path.exists(path):
        print(f"✅ {tpl} já existe, pulando.")
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(template_base(tpl))
        print(f"🆕 Criado: {tpl}")

print("\n✅ Todos os templates faltantes foram criados.")
