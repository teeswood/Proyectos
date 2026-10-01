# Catálogo de fuentes públicas en internet — Procedimientos y guías para plantas solares FV utility-scale con trackers

**Proyecto:** Neptuno — insumo para redactar procedimientos propios aterrizados a Colombia
**Fecha de la investigación:** 1 de octubre de 2026
**Método:** búsqueda web (WebSearch). **Limitación importante:** el proxy de salida de este entorno bloqueó la descarga directa (WebFetch) de todos los dominios que se probaron (nrel.gov/nlr.gov, solarpowereurope.org, minenergia.gov.co, alcaldiabogota.gov.co, funcionpublica.gov.co, fluke.com, datatec.es, physicsnorm.com, mayfield.energy). Por eso, **ninguna URL se abrió y leyó completa**. La existencia de cada URL se comprobó porque aparece indexada en los resultados del buscador con título y fragmento coherentes. Los valores técnicos se tomaron de fragmentos indexados de la fuente primaria (manual o norma) o, cuando se indica, de fuentes secundarias que coinciden entre sí. Antes de convertir cualquier valor en criterio contractual o de aceptación hay que contrastarlo con el documento original (ver sección 5).

Convenciones de la columna «Verif.»:
- **V-idx**: URL que existe (indexada con título correcto) pero no se abrió.
- **V-sec**: contenido confirmado solo por fuentes secundarias concordantes.
- **NV**: no verificado.

---

## 1. Resumen

- **Marcos de buenas prácticas de referencia** (gratuitos):
  - SolarPower Europe: O&M v6.0 (feb-2025), EPC v3.0 (incluye híbridos FV+BESS) y Asset Management.
  - NREL/SunSpec: O&M Best Practices, 3.ª ed. (2018), y SAPC Best Practices in PV System Installation (2015).
  - IFC: Utility-Scale Solar PV Developer's Guide (2015) y EHS Guidelines.
  - IEA-PVPS Task 13: fallas de módulos e inspección IR/EL.
  - IRENA: fin de vida de módulos (actualización de jul-2026).
  - Ministerio de Energía de Chile/GIZ: Guía de O&M FV y Guía de buenas y malas prácticas.
  - IDAE (España): Pliego de Condiciones Técnicas PCT-C-REV 2011.
- **Pruebas de puesta en marcha:**
  - IEC 62446-1:2016+AMD1:2018. Categoría 1: inspección visual, continuidad de tierras, polaridad, Voc, Isc, prueba funcional y aislamiento. Categoría 2: curva I-V e inspección IR.
  - IEC TS 62446-3:2017 (termografía): ≥600 W/m², viento ≤28 km/h y ≤2 octas de nubes.
  - ASTM E2848: prueba de capacidad con irradiancia ≥400 W/m².
  - IEC 62446-2:2020: mantenimiento.
- **Normativa colombiana: hay cambios recientes que se deben incorporar.**
  - El **RETIE** vigente es la **Res. 40117 de 2024, modificada por la Res. 40284 del 23-jun-2026** (D.O. 53.539 del 1-jul-2026), que modificó los Libros 1 a 4 y los anexos.
  - El título de **RESPEL del Decreto 1076/2015 fue modificado por el Decreto 0766 del 15-jul-2026**.
  - La **Res. 1843 de 2025** (evaluaciones médicas ocupacionales) derogó la Res. 2346 de 2007.
  - La **Res. 5018 de 2019** derogó la Res. 1348 de 2009.
  - La **Res. 4272 de 2021** derogó las Res. 1409/2012, 1903/2013, 3368/2014, 1178/2017 y 1248/2020.
- **Vacío normativo:** en Colombia, los módulos FV no tienen un esquema de responsabilidad extendida del productor (REP) específico. Se gestionan bajo el marco general de RAEE (Ley 1672/2013, Decreto 284/2018 y Res. 851/2022). Si contienen sustancias peligrosas, también aplica RESPEL.
- **Fabricantes con manuales públicos:**
  - Módulos: LONGi, Jinko, Trina y First Solar.
  - Inversores: SMA, Huawei, Sungrow e Ingeteam.
  - Trackers: Nextracker y Array.
  - Conectores: Stäubli MC4.
  - Cables: Prysmian y Southwire.
- **Temas sin buena fuente pública abierta:**
  - Los procedimientos internos de Ecopetrol, ISA y EPM no se publican, salvo algunas normas técnicas de EPM (RA6/RA8).
  - No existe una guía UPME específica de construcción de plantas utility-scale.
  - IEC 62446-1, IEC TS 62446-3, IEEE 81, IEEE 400.2, NFPA 70E y NTC 2050/4552 son normas de pago. Solo se accedió a fragmentos y resúmenes.

---

## 2. Catálogo por tema

### 2.1 Marcos generales: EPC, construcción y desarrollo

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia (qué ajustar) | Verif. |
|---|---|---|---|---|---|---|---|
| EPC / construcción | Engineering, Procurement & Construction Best Practice Guidelines v3.0 | SolarPower Europe | v3.0 (2025-2026), con capítulo FV+BESS | https://www.solarpowereurope.org/insights/thematic-reports/engineering-procurement-and-construction-best-practice-guidelines-version-3-0 | Calidad EPC, gestión de riesgos, HSE, seguridad eléctrica, pruebas de aceptación (PAC/FAC) y híbridos con BESS | Sustituir las referencias normativas de la UE por RETIE, NTC 2050 y Res. 5018. Integrar la licencia ANLA/CAR y los requisitos de conexión CREG 075/UPME | V-idx |
| EPC | EPC Best Practice Guidelines v2.0 (PDF) | SolarPower Europe | v2.0 | https://api.solarpowereurope.org/uploads/EPC_Best_Practice_Guidelines_V_2_0_ea4d7d3bc5.pdf | Versión anterior descargable sin formulario: pruebas de comisionado, PR test y responsabilidades | Igual que la anterior | V-idx |
| EPC | EPC Best Practice Guidelines v1.0 (PDF) | SolarPower Europe | v1.0 | https://api.solarpowereurope.org/uploads/EPC_Best_Practice_Guidelines_V1_0_88e0654756.pdf | Línea base | Histórico | V-idx |
| EPC regional | EPC Guidelines Sub-Saharan Africa v1.0 | SolarPower Europe | mar-2022 | https://www.digital-energy.eu/sites/default/files/2024-03/SPE_EPC_Africa_Guidelines_v1_0_March_2022_132f552916.pdf | Adaptación a mercados emergentes (logística, clima, mano de obra local) | Útil como modelo de «aterrizaje» a un país no europeo | V-idx |
| Plataforma | Solar Best Practices (EPC, O&M, AM, Lifecycle Quality) | SolarPower Europe | en línea | https://solarbestpractices.com/guidelines/detail/foreword | Versión web navegable por capítulo | — | V-idx |
| Desarrollo | Utility-Scale Solar Photovoltaic Power Plants: A Project Developer's Guide | IFC (Grupo Banco Mundial) | 2015 (2.ª ed., 208 p.) | https://www.ifc.org/wps/wcm/connect/topics_ext_content/ifc_external_corporate_site/sustainability-at-ifc/publications/publications_utility-scale+solar+photovoltaic+power+plants | Ciclo completo: sitio, diseño, rendimiento, permisos, contratos EPC/O&M, construcción, comisionado y financiación | Cambiar el marco de permisos por ANLA/CAR, UPME, CREG y el operador de red | V-idx |
| Desarrollo | Utility Scale Solar Power Plants: A Guide for Developers and Investors (India) | IFC | 2012 | https://documents1.worldbank.org/curated/en/868031468161086726/pdf/667620WP00PUBL005B0SOLAR0GUIDE0BOOK.pdf | 1.ª edición, con enfoque en la India | Histórico | V-idx |
| Instalación | SAPC Best Practices in PV System Installation v1.0 | NREL (SAPC WG) | mar-2015, NREL/SR-6A20-63234 | https://docs.nrel.gov/docs/fy15osti/63234.pdf | Calificación de contratistas, diseño, inspecciones y documentación | Pensado para EE. UU. (NEC). Mapear a NTC 2050 (basada en NEC 2017) | V-idx |
| Especificación técnica | Pliego de Condiciones Técnicas de Instalaciones Conectadas a Red PCT-C-REV | IDAE (España) | jul-2011 | https://www.idae.es/sites/default/files/documentos_5654_FV_pliego_condiciones_tecnicas_instalaciones_conectadas_a_red_C20_Julio_2011_3498eaaf.pdf | Condiciones mínimas de componentes, montaje, recepción y pruebas, en español | Referenciar RETIE y NTC en lugar del REBT | V-idx |
| Buenas prácticas | Guía de buenas y malas prácticas de instalaciones fotovoltaicas | Min. Energía Chile / GIZ (Programa Techos Solares Públicos) | 2017 | https://techossolares.minenergia.cl/wp-content/uploads/2017/02/Guia-de-buenas-y-malas-practicas-de-instalaciones-fotovoltaicas.pdf (copia en sec.cl) | Ejemplos fotográficos de errores de montaje, cableado, conectores y puesta a tierra | Útil para capacitación de cuadrillas. Escala menor | V-idx |
| Norma de diseño y ejecución | Instrucción Técnica RGR N.º 02/2020 (FV conectada a red de distribución) | SEC Chile | 2020 v5 | https://www.sec.cl/sitio-web/wp-content/uploads/2020/11/RGR-N-02-2020-v5-1.pdf | Requisitos de ejecución, puesta a tierra (fuente secundaria: ≤20 Ω, excepciones hasta 80 Ω) e inspección | Solo referencial. En Colombia rige el RETIE | V-idx |
| Pruebas (Arabia) | SEC Inspection and Testing Guidelines (Solar PV) | Saudi Electricity Co. | v2 | https://www.se.com.sa/-/media/sec/Sustainability/Solar-PV/ProceduresandGuides/6-SEC--Inspection-and-Testing-Guidelinesv2Clean.ashx | Guía de inspección y ensayos alineada con IEC 62446 | Referencial para formatos de protocolo | V-idx |
| Riesgo de incendio | FM Global DS 7-106 Ground-Mounted Solar PV Power | FM Global | oct-2012, rev. interina abr-2026 | https://www.fm.com/-/media/project/publicwebsites/fmglobal/documentum-new/data-sheet-individual/07-hazards/fmds07106.pdf | Prevención de pérdidas: viento, granizo, incendio, vegetación, inspección y pruebas | Útil si el asegurador exige criterios FM | V-idx |

