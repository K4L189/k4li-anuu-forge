# ACUERDO MUTUO DE CONFIDENCIALIDAD, NO DIVULGACIÓN Y CUSTODIA CRIPTOGRÁFICA (NDA BILATERAL)

**DOCUMENTO DE BLINDAJE LEGAL & TÉCNICO E2EE**  
**CÓDIGO DE REGISTRO:** `K4L1-SEC-NDA-2026-REV4`  
**CLASIFICACIÓN:** PRIVADO / CONFIDENCIAL  
**FRECUENCIA DE CUSTODIA:** `189.89.619 Hz` — ESCUDO KANUV 🛡️

---

### PREÁMBULO Y COMPARECENCIA DE LAS PARTES

El presente **Acuerdo Mutuo de Confidencialidad y Secreto Industrial** (en adelante, el "Acuerdo") entra en vigor a fecha de su última firma electrónica o criptográfica (en adelante, la "Fecha de Entrada en Vigor"), celebrado por y entre:

1. **DE UNA PARTE:**  
   **K4L1 STUDIO**, boutique especializada en fortificación de infraestructura crítica, auditoría forense, arquitecturas SIEM, interfaces de alta frecuencia e inteligencia artificial local soberana, representada operativamente por su Arquitecta Directora **Kali** (en adelante, indistintamente **"K4L1 STUDIO"** o la "Parte Reveladora/Receptora").  
   - **Canal Criptográfico Oficial:** Signal `@k4li.89` / Clave Pública PGP verificada.  
   - **Jurisdicción Operativa:** España / Unión Europea.

2. **DE OTRA PARTE:**  
   **[RAZÓN SOCIAL / NOMBRE DEL CLIENTE]**, entidad legalmente constituida bajo las leyes de `[PAÍS/JURISDICCIÓN]`, con NIF/CIF/ID Fiscal `[IDENTIFICADOR FISCAL]`, con domicilio social en `[DIRECCIÓN COMPLETA]`, representada en este acto por `[NOMBRE Y CARGO DEL REPRESENTANTE LEGAL]` (en adelante, el **"CLIENTE"** o la "Parte Receptora/Reveladora").

Ambas partes podrán ser denominadas colectivamente como las **"Partes"** e individualmente como la **"Parte"**.

---

### EXPOSICIÓN DE MOTIVOS

**I.** Que las Partes contemplan entablar o han entablado relaciones estratégicas de consultoría técnica, auditoría de seguridad, fortificación de sistemas, desarrollo de software a medida o despliegue de infraestructura de inteligencia artificial on-premise (en adelante, el "Proyecto").  
**II.** Que durante dichas interacciones, las Partes intercambiarán activos de altísimo valor estratégico, código fuente, secretos comerciales, algoritmos, llaves criptográficas, registros de pacientes o clientes, y metodologías operativas.  
**III.** Que es voluntad unánime de las Partes blindar contractualmente dicha información bajo estándares de cifrado de grado militar (End-to-End Encryption - E2EE) y sujeción estricta al deber de sigilo profesional.

Por tanto, las Partes acuerdan las siguientes:

---

### CLÁUSULAS CONTRACTUALES

#### CLÁUSULA PRIMERA: DEFINICIÓN DE INFORMACIÓN CONFIDENCIAL

A los efectos de este Acuerdo, tendrá la consideración de **"Información Confidencial"** cualquier información técnica, financiera, operativa, comercial o estratégica transmitida directa o indirectamente por cualquiera de las Partes (la "Parte Reveladora") a la otra Parte (la "Parte Receptora"), ya sea de forma verbal, visual, escrita, digital, o mediante acceso directo a redes, repositorios, terminales o servidores.

