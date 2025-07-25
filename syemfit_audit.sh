#!/bin/bash
echo "📦 SYEMFIT AUDITOR v1.0 - $(date)"
echo "────────────────────────────────────────────"

ROOT_DIR="./"
TEMPLATES_DIR="${ROOT_DIR}/templates"
STATIC_DIR="${ROOT_DIR}/static"
REQUIRED_PY=("main.py" "app.py" "seed.py")
REQUIRED_DIRS=("templates" "static" "logs" "uploads" "backups" "docs")
REQUIRED_FILES=("requirements.txt" "banco.db" "syemfit_appcheck.sh" "syemfit_audit.sh")

# Função para checar presença
check_file() {
    if [[ -f "$1" ]]; then
        echo "✅ $1"
    else
        echo "❌ $1 (FALTANDO)"
    fi
}

check_dir() {
    if [[ -d "$1" ]]; then
        echo "📁 $1/ encontrado"
    else
        echo "❌ Diretório $1/ NÃO encontrado"
    fi
}

echo "🔍 Verificando diretórios..."
for dir in "${REQUIRED_DIRS[@]}"; do
    check_dir "${ROOT_DIR}/${dir}"
done

echo ""
echo "🔍 Verificando arquivos principais..."
for file in "${REQUIRED_FILES[@]}"; do
    check_file "${ROOT_DIR}/${file}"
done

echo ""
echo "🔍 Verificando scripts Python..."
for py in "${REQUIRED_PY[@]}"; do
    check_file "${ROOT_DIR}/${py}"
done

echo ""
echo "🧩 Verificando templates HTML..."
if [[ -d "$TEMPLATES_DIR" ]]; then
    COUNT=$(find "$TEMPLATES_DIR" -name "*.html" | wc -l)
    echo "🗂️  $COUNT arquivos .html encontrados em $TEMPLATES_DIR"
    find "$TEMPLATES_DIR" -name "*.html" -exec basename {} \;
else
    echo "❌ Diretório templates/ não encontrado"
fi

echo ""
echo "🧪 Verificando estilo (CSS)..."
if [[ -f "${STATIC_DIR}/style.css" ]]; then
    echo "✅ style.css localizado"
else
    echo "❌ style.css não encontrado em static/"
fi

echo "────────────────────────────────────────────"
echo "✅ Auditoria concluída!"
