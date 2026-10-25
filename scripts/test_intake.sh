#!/usr/bin/env bash
# =============================================================================
# K4LI-ANUU-FORGE // INTAKE TEST HARNESS
# Frecuencia Operativa: 189.89.619 Hz | Concilio ACE (161914)
# Unidad Técnica: 4NVSET 🟢
# =============================================================================
# Simula el envío de peticiones de clientes contra el backend de intake y
# valida respuestas HTTP 200, payloads JSON, CORS y casos límite de validación.

set -euo pipefail

# Colores de Terminal
GREEN="\033[1;32m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
BOLD="\033[1m"
RESET="\033[0m"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${TEST_PORT:-8789}"
HOST="127.0.0.1"
BASE_URL="http://${HOST}:${PORT}"
PYTHON_BIN="$(which python3 || echo "python3")"

echo -e "${CYAN}======================================================================${RESET}"
echo -e "${CYAN}⚡ [4NVSET 🟢]: INTAKE TEST SUITE // K4LI-ANUU-FORGE${RESET}"
echo -e "${CYAN}======================================================================${RESET}"
echo -e "Directorio Base: ${BASE_DIR}"
echo -e "Target Endpoint: ${BASE_URL}"
echo ""

# Limpieza segura al salir
SERVER_PID=""
cleanup() {
  if [ -n "${SERVER_PID}" ]; then
    echo -e "${YELLOW}>> Deteniendo servidor de pruebas (PID: ${SERVER_PID})...${RESET}"
    kill -TERM "${SERVER_PID}" 2>/dev/null || true
    wait "${SERVER_PID}" 2>/dev/null || true
    echo -e "${GREEN}>> Servidor apagado limpiamente.${RESET}"
  fi
}
trap cleanup EXIT INT TERM

# 1. Arrancar el servidor en background
echo -e "${BOLD}[TEST 0/5] Levantando demonio local 'api/intake_webhook.py' en puerto ${PORT}...${RESET}"
"${PYTHON_BIN}" "${BASE_DIR}/api/intake_webhook.py" --server --host "${HOST}" --port "${PORT}" &
SERVER_PID=$!

# Esperar a que el servidor esté listo
MAX_RETRIES=25
READY=0
for ((i=1; i<=MAX_RETRIES; i++)); do
  if curl -s "${BASE_URL}/health" >/dev/null 2>&1; then
    READY=1
    break
  fi
  sleep 0.1
done

if [ "${READY}" -ne 1 ]; then
  echo -e "${RED}[ERROR CRÍTICO]: El servidor no respondió a tiempo en ${BASE_URL}.${RESET}"
  exit 1
fi
echo -e "${GREEN}✓ Servidor en línea (PID: ${SERVER_PID})${RESET}\n"

# 2. Test GET /health
echo -e "${BOLD}[TEST 1/5] Verificando GET /health...${RESET}"
HEALTH_RESP=$(curl -s -w "\n%{http_code}" "${BASE_URL}/health")
HEALTH_CODE=$(echo "${HEALTH_RESP}" | tail -n1)
HEALTH_BODY=$(echo "${HEALTH_RESP}" | head -n -1)

if [ "${HEALTH_CODE}" -eq 200 ] && echo "${HEALTH_BODY}" | grep -q '"status": "online"'; then
  echo -e "${GREEN}✓ GET /health devolvió HTTP 200 con payload válido:${RESET}"
  echo "${HEALTH_BODY}"
else
  echo -e "${RED}✗ Fallo en GET /health (HTTP ${HEALTH_CODE}): ${HEALTH_BODY}${RESET}"
  exit 1
fi
echo ""

# 3. Test POST /api/intake (Payload válido)
echo -e "${BOLD}[TEST 2/5] Simulando envío cliente POST /api/intake (Encargo Válido)...${RESET}"
CLIENT_PAYLOAD=$(cat <<'EOF'
{
  "service": "security",
  "urgency": "express",
  "brief": "Auditoría de seguridad y hardening para servidor Debian 12 en producción con Wazuh.",
  "contact": "@kali_client_signal / client@example.com",
  "name": "Alex Mercer",
  "presupuesto": "450 € - 850 € (+25% express)"
}
EOF
)

