/**
 * =============================================================================
 * K4LI-ANUU-FORGE // CLOUDFLARE WORKER INTAKE (SERVERLESS EDGE)
 * Frecuencia Operativa: 189.89.619 Hz | Concilio ACE (161914)
 * Coste: 0 € / mes (Cloudflare Workers Free Tier - 100k req/día)
 * Unidad Técnica: 4NVSET 🟢
 * =============================================================================
 * Recibe peticiones POST desde la web de K4li Forge, valida los datos técnicos,
 * extrae metadatos de red (IP, País, Colo) y reenvía la alerta instantánea
 * al chat de Kali vía Telegram Bot API.
 */

const SERVICE_MAP = {
  security: "🛡️ Auditoría / Hardening / SIEM Wazuh",
  dashboard: "📊 Dashboard React / Web App",
  ai: "🧠 IA Local Soberana (On-Prem LLM)",
  automation: "⚙️ Automatización / Bots / Scrapers"
};

const URGENCY_MAP = {
  normal: "⏱️ Estándar (1-2 semanas)",
  express: "🚨 Urgente / Express (3-5 días) [+25%]",
  retainer: "🔄 Mantenimiento Mensual Recurrente"
};

/**
 * Escapa caracteres HTML para Telegram API
 */
function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

/**
 * Limpieza básica de cadenas
 */
function cleanString(val, maxLen = 2000) {
  if (!val) return "";
  return String(val)
    .replace(/[\x00-\x08\x0b\x0c\x0e-\x1f]/g, "")
    .trim()
    .slice(0, maxLen);
}

/**
 * Genera cabeceras CORS
 */
function getCorsHeaders(env) {
  const origin = env.CORS_ORIGIN || "*";
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Requested-With",
    "Access-Control-Max-Age": "86400"
  };
}

/**
 * Respuesta JSON estandarizada con cabeceras CORS
 */