### 2.2 Comisionado, pruebas y aceptación

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| Comisionado DC | IEC 62446-1:2016+AMD1:2018 (Ed. 1.1) Documentación, pruebas de puesta en marcha e inspección | IEC | 2016 / AMD1 2018 | Muestra: https://cdn.standards.iteh.ai/samples/20417/687a20e1bdfd42c4aef96348958655ad/IEC-62446-1-2016.pdf · Catálogo: https://standards.iteh.ai/catalog/standards/iec/19962756-e089-492c-a4a6-b5d256f6a05a/iec-62446-1-2016-amd1-2018 | Secuencia de pruebas Cat. 1 y 2 y tabla de aislamiento (ver §3.1) | Norma de pago: comprar el original. Complementar con la inspección RETIE (dictamen) | V-idx (solo muestra) |
| Mantenimiento | IEC 62446-2:2020 Maintenance of PV systems | IEC | 2020-03-18 | https://webstore.iec.ch/en/publication/27382 | Mantenimiento preventivo, correctivo y orientado al desempeño. Limpieza y vegetación | Base para el plan de O&M | V-idx |
| Termografía | IEC TS 62446-3:2017 Outdoor infrared thermography | IEC | Ed. 1.0 2017-06 | Muestra: https://cdn.standards.iteh.ai/samples/22683/4de66fa53f2c4b8591ebe1672331acb4/IEC-TS-62446-3-2017.pdf | Condiciones mínimas y clases de anomalía (ver §3.1) | Considerar la nubosidad tropical: programar ventanas de medición | V-idx (muestra) |
| IR/EL | Review on Infrared and Electroluminescence Imaging for PV Field Applications (T13-10:2018) | IEA-PVPS Task 13 | 2018 | https://iea-pvps.org/wp-content/uploads/2020/01/Review_on_IR_and_EL_Imaging_for_PV_Field_Applications_by_Task_13.pdf | Requisitos de ensayo, registro y análisis IR/EL en campo | Directa | V-idx |
| Fallas | Review of Failures of PV Modules (T13-01:2014) | IEA-PVPS | 2014 | https://iea-pvps.org/wp-content/uploads/2020/01/IEA-PVPS_T13-01_2014_Review_of_Failures_of_Photovoltaic_Modules_Final.pdf | Catálogo de fallas, curvas I-V como diagnóstico y métodos IR | Directa | V-idx |
| Fallas | Assessment of PV Module Failures in the Field (T13-09:2017) | IEA-PVPS | 2017 | https://iea-pvps.org/wp-content/uploads/2017/09/170515_IEA-PVPS-report_T13-09-2017_Internetversion_2.pdf | Evaluación de severidad de fallas | Directa | V-idx |
| Fallas | PV Failure Specification — Degradation and Failure (T13-30:2025) | IEA-PVPS | 2025 | https://iea-pvps.org/wp-content/uploads/2025/02/IEA-PVPS-T13-30-2025-PVFS-ANNEX-Degradation-and-Failure.pdf | Fichas de fallas actualizadas (2024) | Directa | V-idx |
| Aceptación desempeño | Commissioning for PV Performance — Best Practice Guide | SunSpec Alliance | s. f. | https://www.solmetric.com/wp-content/uploads/2022/11/SunSpec_commissioning_guidelines.pdf | Pruebas de aceptación de desempeño durante el primer año | Ajustar a los contratos PPA colombianos | V-idx |
| O&M / aceptación | SAND2014-19432 (O&M y aceptación de sistemas FV comerciales y utility) | Sandia | nov-2014 | https://www.osti.gov/servlets/purl/1324303 | Estándares y prácticas de O&M y aceptación | Directa | V-idx |
| Capacidad | ASTM E2848 (prueba de capacidad), ejemplo de reporte | ASTM (resumen por terceros) | E2848-13 (reaprob. 2023) | https://heliotest.com/resources/article/sample-astm-e2848-capacity-test-report | Excluye datos <400 W/m². Criterio típico de contrato: medido/esperado ≥97 % (depende de la incertidumbre) | Norma de pago. El umbral de aceptación lo define el contrato EPC | V-sec |
| Pruebas cable MT | On Site Testing Guidelines for MV Cables | Prysmian UK | 2019 | https://uk.prysmian.com/sites/uk.prysmian.com/files/media/documents/On%20Site%20Testing%20Guidelines%20(2019)%20(3).pdf | Pruebas de cable MT tras la instalación (VLF, DC, cubierta) | Directa | V-idx |
| Pruebas cable MT | IEEE 400.2 (VLF): artículo NETA de aceptación y mantenimiento de cables MT | NETA World Journal | 2020 | https://netaworldjournal.org/2020/09/thomasdsandri/features/acceptance-and-maintenance-testing-medium-voltage-electrical-power-cables/ | Resumen de pruebas VLF y PD | IEEE 400.2 es de pago | V-idx |
| Pruebas transformador | IEEE C57.152-2013 Diagnostic Field Testing of Fluid-Filled Power Transformers | IEEE | 2013 | https://store.accuristech.com/standards/ieee-c57-152-2013?product_id=1859951 | Relación de transformación ±0,5 %, IR, PI, tan δ y resistencia de devanados (ver §3) | Norma de pago | V-sec |
| Fibra óptica | Corning AEN135 Fiber Optic System Testing Tutorial y LAN-1561 Test Guidelines | Corning | s. f. | https://www.corning.com/catalog/coc/documents/application-engineering-notes/AEN135.pdf | Pruebas Tier 1 (pérdida/OLTS) y Tier 2 (OTDR). Presupuesto de pérdidas | Aplicable a la red SCADA de la planta | V-idx |

