#!/bin/bash

APP_FILE="./app.py"
echo "🧠 SYEMFIT APP INSPECTOR | $(date)"
echo "📄 Verificando: $APP_FILE"
echo "────────────────────────────────────────────"

check() {
    local label="$1"
    local pattern="$2"
    if grep -qE "$pattern" "$APP_FILE"; then
        echo "✅ $label"
    else
        echo "❌ $label NÃO encontrado"
        return 1
    fi
}

fail=0

check "Importações Flask" "from flask|import Flask"
((fail+=$?))

check "Chave secreta definida" "app\.secret_key\s*="
((fail+=$?))

check "Função get_db_connection()" "def get_db_connection\(\)"
((fail+=$?))

check "Rota de login" "@app\.route\(['\"]?/login['\"].*methods=\[.*POST.*\]"
((fail+=$?))

check "Rota de dashboard" "@app\.route\(['\"]?/dashboard['\"]?\)"
((fail+=$?))

check "Rota de logout" "@app\.route\(['\"]?/logout['\"]?\)"
((fail+=$?))

check "Sessão verificada" "if 'user' in session|if 'user' not in session"
((fail+=$?))

check "Mensagens flash implementadas" "flash\("
((fail+=$?))

check "Renderização do dashboard" "render_template\(['\"]dashboard\.html['\"]"
((fail+=$?))

check "Redirecionamento de login presente" "redirect\(url_for\(['\"]login['\"]"
((fail+=$?))

echo "────────────────────────────────────────────"
if [[ $fail -eq 0 ]]; then
    echo "🎯 Todos os blocos críticos foram encontrados. app.py OK!"
else
    echo "⚠️ Um ou mais blocos críticos estão ausentes. Recomenda-se revisar o app.py."
fi