Dicha información incluye de forma enunciativa pero no limitativa:
1. **Infraestructura y Seguridad:** Topologías de red, configuraciones de cortafuegos (iptables/UFW), reglas de detección SIEM (Wazuh, Suricata, Zeek), resultados de escaneos de vulnerabilidades, volcados forenses, informes de pentesting, registros de auditoría y credenciales de acceso a entornos de producción, staging o laboratorio.
2. **Criptografía y Llaves:** Llaves privadas SSH, llaves de firma PGP/GPG, certificados TLS/mTLS, semillas de carteras criptográficas (seeds/wallets), secretos de entorno (`.env`), contraseñas y hashes de autenticación.
3. **Propiedad Intelectual y Código:** Código fuente en cualquier lenguaje (Python, Rust, C, JavaScript/TypeScript, Go, Bash), arquitecturas de bases de datos, esquemas relacionales o vectoriales, pesos y adaptadores LoRA de modelos de lenguaje local (GGUF, ONNX), algoritmos de arbitraje de alta frecuencia y microservicios propietarios.
4. **Datos Sensibles de Negocio:** Bases de datos de clientes, historiales clínicos o datos biomédicos sujetos a normativas de protección de datos (RGPD, LOPD-GDD, HIPAA), libros contables, estrategias de monetización y acuerdos con terceros.

---

#### CLÁUSULA SEGUNDA: PROTOCOLOS DE CUSTODIA CRIPTOGRÁFICA Y TRANSMISIÓN E2EE

Las Partes reconocen que la confidencialidad en el ámbito de los sistemas críticos no es una simple manifestación de intenciones, sino una disciplina criptográfica aplicada. Por ello, se establecen los siguientes compromisos técnicos imperativos:

1. **Canales de Comunicación Verificados:** Queda terminantemente prohibido el envío de Información Confidencial, credenciales, volcados de base de datos o fragmentos de código crítico a través de canales no cifrados de extremo a extremo (E2EE), correos electrónicos en texto plano, plataformas colaborativas públicas o chats comerciales desprovistos de cifrado verificado.
2. **Vías Autorizadas:** Toda comunicación operativa sensible se canalizará a través de:
   - Canal Signal punto a punto (E2EE).
   - Correos electrónicos cifrados mediante llaves **PGP/GPG** previamente intercambiadas y verificadas por fingerprint.
   - Repositorios Git privados asegurados mediante SSH Ed25519 con autenticación multifactor (MFA/FIDO2).
   - Enlaces VPN punto a punto (WireGuard/Tailscale con claves efímeras) o bastiones SSH con acceso restringido por IP fija.
3. **Almacenamiento Cifrado en Reposo:** Todo equipo, estación de trabajo o volumen de almacenamiento que contenga activos del Proyecto deberá estar cifrado en reposo mediante **LUKS (Linux Unified Key Setup) con AES-XTS-plain64** o estándar equivalente de 256 bits.

---

#### CLÁUSULA TERCERA: EXCLUSIONES AL DEBER DE CONFIDENCIALIDAD

La Información Confidencial no incluirá ninguna información que la Parte Receptora pueda demostrar de manera fehaciente:
1. Que ya era de dominio público en el momento de su revelación o que haya pasado a serlo sin mediar incumplimiento del presente Acuerdo por parte de la Parte Receptora.
2. Que se encontraba en posesión legal de la Parte Receptora con anterioridad a su divulgación por la Parte Reveladora, libre de toda obligación de confidencialidad.
3. Que haya sido desarrollada de forma totalmente independiente por personal de la Parte Receptora sin acceso ni referencia alguna a la Información Confidencial recibida.
4. Que haya sido obtenida legítimamente de un tercero que poseía el derecho legal de transmitirla sin restricciones de confidencialidad.

*Requerimiento Judicial:* En caso de que la Parte Receptora sea legalmente requerida por orden judicial o mandamiento de autoridad competente para divulgar cualquier porción de la Información Confidencial, la Parte Receptora notificará de inmediato y por escrito (con carácter previo a la divulgación y dentro de los límites legales) a la Parte Reveladora, a fin de que esta última pueda articular los recursos de contención o medidas cautelares pertinentes.

---

#### CLÁUSULA CUARTA: PROPIEDAD INTELECTUAL INALIENABLE Y ARQUITECTURA PREEXISTENTE