### 2.3 Inversores, centros de transformación y SCADA

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| Inversor central / MVPS | System Manual Medium Voltage Power Station (varios) | SMA | varias | https://files.sma.de/downloads/MVPS-S2-SCS-US-B8-SH-en-11.pdf ; https://files.sma.de/downloads/SCCPXT-E7-BA-en-58.pdf | Recepción, izaje, conexión MT, comisionado, tolerancia de tensión de suministro (fragmento: −10 %/+15 %) y mantenimiento | Usar el manual exacto del modelo comprado | V-idx |
| Inversor string | SUN2000-(250/280/300/330KTL) User Manual Issue 12 | Huawei | 2024-03-20 | https://ske-solar.com/productdata/SUN2000-H1/02_Manuals/SUN2000-%28250KTL%2C%20280KTL%2C%20300KTL%2C%20330KTL%29%20User%20Manual_2024-03-20_V12_EN.pdf | Instalación, comisionado y localización de fallas de aislamiento | Ídem | V-idx |
| Inversor string | SG320HX/SG350HX User Manual | Sungrow | s. f. | https://quantumsolarpv.de/wp-content/uploads/2023/02/SUNGROW-SG320_350HX-User-Manual-en.pdf | Instalación, conexión y mantenimiento | Ídem | V-idx |
| Inversor central | Ingecon Sun Power Installation Manual | Ingeteam | s. f. | https://www.ingeteam.com/Portals/0/Catalogo/Producto/Documento/PRD_1812_Archivo_is-power-installation-manual.pdf | Recepción, instalación, arranque y mantenimiento | Ídem | V-idx |
| Power Electronics | Manuales HEM/FS | Power Electronics | — | (no encontrado en búsqueda pública) | — | Solicitar al proveedor | NV |
| Monitoreo | IEC 61724-1:2021, resumen de clases de monitoreo | Kipp & Zonen/OTT HydroMet (hukx.com) | 2021 | https://www.hukx.com/uploads/iec-61724-1_2021-version-selection-of-pyranometers.pdf | Clase A para utility. Piranómetros ISO 9060:2018 clase A. Calibración recomendada cada 1 año (>2 años implica riesgo significativo) | Directa para la estación meteorológica de la planta | V-sec |

### 2.4 Trackers y estructura

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| Tracker 1 eje | NX Horizon Installation Manual (PDM-000176, 2.4.1 Short Rail) | Nextracker | Rev. B/C/E | Solo en terceros (Scribd/vbook). Ejemplo de anexo en expediente público: https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7B6401C5F1-42FF-4E07-BDBE-68068086C1CF%7D | Fragmentos: slew drive M20 a 240 N·m; motor/antena 60 N·m; U-bolt SPC 20 N·m; tolerancia ±10 % en todos los torques | **Usar exclusivamente el manual oficial entregado por Nextracker para el proyecto.** Los torques dependen de la revisión | V-sec |
| Tracker | DuraTrack HZ v3: hoja técnica / O&M Guide Rev B | Array Technologies | 2020 | https://www.aes.com/sites/vault/files/2025-04/Appendix%202-2.%20Array%20Technologies%20DuraTrack%C2%AE%20HZ%20v3%20Tracking%20System%20Specification%20Sheet.pdf | Datos técnicos. La guía O&M solo está en Scribd | Pedir el manual al fabricante | V-idx |

### 2.5 Módulos: recepción, almacenamiento, instalación y limpieza

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| Recepción/almacén | PV Module Unpacking, Handling and Storing Guide v16 | LONGi | v16 | https://static.longi.com/LON_Gi_PV_Module_Unpacking_Handling_and_Storing_Guide_v16_de1d7accd2.pdf | Almacenar en sitio ventilado, seco y bajo techo. No desempacar para almacenamiento prolongado. Apilar según el marcado del pallet. Prohibido cargar el módulo por la caja de conexiones o los cables | Lluvias intensas y alta humedad (Caribe, Llanos): cubrir y drenar | V-idx |
| Mantenimiento/limpieza | LONGi Maintenance Manual V2.0 | LONGi | V2.0 | https://static.longi.com/LON_Gi_Maintenance_Manual_V2_0_EN_43815b2263.pdf | Agua, presión y temperatura (ver §3.3) | Directa | V-idx |
| Limpieza | LONGi PV Modules Cleaning Work Instruction | LONGi | s. f. | https://inergion.com/wp-content/uploads/2022/10/LONGi-PV-Modules-Cleaning-Work-Instruction.pdf | Instructivo específico de limpieza | Directa | V-idx |
| Instalación | JinkoSolar Global Installation Manual A1.5 | JinkoSolar | 2025-06 | https://jinkosolarcdn.shwebspace.com/uploads/JinkoSolar%20Global%20Installation%20Manual_202506_A1.5.pdf | Instalación, puesta a tierra y limpieza (ver §3.3) | Directa | V-idx |
| Instalación | JinkoSolar Installation Manual A1 | JinkoSolar | 2024-08-14 | https://www.jinkosolar.com/uploads/JinkoSolar%20Global%20Installation%20Manual_20240814_A1.pdf | Ídem | Ídem | V-idx |
| Instalación | Vertex Series User Manual UM-M-0002 rev. N (y rev. L ago-2024) | Trina Solar | rev. N | https://www-cdn.trinasolar.com/wwwstorage/sites/16/UM-M-0002-N_Trinasolar_Vertex_Series_User_Manual_Clean_EN.pdf | Calidad de agua y presión para limpieza (ver §3.3) | Directa | V-idx |
| Instalación/limpieza | Series 6 Plus / CuRe User Guide | First Solar | s. f. | https://www.firstsolar.com/-/media/first-solar/technical-documents/user-guides/series-6-user-guide.ashx?la=en | Limpieza de noche, EPP aislante y agua (ver §3.3) | Directa | V-idx |
| Limpieza | Module Cleaning Guidelines (Series 4) | First Solar | 2017 | https://www.firstsolar.com/-/media/First-Solar/Technical-Documents/Series-4-Application-Note/Module-Cleaning-Guidelines.ashx?la=en | Guía de limpieza dedicada | Directa | V-idx |

### 2.6 Conectores, cables y tendido

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| Conectores DC | MC4 Assembly Instructions MA231 (PV-KST4/PV-KBT4…-UR) | Stäubli | rev. vigente | https://www.staubli.com/content/dam/spot/PV_MA231-en.pdf | Pelado, crimpado con herramienta PV-CZM, ensamble y torque de la tuerca del prensaestopas (ver §3.4) | Directa. Exigir herramienta calibrada | V-idx |
| Cruce de conectores | Avoid cross-mating / Product Liability Statement | Stäubli | — | https://www.staubli.com/global/en/electrical-connectors/industries/renewable-energy/cross-connection.html ; https://www.staubli.com/content/dam/ecs/pictures/solar-photovoltaics/Statement_PV_Connector_ProductLiability.pdf | Prohíbe acoplar con conectores de otros fabricantes: se pierde la certificación IEC/UL y la garantía | Criterio de inspección obligatorio | V-idx |
| Cable MT | Installation — Bending Radii (Prysmian UK) | Prysmian | s. f. | https://uk.prysmian.com/sites/uk.prysmian.com/files/media/documents/Installation%20Bending%20Radii.pdf | Radios de curvatura de instalación | Usar la ficha del cable comprado | V-idx |
| Cable MT | Installation Pulling Tensions & Side Wall Pressures | Prysmian UK | s. f. | https://uk.prysmian.com/sites/uk.prysmian.com/files/media/documents/Installation%20Pulling%20Tensions%20&%20Side%20Wall%20Pressures%20(1).pdf | Tensión máxima de tiro y presión lateral | Ídem | V-idx |
| Cable | Underground / Buried Cable Installation Practices (Install 04/05) | Prysmian NA | Iss. 3 | https://na.prysmian.com/sites/na.prysmian.com/files/media/documents/Install%2005%20Underground%20Cable%20Installation%20Practices%20Iss%203.pdf | Prácticas de tendido directamente enterrado y en ductos | Directa | V-idx |
| Cable | Guideline for Laying of Cables and Installation of Sleeves | Prysmian | s. f. | https://www.prysmian.com/sites/default/files/atoms/files/Guideline-for-Laying-Cables-and-Installation-of-Sleeves.pdf | Temperaturas mínimas de tendido, radios y tensiones | Directa | V-idx |
| Cable | Southwire Power Cable Manual / Power Cable Installation Guide | Southwire | s. f. | https://www.southwire.com/medias/PowerCableInstallGuidepdf.pdf (URL con token) | Tiro máximo 0,008 lb/cmil (Cu) y presión lateral (ver §3.4) | Unidades imperiales: convertir | V-sec |
| Radio de curvatura | Training and Minimum Bending Radius (Southwire) | Southwire | s. f. | https://www.southwire.com/medias/SW-1003583-Training-and-Minimum-Bend-Radius-Technical-Document-LO.pdf (URL con token) | Radios mínimos por tipo de cable (NEC 300.34) | NTC 2050 se basa en NEC 2017 | V-sec |

