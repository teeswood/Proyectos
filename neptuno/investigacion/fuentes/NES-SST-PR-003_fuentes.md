# Fuentes — NES-SST-PR-003 Procedimiento de Izaje de Cargas con Grúa

> Limitación de la investigación (01-10-2026): en esta sesión el proxy de salida bloqueó la descarga directa (WebFetch/curl) de todos los dominios consultados (gov.co, normogramas, OSHA, NFPA, Wikipedia, etc.) y el presupuesto de búsquedas web de la sesión se agotó tras pocas consultas. Las URL de la tabla se consultaron a través de los resultados del buscador (fragmentos de texto devueltos por la búsqueda), no se abrieron completas. Los contenidos de ASME B30 e ISO se tomaron del conocimiento técnico de esas normas y se citan solo como referencia técnica; deben verificarse contra el texto oficial antes de la aprobación.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Resolución 2400 de 1979 (texto en SUIN-Juriscol) | MinTrabajo / SUIN | 1979 | https://www.suin-juriscol.gov.co/viewDocument.asp?ruta=Resolucion/30035732 | Arts. 415, 416, 417, 420, 421, 423, 425, 426 y 447 (vía fragmentos del buscador). |
| Resolución 2400 de 1979 (normograma Cancillería) | Cancillería de Colombia | 1979 | https://www.cancilleria.gov.co/sites/default/files/Normograma/docs/resolucion_mintrabajo_rt240079.htm | Confirmación del art. 447 (factores 10 / 8 / 5) y art. 420 (cargas sobre personas). |
| Resolución 2400 de 1979 (compilación ICBF) | ICBF | 1979 | https://www.icbf.gov.co/cargues/avance/compilacion/docs/resolucion_mintrabajo_rt240079.htm | Art. 420 (texto). |
| Resolución 2400 de 1979 (PDF Fondo de Riesgos Laborales) | MinTrabajo | 1979 | https://fondoriesgoslaborales.gov.co/documents/normatividad/resoluciones/Res-2400-1979.pdf | Arts. 427 a 429 y tablas de cargas límite de cuerdas, cables, cadenas, grilletes y ganchos. |
| Normatividad de grúas en Colombia | Organismo de certificación de grúas (sitio comercial) | s. f. | https://www.certificaciongruas.com/nuestros-proyectos/ | Confirmación de que no existe reglamento único de grúas y de que se usa Res. 2400 de 1979 + ASME B30 + certificación por organismo acreditado. |
| ASME B30.5 Mobile and Locomotive Cranes | ASME | ed. vigente | (no abierta) | Señales manuales normalizadas, distancia de 3 m a líneas hasta 50 kV, inspección preoperacional, prueba de despegue. Referencia técnica. |
| ASME B30.9 Slings / B30.10 Hooks / B30.26 Rigging Hardware | ASME | ed. vigentes | (no abierta) | Factores de diseño de eslingas (5 cable y sintética, 4 cadena aleada), ángulo mínimo 30°, criterios de descarte de eslingas, ganchos (5% apertura, 10° giro) y grilletes. Referencia técnica. |
| ISO 4309 / ISO 12480-1 | ISO | ed. vigentes | (no abierta) | Criterios de descarte de cable de acero y uso seguro de grúas. Referencia técnica. |

## Ajustes para Colombia

- Requisitos legales tomados de la Res. 2400 de 1979 (arts. verificados por fragmento de búsqueda); OSHA 1926 Subpart CC no se cita como requisito.
- Distancias a líneas: requisito = tabla del RETIE (Res. 40117 de 2024) para la tensión; ASME B30.5 queda como referencia y se adopta la mayor (criterio interno). El valor RETIE queda como marcador [____] m.
- Certificación de operador/aparejador/señalero: organismo de certificación de personas acreditado ante ONAC o SENA (competencias laborales) como buena práctica; aptitud médica ligada al art. 415.
- Ingeniero de izaje con matrícula COPNIA; responsable SST con licencia; coordinación con [OPERADOR DE RED] para desenergización (NES-SST-PR-001).
- Unidades SI (kg, m, kPa, m/s); valores imperiales de ASME convertidos (10 ft → 3,0 m).
- Umbrales de izaje crítico (75%), máximo planificable (90%), tándem (75% por grúa), estimación de reacción en estabilizador (75%) y reanudación tras tormenta (30 min) marcados como criterio interno.

## Pendientes de verificar

- Tabla de distancias mínimas de seguridad del RETIE vigente para cada tensión presente en el proyecto (verificar numeral y tabla del Anexo General de la Res. 40117 de 2024).
- Límite de viento de la grúa asignada (9,8 m/s se dejó como valor típico de fabricante).
- Capacidad portante de las plataformas de grúa (estudio de suelos).
- Pesos, centros de gravedad, puntos y accesorios de izaje de estaciones de potencia, transformadores, inversores y celdas (manuales de los fabricantes); método de izaje de palés de módulos autorizado por el fabricante del módulo.
- Confirmar en el texto oficial de la Res. 2400 de 1979 los arts. 415–426 y 447 (verificados solo por fragmentos del buscador).
- Permiso de carga extradimensionada para la grúa en vía pública (autoridad vial).
