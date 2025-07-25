import os

ROUTES = [
    'cadastro',
    'assinaturas',
    'financeiro',
    'acesso',
    'agendamentos',
    'relatorios',
    'backup',
    'usuarios',
    'configuracoes',
    'integracoes'
]

TEMPLATE_DIR = 'templates'
MAIN_FILE = 'main.py'

def append_route_to_main(route):
    route_block = f'''

@app.route('/{route}')
def {route}():
    return render_template('{route}.html')
'''
    with open(MAIN_FILE, 'a') as f:
        f.write(route_block)

def create_template(route):
    path = os.path.join(TEMPLATE_DIR, f'{route}.html')
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(f'''{{% extends "base.html" %}}
{{% block content %}}
<h2>{route.capitalize()}</h2>
<p>Página de {route} em construção.</p>
{{% endblock %}}''')

if __name__ == '__main__':
    print('📦 Iniciando verificação de rotas SYEMFIT...')
    existing_templates = set(os.listdir(TEMPLATE_DIR))
    created = 0

    for route in ROUTES:
        if f'{route}.html' not in existing_templates:
            create_template(route)
            print(f'🆕 Template criado: {route}.html')
            created += 1

        with open(MAIN_FILE) as f:
            content = f.read()
            if f'def {route}()' not in content:
                append_route_to_main(route)
                print(f'🧩 Rota adicionada ao main.py: {route}()')

    print(f'\n✅ Auditoria concluída. {created} templates criados.\n⚠️ Reinicie o servidor para aplicar as rotas.')