### 2.7 O&M, limpieza y vegetación

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| O&M | Operation & Maintenance Best Practice Guidelines v6.0 | SolarPower Europe | 18-feb-2025 | https://www.solarpowereurope.org/insights/thematic-reports/operation-and-maintenance-best-practice-guidelines-version-6-0-1 | Capítulos nuevos de seguridad eléctrica y de pruebas e inspecciones comunes. Fin de vida en repotenciación. KPI y contratos | Descarga con formulario | V-idx |
| O&M | O&M Best Practice Guidelines v5.0 | SolarPower Europe | dic-2021 | https://www.solarpowereurope.org/insights/thematic-reports/o-and-m-best-practice-guidelines-version-5-0 | Versión anterior | — | V-idx |
| O&M | Best Practices for O&M of PV and Energy Storage Systems, 3rd ed. (NREL/TP-7A40-73822) | NREL / Sandia / SunSpec | dic-2018 | https://sunspec.org/wp-content/uploads/2025/01/BestPracticesforOperationandMaintenanceofPhotovoltaicandEnergyStorageSystems3rdEdition.pdf (también https://docs.nlr.gov/docs/fy19osti/73822.pdf) | Plan de O&M, tareas e intervalos y costos; integra BESS | Directa (ajustar a la climatología local) | V-idx |
| O&M | SAPC Best Practices in PV Operations and Maintenance v1.0 | NREL | mar-2015 | https://my.solarroadmap.com//userfiles/Best-Practices-in-PV-Operations-and-Maintenance.pdf | Versión base | — | V-idx |
| O&M (es) | Guía de Operación y Mantenimiento de Sistemas Fotovoltaicos | Min. Energía Chile / GIZ (NAMA) | 2018 | https://techossolares.minenergia.cl/wp-content/uploads/2018/11/Guia-OM-FV.pdf | Tareas y estrategias de O&M, en español | Escala autoconsumo, pero los procedimientos se pueden adaptar | V-idx |
| O&M (es) | Manual de O&M para parques FV (tesis EPN, Ecuador) | Escuela Politécnica Nacional | s. f. | https://bibdigital.epn.edu.ec/bitstream/15000/10602/1/CD-6279.pdf | Plantillas de O&M en español | Académica | V-idx |
| Vegetación | Vegetation Management Cost and Maintenance Implications of Different Ground Covers at Utility-Scale Solar Sites (McCall et al.) | NREL | 2023 | https://docs.nlr.gov/docs/fy23osti/85418.pdf | Costos comparados: pasto, nativa y pastoreo ovino | Evaluar especies locales y el riesgo de incendio en época seca | V-idx |
| Vegetación | Solar Farm Grazing BMPs for Sheep | Maine DACF | ago-2021 | https://www.maine.gov/dacf/ard/resources/docs/solar-farm-grazing-best-management-practices-vfinal.pdf | Carga de 4 ovejas adultas/acre (≈10/ha) y pastoreo rotacional | Adaptar al ganado ovino/caprino local | V-idx |
| Vegetación | Conservation Guidance for Utility-Scale Solar Projects | USDA NRCS | dic-2024 | https://www.nrcs.usda.gov/sites/default/files/2025-04/Conservation-Guidance-for-Utility-Scale-Solar-Projects_2025415.pdf | Suelo y cobertura vegetal | Referencial | V-idx |

### 2.8 Seguridad (HSE)

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| Riesgo eléctrico FV | Green Job Hazards — Solar Energy: Electrical / Falls | OSHA | en línea | https://www.osha.gov/green-jobs/solar/electrical ; https://www.osha.gov/green-jobs/solar/falls | Peligros eléctricos (cubrir módulos con material opaco) y caídas (construcción ≥6 ft; industria general ≥4 ft) | En Colombia, el umbral de alturas es 2,0 m (Res. 4272/2021) | V-idx |
| LOTO | 29 CFR 1910.147 Control of Hazardous Energy | OSHA | vigente | https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147 | 6 pasos: preparación, apagado, aislamiento, bloqueo/etiqueta, energía almacenada, verificación | Integrar con las 5 reglas de oro y la Res. 5018/2019 | V-idx |
| Seguridad eléctrica | NFPA 70E-2024 Standard for Electrical Safety in the Workplace | NFPA | 2024 | Norma de pago. Resumen de cambios: https://www.ecmag.com/magazine/articles/article-detail/2024-nfpa-70e-update-major-changes-in-the-new-edition | Tabla 130.7(C)(15)(b) DC revisada (>150 V a <600 V). Protección auditiva obligatoria dentro de la frontera de arco | En Colombia la referencia legal es RETIE + Res. 5018. NFPA 70E aplica como buena práctica (ver §5) | V-sec |
| Trabajo en caliente | NFPA 51B-2024 / OSHA Fire Watch (OSHA 4188) | NFPA / OSHA | 2024 | https://www.osha.gov/sites/default/files/publications/OSHA4188.pdf | Radio de 35 ft (≈11 m) para combustibles. Vigía de incendio ≥60 min tras el trabajo (NFPA 51B-2024; OSHA: 30 min) | Incluir en el permiso de trabajo en caliente | V-sec |
| Izaje (es) | Izaje de cargas — Guía técnica especializada | Consejo Colombiano de Seguridad (CCS) | 2023 | https://ccs.org.co/wp-content/uploads/2023/06/GUIA_CCS_IZAJE_CARGAS.pdf | Plan de izaje, competencias y equipos (referencia ASME B30) | Colombia no tiene un reglamento nacional específico de izaje (ver §4) | V-idx |
| EHS | IFC EHS Guidelines: Electric Power Transmission and Distribution | IFC | 30-abr-2007 | https://www.ifc.org/content/dam/ifc/doc/2000/2007-electric-transmission-distribution-ehs-guidelines-en.pdf | Riesgos en construcción y operación de líneas y subestaciones | Exigible si hay financiación multilateral | V-idx |
| EHS | IFC General EHS Guidelines | IFC / Banco Mundial | 2007 | https://documents1.worldbank.org/curated/en/157871484635724258/pdf/112110-WP-Final-General-EHS-Guidelines.pdf | Generales (ruido, residuos, SST) | Ídem | V-idx |
| Riesgo eléctrico (es) | Plan de gestión del riesgo TT10 (Ecopetrol) | Ecopetrol | s. f. | https://www.ecopetrol.com.co/wps/wcm/connect/ecopetrolenergia/2e0d7f7a-0278-4ee4-9c37-e98528024ff2/TT10.+Plan+de+Gesti%C3%B3n+del+Riesgo.pdf?MOD=AJPERES&CVID=n-pR4L5 | Gestión de riesgos de un proyecto de transmisión | El manual MASE GHS-M-001 de Ecopetrol no está publicado | V-idx |
| Permisos de trabajo (es) | Procedimiento Permisos de Trabajo HSEQ-PR-001 v4 | OPAIN (Colombia) | v4 | https://www.opain.co/archivos/HSEQ-PR-001-PROCEDIMIENTO%20PERMISOS%20DE%20TRABAJO.pdf | Ejemplo colombiano de procedimiento de permisos (alturas, caliente, eléctrico, espacios confinados) | Plantilla de formato | V-idx |

