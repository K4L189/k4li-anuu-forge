#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
K4LI-ANUU-FORGE // INTAKE WEBHOOK BACKEND
Frecuencia Operativa: 189.89.619 Hz | Concilio ACE (161914)
Unidad Técnica: 4NVSET 🟢
=============================================================================
Procesa peticiones de cotización y requerimientos técnicos desde la UI de Forge.
Valida el payload JSON y despacha alertas formateadas a Telegram / Webhook.
"""

import sys
import os
import json
import re
import html
import time
import datetime
import argparse
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.error
import urllib.parse

# Configuración y Variables de Entorno
PORT = int(os.getenv("PORT", "8787"))
HOST = os.getenv("HOST", "0.0.0.0")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()
WEBHOOK_URL = os.getenv("WEBHOOK_URL", os.getenv("DISCORD_WEBHOOK_URL", "")).strip()
CORS_ORIGIN = os.getenv("CORS_ORIGIN", "*")
MAX_PAYLOAD_BYTES = 65536  # 64 KB

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [4NVSET-INTAKE] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("intake_webhook")

SERVICE_MAP = {
    "security": "🛡️ Auditoría / Hardening / SIEM Wazuh",
    "dashboard": "📊 Dashboard React / Web App",
    "ai": "🧠 IA Local Soberana (On-Prem LLM)",
    "automation": "⚙️ Automatización / Bots / Scrapers"
}

URGENCY_MAP = {
    "normal": "⏱️ Estándar (1-2 semanas)",
    "express": "🚨 Urgente / Express (3-5 días) [+25%]",
    "retainer": "🔄 Mantenimiento Mensual Recurrente"
}


def sanitize_input(val: str, max_length: int = 2000) -> str:
    """Limpia caracteres de control y acota longitud máxima."""
    if not isinstance(val, str):
        val = str(val or "")
    val = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", val)
    return val.strip()[:max_length]


def validate_intake_payload(data: dict) -> tuple[bool, str, dict]:
    """Valida los campos obligatorios del payload de cotización/intake."""
    if not isinstance(data, dict):
        return False, "El cuerpo de la petición debe ser un objeto JSON válido.", {}

    raw_service = sanitize_input(data.get("service", "security"), 50).lower()
    raw_urgency = sanitize_input(data.get("urgency", "normal"), 50).lower()
    raw_brief = sanitize_input(data.get("brief", ""), 2500)
    raw_contact = sanitize_input(data.get("contact", ""), 200)
    raw_name = sanitize_input(data.get("name") or data.get("clientName") or "Cliente Anónimo", 150)
    raw_budget = sanitize_input(data.get("presupuesto") or data.get("budget") or data.get("priceDisplay") or "A determinar", 100)

    # Validaciones críticas
    if not raw_brief or len(raw_brief) < 5:
        return False, "El campo 'brief' es obligatorio (mínimo 5 caracteres).", {}

    if not raw_contact or len(raw_contact) < 3:
        return False, "El campo 'contact' (Signal/Email/Telegram) es obligatorio.", {}

    service_label = SERVICE_MAP.get(raw_service, f"🛠️ {raw_service.capitalize()}")
    urgency_label = URGENCY_MAP.get(raw_urgency, f"⏱️ {raw_urgency.capitalize()}")

    iso_timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    cleaned_data = {
        "service_raw": raw_service,
        "service_label": service_label,
        "urgency_raw": raw_urgency,
        "urgency_label": urgency_label,
        "brief": raw_brief,
        "contact": raw_contact,
        "name": raw_name,
        "budget": raw_budget,
        "timestamp": iso_timestamp
    }
    return True, "", cleaned_data


def format_telegram_message(clean: dict) -> str:
    """Genera mensaje formateado en HTML compatible con Telegram Bot API."""
    esc_name = html.escape(clean["name"])
    esc_contact = html.escape(clean["contact"])
    esc_service = html.escape(clean["service_label"])
    esc_urgency = html.escape(clean["urgency_label"])
    esc_budget = html.escape(clean["budget"])
    esc_brief = html.escape(clean["brief"])
    esc_time = html.escape(clean["timestamp"])

    msg = (
        "⚡ <b>NUEVO ENCARGO TÉCNICO // K4LI FORGE</b> ⚡\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>Cliente:</b> {esc_name}\n"
        f"📡 <b>Contacto:</b> <code>{esc_contact}</code>\n"
        f"🛠️ <b>Servicio:</b> {esc_service}\n"
        f"⏱️ <b>Urgencia:</b> {esc_urgency}\n"
        f"💰 <b>Presupuesto:</b> {esc_budget}\n"
        f"📅 <b>Fecha:</b> {esc_time}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "📝 <b>Requerimiento Técnico:</b>\n"
        f"<blockquote>{esc_brief}</blockquote>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔒 <i>ACE Council (161914) · Frecuencia: 189.89.619 Hz</i>"
    )
    return msg


def dispatch_telegram(message_html: str) -> tuple[bool, str]:
    """Envía la notificación formateada a Telegram Bot API."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logger.info("[DISPATCH_MOCK] Variables de Telegram no configuradas. Simulando entrega OK.")
        return True, "mock_delivered"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message_html,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            resp_body = resp.read().decode("utf-8")
            res_json = json.loads(resp_body)
            if res_json.get("ok"):
                return True, "telegram_delivered"
            return False, f"Telegram API error: {res_json}"
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="ignore")
        logger.error(f"Error HTTP al contactar Telegram: {e.code} - {err_msg}")
        return False, f"HTTPError {e.code}: {err_msg}"
    except Exception as e:
        logger.error(f"Excepción en dispatch_telegram: {e}")
        return False, str(e)


