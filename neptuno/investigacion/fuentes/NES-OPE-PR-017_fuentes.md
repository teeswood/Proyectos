# NES-OPE-PR-017 — Fuentes consultadas

Nota de método: en esta sesión el proxy de salida bloqueó la apertura directa (WebFetch) de todos los dominios intentados (fabricantes, IFC, NREL, SolarPower Europe). El contenido se tomó de los extractos que devolvió el motor de búsqueda (WebSearch) para cada URL listada. Las URL no se abrieron completas; conviene contrastar los valores marcados como "valor típico de fabricante" contra el manual del equipo del proyecto.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| PV DC Combiner Box – Operating instructions v.2.4 | Fabricante de cajas combinadoras (Weidmüller) | 2020/2024 | https://assets.dam.weidmueller.com/assets/api/6cc83617-0379-48b5-b4f2-871bd407a366/Original/4000001903_00_08-2020_OPIN_PV-DC-COMBINER-BOX_en_2024.pdf | Fusibles gPV IEC 60269-6; torque portafusibles 10×85 de 2 a 2,5 N·m; selección de fusible por proyecto según Isc, tensión y temperatura. |
| PV DC Combiner Box – Operating instructions (versión distribuidor) | Fabricante de cajas combinadoras (Weidmüller) | s. f. | https://rspsupply.com/images/downloads/Weidmuller/8/Weidmuller%208000050568/User%20Documentation%20-%20User%20Manual%20PV%20DC%20Combiner%20Boxes.pdf | Montaje vertical con prensaestopas abajo; inclinación positiva 15° a 90°; almacenamiento acostada sobre cara posterior, -25 a +40 °C; operación -20 a +50 °C; no poner en servicio si hubo ingreso de polvo, líquido o condensación sin aprobación del fabricante; inspección visual anual de prensaestopas. |
| PV DC Combiner Box – instrucciones (solarmarkt) | Fabricante de cajas combinadoras (Weidmüller) | s. f. | https://www.solarmarkt.ch/herstimg/82-Generatoranschlusskasten/Weidmueller/MA_EN_Weidm%C3%BCller_Combinerbox_PV-DC-COMBINER-BOX.pdf | Prensaestopas multivía, un cable por orificio, pelado 18 mm con puntera, identificación de string y polaridad. |
| PV Combiner Box (catálogo y manual) | Fabricante de fusibles y cajas (Eaton/Bussmann) | s. f. | https://media.salvex.com/auction/d/1830007/183000654_637680.pdf | Prensaestopas IP65, portafusibles modulares apretados al torque especificado (solo extracto). |
| PVI-STRINGCOMB Product manual | Fabricante de inversores (FIMER) | s. f. | https://fimer.com/sites/default/files/PVI-STRINGCOMB-Product%20manual%20EN-RevA(M000020AG).pdf | Torques de prensaestopas por diámetro para conservar IP65 (solo extracto, sin valores usados). |
| PV System: how to ensure safety during normal operation | Electrical Installation Guide (wiki técnica) | s. f. | https://www.electrical-installation.org/enwiki/PV_System:_how_to_ensure_safety_during_normal_operation | Condición de necesidad de fusible 1,35 IRM < (Ns−1) Isc; no se requiere con 1 o 2 strings; calibre entre 1,5 y 2,4 Isc. |
| IEC 62548:2016 (muestra) | IEC | 2016 | https://cdn.standards.iteh.ai/samples/22202/f8767a8d9ee94f3c8452018aaa563dc7/IEC-62548-2016.pdf | Referencia de la norma de diseño de arreglos (protección de sobrecorriente de strings). |
| Solar Combiner Box Wiring Diagram and Installation Guide | Guía técnica de fabricante de DPS (LSP) | 2024-2025 | https://lsp.global/dc-pv-solar-combiner-box-installation-and-wiring-diagram/ | Altura típica 1,5–2,0 m; torques típicos de portafusibles 2,0–3,5 N·m y barras M5–M6 4–6 N·m; verificar polaridad antes de apretar; Voc por string con fusibles abiertos. |
| Type 2 DC Surge Protector | Guía técnica de fabricante de DPS (LSP) | s. f. | https://lsp.global/type-2-dc-surge-protector/ | DPS tipo 2 IEC 61643-31 cerca de la caja; conexión corta. |
| IEC 61643-11 vs IEC 61643-31 / Solar surge protection guide | Guías técnicas (cnspd, trilpeak) | 2025-2026 | https://trilpeak.com/solar-surge-protection-guide/ | Longitud de conexión del DPS menor a 0,5 m; conductor PE mínimo 6 mm² Cu; Uc respecto de Voc máx. |
| PV Combiner Box Wiring Diagrams / Terminal bus bars | Guías técnicas (sinobreaker, payapress) | 2025 | https://payapress.com/terminal-bus-bar/ | Torques típicos de barra M10 28–40 N·m y M12 45–70 N·m; no mezclar cobre y aluminio sin transición bimetálica; presión de contacto. |
| How are PV Combiner Boxes Installed / LETOP | Guías técnicas | s. f. | https://letopv.com/how-to-install-a-solar-combiner-box/ | Montaje en poste, muro o suelo; preferir sombra; espacio de apertura de puerta. |