### 2.9 Puesta a tierra y SPCR (rayos)

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| RETIE puesta a tierra | RETIE Libro 3 — Instalaciones (Art. 3.12.3 valores de referencia, Art. 3.12.4 mediciones) | MinEnergía | Res. 40117/2024, modificado por Res. 40284/2026 | https://www.minenergia.gov.co/documents/15921/Libro-3-Resolucion-40284-23-06-2026.pdf (versión 2024: https://www.minenergia.gov.co/documents/11566/4._Libro_3_-_Instalaciones.pdf) | Tabla 3.12.3.a, Wenner y caída de potencial al 61,8 % (ver §3.2) | Obligatoria | V-idx |
| Medición SPT | NC-RA6-014 Mediciones para el sistema de puesta a tierra | Grupo EPM (EDEQ / CENS / ESSA) | Rev. A / 2024 | https://www.edeq.com.co/Portals/0/clientes-y-usuarios/documentos/capitulo-8-normas-y-guias/NC-RA6-014MedicionesSPT_RevA.pdf ; https://www.essa.com.co/site/Portals/proveedores/ra6-014%20norma%20tecnica%20para%20medicion%20de%20resistividad%20de%20suelo%20y%20de%20resistencia%20del%20SPT.pdf?ver=2024-02-01-002403-983 | Procedimiento colombiano de medición de resistividad y resistencia de puesta a tierra | Directa (modelo de procedimiento) | V-idx |
| Diseño SPT | GM-04 Guía metodológica: cálculo del sistema de puesta a tierra | CENS / Grupo EPM | s. f. | https://www.cens.com.co/Portals/cens/institucional/Especificaciones/Documentos-en-revision/norma-tecnica/Guias-complementarias-de-dise%C3%B1o-grupo-EPM/GM-04-guia.pdf | Metodología de cálculo según IEEE 80 | Directa | V-idx |
| IEEE 81 | IEEE Std 81 Tutorial (handouts) | IEEE PES Substations Committee | s. f. | https://ewh.ieee.org/cmte/substations/sce0/wge6/IEEE%20Std%2081%20Tutorial%20Handouts.pdf | Métodos de medición (Wenner, caída de potencial) | Hay versión **IEEE 81-2025** (dic-2025) que reemplaza la de 2012: verificar cambios | V-idx |
| SPCR | NTC 4552-1/-2/-3 (2008) Protección contra descargas eléctricas atmosféricas | ICONTEC | 2008-11-26 | Norma de pago. Análisis comparativo: http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0123-921X2014000200009 | Adopción modificada de IEC 62305 (principios generales, gestión del riesgo, daño físico) | Obligatoria vía RETIE | V-sec |

### 2.10 Ambiental, residuos y fin de vida

| Tema | Título | Emisor | Año/versión | URL | Qué aporta | Aplicabilidad Colombia | Verif. |
|---|---|---|---|---|---|---|---|
| Fin de vida | End-of-Life Management for a Circular Economy: Solar PV Panels | IRENA | jul-2026 | https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/Jul/IRENA_POL_End-of-life_solar_PV_2026.pdf | Actualización del informe IRENA/IEA-PVPS de 2016 | Base para el plan RAEE de módulos rotos | V-idx |
| Reciclaje | End-of-Life Management of PV Panels: Trends in Recycling Technologies (T12-10:2018) | IEA-PVPS Task 12 | 2018 | https://iea-pvps.org/wp-content/uploads/2020/01/End_of_Life_Management_of_Photovoltaic_Panels_Trends_in_PV_Module_Recycling_Technologies_by_task_12.pdf | Tecnologías de reciclaje | Referencial | V-idx |
| EIA solar | Términos de referencia EIA para proyectos de energía solar FV (TdR-015, Res. 1670 de 2017) | ANLA / MinAmbiente | 2017 | https://www.anla.gov.co/documentos/normativa/terminos_referencia/anexo_tdr_solar_ajustado_26072017vf.pdf | Contenido del EIA. Fuente secundaria: DAA exigible para >10 MW | Directa (verificar umbrales vigentes de licenciamiento) | V-idx |
| Guía ambiental | Guía ambiental y social para proyectos de generación FV e híbridos ≤1 MW | MinAmbiente | s. f. | https://archivo.minambiente.gov.co/images/AsuntosambientalesySectorialyUrbana/pdf/Guia-ambiental-y-social-para-proyectos-de-generacion-fotovoltaicos-e-hibridos-menores-o-iguales-a-1-MW.pdf | Buenas prácticas ambientales por etapa | Escala ≤1 MW, pero las prácticas sirven como referencia | V-idx |
| Sostenibilidad | Recomendaciones de mejores prácticas para la sostenibilidad ambiental de instalaciones FV | UNEF (España) | 2020 | https://elperiodicodevillena.com/wp-content/uploads/2021/04/200129-UNEF-Recomendaciones-sostenibilidad-ambiental-instalaciones-fotovoltaicas-2.pdf (copia en tercero) | Biodiversidad, vallado permeable y suelo | Referencial | V-idx |
| RAEE paneles (es) | Gestión integral de residuos de paneles solares (trabajo de grado) | Uniagustiniana | s. f. | https://repositorio.uniagustiniana.edu.co/bitstreams/ec0a0b6c-211b-4454-ab63-f85d49c635dc/download | Señala el vacío normativo para módulos FV en Colombia | Contexto | V-idx |

### 2.11 Documentos de referencia de UPME y Colombia

| Tema | Título | Emisor | Año | URL | Qué aporta | Verif. |
|---|---|---|---|---|---|---|
| Requisitos técnicos | Generación solar fotovoltaica (UPME 570 IEB) | UPME / IEB | s. f. | https://bdigital.upme.gov.co/bitstream/handle/001/1395/Upme%20570%20IEB%20Generacion%20solar%20fotovoltaica.pdf?sequence=1&isAllowed=y | Estudio de requisitos técnicos de plantas solares | V-idx |
| Conexión | Documento técnico anexo, proyecto de resolución (Circular 037 de 2024, 5 MW) | MinEnergía / UPME | 2024 | https://docs.upme.gov.co/ServicioCiudadano/Documents/Proyectos_normativos/Documento_tecnico_anexo_proy_res_cir_037_2024_5MW.pdf | Proyecto normativo: verificar si quedó en firme | V-idx |
| Proyectos tipo | Instalación de sistemas solares fotovoltaicos (Proyectos Tipo) | DNP | s. f. | https://proyectostipo.dnp.gov.co/images/pdf/Celdas/DocumentoMetodologicoPTIPOCELDASSOLARES.pdf | Especificaciones tipo (escala menor) | V-idx |

---

## 3. Valores técnicos extraídos, con su fuente

> Todos los valores deben contrastarse con el documento original antes de usarse como criterio de aceptación. El estado se indica en cada caso.

### 3.1 IEC 62446-1:2016+AMD1:2018 y IEC TS 62446-3:2017

**Secuencia de pruebas.** Fuente: resúmenes de la norma (Hioki, AQ Electric, Fluke/pv-magazine 2024). Estado: V-sec.
- **Regla general:** las pruebas se ejecutan en el orden indicado. Si una prueba revela una falla, después de corregirla se **repiten todas las pruebas anteriores**. La Categoría 1 debe estar completa y aprobada antes de pasar a la Categoría 2.
- **Categoría 1** (todas las instalaciones):
  1. Inspección visual (cl. 5.2 y Anexo de inspección).
  2. Continuidad de los conductores de protección y de equipotencialidad (cuando existan).
  3. Polaridad.
  4. Prueba de cajas combinadoras (de string).
  5. Tensión de circuito abierto Voc por string.
  6. Corriente de string: Isc (o corriente de operación).
  7. Pruebas funcionales (seccionadores, inversor).
  8. Resistencia de aislamiento del circuito DC.
- **Categoría 2** (sistemas grandes o complejos): todas las de la Categoría 1, más la **curva I-V por string** y la **inspección termográfica (IR)**. Según la norma, la curva I-V puede reemplazar las mediciones de Voc e Isc.

**Criterios de aceptación de string** (práctica derivada de la norma; verificar la redacción exacta en el original). Estado: V-sec.
- Voc: dentro de ±5 % del valor esperado (corregido por temperatura) o de strings idénticos.
- Isc: dentro de ±5 % entre strings idénticos con irradiancia estable. Muchas especificaciones usan ±10 % frente al valor esperado.

**Resistencia de aislamiento.** Tabla 2, arreglos de hasta 10 kWp. Estado: V-sec, con 3 o más fuentes concordantes.

| Tensión del sistema (Voc stc × 1,25) | Tensión de ensayo DC | Resistencia mínima |
|---|---|---|
| < 120 V | 250 V | 0,5 MΩ |
| 120 V – 500 V | 500 V | 1 MΩ |
| > 500 V (hasta 1000 V) | 1000 V | 1 MΩ |
| > 1000 V – 1500 V (fila añadida por AMD1:2018) | 1000 V (V-sec) | 1 MΩ |

- **Métodos:**
  - Método 1: positivo y negativo cortocircuitados, medición contra tierra.
  - Método 2: positivo–tierra y negativo–tierra por separado.
