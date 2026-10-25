# PROPUESTA TÉCNICA COMERCIAL Y DECLARACIÓN DE TRABAJO (STATEMENT OF WORK - SOW)

**CÓDIGO DE PROPUESTA:** `K4L1-SOW-[AÑO]-[NÚMERO]`  
**VERSIÓN:** 1.0 — DEFINITIVA  
**ESTADO:** PENDIENTE DE ACEPTACIÓN / EN EJECUCIÓN  
**ESTUDIO:** K4L1 STUDIO (Arquitectura Crítica & Sistemas Soberanos)  
**FRECUENCIA TÉCNICA:** `189.89.619 Hz` — ESCUDO KANUV 🛡️

---

## 1. IDENTIFICACIÓN Y DATOS GENERALES

| DATOS DEL PROVEEDOR | DATOS DEL CLIENTE |
| :--- | :--- |
| **Proveedor:** K4L1 STUDIO | **Cliente / Razón Social:** `[NOMBRE / EMPRESA DEL CLIENTE]` |
| **Responsable Técnica:** Kali (Arquitecta Directora) | **Representante Técnico / PM:** `[NOMBRE Y APELLIDOS]` |
| **Contacto Criptográfico:** Signal `@k4li.89` | **Contacto E2EE / Email:** `[EMAIL / SIGNAL DEL CLIENTE]` |
| **Jurisdicción:** España / Unión Europea | **Identificación Fiscal / CIF:** `[NIF / CIF / VAT ID]` |
| **Fecha de Emisión:** `[DD/MM/AAAA]` | **Fecha Límite de Validez:** `[DD/MM/AAAA]` *(15 días naturales)* |

---

## 2. RESUMEN EJECUTIVO Y OBJETIVO DEL PROYECTO

### 2.1. Diagnóstico Inicial
`[Describir de forma concisa la problemática o necesidad del cliente: ej. Infraestructura expuesta a ataques de fuerza bruta y dumping de credenciales; carencia de visibilidad en tiempo real de flujos de liquidez; dependencia de APIs de terceros (OpenAI) con riesgo de fuga de datos clínicos o financieros; procesos manuales repetitivos con alto coste operativo].`

### 2.2. Objetivo Operativo
K4L1 STUDIO diseñará, implementará y auditará una solución tecnológica de grado militar consistente en:  
`[Definir el objetivo central: ej. Despliegue de stack SIEM Wazuh con hardening integral de kernel Linux / Desarrollo de Dashboard React reactivo de baja latencia / Servidor de IA local On-Premise con Ollama y RAG privado / Automatización distribuida en Python]`.

---

## 3. ALCANCE DETALLADO DEL TRABAJO (SCOPE OF WORK)

### 3.1. Módulos Técnicos a Ejecutar

#### Módulo 1: Auditoría Preliminar, Análisis de Arquitectura & Línea Base
- Levantamiento de requisitos de hardware, conectividad y seguridad perimetral.
- Mapeo de superficie de ataque y validación de puertos/servicios expuestos.
- Establecimiento de canales E2EE de trabajo y firmas de llaves SSH/PGP.

#### Módulo 2: Ingeniería de Implementación / Desarrollo
- `[Especificar tareas técnicas detalladas según el servicio contratado]`.
- Configuración de entornos aislados mediante contenedores Docker/Podman o servicios nativos `systemd`.
- Implementación de reglas de negocio, componentes de interfaz de usuario reactiva o modelos de lenguaje cuantizados.

#### Módulo 3: Fortificación, Pruebas de Carga & Verificación Forense
- Validación estricta de mitigación de vulnerabilidades o pruebas unitarias de software.
- Pruebas de estrés y benchmarking de consumo de RAM/VRAM/CPU.
- Auditoría de logs y verificación del sellado del sistema conforme al Escudo Kanuv.

#### Módulo 4: Entrega, Documentación de Operaciones & Handover
- Traspaso de credenciales administrativas por canal seguro Signal/PGP.
- Entrega de manual técnico de mantenimiento y arquitectura.
- Sesión de transferencia de conocimiento técnico (Handover) de 1 hora vía canal privado.

### 3.2. Exclusiones Expresas (Límites del Alcance / Scope Boundaries)
Para evitar desviaciones de tiempo y costes no planificados (*scope creep*), **NO se consideran incluidos** en el presente SOW:
- Mantenimiento o resolución de problemas en infraestructuras ajenas al servidor/sistema objeto del contrato.
- Costes de licencias de terceros, alquiler de servidores (VPS/Bare-Metal), dominios o costes de APIs externas.
- Modificaciones estructurales de la lógica de negocio solicitadas con posterioridad a la aprobación de este documento.
- Migración de bases de datos masivas no contempladas expresamente en la propuesta inicial.

