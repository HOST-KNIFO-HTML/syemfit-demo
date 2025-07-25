import os

# Rotas a serem garantidas com base nos botões do menu
ROUTES = [
    'cadastro', 'assinaturas', 'financeiro', 'acesso', 'agendamentos',
    'relatorios', 'backup', 'usuarios', 'configuracoes', 'integracoes'
]

TEMPLATE_DIR = 'templates'
MAIN_FILE = 'main.py'

def append_route_to_main(route):
    block = f'''

@app.route('/{route}')
def {route}():
    return render_template('{route}.html')
'''
    with open(MAIN_FILE, 'a') as f:
        f.write(block)

def create_template(route):
    filepath = os.path.join(TEMPLATE_DIR, f'{route}.html')
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(f'''{{% extends "base.html" %}}

{{% block content %}}
<div class="container">
  <h2>{route.capitalize()}</h2>
  <p>Em breve conteúdo dinâmico de <strong>{route}</strong>.</p>
</div>
{{% endblock %}}''')

def route_exists_in_main(route):
    with open(MAIN_FILE, 'r') as f:
        return f'def {route}()' in f.read()

def main():
    print('🧩 PATCH SYEMFIT ROUTES\n────────────────────────────')
    created_routes = 0
    created_templates = 0

    for route in ROUTES:
        if not os.path.exists(os.path.join(TEMPLATE_DIR, f'{route}.html')):
            create_template(route)
            print(f'✅ Template gerado: {route}.html')
            created_templates += 1

        if not route_exists_in_main(route):
            append_route_to_main(route)
            print(f'✅ Rota adicionada: def {route}()')
            created_routes += 1

    print(f'\n📊 Resultados:')
    print(f'→ {created_routes} rotas adicionadas ao main.py')
    print(f'→ {created_templates} templates criados em /templates/')
    print('✅ Finalizado! Reinicie a aplicação para testar.')

if __name__ == '__main__':
    main()