function jsonResponse(data, status = 200, env = {}) {
  const cors = getCorsHeaders(env);
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      ...cors
    }
  });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // 1. Manejo de Preflight CORS (OPTIONS)
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: getCorsHeaders(env)
      });
    }

    // 2. Health check / Estado del Worker
    if (request.method === "GET") {
      if (url.pathname === "/" || url.pathname === "/health" || url.pathname === "/api/intake") {
        return jsonResponse({
          status: "online",
          service: "k4li-anuu-forge-worker",
          version: "1.0.0",
          runtime: "cloudflare-workers",
          colo: request.cf?.colo || "local",
          country: request.cf?.country || "unknown",
          telegram_ready: Boolean(env.TELEGRAM_BOT_TOKEN && env.TELEGRAM_CHAT_ID)
        }, 200, env);
      }
      return jsonResponse({ status: "error", message: "Not Found" }, 404, env);
    }

    // 3. Solo permitir POST en endpoints de intake
    if (request.method !== "POST") {
      return jsonResponse({ status: "error", message: `Método ${request.method} no permitido.` }, 405, env);
    }

    if (url.pathname !== "/" && url.pathname !== "/api/intake" && url.pathname !== "/intake") {
      return jsonResponse({ status: "error", message: "Ruta no encontrada" }, 404, env);
    }

    // 4. Parseo y Validación de Payload JSON
    let body;
    try {
      body = await request.json();
    } catch (e) {
      return jsonResponse({
        status: "error",
        code: "INVALID_JSON",
        message: "Cuerpo de petición no es un JSON válido."
      }, 400, env);
    }

    if (!body || typeof body !== "object") {
      return jsonResponse({
        status: "error",
        code: "INVALID_BODY",
        message: "El cuerpo debe ser un objeto JSON."
      }, 400, env);
    }

    const rawService = cleanString(body.service || "security", 50).toLowerCase();
    const rawUrgency = cleanString(body.urgency || "normal", 50).toLowerCase();
    const brief = cleanString(body.brief || "", 3000);
    const contact = cleanString(body.contact || "", 250);
    const name = cleanString(body.name || body.clientName || "Cliente Anónimo", 150);
    const budget = cleanString(body.presupuesto || body.budget || body.priceDisplay || "A determinar", 100);

    // Validaciones de obligatoriedad
    if (!brief || brief.length < 5) {
      return jsonResponse({
        status: "error",
        code: "VALIDATION_FAILED",
        message: "El campo 'brief' es obligatorio (mínimo 5 caracteres)."
      }, 400, env);
    }

    if (!contact || contact.length < 3) {
      return jsonResponse({
        status: "error",
        code: "VALIDATION_FAILED",
        message: "El campo 'contact' (Signal/Email/Telegram) es obligatorio."
      }, 400, env);
    }

    const serviceLabel = SERVICE_MAP[rawService] || `🛠️ ${rawService}`;
    const urgencyLabel = URGENCY_MAP[rawUrgency] || `⏱️ ${rawUrgency}`;
    const nowIso = new Date().toISOString();

    // Metadatos de red proporcionados por Cloudflare Edge
    const clientIp = request.headers.get("cf-connecting-ip") || request.headers.get("x-real-ip") || "Desconocida";
    const country = request.cf?.country || request.headers.get("cf-ipcountry") || "XX";
    const colo = request.cf?.colo || "UNK";
    const rayId = request.headers.get("cf-ray") || "N/A";

    // 5. Formateo de Mensaje para Telegram Bot API
    const telegramMessage = [
      "⚡ <b>NUEVO ENCARGO TÉCNICO // K4LI FORGE</b> ⚡",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
      `👤 <b>Cliente:</b> ${escapeHtml(name)}`,
      `📡 <b>Contacto:</b> <code>${escapeHtml(contact)}</code>`,
      `🛠️ <b>Servicio:</b> ${escapeHtml(serviceLabel)}`,
      `⏱️ <b>Urgencia:</b> ${escapeHtml(urgencyLabel)}`,
      `💰 <b>Presupuesto:</b> ${escapeHtml(budget)}`,
      `🌍 <b>Origen:</b> <code>${escapeHtml(clientIp)}</code> (${escapeHtml(country)} · ${escapeHtml(colo)})`,
      `📅 <b>Fecha:</b> ${escapeHtml(nowIso)}`,
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
      "📝 <b>Requerimiento Técnico:</b>",
      `<blockquote>${escapeHtml(brief)}</blockquote>`,
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
      `🔒 <i>Cloudflare Edge Worker · Ray: ${escapeHtml(rayId)}</i>`
    ].join("\n");

    let dispatchResult = { telegram: "not_configured", webhook: "not_configured" };

    // 6. Despacho a Telegram Bot API
    if (env.TELEGRAM_BOT_TOKEN && env.TELEGRAM_CHAT_ID) {
      try {
        const tgUrl = `https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`;
        const tgResp = await fetch(tgUrl, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            chat_id: env.TELEGRAM_CHAT_ID,
            text: telegramMessage,
            parse_mode: "HTML",
            disable_web_page_preview: true
          })
        });

        const tgData = await tgResp.json();
        dispatchResult.telegram = tgData.ok ? "delivered" : `error: ${tgData.description || tgResp.status}`;
      } catch (err) {
        dispatchResult.telegram = `exception: ${err.message}`;
      }
    } else {
      dispatchResult.telegram = "mock_mode_no_credentials";
    }

    // 7. Despacho a Webhook secundario opcional (Discord / Slack)
    if (env.WEBHOOK_URL) {
      const isDiscord = env.WEBHOOK_URL.includes("discord.com") || env.WEBHOOK_URL.includes("discordapp.com");
      const webhookPayload = isDiscord
        ? {
            content: "⚡ **NUEVO INTAKE TÉCNICO // K4LI FORGE** ⚡",
            embeds: [{
              title: `Proyecto: ${serviceLabel}`,
              color: 65280,
              fields: [
                { name: "Cliente", value: name, inline: true },
                { name: "Contacto", value: contact, inline: true },
                { name: "Urgencia", value: urgencyLabel, inline: true },
                { name: "Presupuesto", value: budget, inline: true },
                { name: "Origen", value: `${country} (${clientIp})`, inline: true },
                { name: "Brief", value: brief.slice(0, 1024), inline: false }
              ],
              footer: { text: `Cloudflare Ray: ${rayId}` }
            }]
          }
        : {
            text: `Nuevo intake de ${name} (${contact}): ${serviceLabel}`,
            data: { name, contact, service: rawService, urgency: rawUrgency, budget, brief, clientIp, country, timestamp: nowIso }
          };

      try {
        const whPromise = fetch(env.WEBHOOK_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(webhookPayload)
        });
        if (ctx && ctx.waitUntil) {
          ctx.waitUntil(whPromise);
          dispatchResult.webhook = "queued";
        } else {
          await whPromise;
          dispatchResult.webhook = "delivered";
        }
      } catch (err) {
        dispatchResult.webhook = `exception: ${err.message}`;
      }
    }

    // 8. Retorno HTTP 200 con confirmación JSON
    return jsonResponse({
      status: "success",
      message: "Petición técnica registrada y procesada por Cloudflare Edge.",
      service: rawService,
      urgency: rawUrgency,
      timestamp: nowIso,
      dispatch: dispatchResult,
      edge: {
        datacenter: colo,
        country: country
      }
    }, 200, env);
  }
};