def dispatch_webhook(clean: dict, message_html: str) -> tuple[bool, str]:
    """Envía la notificación a un webhook secundario (Discord / Slack / Genérico)."""
    if not WEBHOOK_URL:
        return True, "no_webhook_configured"

    is_discord = "discord.com" in WEBHOOK_URL or "discordapp.com" in WEBHOOK_URL
    if is_discord:
        body = {
            "content": "⚡ **NUEVO INTAKE TÉCNICO // K4LI FORGE** ⚡",
            "embeds": [{
                "title": f"Proyecto: {clean['service_label']}",
                "color": 65280,  # Emerald
                "fields": [
                    {"name": "Cliente", "value": clean["name"], "inline": True},
                    {"name": "Contacto", "value": clean["contact"], "inline": True},
                    {"name": "Urgencia", "value": clean["urgency_label"], "inline": True},
                    {"name": "Presupuesto", "value": clean["budget"], "inline": True},
                    {"name": "Brief", "value": clean["brief"][:1024], "inline": False}
                ],
                "footer": {"text": f"K4li Forge · {clean['timestamp']}"}
            }]
        }
    else:
        body = {
            "text": f"Nuevo encargo de {clean['name']} ({clean['contact']}): {clean['service_label']}",
            "payload": clean
        }

    try:
        data_bytes = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            WEBHOOK_URL,
            data=data_bytes,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return True, f"webhook_delivered_{resp.status}"
    except Exception as e:
        logger.warning(f"Fallo enviando a WEBHOOK_URL: {e}")
        return False, str(e)


def process_intake(data: dict) -> tuple[int, dict]:
    """Ejecuta el pipeline completo de validación y despacho."""
    valid, err_msg, clean = validate_intake_payload(data)
    if not valid:
        return 400, {
            "status": "error",
            "code": "VALIDATION_FAILED",
            "message": err_msg
        }

    telegram_msg = format_telegram_message(clean)
    tg_ok, tg_status = dispatch_telegram(telegram_msg)
    wh_ok, wh_status = dispatch_webhook(clean, telegram_msg)

    response_payload = {
        "status": "success",
        "message": "Petición técnica registrada correctamente.",
        "service": clean["service_raw"],
        "urgency": clean["urgency_raw"],
        "timestamp": clean["timestamp"],
        "dispatch": {
            "telegram": tg_status,
            "webhook": wh_status
        }
    }
    return 200, response_payload