### 3.3. Requisitos y Dependencias que Debe Facilitar el Cliente
Para dar cumplimiento a los plazos pactados, el CLIENTE se compromete a suministrar en un plazo máximo de **48 horas** tras la firma:
1. Acceso temporal mediante llave pública SSH proporcionada por K4L1 STUDIO con privilegios de `sudo`.
2. Servidor con sistema operativo base limpio (Debian 12 / Ubuntu 22.04-24.04 LTS / Arch Linux) o credenciales de la nube elegida.
3. Claves de API, credenciales de prueba o documentación técnica de los sistemas externos a integrar.

---

## 4. CRONOGRAMA DE ENTREGABLES Y CRITERIOS DE ACEPTACIÓN

### 4.1. Cronograma de Hitos

| Hito | Denominación del Entregable | Plazo Estimado | Estado |
| :---: | :--- | :---: | :---: |
| **H1** | Plan de Arquitectura, Accesos Validados & Entorno de Staging | Día T + 3 | Pendiente |
| **H2** | Implementación Núcleo / Despliegue de Código & Servicios | Día T + 8 | Pendiente |
| **H3** | Pruebas Integrales, Hardening & Benchmarking Forense | Día T + 11 | Pendiente |
| **H4** | **Entrega Final:** Despliegue en Producción, Manual & Handover | Día T + 14 | Pendiente |

*(Donde **T** es la fecha de recepción efectiva del Pago Inicial del 50% y los accesos requeridos).*

### 4.2. Criterios de Aceptación Objetivos (Definición de "Done")
Se considerará que un entregable ha sido completado satisfactoriamente y está listo para su aprobación cuando cumpla con los siguientes estándares verificables:
1. **Funcionalidad:** El sistema ejecuta el 100% de las especificaciones descritas en el Módulo de Trabajo correspondiente.
2. **Estabilidad:** Ausencia de fallos críticos (*crashes*), fugas de memoria o errores 5xx bajo condiciones operativas normales.
3. **Seguridad:** Cero vulnerabilidades críticas o altas detectadas en el análisis forense de cierre.
4. **Validación:** El CLIENTE dispondrá de un período de **cinco (5) días hábiles** tras la entrega formal para validar las pruebas. Transcurrido dicho plazo sin observaciones formales fundamentadas por escrito, o si el sistema es puesto en explotación comercial/producción por el CLIENTE, el entregable se considerará aceptado a todos los efectos legales y técnicos (*Aceptación Tácita*).

---

## 5. CONDICIONES ECONÓMICAS E HITOS DE PAGO

### 5.1. Cuantía del Proyecto

| Concepto / Servicio | Importe Base |
| :--- | :---: |
| `[Servicio Contratado: ej. Fortificación Integral Linux + SIEM Wazuh]` | `[X.XXX,00] €` |
| `[Opcional: Módulo Complementario / Add-on]` | `[XXX,00] €` |
| **TOTAL BASE IMPONIBLE:** | **`[X.XXX,00] €`** |
| Impuestos aplicables (según legislación fiscal y residencia): | `[Exento / 21% IVA]` |
| **TOTAL NETO DEL CONTRATO:** | **`[X.XXX,00] €`** *(o equiv. en Crypto)* |

### 5.2. Estructura de Pagos Innegociable (Regla 50 / 50)

En estricta observancia de los protocolos operativos de K4L1 STUDIO, los fondos se liquidarán conforme al siguiente esquema:

```
[ INICIO DEL PROYECTO ]  ──►  50% PAGO POR ADELANTADO (Hito de Reserva e Ingeniería)
                                   │
                                   ▼ (Ejecución técnica según SOW)
                                   │
[ ENTREGA & CONFORMIDAD ] ──►  50% PAGO FINAL (Handover, Credenciales y Cierre)
```

1. **Hito 1 (50% por Adelantado):**  
   - Importe: **`[50% del TOTAL]` €**  
   - Carácter: Condición suspensiva indispensable. Ninguna labor de análisis técnico, reserva de recursos de cómputo o desarrollo se iniciará hasta la recepción efectiva de este anticipo.
2. **Hito 2 (50% a la Entrega Final):**  
   - Importe: **`[50% restante]` €**  
   - Carácter: Pagadero tras la presentación del sistema funcional y aprobación de los criterios de aceptación del Hito 4, con carácter previo o simultáneo a la transferencia de credenciales de acceso administrativo maestro y repositorio privado definitivo.