- **Arreglos mayores de 10 kWp:** la norma trae un tratamiento diferente (otra tabla o criterio en función del tamaño). **NV**: no se pudo leer la tabla. Hay que confirmarla en el original antes de redactar el criterio para strings y arreglos de utility-scale.

**Curva I-V** (IEC 62446-1, Cat. 2; corrección según IEC 60891). Estado: V-sec.
- Irradiancia en el plano del arreglo **≥400 W/m² y estable**.
- Sensor de irradiancia coplanar con el arreglo.
- Sonda de temperatura en la parte posterior del módulo, en el centro.

**Termografía, IEC TS 62446-3:2017.** Estado: V-sec, con varias fuentes concordantes.
- Irradiancia mínima **600 W/m²** en el plano del arreglo, y estable.
- Viento máximo **28 km/h (4 Bft)**.
- Nubosidad máxima **2 octas** de cúmulos.
- Planta en estado térmico estable.
- Suciedad baja: pérdida de Isc por suciedad menor del 10 %.
- Sin sombras parciales.
- Resolución geométrica: en las fuentes secundarias aparece **≥5×5 píxeles por celda** (spot real de medición de 3×3 px). Sensibilidad NETD ≤0,1 K a 30 °C. Estado: V-sec. Confirmar en la norma si es requisito o recomendación.
- Clases de anomalía:
  - CoA 1: sin anomalía.
  - CoA 2: anomalía térmica (investigar y monitorear).
  - CoA 3: anomalía relevante para la seguridad (actuar).
  - Los umbrales de ΔT (por ejemplo, <10 K, 10–30 K, >30 K) son **práctica de operadores, no texto normativo** (V-sec).

**Prueba de capacidad, ASTM E2848** (resumen secundario). Estado: V-sec.
- Se excluyen los datos con irradiancia <400 W/m².
- Para la regresión se usan puntos dentro de ±20 % de la irradiancia de reporte.
- Criterio contractual típico: capacidad medida/esperada ≥97 %, según la incertidumbre.

### 3.2 Puesta a tierra: IEEE 81 y RETIE

**IEEE 81-2012**, §6.3.2 (caída de potencial). Fuentes: EEPower, AGI, resúmenes. Estado: V-sec.
- Electrodo de potencial a **X = 0,62·D** (D = distancia entre el electrodo bajo prueba y el electrodo de corriente).
- Zona plana aproximada entre 52,8 % y 62,8 % de D. Comprobar la planitud de la curva moviendo el electrodo de potencial ±10 %.
- Ejemplo de dimensionamiento: para una varilla de 3 m, D ≥15 m y P ≈9,3 m.
- Sondas auxiliares enterradas ≈400 mm.
- En mallas extensas, D debe ser varias veces la diagonal de la malla (verificar en la norma).
- **Nota:** IEEE publicó **IEEE 81-2025** (dic-2025). Revisar si cambia el procedimiento.

**Wenner (4 picas):**
- 4 electrodos en línea, separación «a».
- Corriente por C1 y C2 (externos), tensión entre P1 y P2 (internos).
- ρ = 2πaR, con la profundidad de enterramiento de las picas mucho menor que «a» (fórmula estándar).
- Repetir con varias separaciones «a» para el perfil por capas.

**RETIE** (Libro 3, Res. 40117/2024; Libro 3 modificado por la Res. 40284/2026):
- **Art. 3.12.4.1:** la resistividad aparente puede medirse con el método tetraelectródico de **Wenner**.
- **Art. 3.12.4.2:** la resistencia de puesta a tierra se mide con los métodos de la **IEEE 81**, entre ellos la **caída de potencial**. El valor se toma con el electrodo de tensión al **61,8 %** de la distancia al electrodo de corriente, en terreno uniforme.
- Estado: V-sec, mediante fragmentos indexados que citan el texto del RETIE.

**Tabla 3.12.3.a RETIE: valores de referencia de resistencia de puesta a tierra.** Los valores se adoptaron de ANSI/IEEE 80, NTC 2050 (2.ª actualización) y NTC 4552-1. Estado: V-sec, porque varias fuentes coinciden con la tabla histórica del RETIE 2013. **Hay que confirmar contra el Libro 3 modificado por la Res. 40284/2026.**

| Aplicación | Valor de referencia máximo |
|---|---|
| Estructuras y torrecillas metálicas de líneas o redes con cable de guarda | 20 Ω |
| Subestaciones de alta y extra alta tensión | 1 Ω |
| Subestaciones de media tensión | 10 Ω |
| Protección contra rayos | 10 Ω |
| Punto neutro de acometida en baja tensión | 25 Ω |
| Redes para equipos electrónicos o sensibles | 10 Ω |

- Importante: en el RETIE estos son **valores de referencia**. El criterio de seguridad es no superar las **tensiones de paso y de contacto** admisibles, calculadas según IEEE 80.
- Para centrales de generación y subestaciones se exige un procedimiento de cálculo reconocido.

### 3.3 Limpieza de módulos (manuales de fabricantes)

| Parámetro | LONGi | JinkoSolar | Trina (Vertex) | First Solar (Series 6) |
|---|---|---|---|---|
| Presión de agua | < 3000 Pa en la cara frontal; < 1500 Pa en la cara posterior de bifaciales (según el fragmento del manual; ver nota) | ≤ 3500 kPa (35 bar) con boquilla a ≥0,5 m; con manguera o mochila < 675 kPa | ≤ 4 MPa (40 bar) | < 35 bar (500 psi) en la boquilla; no apuntar a la caja de conexiones, al sellado de bordes ni a los conectores |
| pH | ≈ 6 – 8 | 6,5 – 8 | 5 – 7 | detergente suave con pH 6,5 – 8,5 a 25 °C (si se usa) |
| Dureza | evitar agua con alto contenido mineral | ≤ 450 mg/L | 0 – 40 mg/L (Ca + Mg) | < 75 mg/L (agua de grifo de baja mineralización), o agua RO o desionizada |
| TDS | (no indicado en el fragmento) | ≤ 1000 mg/L | ≤ 1000 mg/L | < 1500 mg/L (agua dulce) |
| Cloruros/salinidad | (si no hay agua de baja mineralización, admite NaCl ≤2 ‰ según el fragmento: dato poco usual, verificar) | ≤ 1000 mg/L | 0 – 3000 mg/L | — |
| Otros | ΔT agua–módulo ≤ 10 °C. Esponja o paño suave. Sin detergentes ácidos ni alcalinos | ΔT agua–módulo ≤ 10 °C. No limpiar con temperatura ambiente < 5 °C. Se recomienda agua municipal | Turbidez 0 – 30 NTU; conductividad 1500 – 3000 µS/cm. Agua no alcalina; desmineralizada si es posible. Sin vapor | De preferencia limpiar entre el atardecer y el amanecer. EPP eléctricamente aislante. Solo personal entrenado |
| Fuente | LONGi Maintenance Manual V2.0 / Installation Manual | Jinko Global Installation Manual A1/A1.5 | Trina UM-M-0002 | First Solar Series 6 / CuRe User Guide |
| Estado | V-sec (fragmentos del manual) | V-sec (fragmentos del manual) | V-sec | V-sec |

- Nota LONGi: «3000 Pa» (0,03 bar) es muy bajo comparado con los demás fabricantes. Puede ser un error de unidades del manual o del fragmento (¿3000 kPa?). **Hay que verificarlo en el manual vigente del módulo comprado.**
- **Horario** (síntesis de fuentes): limpiar temprano en la mañana, al atardecer o de noche. Evitar el choque térmico con el módulo caliente (ΔT ≤10 °C) y reducir las pérdidas de producción.

### 3.4 Conectores MC4 (Stäubli), cable MT y tendido

**Conectores MC4 de Stäubli.** Estado: V-sec.
- Torque de la tuerca del prensaestopas (PV-KST4/PV-KBT4, MA231): **típico 3,4 – 3,5 N·m, adaptado al cable usado**.
- Se pre-aprieta con llave PV-MS-PLS y se aprieta con el juego dinamométrico PV-WZ-Torque-Set, sosteniendo el aislador.
- Crimpado únicamente con la herramienta Stäubli especificada en el manual.
- **Confirmar en el MA231 vigente** (el valor puede variar según la sección y el diámetro del cable).
- **Prohibido el acople cruzado** con conectores de otros fabricantes («MC4-compatibles»): anula la certificación y la garantía (declaración de Stäubli). Estado: V-idx.