class IntakeHTTPRequestHandler(BaseHTTPRequestHandler):
    """Manejador HTTP ligero con soporte CORS y rutas de intake."""

    def _set_cors_headers(self, status_code: int = 200):
        self.send_response(status_code)
        self.send_header("Access-Control-Allow-Origin", CORS_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With")
        self.send_header("Access-Control-Max-Age", "86400")
        self.send_header("Content-Type", "application/json; charset=utf-8")

    def do_OPTIONS(self):
        """Maneja preflight CORS del navegador."""
        self._set_cors_headers(204)
        self.end_headers()

    def do_GET(self):
        """Endpoint de salud y comprobación de estado."""
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ("/", "/health", "/api/intake"):
            self._set_cors_headers(200)
            self.end_headers()
            payload = {
                "status": "online",
                "service": "k4li-anuu-forge-intake",
                "version": "1.0.0",
                "frequency": "189.89.619 Hz",
                "telegram_configured": bool(TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID),
                "webhook_configured": bool(WEBHOOK_URL)
            }
            self.wfile.write(json.dumps(payload, indent=2).encode("utf-8"))
        else:
            self._set_cors_headers(404)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": "Not Found"}).encode("utf-8"))

    def do_POST(self):
        """Recibe y procesa el intake en JSON."""
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path not in ("/", "/api/intake", "/intake"):
            self._set_cors_headers(404)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": "Ruta no encontrada"}).encode("utf-8"))
            return

        content_length = self.headers.get("Content-Length")
        if not content_length:
            self._set_cors_headers(411)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": "Content-Length requerido"}).encode("utf-8"))
            return

        try:
            length = int(content_length)
            if length > MAX_PAYLOAD_BYTES:
                self._set_cors_headers(413)
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": "Payload demasiado grande (max 64KB)"}).encode("utf-8"))
                return

            raw_bytes = self.rfile.read(length)
            data = json.loads(raw_bytes.decode("utf-8"))
        except json.JSONDecodeError:
            self._set_cors_headers(400)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "code": "INVALID_JSON", "message": "Sintaxis JSON inválida"}).encode("utf-8"))
            return
        except Exception as e:
            self._set_cors_headers(400)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
            return

        status_code, response_data = process_intake(data)
        self._set_cors_headers(status_code)
        self.end_headers()
        self.wfile.write(json.dumps(response_data, indent=2).encode("utf-8"))

    def log_message(self, format, *args):
        """Silencia logs verbosos por defecto en terminal."""
        logger.info(f"{self.address_string()} - {format % args}")


def run_server(host: str = HOST, port: int = PORT):
    """Inicia el servidor HTTP del webhook."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, IntakeHTTPRequestHandler)
    logger.info(f"Servidor Intake K4li Forge levantado en http://{host}:{port}")
    logger.info(f"Telegram Configurado: {bool(TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID)}")
    logger.info("Presiona CTRL+C para detener.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Apagando servidor...")
    finally:
        httpd.server_close()
        logger.info("Servidor detenido.")


def main():
    parser = argparse.ArgumentParser(description="K4li Forge Intake Webhook Daemon & CLI")
    parser.add_argument("--server", action="store_true", help="Ejecuta en modo demonio HTTP")
    parser.add_argument("--host", default=HOST, help=f"Host de escucha (defecto: {HOST})")
    parser.add_argument("--port", type=int, default=PORT, help=f"Puerto de escucha (defecto: {PORT})")
    parser.add_argument("--payload", type=str, help="Ejecución one-shot pasando cadena JSON")
    parser.add_argument("--stdin", action="store_true", help="Lee payload JSON desde entrada estándar")

    args = parser.parse_args()

    if args.server:
        run_server(args.host, args.port)
        return

    if args.stdin or args.payload:
        raw_text = sys.stdin.read() if args.stdin else args.payload
        try:
            data = json.loads(raw_text)
            code, res = process_intake(data)
            print(json.dumps(res, indent=2))
            sys.exit(0 if code == 200 else 1)
        except Exception as e:
            print(json.dumps({"status": "error", "message": str(e)}, indent=2))
            sys.exit(1)

    # Por defecto si no se indican flags, levantar en modo servidor
    run_server(args.host, args.port)


if __name__ == "__main__":
    main()
