# Fuentes — NES-OPE-PR-022 Procedimiento de Pruebas y Comisionado del Generador FV

> Limitación de la investigación (01-10-2026): en esta sesión el proxy de salida bloqueó WebFetch para todos los dominios que se probaron (datatec.es, mayfield.energy, fluke.com, aerialaccuracy.com, iea-pvps.org, cdn.standards.iteh.ai, sis.se), así que no se abrieron las páginas completas. El contenido se tomó de los resúmenes del buscador (WebSearch) de las URL que siguen. Los valores normativos se contrastaron entre al menos dos resultados cuando fue posible. Antes de publicar se debe verificar contra la copia oficial de IEC 62446-1 (ed. 1.1 consolidada 2018) e IEC TS 62446-3:2017.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Insulation Resistance Testing (IRT) in solar installations | Fabricante de instrumentos (blog técnico) | s. f. | https://www.fluke.com/en-us/learn/blog/renewable-energy/insulation-resistance-testing-in-solar | Tabla de IEC 62446-1: tensión de ensayo de 250/500/1.000 V y mínimos de 0,5/1/1 MΩ. |
| Insulation Resistance Testing Explained | Consultora de ingeniería FV | s. f. | https://www.mayfield.energy/technical-articles/insulation-resistance-testing-explained/ | Métodos 1 y 2 del ensayo de aislamiento; secuencia y seguridad. |
| Standards and regulations for the design, construction... | Fabricante de instrumentos (guía normativa) | 2024 | https://www.ht-instruments.it/media/filer_public/b9/95/b9952542-de2e-40f3-92e7-d0922bce1144/ht_normative_03_2024_en1-00web.pdf | Confirmación de la tabla de aislamiento y del régimen de ensayos. |
| IEC 62446-1 PV Systems (guía de aplicación) | Fabricante de instrumentos / pv magazine | 2024 | https://www.pv-magazine.com/wp-content/uploads/2024/04/Fluke_FINAL_May-2024.pdf | Comparación de Voc entre strings idénticos (típicamente dentro del 5 %); comparación de corrientes; ensayos adicionales. |
| Maintenance of solar PV systems according to IEC 62446-1 | Fabricante de instrumentos | s. f. | https://www.hioki.com/us-en/learning/common-devices/PV-test-standard.html | Contenido de las categorías 1 y 2 y orden de ensayos. |
| IEC 62446-1:2016/AMD1:2018 (ficha de catálogo) | iTeh Standards / IEC | 2018 | https://standards.iteh.ai/catalog/standards/iec/19962756-e089-492c-a4a6-b5d256f6a05a/iec-62446-1-2016-amd1-2018 | Alcance de la enmienda 1: tabla de mínimos de aislamiento (rango "500 a 1.000"), ensayo por subarreglos en arreglos grandes. |
| IEC 62446-1 Ed. 1.1 consolidada (vista previa) | IEC | 2018 | https://www.normsplash.com/Samples/IEC/295735436/IEC-62446-1-2016-AMD1-2018-CSV-en-fr.pdf | Estructura de la norma, ensayos adicionales (aislamiento en húmedo, diodos de bloqueo, tensión a tierra). |
| Commissioning for PV Performance — Best Practice Guide | SunSpec Alliance | 2022 | https://www.solmetric.com/wp-content/uploads/2022/11/SunSpec_commissioning_guidelines.pdf | Buenas prácticas de comisionado: comparación entre strings, curva I-V, ensayo de caja combinadora. |
| IEC 62446-1 Summarized | Proveedor de software FV | s. f. | https://help.illu.works/best-practices/examples/iec-62446-1-summarized | Lista de ensayos de categoría 1, 2 y adicionales. |
| Curve Tracing FAQ's | Fabricante de instrumentos | s. f. | https://www.seaward.com/gb/support/solar/faqs/29495-curve-tracing-faq-s/ | Curva I-V: irradiancia estable mínima de 400 W/m² (IEC 62446-1); 700 W/m² recomendado para trasladar a STC (IEC 61829); traslado con IEC 60891. |
| Performance evaluation of IEC 60891:2021 procedures | Progress in Photovoltaics (Wiley) | 2023 | https://onlinelibrary.wiley.com/doi/full/10.1002/pip.3652 | Limitaciones de los procedimientos de traslado de curvas I-V. |
| IEC TS 62446-3 Ed. 1.0 (vista previa) | IEC | 2017 | https://webstore.ansi.org/preview-pages/iec/preview_iec62446-3%7Bed1.0%7Den.pdf | Inspección simplificada y detallada; calificación ISO 9712 (nivel 1 y nivel 2). |
| Understanding IEC 62446-3:2017 | Empresa de inspección | s. f. | https://www.abovesurveying.com/blog/understanding-iec-62446-32017-outdoor-infrared-thermography | Condiciones: 600 W/m², estado estable (esperar 15 min tras un cambio mayor del 10 %/min), nubosidad de 2 octas o menos, viento de 4 Bft o menos. |
| IEC 62446-3 (resumen) | Proveedor de inspección con dron | s. f. | https://mapperx.com/en/iec-62446-3/ | Viento máximo de 28 km/h; irradiancia mínima de 600 W/m². |
| IEC TS 62446-3 Thermal Methodology | Empresa de inspección | s. f. | https://aerialaccuracy.com/resources/iec-62446-3-methodology | Requisitos de cámara: NETD de 0,1 K o menos a 30 °C; 5 × 5 píxeles por célula; error absoluto de ±2 K. |
| Solar Thermography Inspection to IEC 62446-3 | Empresa de inspección | s. f. | https://sinovoltaics.com/field-inspection-services/pv-field-inspection/thermography/ | Clases de anomalía CoA 1, 2 y 3. |
| Review on IR and EL Imaging for PV Field Applications | IEA PVPS Task 13 | 2020 | https://iea-pvps.org/wp-content/uploads/2020/01/Review_on_IR_and_EL_Imaging_for_PV_Field_Applications_by_Task_13.pdf | Contexto técnico de la termografía en campo y de los ΔT de módulos en circuito abierto (2 a 7 K). |
| Documentación del sistema según IEC 62446-1 | iTeh Standards / pv magazine | 2016 / 2024 | https://standards.iteh.ai/catalog/standards/iec/3f2bbcff-b79d-40c8-b45f-c189131eb414/iec-62446-1-2016 | Contenido del dossier: datos del sistema, unifilar, plano de strings (3 o más strings), fichas técnicas, O&M, resultados de ensayos. |