**Radio mínimo de curvatura de cable > 1000 V** (NEC 300.34, base de NTC 2050). Estado: V-sec.
- Cable sin pantalla: **8 ×** el diámetro exterior.
- Cable apantallado o con cubierta de plomo: **12 ×** el diámetro exterior.
- Cable multiconductor con conductores apantallados individualmente: el mayor entre 12 × el diámetro del conductor individual y 7 × el diámetro total.
- Algunos fabricantes europeos aplican un radio dinámico (durante el tiro) mayor que el estático. Usar la ficha del fabricante.

**Tensión máxima de tiro sobre el conductor** (con ojo de tiro).
- Cobre: **0,008 lb/cmil** (≈70 N/mm²).
- Aluminio: **0,006 lb/cmil** (≈50 N/mm²; algunas fuentes citan 40 N/mm², AEIC CS8).
- Fuentes: Southwire, IEWC y AWG. Estado: V-sec.
- Con media de tiro (camisa) sobre la cubierta, los límites son menores (según el fabricante).
- **Presión lateral (SWBP):** Southwire indica hasta 1000 lb/ft para calibres ≥8 AWG en cables de potencia (V-sec). El valor depende del tipo de cable. Usar la ficha del fabricante.

**Pruebas de cable MT tras la instalación** (IEC 60502-2, cl. 20.3; resumen secundario). Estado: V-sec.
- Opciones en AC:
  - Tensión U (fase–fase) a 20 – 300 Hz durante 15 min.
  - U0 durante 24 h.
  - **VLF de 0,1 Hz a 3U0 durante 15 min.**
- Alternativa en DC: 4U0 durante 15 min (solo para cable nuevo; no recomendada para XLPE envejecido).
- IEEE 400.2: aceptación VLF a ≈2,5 – 3 U0, entre 15 y 60 min (recomendado ≥30 min). Revisar la tabla de la edición 2024.

**Transformadores** (IEEE C57.152-2013). Estado: V-sec.
- Relación de transformación (TTR) dentro de **±0,5 %** de la placa.
- Resistencia de aislamiento mínima orientativa de (kV + 1) MΩ a 20 °C, corrigiendo la lectura a 20 °C.

**Fibra óptica** (TIA-568-C.3). Estado: V-sec.
- Pérdida máxima de **0,75 dB por par de conectores** y **0,3 dB por empalme**.
- Tier 1: OLTS (pérdida, longitud y polaridad).
- Tier 2: más OTDR, con promedio bidireccional en monomodo (IEC 61280-4-1 / TIA-568.3-E).

**Trackers Nextracker** (fragmentos de la NX Horizon 2.4.1). Estado: V-sec.
- Slew drive M20: 240 N·m (175 ft·lb).
- Motor y antena: 60 N·m.
- U-bolt SPC: 20 N·m.
- Tolerancia de ±10 % en todos los torques.
- **Usar solo el manual oficial del proyecto.**

### 3.5 Otros valores de seguridad

- **Trabajo en alturas** (Res. 4272/2021): aplica a toda actividad con riesgo de caída **mayor de 2,0 m** sobre el plano inferior más cercano. Antes, con la Res. 1409/2012, el umbral era 1,5 m.
- **Espacios confinados** (Res. 0491/2020):
  - Tipo 1: abiertos por arriba, por ejemplo zanjas de **más de 1,2 m** de profundidad.
  - Tipo 2: cerrados con abertura pequeña.
  - Aplica a zanjas profundas de cable MT y a cámaras o bóvedas.
- **Trabajo en caliente** (NFPA 51B-2024): retirar combustibles en un radio de 35 ft (≈11 m). Vigía de incendio **≥60 min** tras terminar el trabajo (OSHA: 30 min).
- **Ruido** (GATI-HNIR, adoptada por la Res. 2844/2007): tasa de intercambio de 3 dB. El nivel de acción y el TLV de 85 dBA/8 h se citan comúnmente, pero **NV** en la norma.

---

## 4. Normativa colombiana verificada

Estado: **V-idx** = la norma existe y su objeto se confirmó con varias fuentes indexadas (normogramas oficiales, gestores normativos o sitios jurídicos). No se pudo abrir el texto oficial completo.

