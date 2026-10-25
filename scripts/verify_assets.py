#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
K4LI-ANUU-FORGE // ASSET & HYPERLINK INTEGRITY AUDITOR
Frecuencia Operativa: 189.89.619 Hz | Concilio ACE (161914)
Unidad Técnica: 4NVSET 🟢
=============================================================================
Verifica la integridad de referencias locales (src/href), archivos estáticos
vitales y estructura para el despliegue en GitHub Pages.
"""

import os
import sys
import re
from pathlib import Path

def run_integrity_check(repo_root: Path):
    print("=" * 70)
    print(" [4NVSET 🟢] K4LI-ANUU-FORGE - ASSET & HYPERLINK INTEGRITY AUDIT")
    print(f" Root Directory: {repo_root}")
    print("=" * 70)

    # 1. Verificar archivos esenciales del despliegue
    critical_files = [
        repo_root / "index.html",
        repo_root / ".nojekyll",
        repo_root / "components" / "roi_calculator.html",
        repo_root / "docs" / "ROI_CALCULATOR_GUIDE.md"
    ]

    missing_critical = []
    for cf in critical_files:
        if not cf.exists():
            missing_critical.append(str(cf.relative_to(repo_root)))
            print(f"[-] CRITICAL MISSING: {cf.relative_to(repo_root)}")
        else:
            print(f"[+] FOUND: {cf.relative_to(repo_root)} ({cf.stat().st_size} bytes)")

    if missing_critical:
        print(f"\n[FAIL] Archivos esenciales faltantes: {missing_critical}")
        return False, len(missing_critical), 0

    # 2. Escanear enlaces y recursos locales en páginas principales
    core_html_files = [repo_root / "index.html"] + list((repo_root / "components").glob("*.html"))
    
    broken_links = []
    checked_count = 0

    ignored_prefixes = (
        "http://", "https://", "mailto:", "tel:", "javascript:", "data:", "#", "file://", "blob:"
    )

    print("\n[+] Auditando referencias locales en componentes de producción:")
    for doc in core_html_files:
        content = doc.read_text(encoding="utf-8", errors="ignore")
        matches = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', content)
        doc_rel = doc.relative_to(repo_root)

        for ref in matches:
            ref_clean = ref.strip()
            if not ref_clean or ref_clean.startswith(ignored_prefixes) or "${" in ref_clean:
                continue

            checked_count += 1
            # Normalizar URL relativa eliminando queries y anclas
            target_path = ref_clean.split("?")[0].split("#")[0]
            if not target_path:
                continue

            # Buscar respecto al directorio del archivo o a la raíz
            cand_local = (doc.parent / target_path).resolve()
            cand_root = (repo_root / target_path).resolve()

            if not (cand_local.exists() or cand_root.exists()):
                broken_links.append((str(doc_rel), ref_clean))
                print(f"[-] ERROR: {doc_rel} -> referencia rota '{ref_clean}'")
            else:
                print(f"[✓] VALID: {doc_rel} -> '{ref_clean}'")

    print("\n" + "-" * 70)
    print(f"Total referencias locales auditadas: {checked_count}")
    print(f"Total enlaces rotos detectados: {len(broken_links)}")
    print("-" * 70)

    if broken_links:
        print("[FAIL] Se detectaron hipervínculos o recursos locales inexistentes.")
        return False, len(missing_critical), len(broken_links)

    print("[SUCCESS] Integridad de activos y estructura 100% verificada.")
    return True, 0, 0

if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent.parent
    success, missing_crit, broken = run_integrity_check(current_dir)
    sys.exit(0 if success else 1)
