# NES-CAL-PLN-003 — Fuentes consultadas

Nota de acceso: en esta sesión la salida a internet estaba restringida y el cupo de búsquedas compartido de la sesión se agotó durante la investigación del documento NES-OPE-PR-023. La estructura del plan, los puntos H/W/R/M y los criterios se tomaron de las normas técnicas citadas en el documento (IEC 62446-1, IEC 60364-6, IEEE 400.2, IEEE 48/404, IEEE 81, IEC 60076, IEC 62271, ISO 6789, NTC-ISO/IEC 17025), de los procedimientos Neptuno ya redactados (NES-OPE-PR-014, PR-015, PR-017, PR-022, PR-023, NES-SST-PR-001) y de las fuentes de internet siguientes. No se transcribió ningún valor que no estuviera verificado: los valores no verificados quedan genéricos o con [____].

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Anexo 1 del Acuerdo 1214 — Procedimiento para la entrada en operación comercial | CNO | 2019 | https://cnostatic.s3.amazonaws.com/cno-public/archivosAdjuntos/anexo_1_acuerdo_cno1214_2.pdf | Documentos de interfaz con la energización: certificado del OR de cumplimiento y pruebas de protecciones, EACP, señales SCADA/SOE; alimentan las líneas 12.x de la matriz y el capítulo 14 del dossier. |
| Acuerdo 1937 — Procedimiento para la declaración de entrada en operación comercial | CNO | 2025 | https://cnostatic.s3.amazonaws.com/cno-public/archivosAdjuntos/Acuerdo%201937.pdf | Referencia a "acuerdo CNO vigente" en las pruebas de desempeño y capacidad (línea 12.9). |
| Guías de comisionado FV (resultados de búsqueda; páginas bloqueadas) | Sitios técnicos del sector | 2024–2026 | https://www.surgepv.com/blog/solar-commissioning-checklist ; https://mitti.com/library/energy-and-utilities/solar-commissioning-sheet-qx1oppukhmg5nfui ; https://www.ginzasolar.com/blog/solar-power-system-commissioning-checklist/ | Pruebas básicas del comisionado (polaridad, Voc, corriente, aislamiento, continuidad de tierra, verificación de protecciones, arranque del inversor) y paso por completamiento mecánico, comisionado y entrega usados para ordenar las secciones 7.11 y 7.12. |
| Resolución CREG 075 de 2021 (resultado de búsqueda; página bloqueada) | CREG | 2021 | https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0075_2021.htm | Solo contexto: el OR puede exigir aprobación y calibración vigente de los equipos de prueba de conexión; se dejó como "cuando el [OPERADOR DE RED] o el contrato fijen una antigüedad máxima de calibración" sin cifra. |

## Ajustes para Colombia

- Calibración trazable mediante laboratorios acreditados por ONAC bajo NTC-ISO/IEC 17025 (en lugar de UKAS/A2LA/ENAC de las fuentes extranjeras), con reconocimiento de acreditaciones extranjeras por acuerdos de reconocimiento mutuo.
- Certificados de conformidad de producto exigidos por el RETIE en recepción de materiales, dictamen de inspección RETIE como punto R antes de energizar y capítulo propio en el dossier.
- Puesta a tierra: valor máximo del RETIE (sin cifra, depende del tipo de instalación) además del valor de diseño; SIPRA según NTC 4552 / IEC 62305.
- Rotulado de cajas combinadoras y DC según NTC 2050 sección 690 y RETIE (en lugar de NEC 690).
- Roles: responsable eléctrico con matrícula COPNIA, técnicos con matrícula CONTE; ensayos con tensión aplicada bajo NES-SST-PR-001 y Res. 5018 de 2019.
- Interfaz con [OPERADOR DE RED] y XM a través de NES-OPE-PR-023 (prerrequisitos F-160, entrega F-169).
- Máximo 7 columnas por tabla; puntos con la convención Neptuno / [CLIENTE].

## Pendientes de verificar

- Matriz H/W/R definitiva de [CLIENTE] y plazos de notificación (se propusieron 24 h para W y 48 h para H como criterio interno).
- Códigos exactos de los formatos de NES-OPE-PR-002, PR-011, PR-016, PR-018, PR-019, PR-020 y PR-021 (no estaban redactados al cerrar este plan; se citan como "formatos del procedimiento" o por su serie).
- Valor máximo de resistencia de puesta a tierra del RETIE aplicable a cada tipo de instalación del proyecto (no se pudo abrir el texto de la Res. 40117 de 2024).
- Tensión y duración del ensayo VLF según la edición vigente de IEEE 400.2 y la clase de aislamiento de los cables del proyecto; criterios de tangente delta y descargas parciales si el contrato los exige.
- Tolerancias de relación de transformación y resistencia de contactos según IEC 60076-1 y protocolos de fábrica.
- Intervalos de calibración e intervalos de verificación intermedia (criterio interno propuesto) frente a recomendaciones de cada fabricante de instrumento.
- Criterio de atenuación por empalme de fibra y presupuesto de enlace: según diseño del proyecto.