### 5.3. Métodos de Pago Habilitados
- **Transferencia Bancaria SEPA / SWIFT:** A la cuenta IBAN designada en la factura proforma.
- **Criptoactivos Soberanos (Paridad fijada a fecha de emisión de factura):**
  - **USDT / USDC:** Red Tron (TRC-20) o Ethereum (ERC-20).
  - **Monero (XMR):** Red nativa (Transacciones confidenciales de máxima privacidad).
  - **Bitcoin (BTC):** Red principal o Lightning Network.

---

## 6. ACUERDO DE NIVEL DE SERVICIO (SLA) Y GARANTÍA POST-ENTREGA

### 6.1. Período de Garantía de Quince (15) Días Naturales
K4L1 STUDIO otorga una garantía de soporte técnico post-entrega de **quince (15) días naturales**, contados a partir de la fecha de entrega definitiva y liquidación final del proyecto.

### 6.2. Alcance de la Garantía Gratuita
- Corrección de anomalías, inconsistencias o bugs no detectados durante la fase de validación, siempre que provengan directamente de defectos en los componentes suministrados por K4L1 STUDIO.
- Ajuste menor de parámetros de rendimiento y calibración de umbrales de alerta.
- Asistencia y resolución de dudas técnicas al equipo del CLIENTE respecto al funcionamiento del sistema.

### 6.3. Tiempos de Respuesta y Resolución durante el SLA

| Nivel de Severidad | Definición Operativa | Tiempo de Respuesta | Tiempo Objetivo de Mitigación |
| :---: | :--- | :---: | :---: |
| **Severidad 1 (Crítica)** | Bloqueo absoluto del sistema entregado, caída de servicio o incidente grave de seguridad. | **< 2 Horas** | **< 6 Horas** |
| **Severidad 2 (Alta)** | Degradación relevante de rendimiento o mal funcionamiento de una característica principal sin caída total. | **< 6 Horas** | **< 24 Horas** |
| **Severidad 3 (Media/Baja)** | Incidencia estética menor, consulta de configuración o bug que permite trabajar sin bloqueo. | **< 24 Horas** | **< 48 Horas** |

### 6.4. Exclusiones del Soporte Gratuito
Quedan expresamente excluidos de la garantía gratuita de 15 días:
- Fallos derivados de modificaciones, manipulaciones o alteraciones del código o configuración realizadas por el CLIENTE o terceros ajenos a K4L1 STUDIO.
- Caídas o fallos causados por proveedores de infraestructura de nube (AWS, Hetzner, DigitalOcean), cortes de red o proveedores de APIs de terceros.
- Solicitudes de nuevas funcionalidades, rediseños o ampliaciones de alcance no estipuladas en este SOW.

*(Finalizado el período de 15 días, el CLIENTE podrá contratar una póliza de Mantenimiento Mensual Recurrente / Retainer para garantizar soporte permanente y auditoría continua).*

---

## 7. PROTOCOLO DE CONTROL DE CAMBIOS (CHANGE ORDER)

Cualquier variación en el alcance, requisitos, plazos o entregables deberá gestionarse formalmente mediante el siguiente protocolo:
1. El CLIENTE o K4L1 STUDIO formulará la solicitud de cambio por escrito.
2. K4L1 STUDIO evaluará en un plazo de 48 horas el impacto en costes adicionales y tiempo de entrega.
3. Se emitirá un anexo formal (*Addendum / Change Order*). No se implementará ningún cambio hasta su aprobación expresa y pago del ajuste económico correspondiente.

---

## 8. CONFIDENCIALIDAD Y BLINDAJE LEGAL

El presente SOW se rige subsidiariamente por los términos del **Acuerdo Mutuo de Confidencialidad (NDA Bilateral)** suscrito entre las Partes. Toda información intercambiada, credenciales y arquitectura mantendrán la clasificación de Secreto Industrial bajo custodia criptográfica E2EE.

---

## 9. FORMALIZACIÓN Y FIRMAS DE ACEPTACIÓN

Al estampar su firma digital o remitir confirmación firmada criptográficamente por canal Signal verificado, las Partes aceptan en su totalidad los términos, plazos, costes y condiciones de este Statement of Work.

| POR: **K4L1 STUDIO** | POR: **EL CLIENTE** |
| :--- | :--- |
| **Firma:** ___________________________________ | **Firma:** ___________________________________ |
| **Nombre:** Kali | **Nombre:** `[NOMBRE DEL REPRESENTANTE]` |
| **Cargo:** Arquitecta Directora | **Cargo:** `[CARGO DIRECTIVO]` |
| **Fecha:** `[DD/MM/AAAA]` | **Fecha:** `[DD/MM/AAAA]` |
| **Signal E2EE:** `@k4li.89` | **Email / Signal:** `[CONTACTO]` |

---
*Escudo Kanuv 🛡️ — Certificación Técnica de Alcance & Compromiso Contractual (189.89.619 Hz).*
