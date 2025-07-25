import os

templates_dir = "templates"
os.makedirs(templates_dir, exist_ok=True)

templates = {
    "index.html": "Bem-vindo ao SYEMFIT",
    "cadastro.html": "Cadastro de Alunos",
    "assinaturas.html": "Gerenciamento de Assinaturas",
    "financeiro.html": "Controle Financeiro",
    "acesso.html": "Controle de Acesso",
    "agendamentos.html": "Agendamento de Horários",
    "relatorios.html": "Geração de Relatórios",
    "backup.html": "Backup e Restauração",
    "usuarios.html": "Gestão de Usuários",
    "configuracoes.html": "Configurações do Sistema",
    "integracoes.html": "Integrações com APIs e Sistemas"
}

menu_html = """
<div style="background-color: #222; padding: 10px;">
  <a href='/' style='margin-right: 10px; color: #fff;'>Início</a>
  <a href='/cadastro' style='margin-right: 10px; color: #fff;'>Cadastro</a>
  <a href='/assinaturas' style='margin-right: 10px; color: #fff;'>Assinaturas</a>
  <a href='/financeiro' style='margin-right: 10px; color: #fff;'>Financeiro</a>
  <a href='/acesso' style='margin-right: 10px; color: #fff;'>Acesso</a>
  <a href='/agendamentos' style='margin-right: 10px; color: #fff;'>Agendamentos</a>
  <a href='/relatorios' style='margin-right: 10px; color: #fff;'>Relatórios</a>
  <a href='/backup' style='margin-right: 10px; color: #fff;'>Backup</a>
  <a href='/usuarios' style='margin-right: 10px; color: #fff;'>Usuários</a>
  <a href='/configuracoes' style='margin-right: 10px; color: #fff;'>Configurações</a>
  <a href='/integracoes' style='margin-right: 10px; color: #fff;'>Integrações</a>
</div>
"""

for filename, title in templates.items():
    content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SYEMFIT - {title}</title>
</head>
<body>
{menu_html}
    <div style="padding: 20px;">
        <h1>{title}</h1>
        <p>Conteúdo da página {filename}</p>
    </div>
</body>
</html>
"""
    with open(os.path.join(templates_dir, filename), "w") as f:
        f.write(content)

print("✅ Templates com menu gerados com sucesso.")
