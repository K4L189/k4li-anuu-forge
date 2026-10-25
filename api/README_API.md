# ⚡ K4LI-ANUU-FORGE // INTAKE & DISPATCH BACKEND

> **Frecuencia Operativa:** `189.89.619 Hz` | **Concilio ACE:** `161914`  
> **Unidad Técnica:** `4NVSET 🟢`  
> **Coste de Infraestructura:** `0 € / mes` (Free Tier Cloudflare Workers o Daemons locales)

Infraestructura de recepción técnica y despacho de encargos para el ecosistema **K4li Forge**. Diseñado con una arquitectura dual intercambiable:
1. **Edge Serverless (Recomendado para producción):** [Cloudflare Worker (`api/worker_cloudflare.js`)](file:///home/kali/k4li-anuu-forge/api/worker_cloudflare.js).
2. **Local Daemon (Self-hosted / VPS / Kali):** [Python Webhook (`api/intake_webhook.py`)](file:///home/kali/k4li-anuu-forge/api/intake_webhook.py).

---

## 🛰️ 1. Configuración de Credenciales Telegram (Bot & Chat)

Para recibir las alertas instantáneas en tu Telegram privado o canal cifrado:

### Paso 1: Crear el Bot de Telegram
1. Abre Telegram y busca el bot oficial **`@BotFather`**.
2. Envía el comando `/newbot`.
3. Asigna un nombre (ej. `K4li Forge Dispatcher`) y un username terminado en `bot` (ej. `k4li_forge_intake_bot`).
4. `@BotFather` te responderá con tu **Token de Acceso HTTP**:
   ```
   TELEGRAM_BOT_TOKEN="7123456789:AAFlm3k_XXXXXXXXXXXXXX_K4liSec"
   ```

### Paso 2: Obtener tu Chat ID (`TELEGRAM_CHAT_ID`)
1. Inicia conversación con tu nuevo bot pulsando **Start / Iniciar** o enviándole un mensaje como `/start`.
2. Para conocer tu Chat ID personal:
   - Opción rápida: Consulta al bot **`@userinfobot`** en Telegram; te devolverá tu `Id` numérico (ej. `987654321`).
   - Opción por API: Abre en tu navegador sustituyendo tu token:
     ```
     https://api.telegram.org/bot<TU_TELEGRAM_BOT_TOKEN>/getUpdates
     ```
     Busca dentro del JSON: `"chat":{"id": 987654321, ...}`.
3. Si deseas enviar las alertas a un **Grupo o Canal**:
   - Invita al bot al grupo como administrador.
   - Envía un mensaje en el grupo y revisa `getUpdates` (el ID de grupo suele empezar por `-100...`).

---

## ☁️ 2. Opción A: Despliegue en Cloudflare Worker (0 € / mes)

El Worker opera en más de 330 ubicaciones mundiales de Cloudflare con latencia ultra baja, filtrado DDoS y 100.000 peticiones gratuitas al día.

### Método 1: Despliegue con Wrangler CLI
Desde cualquier máquina con Node.js / npm:

```bash
# 1. Instalar o ejecutar wrangler
npx wrangler login

# 2. Configurar las variables secretas cifradas en Cloudflare
npx wrangler secret put TELEGRAM_BOT_TOKEN
# (Introduce el token de BotFather cuando te lo pida)

npx wrangler secret put TELEGRAM_CHAT_ID
# (Introduce el Chat ID numérico)

# (Opcional) Webhook secundario (ej. Discord)
npx wrangler secret put WEBHOOK_URL

# 3. Desplegar el worker
npx wrangler deploy api/worker_cloudflare.js --name k4li-forge-intake
```

Tu worker quedará publicado en `https://k4li-forge-intake.<tu-subdominio>.workers.dev`.

### Método 2: Despliegue visual desde el Panel Web de Cloudflare
1. Entra en [dash.cloudflare.com](https://dash.cloudflare.com/) > **Workers & Pages** > **Create Application**.
2. Asigna el nombre `k4li-forge-intake` y pulsa **Deploy**.
3. Pulsa **Edit code**, pega el contenido de [`api/worker_cloudflare.js`](file:///home/kali/k4li-anuu-forge/api/worker_cloudflare.js) y pulsa **Save and Deploy**.
4. Ve a la pestaña **Settings** > **Variables and Secrets** > **Secrets** y añade:
   - `TELEGRAM_BOT_TOKEN`: `TU_TOKEN`
   - `TELEGRAM_CHAT_ID`: `TU_CHAT_ID`
   - `CORS_ORIGIN`: `*` (o el dominio `https://kali-anuu.github.io`)

---

## 🐍 3. Opción B: Despliegue Servidor Local / VPS (Python)

El script [`api/intake_webhook.py`](file:///home/kali/k4li-anuu-forge/api/intake_webhook.py) utiliza únicamente la biblioteca estándar de Python (zero external dependencies).

### Ejecución Directa
```bash
export TELEGRAM_BOT_TOKEN="7123456789:AAFlm3k_XXXXXXXXXXXXXX_K4liSec"
export TELEGRAM_CHAT_ID="987654321"
export PORT="8787"

python3 /home/kali/k4li-anuu-forge/api/intake_webhook.py --server --port 8787
```

### Configuración como Servicio Systemd (`/etc/systemd/system/k4li-intake.service`)
```ini
[Unit]
Description=K4li Forge Intake Webhook Daemon (189.89.619 Hz)
After=network.target

[Service]
Type=simple
User=kali
WorkingDirectory=/home/kali/k4li-anuu-forge
Environment=PORT=8787
Environment=TELEGRAM_BOT_TOKEN=7123456789:AAFlm3k_XXXXXXXXXXXXXX_K4liSec
Environment=TELEGRAM_CHAT_ID=987654321
Environment=CORS_ORIGIN=*
ExecStart=/usr/bin/python3 /home/kali/k4li-anuu-forge/api/intake_webhook.py --server
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Habilitar e iniciar:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now k4li-intake
sudo systemctl status k4li-intake
```

### Proxy Inverso Nginx (Opcional)
```nginx
location /api/intake {
    proxy_pass http://127.0.0.1:8787/api/intake;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

---

## 📡 4. Especificación del Payload JSON

### Petición `POST /api/intake`
```json
{
  "service": "security",
  "urgency": "express",
  "brief": "Auditoría de seguridad y hardening para servidor Debian 12 en producción.",
  "contact": "@k4li_client_signal / client@example.com",
  "name": "Alex Mercer",
  "presupuesto": "450 € - 850 €"
}
```

| Campo | Tipo | Requerido | Descripción / Valores |
|---|---|---|---|
| `service` | string | Sí | `security`, `dashboard`, `ai`, `automation` |
| `urgency` | string | No | `normal`, `express`, `retainer` (defecto: `normal`) |
| `brief` | string | Sí | Descripción técnica (mínimo 5 caracteres) |
| `contact` | string | Sí | Signal ID, Telegram handle o correo electrónico |
| `name` | string | No | Nombre o razón social del cliente |
| `presupuesto` | string | No | Estimación económica calculada por la UI |

### Respuesta `HTTP 200 OK`
```json
{
  "status": "success",
  "message": "Petición técnica registrada correctamente.",
  "service": "security",
  "urgency": "express",
  "timestamp": "2026-10-25 05:02:48 UTC",
  "dispatch": {
    "telegram": "telegram_delivered",
    "webhook": "no_webhook_configured"
  }
}
```

---

## 🧪 5. Verificación y Pruebas Automatizadas

El repositorio incluye el suite [`scripts/test_intake.sh`](file:///home/kali/k4li-anuu-forge/scripts/test_intake.sh). Ejecuta de forma aislada:
- Comprobación de salud `GET /health`
- Validación de intake completo `POST /api/intake`
- Pruebas negativas de integridad de payload (campo `brief` omitido)
- Pruebas negativas de sintaxis JSON corrupta
- Ejecución CLI en tubería (stdin)

Ejecutar:
```bash
chmod +x scripts/test_intake.sh
./scripts/test_intake.sh
```

---

## 💻 6. Enlace en el Frontend (`index.html`)

En `index.html`, la función `handleFormSubmit` despacha la petición al endpoint configurado en `window.FORGE_INTAKE_ENDPOINT` (o `/api/intake` por defecto). Si estás usando el Cloudflare Worker, puedes configurar en tu HTML o cabecera:

```html
<script>
  // Apunta a tu Cloudflare Worker desplegado:
  window.FORGE_INTAKE_ENDPOINT = "https://k4li-forge-intake.<tu-subdominio>.workers.dev/api/intake";
</script>
```

Si la red estuviera desconectada o la petición tardara, el formulario garantiza la continuidad de negocio ofreciendo instantáneamente el enlace directo E2EE a **Signal**.
