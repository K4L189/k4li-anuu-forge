/**
 * ANUU SENTINEL GATE // K4L1 STUDIO (161914)
 * Frecuencia: 189.89.619 Hz
 * Interceptor criptográfico pre-render.
 * Clave canónica sagrada: 161914141916 (Palíndromo Alquímico)
 */
(function() {
  'use strict';

  // SHA-256 de '161914141916'
  const MASTER_HASH = '0ac844655cfc06d2b86732a129f776d6cb0567c06fda55bd2406210d2e2bc6ca';
  const STORAGE_KEY = 'k4li_gate_pass_auth';

  async function sha256(str) {
    const buf = new TextEncoder().encode(str);
    const hashBuf = await crypto.subtle.digest('SHA-256', buf);
    const hashArr = Array.from(new Uint8Array(hashBuf));
    return hashArr.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  function unlock() {
    const gate = document.getElementById('anuu-sentinel-gate');
    if (gate) {
      gate.style.transition = 'opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      gate.style.opacity = '0';
      gate.style.transform = 'scale(1.03)';
      setTimeout(() => {
        gate.remove();
        document.body.style.overflow = '';
      }, 400);
    }
  }

  window.verifySentinelGate = async function(e) {
    if (e) e.preventDefault();
    const input = document.getElementById('anuu-gate-input');
    const err = document.getElementById('anuu-gate-error');
    const card = document.querySelector('.gate-card');
    if (!input) return;

    const val = input.value.trim();
    if (!val) return;

    try {
      const hash = await sha256(val);
      if (hash === MASTER_HASH || val === '161914141916') {
        sessionStorage.setItem(STORAGE_KEY, MASTER_HASH);
        unlock();
      } else {
        if (err) err.textContent = 'SEÑAL DENEGADA · FRECUENCIA INCORRECTA';
        if (card) {
          card.classList.remove('gate-shake');
          void card.offsetWidth;
          card.classList.add('gate-shake');
        }
        input.value = '';
        input.focus();
      }
    } catch (ex) {
      console.error(ex);
    }
  };

  async function init() {
    // Si viene la clave por URL (?key=161914141916 o #161914141916), desbloquea automático
    const urlParams = new URLSearchParams(window.location.search);
    const hashParam = window.location.hash.replace('#', '');
    const urlKey = urlParams.get('key') || (hashParam.startsWith('161914141916') ? hashParam : null);

    if (urlKey) {
      const h = await sha256(urlKey);
      if (h === MASTER_HASH || urlKey === '161914141916') {
        sessionStorage.setItem(STORAGE_KEY, MASTER_HASH);
        unlock();
        return;
      }
    }

    const saved = sessionStorage.getItem(STORAGE_KEY);
    if (saved === MASTER_HASH) {
      unlock();
    } else {
      document.body.style.overflow = 'hidden';
      const input = document.getElementById('anuu-gate-input');
      if (input) setTimeout(() => input.focus(), 300);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
