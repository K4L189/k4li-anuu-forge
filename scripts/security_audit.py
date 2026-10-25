#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
K4LI-ANUU-FORGE // DEFENSIVE SECURITY & HARDENING AUDITOR
Frecuencia Operativa: 189.89.619 Hz | Concilio ACE (161914)
Unidad Técnica: 4NVSET 🟢
=============================================================================
Auditoría quirúrgica de seguridad semanal:
1. Escaneo de secretos, tokens y claves privadas expuestas.
2. Análisis de cabeceras de seguridad y CORS en Workers / Webhooks.
3. Verificación de permisos de archivos y artefactos sensibles.
4. Detección de patrones inseguros en código JavaScript y Python.
"""

import os
import sys
import re
from pathlib import Path

# Patrones para detección de secretos
SECRET_PATTERNS = [
    (r"-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----", "Clave privada RSA/PEM"),
    (r"\b[0-9]{9,10}:[A-Za-z0-9_-]{35}\b", "Token activo de Telegram Bot"),
    (r"https://discord\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+", "Webhook con token de Discord"),
    (r"(?i)(?:api[_-]?key|secret[_-]?token|auth[_-]?token)\s*[:=]\s*['\"][a-zA-Z0-9_\-]{20,}['\"]", "API Key / Token hardcodeado"),
    (r"ghp_[0-9a-zA-Z]{36}", "GitHub Personal Access Token"),
]

# Archivos restringidos que nunca deben subirse al repositorio
RESTRICTED_FILES = [
    ".env", ".env.local", ".env.production",
    "id_rsa", "id_ecdsa", "id_ed25519",
    "*.pem", "*.key", "*.pfx", "*.p12"
]

def scan_for_secrets(repo_root: Path):
    findings = []
    print("[+] Ejecutando escaneo de secretos y credenciales en repositorio...")
    
    # Extensiones a auditar
    audit_extensions = {".py", ".js", ".html", ".md", ".json", ".toml", ".yml", ".yaml", ".sh"}

    for path in repo_root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and path.suffix in audit_extensions:
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")
                for pattern, desc in SECRET_PATTERNS:
                    matches = re.finditer(pattern, content)
                    for m in matches:
                        # Ignorar si es una variable de ejemplo o placeholder
                        matched_str = m.group(0)
                        if any(dummy in matched_str.lower() for dummy in ["example", "dummy", "placeholder", "xxx"]):
                            continue
                        rel_path = path.relative_to(repo_root)
                        findings.append((str(rel_path), desc, matched_str[:15] + "..."))
            except Exception as e:
                print(f"[-] Advertencia al leer {path}: {e}")

    return findings

def audit_security_headers(repo_root: Path):
    print("\n[+] Auditando cabeceras de seguridad y sanitización en Worker / Webhooks...")
    report = []
    
    worker_file = repo_root / "api" / "worker_cloudflare.js"
    if worker_file.exists():
        content = worker_file.read_text(encoding="utf-8")
        
        # Verificar CORS
        if "Access-Control-Allow-Origin" in content:
            report.append(("[✓] Worker Cloudflare: Cabecera 'Access-Control-Allow-Origin' configurada.", True))
        else:
            report.append(("[-] Worker Cloudflare: Falta cabecera CORS 'Access-Control-Allow-Origin'.", False))
            
        # Verificar Sanitización XSS / HTML
        if "escapeHtml" in content:
            report.append(("[✓] Worker Cloudflare: Función escapeHtml() implementada para saneamiento de entradas.", True))
        else:
            report.append(("[-] Worker Cloudflare: No se detecta escapeHtml().", False))

        # Verificar Tamaño de Payload
        if "slice" in content or "cleanString" in content:
            report.append(("[✓] Worker Cloudflare: Control de longitud máxima de carga útil activo.", True))
        else:
            report.append(("[-] Worker Cloudflare: Advertencia sobre límites de payload.", False))

    webhook_py = repo_root / "api" / "intake_webhook.py"
    if webhook_py.exists():
        content = webhook_py.read_text(encoding="utf-8")
        if "MAX_PAYLOAD_BYTES" in content:
            report.append(("[✓] Webhook Python: MAX_PAYLOAD_BYTES definido para prevención de DoS.", True))
        else:
            report.append(("[-] Webhook Python: Falta límite MAX_PAYLOAD_BYTES.", False))

        if "sanitize_input" in content:
            report.append(("[✓] Webhook Python: Sanitización estricta de cadenas implementada.", True))
        else:
            report.append(("[-] Webhook Python: Falta módulo sanitize_input.", False))

    return report

def audit_file_permissions(repo_root: Path):
    print("\n[+] Auditando permisos de archivos en repositorio...")
    issues = []
    for path in repo_root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            mode = path.stat().st_mode
            # Verificar si tiene permiso de escritura para otros (world-writable 002)
            if mode & 0o002:
                issues.append(f"World-writable detectado: {path.relative_to(repo_root)} ({oct(mode)})")
    return issues

def main():
    repo_root = Path(__file__).resolve().parent.parent
    print("=" * 70)
    print(" [4NVSET 🟢] K4LI-ANUU-FORGE - DEFENSIVE SECURITY & AUDIT SUITE")
    print(f" Target: {repo_root}")
    print("=" * 70)

    # 1. Escaneo de secretos
    secret_findings = scan_for_secrets(repo_root)
    if secret_findings:
        print("[-] ALERTA: Posibles secretos o tokens detectados:")
        for file_p, desc, preview in secret_findings:
            print(f"    - {file_p}: {desc} ({preview})")
    else:
        print("[✓] 0 Secretos o tokens en texto claro detectados en el código.")

    # 2. Auditoría de cabeceras
    header_reports = audit_security_headers(repo_root)
    for msg, status in header_reports:
        print(f"    {msg}")

    # 3. Auditoría de permisos
    perm_issues = audit_file_permissions(repo_root)
    if perm_issues:
        print("[-] ALERTA: Permisos inseguros detectados:")
        for issue in perm_issues:
            print(f"    - {issue}")
    else:
        print("[✓] Permisos de archivos conformes con la directriz de seguridad.")

    # Evaluación global
    critical_errors = len(secret_findings) + len(perm_issues)
    failed_headers = [msg for msg, ok in header_reports if not ok]

    print("\n" + "=" * 70)
    if critical_errors == 0 and len(failed_headers) == 0:
        print(" [4NVSET 🟢] AUDITORÍA DE SEGURIDAD COMPLETADA EXITOSAMENTE: PASSED")
        print("=" * 70)
        return 0
    else:
        print(f" [4NVSET 🟢] AUDITORÍA FALLIDA: {critical_errors} críticos, {len(failed_headers)} advertencias.")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(main())