## Ajustes para Colombia

- Las referencias a NEC 690 de las guías de EE. UU. se sustituyeron por el RETIE (Res. 40117 de 2024) y la NTC 2050, artículo 690, en lo que el RETIE adopta.
- Los roles de "PV installer" y "qualified person" pasaron a técnico electricista con matrícula CONTE (Ley 1264 de 2008), que ejecuta, e ingeniero con matrícula COPNIA (Ley 842 de 2003), que firma. Al termógrafo se le exige la certificación ISO 9712 que pide la IEC TS 62446-3.
- La seguridad del ensayo se tomó de las guías de fabricantes y se aterrizó a las cinco reglas de oro de la Res. 5018 de 2019, al PTE y al LOTO de NES-SST-PR-001, y a EPP con categoría de arco (NFPA 70E como referencia técnica).
- Se añadió el dictamen de inspección RETIE y la autorización escrita de energización (NES-OPE-PR-023, [OPERADOR DE RED] y XM) como condición previa a los ensayos con inversor operando.
- Inspección aérea: se remite a la reglamentación de la Aeronáutica Civil de Colombia para aeronaves no tripuladas.
- Clima: tormenta eléctrica, lluvia y rocío (que invalidan el ensayo de aislamiento) y estrés térmico (los ensayos de corriente, I-V y termografía exigen alta irradiancia).
- Ambiente: Res. 2184 de 2019, RESPEL (Decreto 1076 de 2015), RAEE (Ley 1672 de 2013), agua del ensayo en húmedo según el PMA.
- Emergencias: línea 123, ARL, Res. 1401 de 2007 y NES-SST-PLN-001.
- Unidades SI y decimales con coma; viento en km/h.

## Pendientes de verificar

- Tensión de ensayo de aislamiento y valor mínimo para sistemas de 1.500 V y para arreglos grandes. La tabla de la ed. 1.1 cubre hasta 1.000 V, y no se pudo confirmar si la enmienda incluye un criterio por área. Quedó como [____] en el documento.
- Tolerancia de comparación de corriente entre strings. Las fuentes discrepan (±5 % frente a ±10 %); se dejó el 5 % como criterio interno, marcado como tal.
- Ángulo de observación de la cámara en IEC TS 62446-3. Una fuente lo da como mínimo de 30° respecto de la superficie, pero no se confirmó, así que se dejó como "verificar en la edición vigente".
- Umbrales de ΔT de la matriz de anomalías de IEC TS 62446-3: no se reprodujeron; se remite a la matriz de la norma.
- Criterio de aceptación de Pmax trasladada a STC y del factor de forma: lo fija la especificación del proyecto.
- Límite de resistencia de continuidad de protección: lo fija la especificación del proyecto.
- Condiciones de ensayo de aislamiento admitidas por el inversor, la caja combinadora y los DPS del proyecto: dependen del manual del fabricante.
