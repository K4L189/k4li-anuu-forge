# 📊 MÓDULO INTERACTIVO DE ROI & CALCULADORA DE AHORRO // K4L1 STUDIO
**Autoría & Arquitectura:** Kali (`K4L1 STUDIO`) & Concilio ACE (161914)  
**Componente:** [`components/roi_calculator.html`](file:///home/kali/k4li-anuu-forge/components/roi_calculator.html)  
**Frecuencia:** `189.89.619 Hz`  

---

## 1. Visión & Propósito Ejecutivo

El módulo de ROI de K4L1 STUDIO transforma el diálogo comercial con clientes corporativos y PyMEs: sustituye discursos comerciales abstractos por **números fríos, matemáticos e irrefutables**. Demuestra cómo contratar a Kali genera un retorno positivo e inmediato (a menudo amortizado en menos de 60 días o días hábiles).

---

## 2. Los 3 Escenarios Canónicos Demostrados

### 🤖 Ejemplo A: IA Local Soberana vs OpenAI Cloud APIs
* **Contexto:** Equipos de marketing, legal o desarrollo pagando facturas recurrentes de tokens en OpenAI / Anthropic.
* **Métrica Base:** Gasto promedio de **400 €/mes** (4.800 €/año).
* **Solución Kali:** Despliegue de modelo privado local (Llama-3, Mistral 7B/14B con GGUF / Ollama) en servidores existentes o hardware dedicado (~850 € setup único).
* **Retorno Financiero:**
  $$\text{Amortización} = \frac{850 €}{400 €/\text{mes}} = 2.125 \text{ meses}$$
  $$\text{Ahorro Neto Año 1} = (400 € \times 12) - 850 € = 3.950 €$$
  $$\text{Ahorro Años 2+} = 4.800 €/\text{año limpio (100\%)}$$
* **Factor Blindaje Legal:** Neutralización completa del riesgo de multas del RGPD (hasta 20M€ o 4% de la facturación global anual) al no transferir datos sensibles ni PII de clientes a nubes de terceros en EE.UU.

---

### 🛡️ Ejemplo B: Hardening & SIEM Preventivo vs Ransomware
* **Contexto:** PyMEs y empresas sin monitorización forense ni hardening en sus servidores Linux.
* **Métrica Base:** Coste medio oficial de un ataque con secuestro de datos / ransomware según INCIBE y ENISA: **50.000 € a 150.000 €** (rescate, paralización operativa de 14-21 días, peritaje forense externo y pérdida reputacional).
* **Solución Kali:** Auditoría profunda de vulnerabilidades, hardening de kernel/SSH/Iptables y despliegue del agente Wazuh SIEM con correlación MITRE ATT&CK (**450 €** tarifa base).
* **Retorno de Seguridad (ROSI):**
  $$\text{ROSI} = \frac{50.000 € - 450 €}{450 €} \times 100 \approx 11.011\% \text{ (111x por euro invertido)}$$
* **Garantía Operativa:** Evita 2 a 3 semanas de inactividad de servidores críticos y asegura el cumplimiento del ENS (Esquema Nacional de Seguridad) y NIS2.

---

### ⚙️ Ejemplo C: Automatización Python & Eliminación de Tareas Manuales
* **Contexto:** Empleados perdiendo horas semanales copiando datos, scraping manual, conciliando inventarios o descargando informes.
* **Métrica Base:** **20 horas semanales** a un coste de empresa de **15 €/hora** = **1.300 €/mes** (15.600 €/año en horas improductivas).
* **Solución Kali:** Script o bot Python con ejecución programada por cron/systemd (**350 €** entrega única documentada).
* **Retorno Operativo:**
  $$\text{Break-Even} = \frac{350 €}{1.300 € / 21 \text{ días}} \approx 5.6 \text{ días laborables}$$
  $$\text{Ahorro Neto Año 1} = 15.600 € - 350 € = 15.250 €$$
  $$\text{Tiempo Recuperado} = 1.040 \text{ horas/año} \text{ para negocio de alto valor}$$

---

## 3. Características de Interfaz & Visualización

1. **Sliders Fluidos y Reactivos:**
   - **Volumen de Peticiones / Empleados / Horas:** Adaptable dinámicamente según el escenario.
   - **Gasto Mensual Actual / Impacto Financiero:** Deslizable de 50 € a 150.000 €.
   - **Inversión Kali:** Parametrizable según alcance (de 200 € a 2.500 €).
2. **Gráfico SVG Dinámico de Break-Even (12 Meses):**
   - Traza la curva de coste acumulado sin Kali frente a la línea plana de inversión fija de Kali.
   - Calcula el punto de intersección exacto (`Break-Even Point`) indicando el mes o día de amortización.
3. **Barras de Progreso Comparativas:** Visualización inmediata del porcentaje que representa la solución Kali frente al despilfarro acumulado.
4. **Sincronización con Signal E2EE:**
   - El botón CTA compila automáticamente los números elegidos por el usuario en el texto del enlace de Signal:
   - `https://signal.me/#u/k4li.89?text=Hola%20Kali...`
   - Agiliza la conversión a contrato en menos de 24 horas.

---

## 4. Guía de Integración Web

### Opción 1: IFrame Reactivo (Recomendado)
```html
<iframe 
  id="roiCalculatorFrame"
  src="components/roi_calculator.html" 
  class="w-full border-0 min-h-[750px] rounded-2xl bg-transparent"
  loading="lazy"
  title="Calculadora ROI K4L1 STUDIO">
</iframe>
```

### Sincronización de Temas vía `postMessage`
El componente responde a mensajes de cambio de tema:
```javascript
const roiFrame = document.getElementById("roiCalculatorFrame");
roiFrame.contentWindow.postMessage({ type: 'SET_THEME', theme: 'anuu' }, '*');
// Temas soportados: anuu, blood, gw2, bioinfo, duat, neon
```

---
*Diseñado bajo la frecuencia del Concilio ACE por Kilonova 🌟 & Saze 🌿 para Kali.*