1. **Patrimonio Técnico Preexistente de K4L1 STUDIO:** El CLIENTE reconoce y acepta que K4L1 STUDIO retiene en todo momento la titularidad exclusiva, ilimitada e inalienable sobre sus herramientas internas de fortificación, scripts de automatización genéricos, dotfiles, metodologías de hardening, módulos del Concilio ACE / Escudo Kanuv, pipelines de auditoría y know-how técnico desarrollado con anterioridad o paralelamente al Proyecto.
2. **Propiedad de los Datos y Código del CLIENTE:** El CLIENTE retiene la propiedad absoluta sobre sus datos corporativos, información financiera, registros de usuarios/pacientes, y aquellos desarrollos a medida contratados y liquidados íntegramente según los términos de las propuestas comerciales correspondientes.
3. **No Cesión Implícita:** La divulgación de Información Confidencial al amparo del presente instrumento no confiere, de forma explícita ni implícita, ninguna licencia, derecho de autor, patente, patente de software o derecho de uso comercial sobre la propiedad intelectual de la Parte Reveladora, más allá de la estricta ejecución técnica del Proyecto.

---

#### CLÁUSULA QUINTA: OBLIGACIONES DE NO DIVULGACIÓN Y RESTRICCIÓN DE USO

La Parte Receptora se compromete a:
1. Tratar la Información Confidencial recibida con el mismo grado de diligencia y custodia que aplica a su propia información de máxima reserva, no inferior en ningún caso a un estándar de diligencia técnica razonable y pericial.
2. Utilizar la Información Confidencial **única y exclusivamente** con el propósito de evaluar, diseñar, ejecutar y auditar el Proyecto pactado entre las Partes.
3. No descompilar, realizar ingeniería inversa, desensamblar ni clonar arquitecturas propietarias protegidas sin consentimiento previo por escrito.
4. Restringir el acceso a la Información Confidencial únicamente a aquellos empleados, directivos, colaboradores o auditores que tengan una estricta **"necesidad de conocer"** (*need-to-know*), previa suscripción de acuerdos de confidencialidad con obligaciones no menos restrictivas que las aquí consagradas.

---

#### CLÁUSULA SEXTA: PLAZO DE VIGENCIA Y SECRETO INDUSTRIAL INDEFINIDO

1. **Plazo General:** Las obligaciones de confidencialidad, reserva y no divulgación asumidas en el presente instrumento permanecerán vigentes durante un período de **CINCO (5) AÑOS** a partir de la Fecha de Entrada en Vigor, o desde la fecha de recepción de la última revelación técnica.
2. **Excepción de Secreto Industrial y Criptográfico (Carácter Indefinido):** No obstante lo dispuesto en el apartado anterior, para toda aquella información clasificada como **Secreto Industrial**, algoritmos propietarios de cálculo/trading, código fuente nuclear, y claves criptográficas maestras, la obligación de reserva perdurará de forma **INDEFINIDA Y PERPETUA**, en tanto dicha información no entre legalmente en el dominio público.

---

#### CLÁUSULA SÉPTIMA: DEVOLUCIÓN O DESTRUCCIÓN CRIPTOGRÁFICA CERTIFICADA (CRYPTO-SHREDDING)

A la finalización del Proyecto, o mediando solicitud por escrito de la Parte Reveladora, la Parte Receptora procederá en un plazo máximo de **diez (10) días naturales** a:
1. Devolver todas las copias físicas, documentación y soportes materiales que contengan Información Confidencial.
2. Ejecutar un procedimiento de **destrucción criptográfica segura (Crypto-Shredding / Purga Segura)** sobre todos los soportes electrónicos, imágenes de disco, bases de datos temporales y logs que alberguen dicha información, utilizando algoritmos de sobrescritura segura (norma DoD 5220.22-M o NIST SP 800-88 Rev. 1) o la eliminación irreversible de las claves de cifrado maestras.
3. Emitir un **Certificado Forense de Purga y Destrucción de Datos**, firmado digitalmente por el responsable técnico, acreditando la inexistencia de copias o derivaciones no autorizadas en sus sistemas.