## Ajustes para Colombia

- NEC 690 y el factor 1,56·Isc de las guías estadounidenses se reemplazaron por el criterio IEC 62548 / IEC 60364-7-712 (1,5 a 2,4 Isc) y por NTC 2050 art. 690 en lo que adopta el RETIE (Res. 40117 de 2024).
- Certificación UL de cajas se reemplazó por certificado de conformidad de producto exigido por el RETIE; IEC 61439-1/-2 queda como referencia técnica de la envolvente.
- Roles: electricistas con matrícula CONTE (Ley 1264 de 2008), ingeniero COPNIA, responsable SST con licencia, coordinador de alturas (Res. 4272 de 2021), ARL y COPASST/vigía.
- Trabajo eléctrico: cinco reglas de oro (Res. 5018 de 2019), distancias del RETIE, EPP de arco (NFPA 70E solo como referencia técnica), PTE y LOTO según NES-SST-PR-001.
- Energización condicionada a dictamen RETIE y a la secuencia de NES-OPE-PR-023; liberación de caja no equivale a autorización.
- Orientación y sombreado adaptados a la latitud colombiana (sol cercano al cenit) en lugar de "orientación norte" de guías del hemisferio norte.
- Clima: tormenta eléctrica, lluvia, calor, ofidios; humedad y salinidad de costa.
- Ambiente: Res. 2184 de 2019, RESPEL (Decreto 1076 de 2015), RAEE (Ley 1672 de 2013), RCD (Res. 0472/2017 mod. 1257/2021).
- Unidades SI, decimales con coma, fechas dd-mm-aaaa; pulgadas y lb·in de las fuentes convertidas o descartadas.

## Pendientes de verificar

- Torques de portafusibles, barras, seccionador, DPS, prensaestopas y tierra: dependen del manual de la caja del proyecto.
- Rango de inclinación, temperatura de almacenamiento y de operación de la caja: valores típicos tomados de un fabricante.
- Altura de montaje 1,5–2,0 m: referencia de guías; manda el plano.
- Longitud y sección del conductor de tierra del DPS (0,5 m y 6 mm²): referencia técnica; confirmar con el diseño del SIPRA y el fabricante.
- Criterio de continuidad de tierra de la caja y criterio interno de ±5% de Voc (heredado de NES-OPE-PR-014).
- Muestreo de torque (10% de cajas y 100% de principales) y frecuencia de inspección de bodega: criterios internos a confirmar por QA/QC.
- Confirmar en la edición vigente de IEC 62446-1 la tabla de aislamiento para sistemas de 1.500 V.
