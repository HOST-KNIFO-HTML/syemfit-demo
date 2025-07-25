#!/bin/bash
echo "📦 Exportando POC final em modo PREMIUM..."
cd "$(dirname "$0")"

ZIP_NAME="syemfit_poc.zip"
FILES="app.py seed.py requirements.txt banco.db templates static docs"

# Verifica e inclui apenas o que existe
INCLUDE=""
for item in $FILES; do
  [ -e "$item" ] && INCLUDE="$INCLUDE $item"
done

zip -r "$ZIP_NAME" $INCLUDE > /dev/null

echo "✅ Exportação finalizada: $ZIP_NAME"
sha256sum "$ZIP_NAME"
