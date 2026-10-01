# NES-OPE-PR-016 — Fuentes consultadas

> Limitación de esta sesión: WebFetch estuvo bloqueado por el proxy de salida para los dominios técnicos y el presupuesto de WebSearch se agotó. Las fuentes de abajo se consultaron por los extractos del buscador, **no abriendo el documento completo**. Confirmar las marcadas con (*) antes de la versión para obra.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| VLF AC withstand testing of cable — test voltages per IEEE 400.2-2013 (*) | Fabricante de equipos VLF (EE. UU.) | 2020–2023 | https://hvinc.com/wp-content/uploads/2020/09/VLF_Cable_Test_Voltages_per_IEEE_400.2-2013_2020.pdf ; https://hvinc.com/wp-content/uploads/2023/08/VLF-2023-Cable-Testing-Voltages-per-IEEE400.2_compressed.pdf | Tensiones VLF 0,1 Hz de instalación y aceptación: 15 kV 19/27 y 21/30; 25 kV 29/41 y 32/45; 35 kV 39/55 y 44/62 kV rms/pico; mantenimiento ≈75% de aceptación |
| VLF cable testing (*) | Enciclopedia en línea | s. f. | https://en.wikipedia.org/wiki/VLF_cable_testing | VLF de 2 U0 a 3 U0, 15–60 min; 30 min recomendado; IEEE 400.2 con criterios de tan delta por tipo de aislamiento |
| Tan delta FAQ / NEETRAC CDFI report (*) | Fabricante de equipos VLF / centro de investigación universitario | 2016–2022 | https://hvinc.com/wp-content/uploads/2019/11/HVI-TD-FAQ-WEB-2019.pdf ; https://hvinc.com/wp-content/uploads/2016/12/NEETRAC_CDFI_Report_Tan_Delta.pdf | Criterios IEEE 400.2 para PE envejecido (estabilidad, diferencia de TD, TD medio) y medición en escalones 0,5/1,0/1,5 U0 |
| Review of changes in IEEE 400.2 (*) | Empresa de diagnóstico de cables | s. f. | https://www.diatech.in/review-of-changes-in-ieee-400-2-for-vlf-cable-testing/ | Estructura de la edición 2013 (tablas de tensión y de TD) |
| Simultaneous PD and TD testing (*) | Fabricante de equipos de ensayo | 2019 | https://hvtechnologies.com/wp-content/uploads/2019/07/Simultaneous-PD-and-TD-Testing.pdf | Secuencia combinada TD + DP en campo; tip-up como indicador de DP |
| IEEE 400.2-2013 (resúmenes públicos) (*) | IEEE | 2013 | https://www.academia.edu/34497785/ | Alcance de la guía, uso de VLF en cables nuevos y envejecidos |
| Recomendaciones / libro blanco de instalación MT y accesorios (*) | Fabricante de cable y accesorios (Europa) | 2018 | https://www.prysmianclub.es/wp-content/uploads/2018/05/Guia_TECNICA_Cables_Accesorios_MEDIA_Tension-1.pdf | Preparación del cable, retiro de semiconductora, limpieza, accesorios en frío y en caliente |
| On site testing guidelines for MV cables (*) | Fabricante de cable (Reino Unido) | 2019 | https://uk.prysmian.com/sites/uk.prysmian.com/files/media/documents/On%20Site%20Testing%20Guidelines%20%282019%29%20%283%29.pdf | Ensayos tras instalación y precauciones con DC en XLPE |

Conocimiento normativo de base (no tomado de internet en esta sesión): clases de terminales IEEE 48; IEEE 404 empalmes; IEEE 386 conectores separables (200 A codo, 600 A tipo T); IEC 61238-1 conectores de compresión; IEC 60502-4 ensayos de accesorios; IEEE 400.3 descargas parciales; buenas prácticas de empalmadores (limpieza del aislamiento hacia la semiconductora, secuencia de compresión, piezas deslizantes antes de unir conductores).

## Ajustes para Colombia

- Cualificación: matrícula CONTE (Ley 1264 de 2008) además de la capacitación del fabricante; ingeniero COPNIA para ensayos y esquema de pantallas.
- Cinco reglas de oro del RETIE / Res. 5018 de 2019, permisos y LOTO remitidos a NES-SST-PR-001; trabajo en caliente a NES-SST-PR-004; dictamen RETIE y energización a NES-OPE-PR-023.
- Tabla VLF relacionada con tensiones de colectores usadas en Colombia (13,2/13,8 kV y 34,5 kV); nota para cables con designación IEC U0/U.
- Clima: humedad alta en la costa Caribe y los llanos (programar en horas secas, higrómetro), tormenta eléctrica, calor dentro de la carpa, ofidios en cámaras.
- Ambiente: solventes y paños como RESPEL (Decreto 1076 de 2015), SGA (Decreto 1496 de 2018), Res. 2184 de 2019.
- Emergencias: 123, ARL, Res. 1401 de 2007.
- Sin nombres de fabricantes en el documento.

## Pendientes de verificar

- Límites de humedad relativa y de temperatura de instalación de cada kit, vida útil de almacenamiento, cotas y torques: instrucción del fabricante del accesorio del proyecto.
- Torques de pasatapas, tapones y conexiones de lug: fabricantes de celdas, transformadores y conectores.
- Tensión de ensayo VLF y duración (30 o 60 min), criterio de tan delta para cable nuevo y criterio de DP (pC): especificación de [CLIENTE]; confirmar contra la edición vigente de IEEE 400.2 (la tabla de 5 kV y 8 kV no se incluyó por no haberse podido confirmar).
- Criterios de tan delta de IEEE 400.2 confirmados solo parcialmente por extractos (PE envejecido: <0,1 / <5 / <4 ×10⁻³ sin acción; >0,5 / >80 / >50 acción); verificar contra el texto de la norma.
- Esquema de conexión de pantallas: diseño eléctrico del proyecto.
- Muestreo de QA/QC tras los tres primeros accesorios (criterio interno, porcentaje en blanco).