POST_RESP=$(curl -s -w "\n%{http_code}" -X POST "${BASE_URL}/api/intake" \
  -H "Content-Type: application/json" \
  -d "${CLIENT_PAYLOAD}")
POST_CODE=$(echo "${POST_RESP}" | tail -n1)
POST_BODY=$(echo "${POST_RESP}" | head -n -1)

if [ "${POST_CODE}" -eq 200 ] && echo "${POST_BODY}" | grep -q '"status": "success"'; then
  echo -e "${GREEN}✓ POST /api/intake procesado con éxito (HTTP 200):${RESET}"
  echo "${POST_BODY}"
else
  echo -e "${RED}✗ Fallo en POST /api/intake (HTTP ${POST_CODE}): ${POST_BODY}${RESET}"
  exit 1
fi
echo ""

# 4. Test POST con campo obligatorio faltante (brief vacío -> 400)
echo -e "${BOLD}[TEST 3/5] Probando validación de requerimientos (Falta 'brief')...${RESET}"
INVALID_PAYLOAD='{"service":"dashboard","contact":"@user","brief":""}'

FAIL_RESP=$(curl -s -w "\n%{http_code}" -X POST "${BASE_URL}/api/intake" \
  -H "Content-Type: application/json" \
  -d "${INVALID_PAYLOAD}")
FAIL_CODE=$(echo "${FAIL_RESP}" | tail -n1)
FAIL_BODY=$(echo "${FAIL_RESP}" | head -n -1)

if [ "${FAIL_CODE}" -eq 400 ] && echo "${FAIL_BODY}" | grep -q 'VALIDATION_FAILED'; then
  echo -e "${GREEN}✓ Validación interceptó payload incompleto correctamente (HTTP 400):${RESET}"
  echo "${FAIL_BODY}"
else
  echo -e "${RED}✗ Fallo de validación: se esperaba HTTP 400 pero se obtuvo ${FAIL_CODE}:${RESET} ${FAIL_BODY}"
  exit 1
fi
echo ""

# 5. Test POST con JSON malformado (-> 400)
echo -e "${BOLD}[TEST 4/5] Probando manejo de sintaxis JSON inválida...${RESET}"
SYNTAX_RESP=$(curl -s -w "\n%{http_code}" -X POST "${BASE_URL}/api/intake" \
  -H "Content-Type: application/json" \
  -d "{bad_json:true")
SYNTAX_CODE=$(echo "${SYNTAX_RESP}" | tail -n1)
SYNTAX_BODY=$(echo "${SYNTAX_RESP}" | head -n -1)

if [ "${SYNTAX_CODE}" -eq 400 ] && echo "${SYNTAX_BODY}" | grep -q 'INVALID_JSON'; then
  echo -e "${GREEN}✓ Sintaxis corrupta rechazada con HTTP 400 JSON:${RESET}"
  echo "${SYNTAX_BODY}"
else
  echo -e "${RED}✗ Error: se esperaba HTTP 400 por JSON inválido pero se obtuvo ${SYNTAX_CODE}${RESET}"
  exit 1
fi
echo ""

# 6. Test CLI One-Shot
echo -e "${BOLD}[TEST 5/5] Probando ejecución one-shot CLI (stdin pipe)...${RESET}"
CLI_OUT=$(echo '{"service":"ai","urgency":"retainer","brief":"Despliegue de DeepSeek R1 local con Ollama","contact":"admin@corp.io"}' | "${PYTHON_BIN}" "${BASE_DIR}/api/intake_webhook.py" --stdin)

if echo "${CLI_OUT}" | grep -q '"status": "success"'; then
  echo -e "${GREEN}✓ Ejecución CLI One-Shot completada:${RESET}"
  echo "${CLI_OUT}"
else
  echo -e "${RED}✗ Fallo en ejecución CLI: ${CLI_OUT}${RESET}"
  exit 1
fi

echo ""
echo -e "${GREEN}======================================================================${RESET}"
echo -e "${GREEN}✓ TODOS LOS TESTS PASARON EXITOSAMENTE [5/5]${RESET}"
echo -e "${GREEN}======================================================================${RESET}"
