# Fuentes — NES-OPE-PR-025 Procedimiento de Mantenimiento Preventivo de Planta FV

> Nota de método: en esta sesión la descarga directa de páginas (WebFetch) estuvo bloqueada por el proxy de salida y el presupuesto de búsquedas se agotó. El contenido se tomó de los extractos devueltos por el buscador para cada URL (no de la lectura completa del documento). Las frecuencias de la tabla 8.2.4.3 se marcaron como criterio interno de referencia y deben confirmarse contra las guías completas y los manuales de los equipos del proyecto.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Best Practices for O&M of PV and Energy Storage Systems, 3rd Ed. (NREL/TP-7A40-73822) | NREL / Sandia / SunSpec | 2018 | https://docs.nrel.gov/docs/fy19osti/73822.pdf | Factores que fijan la frecuencia (tipo de equipo, ambiente, garantía); inspección anual de módulos; torque de módulos y estructura cada 5 años; inspección anual de finales de carrera y mesas del tracker. |
| Best Practices in PV System O&M v1.0 | SunSpec / NREL | s. f. | https://sunspec.org/wp-content/uploads/2019/10/PVOMBestPracticesv1.pdf | Termografía de módulos 1 vez al año o según estudio. |
| O&M Best Practice Guidelines v5.0 y anexo | SolarPower Europe | 2021 | https://solarbestpractices.com/src/Frontend/Files/MediaLibrary/10/o-and-m-best-practice-guidelines-v-5-0-annex-a07c44238b.pdf ; https://solarbestpractices.com/guidelines/detail/maintenance-3 | Plan anual de mantenimiento por equipo; preventivo según fabricante; definiciones de disponibilidad técnica y contractual, PR, tiempos de respuesta; 98 % como disponibilidad mínima de referencia. |
| Guidelines for O&M of PV Power Plants in Different Climates (T13-25:2022) | IEA PVPS | 2022 | https://iea-pvps.org/wp-content/uploads/2022/11/IEA-PVPS-Report-T13-25-2022-OandM-Guidelines.pdf | Optimización del plan preventivo según tamaño, diseño y clima; KPI. |
| Best practice guidelines for technical and economic KPIs (T13-28:2024) | IEA PVPS | 2024 | https://iea-pvps.org/wp-content/uploads/2024/12/IEA-PVPS-T13-28-2024-REPORT-Technical-and-Economic-KPIs.pdf | Definición de KPI. |
| IEC TS 62446-3:2017 (resumen) | iTeh / IEC | 2017 | https://standards.iteh.ai/catalog/standards/iec/51880fd1-6c19-4cdf-a887-fe72607000a2/iec-ts-62446-3-2017 | Alcance de la termografía y matriz de anomalías; mínimo 600 W/m² en plano. |
| Review on IR and EL Imaging for PV Field Applications | IEA PVPS Task 13 | 2018 | https://iea-pvps.org/wp-content/uploads/2020/01/Review_on_IR_and_EL_Imaging_for_PV_Field_Applications_by_Task_13.pdf | Condiciones de inspección IR. |
| Central inverters preventive maintenance (fact file) | Fabricante de inversores (Suiza) | 2014 | https://library.e.abb.com/public/282ee99b40a24bfba8243b652602ff4f/17102_FactFileSP67_EN_RevE_2014_ABB_central_inverter_PVS800_Preventive_Maintenance_lowres.pdf | Inspección anual de ventiladores, filtros y refrigeración del inversor central. |
| Solar inverter maintenance & troubleshooting guide | Proveedor de CMMS | 2026 | https://oxmaint.com/article/solar-inverter-maintenance-troubleshooting-guide | Cadencia trimestral/semestral/anual del inversor; torque de bornes y filtros semestral; termografía de IGBT y bornes. |
| Expert tips for MV switchgear maintenance | Proveedor de servicios | s. f. | https://www.clelek.com/blog/expert-tips-for-mv-switchgear-maintenance | Mantenimiento mayor de celdas MT cada 3 a 5 años; inspección anual. |
| Maintenance of large-scale solar power plants | Proveedor de servicios | s. f. | https://voltageg.com/en/expert-blog/maintenance-of-large-scale-solar-power-plants-10-mw-and-above/ | Tareas de transformador (aceite, radiadores, fugas, protecciones). |
| Regionalización de la lluvia en Colombia | IDEAM | s. f. | http://www.ideam.gov.co/documents/21021/21789/Regionalizaci%C3%B3n+de+la+lluvia+en+Colombia.pdf/92287f96-840f-4408-8e76-98b668b83664 | Planeación por temporadas secas y lluviosas. |
| Prevención y manejo de accidentes por serpientes venenosas | Instituto Nacional de Salud | s. f. | https://www.ins.gov.co/Comunicaciones/Infografias/INFORGRAF%C3%8DA%20ACCIDENTE%20OF%C3%8DDICO.pdf | Primeros auxilios en accidente ofídico. |

## Ajustes para Colombia

- Sin nombres de fabricantes en el documento.
- Normativa extranjera (NEC/OSHA citadas en las guías de EE. UU.) sustituida por RETIE (Res. 40117 de 2024), NTC 2050, Res. 5018 de 2019 (cinco reglas de oro), Decreto 1072 de 2015, Res. 4272 de 2021 y Res. 0491 de 2020.
- Personal: técnicos CONTE (Ley 1264 de 2008), ingenieros COPNIA (Ley 842 de 2003), responsable SST con licencia, coordinador de alturas.
- Maniobras que afectan la conexión coordinadas con [OPERADOR DE RED] y XM (CREG 075 de 2021).
- Residuos: aceites y filtros como RESPEL (Decreto 1076 de 2015), RAEE (Ley 1672 de 2013), código de colores Res. 2184 de 2019.
- Mantenimiento por temporada (IDEAM): drenajes y sellos antes de lluvias; filtros, termografía y control de incendio en temporada seca; quemas agrícolas como fuente de polvo en filtros.
- Ofidios y fauna en gabinetes; línea 123; ARL.
- Dron: sujeto a la reglamentación aeronáutica vigente (sin citar número).

## Pendientes de verificar

- Frecuencias del manual de cada fabricante (tracker, inversor, transformador, celdas, sensores) y condiciones de garantía.
- Metas contractuales de disponibilidad, PR, tiempos de respuesta y prioridades del contrato de O&M.
- Porcentaje de muestreo de curvas I-V e irradiancia mínima de medida (criterio interno por definir).
- Periodicidad de medición de puesta a tierra exigida por el RETIE vigente y por el diseño.
- Norma de referencia para el análisis de aceite que indique el fabricante del transformador.
- Listado de repuestos críticos y mínimos acordados con [PROPIETARIO].
