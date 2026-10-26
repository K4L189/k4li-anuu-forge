/* forge_cards.js — brillo reactivo (--mx/--my) + hidratación de iconos SVG en .forge-card (Saze 🏛️ / Anuu 🌫️). Vanilla, sin dependencias. */
(function () {
  "use strict";

  /* ---- Iconos: sprite.svg -> <svg><use/></svg>; si falla la carga, queda el emoji original ---- */
  function hydrateIcons() {
    var slots = document.querySelectorAll(".card-icon[data-icon]");
    if (!slots.length || !window.fetch) return;
    fetch("assets/icons/sprite.svg", { cache: "force-cache" })
      .then(function (r) { if (!r.ok) throw 0; return r.text(); })
      .then(function (txt) {
        var holder = document.createElement("div");
        holder.setAttribute("aria-hidden", "true");
        /* No usar display:none: algunos navegadores no resuelven los <filter> del sprite si está oculto. */
        holder.style.cssText = "position:absolute;width:0;height:0;overflow:hidden";
        holder.innerHTML = txt;
        document.body.insertBefore(holder, document.body.firstChild);
        slots.forEach(function (el) {
          var id = "icon-" + el.getAttribute("data-icon");
          if (!holder.querySelector("#" + id)) return; /* sin símbolo -> conserva emoji */
          el.innerHTML = '<svg viewBox="0 0 64 64" role="img" aria-hidden="true"><use href="#' + id + '"></use></svg>';
          el.classList.add("has-svg");
        });
      })
      .catch(function () { /* file:// u offline sin caché: el emoji sigue funcionando */ });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", hydrateIcons);
  else hydrateIcons();

  /* ---- Brillo que sigue al cursor (inerte en táctil) ---- */
  if (window.matchMedia && window.matchMedia("(hover: none), (pointer: coarse)").matches) return;
  var raf = 0, card = null, x = 0, y = 0;
  function paint() {
    raf = 0;
    var r = card.getBoundingClientRect();
    card.style.setProperty("--mx", (x - r.left).toFixed(1) + "px");
    card.style.setProperty("--my", (y - r.top).toFixed(1) + "px");
  }
  document.addEventListener("pointermove", function (e) {
    if (e.pointerType === "touch") return;
    var t = e.target && e.target.closest ? e.target.closest(".forge-card") : null;
    if (!t) return;
    card = t; x = e.clientX; y = e.clientY;
    if (!raf) raf = requestAnimationFrame(paint);
  }, { passive: true });
})();