| Norma | Emisor | Objeto | Estado | URL |
|---|---|---|---|---|
| **Res. 40117 de 2024** (2-abr-2024): RETIE | MinEnergía | Nuevo Reglamento Técnico de Instalaciones Eléctricas en 4 libros. Deroga el anexo general de la Res. 90708/2013. Transición: certificados de la 90708 válidos hasta el 2-jul-2025 | Vigente, **modificada por la Res. 40284/2026** | https://www.minenergia.gov.co/documents/11563/Resoluci%C3%B3n_40117_de_2024.pdf |
| **Res. 40284 de 2026** (23-jun-2026; D.O. 53.539 del 1-jul-2026) | MinEnergía | Modifica los Libros 1, 2, 3 y 4 y los anexos del RETIE. Exime de certificación plena a la autogeneración <10 kVA, entre otros cambios | Vigente desde su publicación | https://www.minenergia.gov.co/documents/15918/Resolucion-40284-23-06-2026-RETIE-libros-compilados.pdf ; Libro 3: https://www.minenergia.gov.co/documents/15921/Libro-3-Resolucion-40284-23-06-2026.pdf |
| **NTC 2050** (2.ª actualización, 2020): Código Eléctrico Colombiano | ICONTEC | Adaptación del NEC 2017 (NFPA 70). Los capítulos 1 a 7 son de obligatorio cumplimiento según el RETIE. Incluye la sección 690 (sistemas FV) | Vigente (norma de pago) | https://www.conte.org.co/icontec-lanza-al-mercado-el-nuevo-codigo-electrico-colombia-2050-2020/ |
| **NTC 4552-1, -2, -3** (2008-11-26) | ICONTEC | Protección contra descargas eléctricas atmosféricas: principios generales, gestión del riesgo y daño físico/vida (adopción MOD de IEC 62305) | Vigente (no se encontró una versión más reciente; verificar en ICONTEC) | http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0123-921X2014000200009 |
| **Res. 5018 de 2019** (20-nov-2019; D.O. 51.145) | MinTrabajo | Lineamientos de SST en los procesos de generación (convencional y no convencional), transmisión, distribución y comercialización de energía eléctrica. **Derogó la Res. 1348 de 2009** | Vigente | https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_mtra_5018_2019.htm |
| **Res. 4272 de 2021** (27-dic-2021; D.O. 51.942 del 8-feb-2022) | MinTrabajo | Requisitos mínimos de seguridad para trabajo en alturas (>2,0 m) y centros de entrenamiento. Art. 68: deroga las Res. 1409/2012, 1903/2013, 3368/2014, 1178/2017 y 1248/2020. Rige desde el 26-ago-2022 (según fuentes secundarias) | Vigente | https://www.cancilleria.gov.co/sites/default/files/Normograma/docs/resolucion_mtra_4272_2021.htm |
| **Res. 1409 de 2012** | MinTrabajo | Reglamento anterior de trabajo seguro en alturas | **Derogada** por la Res. 4272/2021 | https://normograma.sena.edu.co/compilacion/docs/resolucion_mtra_1409_2012.htm |
| **Res. 0491 de 2020** | MinTrabajo | Requisitos mínimos de seguridad para trabajos en espacios confinados (Tipo 1 y Tipo 2) | Vigente | https://safetya.co/normatividad/resolucion-0491-de-2020/ (texto en vLex) |
| **Res. 2400 de 1979** (22-may-1979) | MinTrabajo y Seguridad Social | Estatuto de Seguridad Industrial: vivienda, higiene y seguridad en los establecimientos de trabajo | **Parcialmente vigente**, en lo no derogado por normas posteriores | https://www.cancilleria.gov.co/sites/default/files/Normograma/docs/resolucion_mintrabajo_rt240079.htm |
| **Decreto 1072 de 2015** + **Res. 0312 de 2019** | MinTrabajo | Decreto Único Reglamentario del Sector Trabajo (SG-SST) y estándares mínimos del SG-SST (7, 21 o 60 según tamaño y riesgo) | Vigentes | https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=82666 |
| **Res. 1843 de 2025** (29-abr-2025) | MinTrabajo | Evaluaciones médicas ocupacionales e historia clínica ocupacional. **Deroga la Res. 2346/2007** y otras | Vigente | https://safetya.co/normatividad/resolucion-1843-de-2025/ |
| **Res. 2844 de 2007** (16-ago-2007) | MinProtección Social | Adopta las GATISO, incluida la GATI-HNIR (hipoacusia por ruido; tasa de intercambio de 3 dB) | Vigente (V-idx) | https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/Resoluci%C3%B3n_2844_de_2007.pdf |
| **Decreto 1496 de 2018** | Presidencia (MinTrabajo y otros) | Adopta el SGA de la ONU, 6.ª ed. revisada (2015): clasificación, etiquetado y FDS de productos químicos | Vigente. Complementado por la **Res. 773 de 2021** (acciones del empleador para aplicar el SGA) | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=87910 |
| **Decreto 1076 de 2015**, Libro 2, Parte 2, Título 6 (RESPEL) | MinAmbiente | Decreto Único Reglamentario del Sector Ambiente. El Título 6 compila el Decreto 4741 de 2005 (gestión integral de RESPEL) | Vigente, **modificado por el Decreto 0766 de 2026** | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=78153 |
| **Decreto 0766 de 2026** (15-jul-2026; D.O. 53.556, rige desde el 17-jul-2026) | MinAmbiente | Modifica y adiciona el Título 6 del Decreto 1076/2015 (RESPEL): carga digital del plan de gestión integral en la plataforma RUA/IDEAM, figura de «subproductos», calendario de reporte según el último dígito del NIT, corrientes prioritarias | Vigente | https://www.minambiente.gov.co/documento-normativa/decreto-0766-del-15-julio-de-2026/ |
| **Ley 1672 de 2013** (19-jul-2013) | Congreso | Lineamientos para la política pública de gestión integral de RAEE. Responsabilidad extendida del productor | Vigente | https://www.minambiente.gov.co/wp-content/uploads/2021/06/ley-1672-2013.pdf |
| **Decreto 284 de 2018** (15-feb-2018) | MinAmbiente | Adiciona el Decreto 1076/2015 en lo relativo a la gestión integral de RAEE | Vigente | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=85199 |
| **Res. 851 de 2022** (rige desde el 1-ene-2023) | MinAmbiente | Clasificación nacional de AEE y RAEE. Sistemas de recolección y gestión a cargo de los productores | Vigente. No crea una categoría expresa para módulos FV (fuente académica) | https://www.minambiente.gov.co/wp-content/uploads/2022/08/Resolucion-0851-de-2022.pdf |
| **Res. 2184 de 2019** | MinAmbiente | Código de colores para la separación de residuos en la fuente: blanco (aprovechables), negro (no aprovechables) y verde (orgánicos aprovechables). Obligatorio desde el 1-ene-2021 | Vigente | https://www.cancilleria.gov.co/sites/default/files/Normograma/docs/pdf/resolucion_minambienteds_2184_2019.pdf |
| **Res. 1670 de 2017** (15-ago-2017) | ANLA / MinAmbiente | Adopta los Términos de Referencia TdR-015 para el EIA de proyectos de energía solar FV | Vigente (verificar actualizaciones) | https://www.anla.gov.co/documentos/normativa/terminos_referencia/anexo_tdr_solar_ajustado_26072017vf.pdf |
| **Ley 1715 de 2014** | Congreso | Integración de las energías renovables no convencionales al sistema energético nacional. Incentivos tributarios | Vigente, **modificada por la Ley 2099 de 2021** (transición energética) | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=57353 |
| **Ley 2099 de 2021** | Congreso | Transición energética y dinamización del mercado. Modifica la Ley 1715 | Vigente | https://gestornormativo.creg.gov.co/gestor/entorno/docs/ley_2099_2021.htm |
| **CREG 075 de 2021** | CREG | Disposiciones y procedimientos para asignar capacidad de transporte en el SIN: ventanilla única UPME, estudios de conexión para proyectos Clase 1 | Vigente, con modificaciones posteriores | https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0075_2021.htm |
| **CREG 174 de 2021** | CREG | Aspectos operativos y comerciales de la autogeneración a pequeña escala (AGPE) y la generación distribuida (GD). Conexión de autogeneradores a gran escala <5 MW | Vigente (aplica solo si el proyecto es AGPE/GD; no a una planta utility-scale despachada centralmente) | https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_creg_0174_2021.htm |
| **Res. 40595 de 2022** (MinTransporte; n.º completo 20223040040595; D.O. 12-jul-2022) | MinTransporte | Metodología para diseñar, implementar y verificar el PESV. Obligatorio para flotas de más de 10 vehículos o con conductores contratados. Deroga la Res. 1565/2014 | Vigente | https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_mintransporte_40595_2022.htm |
| Izaje de cargas | — | **No existe un reglamento nacional específico de izaje.** Se aplica la Res. 2400/1979 (aparatos de izar), el Decreto 1072/2015 (gestión del riesgo), la Res. 4272/2021 cuando hay trabajo en alturas, y normas técnicas ASME B30 por buena práctica. Guía técnica del CCS (2023) | — | https://ccs.org.co/wp-content/uploads/2023/06/GUIA_CCS_IZAJE_CARGAS.pdf |

---

## 5. Advertencias: lo que quedó sin verificar

1. **No se abrió ningún documento completo.** WebFetch estuvo bloqueado para todos los dominios que se intentaron. Todas las URL se verificaron solo por indexación en el buscador, y los valores se tomaron de fragmentos. Antes de publicar los procedimientos, hay que descargar y revisar: los manuales de fabricantes, el RETIE Libro 3 (versión de la Res. 40284/2026), IEC 62446-1, IEC TS 62446-3, IEEE 81-2025 y el MA231 de Stäubli.
2. **IEC 62446-1, aislamiento en arreglos >10 kWp:** la norma trae un criterio distinto al de la Tabla 2 para arreglos grandes. **NV.** Es crítico para utility-scale.
3. **Edición de IEC 62446-1:** hay indicios de que se prepara una Ed. 2 (2025-2026). **NV.** Comprobar en el webstore de IEC qué edición está vigente al redactar.
4. **RETIE, Tabla 3.12.3.a:** los valores (1, 10, 10, 25, 10 y 20 Ω) coinciden en varias fuentes, pero hay que confirmar si la Res. 40284/2026 los cambió.
5. **Presión de limpieza LONGi «3000 Pa / 1500 Pa»:** dato atípico, posible error de unidades. **Verificar.** Tampoco se confirmó la mención de NaCl ≤2 ‰.
6. **Torque MC4 3,4 – 3,5 N·m:** confirmado solo por fragmentos. El MA231 dice que el torque «debe adaptarse al cable usado».
7. **Torques de Nextracker:** salen de copias no oficiales (Scribd) de revisiones antiguas. No usarlos: pedir al proveedor el manual del proyecto.
8. **ASTM E2848, IEEE 400.2, IEEE C57.152, NFPA 70E y NFPA 51B:** solo se consultaron resúmenes secundarios (normas de pago).
9. **Power Electronics** (inversor central): no se encontraron manuales públicos.
10. **Ecopetrol, ISA y EPM:** sus procedimientos internos de trabajo eléctrico no son públicos. Solo se ubicaron las normas técnicas EPM RA6-014 y RA8 y un plan de riesgos de Ecopetrol (TT10).
11. **UPME:** no se encontró una guía oficial de construcción ni de O&M para plantas utility-scale. El documento «UPME 570 IEB» es un estudio contratado y su fecha no se verificó.
12. **Res. 2844/2007, valores de ruido (85 dBA/8 h):** no se confirmaron en el texto. Solo se confirmó la tasa de intercambio de 3 dB.
13. **CREG 174/2021:** aplica a AGPE/GD y a autogeneradores a gran escala <5 MW. Para una planta de generación despachada en el mercado mayorista rigen la CREG 075/2021, el Código de Redes (CREG 025/1995 y sus modificaciones) y los acuerdos del CNO, que **no se verificaron** en esta búsqueda.
14. **Umbral DAA/EIA de la ANLA (>10 MW):** proviene de una fuente académica de 2017. Verificar los umbrales de licenciamiento vigentes (Decreto 1076/2015, Parte 2, Título 2) y los cambios recientes.
15. **NTC 4552 (2008):** no se confirmó si ICONTEC publicó una versión más reciente.
