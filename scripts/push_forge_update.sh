#!/usr/bin/env bash
set -e
cd /home/kali/k4li-anuu-forge

echo "=== K4L1 STUDIO // DESPLIEGUE FINAL ASSETS Y TARJETAS ==="
if [ -z "$1" ]; then
    echo "Uso: ./scripts/push_forge_update.sh <TU_NUEVO_GITHUB_TOKEN>"
    exit 1
fi

TOKEN="$1"
git add assets/ components/ docs/ index.html manifest.json sw.js
git commit -m "feat(brand-ui): deploy bespoke SVG icons, PWA master seals, OG card and reactive forge cards (161914)"
git push https://K4L189:${TOKEN}@github.com/K4L189/k4li-anuu-forge.git main

echo "[✓] ¡Despliegue a GitHub completado con éxito!"
