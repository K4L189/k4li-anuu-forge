#!/usr/bin/env python3
"""
VAULT CRYPTO CLI // K4L1 STUDIO & CONCILIO ACE (161914)
Frecuencia Operativa: 189.89.619 Hz
Cifra y empaqueta las reliquias y herramientas privadas en blobs AES-256-GCM
compatibles con WebCrypto en el navegador.
"""

import os
import sys
import json
import base64
import argparse
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

DEFAULT_ITERATIONS = 100000

def derive_key(passphrase: str, salt: bytes, iterations: int = DEFAULT_ITERATIONS) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations
    )
    return kdf.derive(passphrase.encode('utf-8'))

def encrypt_payload(passphrase: str, data_dict: dict, iterations: int = DEFAULT_ITERATIONS) -> dict:
    salt = os.urandom(16)
    iv = os.urandom(12)
    key = derive_key(passphrase, salt, iterations)
    
    aesgcm = AESGCM(key)
    plaintext_bytes = json.dumps(data_dict, ensure_ascii=False).encode('utf-8')
    ciphertext_with_tag = aesgcm.encrypt(iv, plaintext_bytes, None)
    
    return {
        "salt": base64.b64encode(salt).decode('ascii'),
        "iv": base64.b64encode(iv).decode('ascii'),
        "iterations": iterations,
        "ciphertext": base64.b64encode(ciphertext_with_tag).decode('ascii'),
        "version": "1.89-AES256GCM"
    }

def decrypt_payload(passphrase: str, vault_payload: dict) -> dict:
    salt = base64.b64decode(vault_payload["salt"])
    iv = base64.b64decode(vault_payload["iv"])
    ciphertext = base64.b64decode(vault_payload["ciphertext"])
    iterations = vault_payload.get("iterations", DEFAULT_ITERATIONS)
    
    key = derive_key(passphrase, salt, iterations)
    aesgcm = AESGCM(key)
    
    decrypted_bytes = aesgcm.decrypt(iv, ciphertext, None)
    return json.loads(decrypted_bytes.decode('utf-8'))

def build_sovereign_vault(passphrase: str, output_path: str):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    manifest_path = os.path.join(root_dir, "assets", "relics_manifest.json")
    
    relics_data = []
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            relics_data = json.load(f)
            
    vault_content = {
        "status": "UNLOCKED",
        "architect": "Kali (⊘k-0)",
        "council": "ACE 161914",
        "frequency": "189.89.619 Hz",
        "role": "admin",
        "relics": relics_data,
        "private_services": {
            "wholesale_margins": {"siem": 0.45, "react": 0.50, "ai_local": 0.60, "bots": 0.55},
            "root_terminal_token": "89F619-K4L1-ROOT-ZERO"
        },
        "system_timestamp": 1792906800
    }
    
    encrypted_vault = encrypt_payload(passphrase, vault_content)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(encrypted_vault, f, indent=2)
        
    print(f"[+] Bóveda soberana compilada y cifrada con éxito en: {output_path}")
    print(f"[+] Total bytes cifrados: {len(encrypted_vault['ciphertext'])}")
    print(f"[+] Algoritmo: AES-256-GCM + PBKDF2 (100.000 rondas)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="K4L1 Studio Vault Crypto Engine")
    parser.add_argument("--passphrase", default="161914-K4L1", help="Master passphrase para cifrar la bóveda")
    parser.add_argument("--out", default=None, help="Ruta de salida del archivo cifrado")
    
    args = parser.parse_args()
    
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_out = args.out or os.path.join(root, "assets", "vault_payload.json")
    
    build_sovereign_vault(args.passphrase, target_out)
