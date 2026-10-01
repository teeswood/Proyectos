# NES-OPE-PR-020 — Fuentes consultadas

> Limitación de la sesión (01-10-2026): la política de red del entorno bloqueó la apertura directa de páginas y PDF (WebFetch/curl con 403 en todos los dominios probados, incluidos minenergia.gov.co, cancilleria.gov.co, gestornormativo.creg.gov.co, electricaplicada.com e instalect.co), y el presupuesto de búsquedas de la sesión se agotó. El contenido se tomó de los extractos del buscador para las URL listadas y del conocimiento técnico de las normas citadas (IEEE 80, IEEE 81, IEEE 837, NTC 4552 / IEC 62305, IEC 61643). Los valores numéricos del RETIE no se trasladaron al documento porque no fue posible abrir el texto oficial.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Resolución 40117 de 2024 — normograma | Ministerio de Relaciones Exteriores / CREG (gestor normativo) | 2024 | https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_minminas_40117_2024.htm | Existencia de la tabla de valores de referencia de resistencia de puesta a tierra (no abierta; valores no trasladados). |
| Libro 3 — Instalaciones objeto del RETIE | MinEnergía | 2024 | https://www.minenergia.gov.co/documents/11566/4._Libro_3_-_Instalaciones.pdf | Ubicación de los requisitos de puesta a tierra en el libro 3 (no abierto). |
| Libro 3 — Resolución 40284 del 23-06-2026 | MinEnergía | 2026 | https://www.minenergia.gov.co/documents/15921/Libro-3-Resolucion-40284-23-06-2026.pdf | Existencia de una versión compilada modificada del RETIE (no abierta); se cita "y sus modificaciones vigentes". |
| Resolución 40284 de 2026 — resúmenes | Varios (safetya.co, holdingconsultants.org, Camacol) | 2026 | https://safetya.co/normatividad/resolucion-40284-de-2026/ | Modifica libros 1 a 4 y anexos del RETIE; cambio en el artículo 3.3.1 sobre autogeneración menor de 10 kVA. |
| Artículo 3.12.3. Valores de referencia de resistencia de puesta a tierra | electricaplicada.com | s. f. | https://electricaplicada.com/valores-referencia-mantenimiento-retie/ | Que el RETIE fija valores de referencia por tipo de instalación y que su cumplimiento no exime de controlar tensiones de paso, contacto y transferidas. |
| Puesta a tierra en Colombia: normativa RETIE y diseño | hidrosolta.com | s. f. | https://www.hidrosolta.com/puesta-a-tierra | Origen de los valores de la tabla (IEEE 80, NTC 2050, NTC 4552-1), contexto. |
| GM-04 Guía metodológica: cálculo del sistema de puesta a tierra | Operador de red colombiano (no se nombra en el documento) | s. f. | https://www.cens.com.co/Portals/cens/institucional/Especificaciones/Documentos-en-revision/norma-tecnica/Guias-complementarias-de-dise%C3%B1o-grupo-EPM/GM-04-guia.pdf | Enfoque de diseño IEEE 80 con resistividad, tensiones tolerables y verificación (título y extracto). |
| Puesta a tierra: cuántos ohmios, cómo se mide y qué exige el RETIE (2026) | instalect.co | 2026 | https://www.instalect.co/blog/puesta-a-tierra-ohmios-medicion-retie/ | Medición por caída de potencial como método de verificación (extracto). |
| Normas de diseño de media y baja tensión — Puesta a tierra | Operador de red colombiano (no se nombra) | 2022 | https://www.emcali.com.co/documents/136518/1202703/11-PUESTA%20A%20TIERRA.pdf | Referencia de práctica colombiana de mallas (título y extracto). |
| ANSI/NETA ATS (sección de puesta a tierra) — extractos | NETA | 2009–2025 | https://forum.testguy.net/content/240-Insulation-Resistance-Test-Values | Práctica de investigar resistencias punto a punto elevadas (marcado como criterio interno 0,5 Ω, verificar contra especificación). |

## Ajustes para Colombia

- Normativa: requisitos legales con RETIE (Res. 40117 de 2024 y modificaciones vigentes), NTC 2050 secciones 250 y 690, NTC 4552 partes 1 a 4; IEEE 80, IEEE 81, IEEE 837, IEC 62305, IEC 62561 e IEC 61643 solo como referencia técnica. No se cita normativa mexicana ni española que apareció en las búsquedas.
- Valores de resistencia: se usa la frase "según la tabla de valores de referencia de resistencia de puesta a tierra del RETIE vigente" sin número, por no haberse podido abrir el texto oficial.
- Dictamen: inspección por organismo acreditado ONAC y declaración de cumplimiento del constructor; energización solo por NES-OPE-PR-023.
- Roles: COPNIA, CONTE, responsable SST con licencia, ARL; soldadura exotérmica como trabajo en caliente (NES-SST-PR-004).
- Clima: tormenta eléctrica como riesgo principal (malla, cercas y cables de medición), lluvia (zanjas y soldadura), estrés térmico, ofidios.
- Ambiente: escoria y moldes según hoja de seguridad y RESPEL; prohibición de sal y productos corrosivos como mejoradores (criterio interno); Res. 2184 de 2019 y RCD.
- Unidades SI (Ω, Ω·m, m) y decimales con coma; se evitaron marcas comerciales de soldadura exotérmica, conectores, telurómetros y acero recubierto de cobre.

## Pendientes de verificar

- Valores de la tabla de referencia de resistencia de puesta a tierra y de tensiones de contacto máximas del RETIE vigente (incluida la Resolución 40284 de 2026) para incluirlos en los formatos al aterrizar.
- Dimensiones mínimas de electrodos y secciones mínimas de conductores exigidas por el RETIE vigente y por el diseño.
- Profundidad de la malla, separación de electrodos, espesor de la capa superficial y valor de diseño de resistencia (memoria del proyecto).
- Distancia del electrodo de corriente en mallas grandes y método alternativo de la IEEE 81 cuando no haya zona plana.
- Criterio de continuidad punto a punto de la especificación del proyecto (el documento usa 0,5 Ω como criterio interno).
- Longitud máxima de conexión de DPS según el fabricante y el diseño (0,5 m queda como referencia usual).
- Vida útil de moldes, tiempos de enfriamiento y criterios de porosidad del fabricante del sistema de soldadura exotérmica.