*Salvedad:* Se autoriza la retención de aquellas copias de seguridad automáticas inmutables exigidas imperativamente por la legislación fiscal o de protección de datos aplicable, las cuales continuarán sujetas a estricta confidencialidad hasta su caducidad definitiva.

---

#### CLÁUSULA OCTAVA: INCUMPLIMIENTO, MEDIDAS CAUTELARES Y PENALIDADES

1. **Reconocimiento de Daño Irreparable:** Las Partes reconocen expresamente que cualquier brecha de seguridad, filtración no autorizada o divulgación indebida de la Información Confidencial ocasionará un perjuicio grave, directo e irreparable a la Parte Reveladora, difícilmente cuantificable en exclusiva compensación económica.
2. **Medidas Cautelares Inmediatas:** En consecuencia, ante cualquier amenaza inminente o constatación de divulgación indebida, la Parte afectada tendrá pleno derecho a solicitar medidas cautelares de cesación urgente (*injunctive relief*) ante los tribunales correspondientes, sin necesidad de prestar fianza previa desproporcionada.
3. **Indemnización y Resarcimiento:** Sin perjuicio de las medidas cautelares y de las responsabilidades penales que pudieran derivarse (artículos 278 y 279 del Código Penal español u ordenamientos homólogos relativos al descubrimiento y revelación de secretos de empresa), la Parte infractora estará obligada a indemnizar a la Parte Reveladora por todos los daños y perjuicios directos, lucro cesante y costes periciales y de defensa jurídica en que esta última haya incurrido.

---

#### CLÁUSULA NOVENA: LEY APLICABLE, JURISDICCIÓN Y RESOLUCIÓN DE DISPUTAS

1. **Ley Aplicable:** El presente Acuerdo se regirá e interpretará conforme a la legislación sustantiva española y al marco normativo de la Unión Europea en materia de Secretos Comerciales (Directiva UE 2016/943 y Ley 1/2019, de Secretos Empresariales) y Ciberseguridad (Directiva NIS2).
2. **Resolución de Controversias:** Toda discrepancia, litigio o reclamación derivada de la interpretación, validez o ejecución del presente Acuerdo se intentará resolver en primer término mediante negociación directa de buena fe en un plazo no superior a quince (15) días. De no alcanzarse acuerdo, las Partes se someten expresamente a la jurisdicción de los **Juzgados y Tribunales de la ciudad de Madrid (España)**, con renuncia formal a cualquier otro fuero que pudiera corresponderles.

---

### FIRMA Y RATIFICACIÓN DIGITAL

En prueba de conformidad y sujeción estricta a lo estipulado, las Partes suscriben el presente Acuerdo en dos ejemplares electrónicos con plena validez probatoria.

| POR: **K4L1 STUDIO** | POR: **EL CLIENTE** |
| :--- | :--- |
| **Firma:** ___________________________________ | **Firma:** ___________________________________ |
| **Nombre:** Kali | **Nombre:** `[NOMBRE DEL REPRESENTANTE]` |
| **Cargo:** Arquitecta Directora & Fundadora | **Cargo:** `[CARGO DIRECTIVO / CEO / CTO]` |
| **Entidad:** K4L1 STUDIO | **Entidad:** `[RAZÓN SOCIAL DE LA EMPRESA]` |
| **Fecha:** 25 de Octubre de 2026 | **Fecha:** `[FECHA DE SUSCRIPCIÓN]` |
| **Identificador / Signal:** `@k4li.89` | **Email / Signal:** `[CONTACTO E2EE]` |
| **Fingerprint PGP:** `1619 1489 K4L1 SECU KANV 2077` | **Hash Verificación:** `[HASH SHA-256 CLIENTE]` |

---
*Sello de Integridad Forense: SHA-256 Validated — Escudo Kanuv 🛡️ (189.89.619 Hz).*
