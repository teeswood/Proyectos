---
code: NES-OPE-PR-025
header_title: PROCEDIMIENTO DE MANTENIMIENTO PREVENTIVO DE PLANTA FV
cover_title: Procedimiento de Mantenimiento Preventivo de Planta Fotovoltaica
cover_subtitle: Plan por equipo y frecuencia, inspecciones avanzadas, órdenes de trabajo, repuestos y KPI de O&M
---

# 1. OBJETIVO

Establecer el plan, el método y los controles para ejecutar el mantenimiento preventivo de la planta fotovoltaica [PROYECTO] — módulos, estructura y tracker, cableado, cajas combinadoras, inversores, centros de transformación, celdas de media tensión, puesta a tierra, SCADA y estación meteorológica, cerramiento y vías — de modo que se conserven la seguridad, la disponibilidad, el rendimiento y las garantías de los equipos, y que toda anomalía detectada se convierta en una orden de trabajo correctiva trazable.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, en especial el contacto eléctrico, el arco eléctrico y la maniobra sin bloqueo.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en la operación y mantenimiento (O&M) de plantas FV en servicio:

- Elaboración, aprobación y seguimiento del plan anual de mantenimiento preventivo.
- Inspecciones y tareas preventivas por equipo y frecuencia (numeral 8.2.4.3).
- Inspecciones avanzadas: termografía (IEC TS 62446-3), curvas I-V de muestreo, resistencia de aislamiento y medición de puesta a tierra.
- Verificación de pares de apriete, limpieza de filtros y sistemas de ventilación.
- Gestión de órdenes de trabajo, repuestos y correctivos derivados.
- Cálculo y reporte de los indicadores (KPI) de O&M.

No incluye la limpieza de módulos (NES-OPE-PR-024), el control de vegetación (NES-OPE-PR-026), la sustitución de módulos (NES-OPE-PR-010), la intervención de conectores DC (NES-OPE-PR-014) ni las maniobras de conexión y desconexión con el [OPERADOR DE RED], que siguen el procedimiento de maniobras del proyecto y, cuando aplique, las instrucciones del operador del sistema (XM).

> NOTA: Las frecuencias de este procedimiento son de referencia. Prevalecen las del manual del fabricante de cada equipo y las condiciones de garantía, y se ajustan al clima del sitio, a los hallazgos y a la disponibilidad contractual pactada con [PROPIETARIO].

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / PT / PTE | Análisis de trabajo seguro, permiso de trabajo y permiso de trabajo eléctrico. |
| Mantenimiento preventivo (MP) | Intervención programada a intervalos fijos o por condición, para reducir la probabilidad de falla. |
| Mantenimiento correctivo (MC) | Intervención para restablecer un equipo que falló o presenta una anomalía. |
| Mantenimiento predictivo | Seguimiento de variables (temperatura, aislamiento, gases en aceite, tendencias del SCADA) para anticipar fallas. |
| Plan anual de mantenimiento | Cronograma de todas las tareas preventivas por equipo, frecuencia y mes, aprobado por [PROPIETARIO]. |
| Orden de trabajo (OT) | Documento que autoriza, describe y registra una intervención: equipo, tarea, permisos, recursos, tiempos, hallazgos y cierre. |
| CMMS | Sistema computarizado de gestión del mantenimiento donde se programan y cierran las OT. |
| SCB | Caja combinadora de strings. |
| CT | Centro de transformación: transformador elevador, celdas de MT y servicios auxiliares asociados a uno o más inversores. |
| Termografía | Inspección con cámara infrarroja para detectar diferencias de temperatura anormales (IEC TS 62446-3). |
| Curva I-V | Característica corriente-tensión de un string o módulo, medida con trazador, para diagnosticar pérdidas. |
| PR (performance ratio) | Relación entre la energía producida y la energía teórica que habría producido la planta con la irradiancia medida en el plano de los módulos, según la IEC 61724-1. |
| Disponibilidad técnica | Porcentaje del tiempo con irradiancia útil en que la planta o el equipo está apto para generar, sin exclusiones. |
| Disponibilidad contractual | Disponibilidad con las exclusiones pactadas en el contrato de O&M (fuerza mayor, red externa, orden del propietario). |
| MTTR | Tiempo medio de reparación. |
| Repuesto crítico | Repuesto cuya falta deja fuera de servicio una parte significativa de la planta o supera el tiempo de reposición aceptable. |
| Cinco reglas de oro | Cortar todas las fuentes, bloquear, verificar ausencia de tensión, poner a tierra y en cortocircuito cuando aplique, y señalizar la zona. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. Bloques, filas, SCB, inversores, CT, subestación, sala de control, estación meteorológica, almacén de repuestos y vías se identifican según el plano general de implantación [N° de plano], el unifilar general [N° de plano] y el listado de activos del CMMS [__________].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

- Manuales de operación y mantenimiento de los fabricantes del módulo, del tracker, de las SCB, del inversor, del transformador, de las celdas de MT, del SCADA y de los sensores meteorológicos.
- Condiciones de garantía de cada equipo y contrato de O&M con [PROPIETARIO], con disponibilidad garantizada, tiempos de respuesta y exclusiones.
- Planos as-built: implantación, unifilares DC y AC, puesta a tierra y apantallamiento, rutas de cable, comunicaciones.
- Protocolos de comisionado de NES-OPE-PR-022 (línea base de Voc, Isc, aislamiento, curvas I-V y termografía inicial).
- NES-OPE-INS-001 Instructivo de comprobación de par de apriete; NES-OPE-PR-008 Montaje de tracker; NES-OPE-PR-010 Montaje y sustitución de módulos FV; NES-OPE-PR-014 Conexionado DC.
- NES-OPE-PR-024 Limpieza de módulos FV; NES-OPE-PR-026 Control de vegetación.
- NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-SST-PR-002 Trabajo en alturas; NES-SST-PLN-001 Plan de emergencias; NES-AMB-PR-001 Gestión integral de residuos.

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía), con la NTC 2050 en lo que el RETIE adopta: seguridad de las instalaciones en operación, distancias de seguridad, puesta a tierra y competencia del personal.
- Ley 1264 de 2008 (técnicos electricistas — CONTE); Ley 51 de 1986 y Ley 842 de 2003 (ingenieros — COPNIA).
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en el sector eléctrico; cinco reglas de oro.
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019 — Estándares mínimos.
- Resolución 4272 de 2021 — Trabajo en alturas; Resolución 0491 de 2020 — Espacios confinados, cuando aplique a fosos o recintos del CT.
- Resolución 2400 de 1979 — Estatuto de seguridad industrial; Resolución 2844 de 2007 — GATI ruido.
- Decreto 1496 de 2018 — SGA para aceites, grasas, solventes y productos químicos de mantenimiento.
- Decreto 1076 de 2015 — RESPEL; Resolución 2184 de 2019 — Código de colores; Ley 1672 de 2013 — RAEE.
- CREG 075 de 2021 y procedimientos del [OPERADOR DE RED] y de XM, para maniobras e indisponibilidades que afecten la conexión.
- IEC 62446-1 (ensayos y documentación), IEC TS 62446-3 (termografía), IEC 61724-1 (monitoreo y desempeño), IEC 60076 (transformadores), IEC 62271 (aparamenta de MT), IEEE 81 (medición de puesta a tierra), IEC 62305 / NTC 4552 (protección contra rayos), ISO 6789 (torquímetros), NFPA 70E (referencia técnica para análisis de arco).
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Jefe de O&M Neptuno Energy Services

- Aprobar y divulgar este procedimiento y el plan anual de mantenimiento, y presentarlos a [PROPIETARIO].
- Asegurar personal calificado, instrumentos calibrados, repuestos y CMMS.
- Reportar mensualmente los KPI y las desviaciones a [PROPIETARIO].
- Detener cualquier actividad que no cumpla este procedimiento o los manuales de los fabricantes.

## 6.2. Ingeniero de mantenimiento (matrícula COPNIA vigente)

- Elaborar el plan anual, programar las OT en el CMMS y verificar su cierre.
- Analizar hallazgos, priorizar correctivos y gestionar garantías con los fabricantes.
- Evaluar los informes de termografía y curvas I-V y definir las acciones.

## 6.3. Responsable eléctrico (ingeniero o técnico con matrícula vigente)

- Emitir los permisos de trabajo eléctrico, definir puntos de corte y dirigir las maniobras, el bloqueo y etiquetado y la verificación de ausencia de tensión.
- Coordinar con el centro de control y, cuando aplique, con el [OPERADOR DE RED], toda maniobra que afecte la conexión.

## 6.4. Analista de desempeño / centro de control

- Vigilar el SCADA, generar alarmas y avisos de falla, abrir las OT correctivas y calcular disponibilidad y PR.
- Validar la calidad de los datos de la estación meteorológica y de los medidores.

## 6.5. Técnicos de mantenimiento (CONTE vigente)

- Ejecutar las tareas de la OT con la lista de chequeo correspondiente y registrar valores y hallazgos.
- Aplicar las cinco reglas de oro y el bloqueo y etiquetado en toda intervención eléctrica.

## 6.6. Almacenista de repuestos

- Controlar existencias, mínimos y máximos, condiciones de almacenamiento, trazabilidad por serial y devoluciones a garantía (NES-OPE-F-187).

## 6.7. Responsable SST (con licencia en SST vigente) y coordinador de trabajo en alturas

- Verificar permisos, EPP con categoría de arco, competencias y condiciones del área; aplicar el protocolo de tormenta eléctrica y de emergencias.
- El coordinador de trabajo en alturas (Res. 4272 de 2021) autoriza las tareas con exposición a 2 m o más.

## 6.8. Responsable ambiental

- Controlar aceites, filtros, baterías, RAEE y RESPEL generados por el mantenimiento, y el cumplimiento del PMA.

## 6.9. Trabajadores

- Cumplir este procedimiento, participar en el ATS, usar el EPP y no intervenir equipos sin OT y permiso.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no hay bloqueo, si no cuentan con el EPP o la herramienta adecuados, si no saben realizar el trabajo o si no existe procedimiento o ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Jefe de O&M, ingeniero de mantenimiento, responsable eléctrico, analista de desempeño, técnicos electricistas y electromecánicos, almacenista, responsable SST, coordinador de alturas, responsable ambiental. Personal eléctrico calificado y autorizado por escrito. |
| Sistemas | Gestión | CMMS con listado de activos, plan anual, OT y repuestos; SCADA con históricos y alarmas; repositorio de manuales y planos as-built. |
| Equipos | Medida eléctrica | Multímetro y pinza DC/AC CAT III o superior para la tensión del sistema; detector de tensión DC y MT; megóhmetro (hasta 1.000 V DC para el campo FV y de mayor tensión para MT); telurómetro; trazador de curvas I-V con sensores de irradiancia y temperatura; analizador de redes cuando se requiera. |
| Equipos | Termografía | Cámara termográfica con resolución y sensibilidad acordes con la IEC TS 62446-3; dron con cámara radiométrica cuando el alcance lo justifique, operado según la reglamentación aeronáutica vigente. |
| Herramientas | Apriete | Torquímetros calibrados según ISO 6789, con certificado vigente; herramienta aislada; marcador de torque. |
| Materiales | Consumibles | Filtros de aire de inversores y CT, grasas y lubricantes especificados, limpiacontactos aprobado, sellantes, precintos UV, rotulación, kits de tapones para conectores. |
| Materiales | Repuestos | Según el listado de repuestos críticos del numeral 8.2.4.12. |
| EPP | Eléctrico | Guantes dieléctricos de la clase según tensión, con sobreguante; ropa y careta con la categoría de arco que indique el análisis; calzado dieléctrico; pértiga y detector de MT. |
| EPP | Básico | Casco con barbuquejo, gafas UV, botas con puntera, chaleco reflectivo, ropa manga larga, cubrenuca, protector solar, protección auditiva en CT y salas de inversores, polainas en zonas con ofidios. |
| EPP | Alturas | Arnés, línea de vida y anclajes certificados para tareas con exposición a 2 m o más. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

- Plan anual aprobado y OT emitida en el CMMS con equipo, tarea, frecuencia, lista de chequeo y repuestos.
- Manual del fabricante del equipo disponible y valores de referencia (pares, filtros, ajustes) transcritos en la OT.
- Permiso de trabajo y, para tareas eléctricas, permiso de trabajo eléctrico con puntos de corte y bloqueo (NES-SST-PR-001).
- Coordinación con el centro de control y, si se afecta la conexión, con el [OPERADOR DE RED].
- Instrumentos con calibración vigente; EPP dieléctrico y con categoría de arco inspeccionado.
- Pronóstico meteorológico: sin tormenta eléctrica; condiciones de irradiancia adecuadas cuando la tarea las exija (termografía, curvas I-V).
- Programación preferente de tareas con parada en horas de baja irradiancia, para reducir la energía perdida.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

Cada OT identifica el equipo por su código del CMMS y su rótulo físico. Se delimitan y señalizan: el equipo intervenido, la zona de maniobra, las celdas o tableros bloqueados y el punto de acopio de residuos. Las salas de inversores y los CT se tratan como zonas de acceso restringido a personal autorizado.

### 8.2.2. Ingreso de personal

- Verificar en el centro de control que no haya trabajos simultáneos incompatibles en el mismo circuito.
- Diligenciar ATS, permiso de trabajo y permiso eléctrico; inspeccionar el EPP.
- Ubicar extintores, botiquín, camilla, pértiga de rescate y punto de encuentro.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional y circulación solo por vías autorizadas; velocidades del PESV del proyecto.
- Ningún vehículo pasa sobre cables expuestos, cajas de paso ni zanjas.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Plan anual de mantenimiento

El ingeniero de mantenimiento elabora el plan anual (NES-OPE-F-180) con:

1. El listado de activos del CMMS agrupado por sistema.
2. Las tareas y frecuencias del fabricante de cada equipo y las de la tabla del numeral 8.2.4.3, tomando la más exigente.
3. Las condiciones del contrato de O&M y de las garantías.
4. Las temporadas climáticas del sitio: las tareas con parada larga, la termografía y las curvas I-V se programan preferiblemente en temporada seca, con cielo despejado; la revisión de drenajes, vías y protección contra rayos se adelanta antes de las temporadas lluviosas.
5. La meta de cumplimiento del plan (KPI de ejecución del preventivo).

El plan se revisa al menos una vez al año y después de fallas repetitivas, cambios de equipo o hallazgos sistemáticos.

#### 8.2.4.2. Seguridad en toda intervención eléctrica

- Aplicar las cinco reglas de oro antes de intervenir: cortar todas las fuentes (red, inversor, strings, servicios auxiliares, UPS), bloquear y etiquetar, verificar ausencia de tensión con detector probado antes y después, poner a tierra y en cortocircuito en MT, y señalizar.
- Respetar las distancias de seguridad del RETIE a partes energizadas y delimitar el área.
- Recordar que el campo FV sigue energizado mientras haya luz: los terminales DC del inversor y de la SCB tienen tensión aunque el inversor esté detenido, salvo que el seccionador de la SCB esté abierto y bloqueado.
- Esperar el tiempo de descarga de los condensadores del inversor que indique su fabricante antes de abrir compartimentos, y verificar ausencia de tensión en el bus DC.
- Toda maniobra en MT la ejecuta o dirige el responsable eléctrico, con la secuencia aprobada y el EPP con la categoría de arco del análisis.

> ALTO: Nadie abre un inversor, una SCB, una celda de MT ni el compartimento del transformador sin OT, permiso de trabajo eléctrico, bloqueo y etiquetado y verificación de ausencia de tensión. Un equipo detenido no es un equipo sin tensión.

#### 8.2.4.3. Plan de mantenimiento por equipo y frecuencia

Frecuencias de referencia (criterio interno, construido a partir de las guías de buenas prácticas de O&M consultadas); prevalece la del fabricante del equipo. M: mensual; T: trimestral; S: semestral; A: anual; 5A: cada cinco años.

| Sistema | Tarea | Frecuencia | Registro |
|---|---|---|---|
| Módulos | Inspección visual por muestreo: vidrio, marco, delaminación, decoloración, caja de conexión, cables y conectores | T (muestreo) / A (100%) | NES-OPE-F-182 |
| Módulos | Termografía del campo FV | A | NES-OPE-F-184 |
| Módulos | Curvas I-V por muestreo y en strings con desvío | A | NES-OPE-F-185 |
| Módulos | Verificación de par de abrazaderas o fijaciones por muestreo | 5A, o antes ante hallazgos | NES-OPE-F-186 |
| Estructura / tracker | Inspección visual de postes, vigas, tubo de torsión, cojinetes, corrosión y tornillería | A | NES-OPE-F-182 |
| Estructura / tracker | Verificación de par por muestreo según NES-OPE-INS-001 | A el primer año; luego según hallazgos y fabricante | NES-OPE-F-186 |
| Estructura / tracker | Accionamiento: motor, reductor o transmisión, lubricación y holguras según fabricante | S o A según fabricante | NES-OPE-F-182 |
| Estructura / tracker | Amortiguadores, finales de carrera, sensores de inclinación y anemómetros del tracker | A | NES-OPE-F-182 |
| Estructura / tracker | Controladores, baterías o fuentes del tracker; prueba de posición de defensa | S | NES-OPE-F-182 |
| Cableado y conectores DC | Inspección de soporte, roce, contacto con el suelo, daño por fauna; termografía de conectores | A | NES-OPE-F-182 / F-184 |
| Cableado y conectores DC | Resistencia de aislamiento por circuito (IEC 62446-1) por muestreo y ante fallas de aislamiento | A (muestreo) | NES-OPE-F-185 |
| Cajas combinadoras | Inspección de envolvente, sellos, prensaestopas, ingreso de agua, polvo, insectos o fauna | S | NES-OPE-F-182 |
| Cajas combinadoras | Fusibles, portafusibles, DPS, seccionador: estado y funcionamiento; termografía bajo carga | A | NES-OPE-F-182 / F-184 |
| Cajas combinadoras | Par de bornes según fabricante | A el primer año; luego según termografía | NES-OPE-F-186 |
| Inversores | Inspección visual y termográfica, alarmas, ruidos, ventiladores | T | NES-OPE-F-183 |
| Inversores | Limpieza o cambio de filtros de aire; verificación de ventiladores y flujo de aire | T a S, más frecuente en temporada seca o con polvo | NES-OPE-F-183 |
| Inversores | Par de conexiones DC y AC, estado de DPS, fusibles, contactores, sellos y calefactores | A | NES-OPE-F-183 / F-186 |
| Inversores | Mantenimiento mayor del fabricante (condensadores, refrigeración líquida, firmware) | Según fabricante | NES-OPE-F-183 |
| Centros de transformación | Inspección visual: fugas, nivel y temperatura de aceite, silicagel, ruidos, ventilación, foso de contención | M | NES-OPE-F-183 |
| Centros de transformación | Toma de muestra de aceite y análisis (rigidez dieléctrica, humedad, gases disueltos) según fabricante y IEC 60076 | A | NES-OPE-F-183 |
| Centros de transformación | Termografía de bornes y conexiones; pruebas de protecciones propias (temperatura, presión, gases) | A | NES-OPE-F-183 / F-184 |
| Celdas de MT | Inspección visual, indicadores de presencia de tensión, presión del gas aislante, calefacción, enclavamientos | S | NES-OPE-F-183 |
| Celdas de MT | Maniobra de prueba, verificación de relés de protección y mantenimiento mayor según fabricante | A (prueba); 3 a 5 años (mayor), según fabricante | NES-OPE-F-183 |
| Puesta a tierra y rayos | Inspección de conexiones visibles, bajantes, uniones equipotenciales y corrosión | A, antes de la temporada de lluvias | NES-OPE-F-182 |
| Puesta a tierra y rayos | Medición de resistencia de puesta a tierra y continuidad (IEEE 81), y revisión del SIPRA (IEC 62305 / NTC 4552) | Según RETIE y diseño; como mínimo tras modificaciones o descargas directas | NES-OPE-F-182 |
| SCADA y comunicaciones | Revisión de alarmas, respaldo de datos, UPS, switches, fibra, sincronización horaria | T | NES-OPE-F-182 |
| Estación meteorológica | Limpieza de piranómetros y celdas de referencia, nivelación, verificación de sensores de temperatura y viento, estaciones de suciedad | Limpieza M o según fabricante; calibración según fabricante e IEC 61724-1 | NES-OPE-F-182 |
| Medición de energía | Verificación de medidores, transformadores de medida y sellos, en coordinación con el [OPERADOR DE RED] | Según la regulación y el contrato | NES-OPE-F-182 |
| Cerramiento y vías | Cerramiento perimetral, puertas, señalización, iluminación, CCTV, drenajes, cunetas, alcantarillas y vías | T y antes de cada temporada de lluvias | NES-OPE-F-182 |

> NOTA: En el primer año de operación se recomienda mayor frecuencia de verificación de pares y de termografía, porque los asentamientos y el ciclo térmico pueden aflojar uniones. La frecuencia posterior se ajusta según los hallazgos registrados.

#### 8.2.4.4. Inspección termográfica (IEC TS 62446-3)

1. Ejecutar con irradiancia estable en el plano de los módulos de al menos 600 W/m², cielo despejado, viento moderado y la planta en operación normal al menos el tiempo suficiente para estabilizar temperaturas.
2. Registrar irradiancia, temperatura ambiente, viento, hora, emisividad y ángulo de observación.
3. Inspeccionar: módulos (celdas calientes, diodos de derivación, cajas de conexión), conectores y cables, SCB, inversores, CT, celdas y uniones de puesta a tierra accesibles.
4. Clasificar cada anomalía según la matriz de la IEC TS 62446-3 y la diferencia de temperatura respecto de un elemento similar en las mismas condiciones.
5. Documentar en NES-OPE-F-184 con imagen térmica y visible, ubicación y acción propuesta.
6. El termógrafo debe tener la competencia que exige la especificación técnica; el uso de dron requiere el cumplimiento de la reglamentación aeronáutica vigente y la autorización de [PROPIETARIO].

#### 8.2.4.5. Curvas I-V de muestreo

1. Seleccionar una muestra representativa de strings por inversor y bloque (criterio interno: [____] % de strings por año, más todos los strings con desvío de corriente en el SCADA o con anomalías térmicas).
2. Medir con irradiancia estable y alta (criterio interno: no menor a [____] W/m²), sensores de irradiancia y temperatura en el plano del módulo y método de traslación a STC del instrumento.
3. Abrir el string según NES-OPE-PR-014; nunca se desconectan conectores bajo carga.
4. Comparar con la línea base de comisionado (NES-OPE-PR-022), con la ficha técnica corregida y con strings vecinos.
5. Analizar la forma de la curva: escalones (sombra, diodo, celda dañada), pendiente anormal (resistencia serie o derivación), reducción de corriente (suciedad, degradación).
6. Registrar en NES-OPE-F-185 y abrir OT correctivas.

#### 8.2.4.6. Verificación de pares de apriete

- Aplicar NES-OPE-INS-001 con torquímetro calibrado (ISO 6789) y el par del fabricante del equipo o del diseño.
- En uniones eléctricas, intervenir siempre sin tensión y con bloqueo. Si la termografía muestra una unión caliente, se corrige la causa (limpieza de superficies, reemplazo de tornillería o terminal) y no solo el par.
- Marcar con pintura testigo las uniones verificadas y registrar en NES-OPE-F-186.

#### 8.2.4.7. Limpieza de filtros y ventilación

- Inversores, CT, salas eléctricas y gabinetes con ventilación forzada: limpiar o reemplazar filtros según el fabricante; en temporada seca, con quemas agrícolas en la región o polvo de vías, aumentar la frecuencia.
- Verificar el funcionamiento de ventiladores, termostatos, calefactores e higrostatos.
- Limpiar el interior de gabinetes solo sin tensión, con aspiradora o aire seco a baja presión cuando el fabricante lo admita; nunca con agua ni solventes no aprobados.
- Revisar sellos y entradas de cable para impedir ingreso de polvo, insectos, roedores y reptiles.

#### 8.2.4.8. Ejecución de la orden de trabajo

1. El técnico recibe la OT (NES-OPE-F-181), revisa la lista de chequeo, los repuestos y los permisos.
2. Se aplica el bloqueo y la verificación de ausencia de tensión cuando la tarea lo exija.
3. Se ejecuta la tarea y se registran valores medidos, hallazgos y repuestos usados.
4. Se normaliza el equipo, se retiran bloqueos según NES-SST-PR-001 y se verifica en el SCADA que el equipo vuelve a generar.
5. El ingeniero de mantenimiento revisa y cierra la OT en el CMMS con los tiempos reales.

#### 8.2.4.9. Correctivos derivados

Todo hallazgo del preventivo se clasifica y se convierte en OT correctiva:

| Prioridad | Criterio | Tiempo de atención de referencia |
|---|---|---|
| 1 — Inmediata | Riesgo para las personas o para la instalación, incendio, pérdida de un inversor o CT completo | Según contrato de O&M [____] h |
| 2 — Alta | Pérdida de producción significativa (varios strings o SCB), anomalía térmica grave | Según contrato de O&M [____] h |
| 3 — Normal | Pérdida menor o defecto sin riesgo inmediato | Siguiente programación [____] días |
| 4 — Programable | Defecto estético o de bajo impacto | Próxima parada programada |

Los defectos cubiertos por garantía se documentan con fotografía, serial y medición, y se tramitan con el fabricante antes de intervenir si la intervención puede afectar la garantía.

#### 8.2.4.10. KPI de O&M

| Indicador | Definición | Meta |
|---|---|---|
| Disponibilidad técnica | Tiempo con irradiancia útil en que el equipo estuvo apto / tiempo total con irradiancia útil | Según contrato [____] % |
| Disponibilidad contractual | Igual que la anterior, con las exclusiones del contrato | Según contrato; las guías consultadas citan 98 % anual como práctica de referencia |
| PR | Energía AC producida / (potencia DC nominal × irradiación en el plano / 1.000 W/m²), según IEC 61724-1; se informa también corregido por temperatura | Según modelo de producción del proyecto [____] % |
| Pérdida por suciedad | 1 − SR de las estaciones de suciedad | Seguimiento (NES-OPE-PR-024) |
| Cumplimiento del preventivo | OT preventivas ejecutadas / programadas en el periodo | [____] % (criterio interno) |
| Tiempo de respuesta | Desde la alarma hasta la llegada del técnico | Según contrato |
| MTTR | Tiempo medio desde el inicio de la intervención hasta la normalización | Seguimiento |
| Accidentalidad | Frecuencia y severidad de accidentes de trabajo | Cero accidentes |

Los KPI se reportan mensualmente en NES-OPE-F-188, con la energía perdida por causa (falla de equipo, red externa, mantenimiento, suciedad, vegetación).

#### 8.2.4.11. Mantenimiento por temporada en Colombia

- Antes de cada temporada lluviosa: limpieza de drenajes, cunetas y alcantarillas; revisión de vías, taludes y erosión bajo las mesas; revisión de sellos de SCB, inversores y CT; inspección de puesta a tierra y apantallamiento.
- Durante la temporada lluviosa: seguimiento de alarmas de aislamiento DC (la humedad revela fallas de aislamiento en cables y conectores) y de inundación en fosos y cajas.
- En temporada seca: mayor frecuencia de cambio de filtros, termografía y curvas I-V, control de suciedad (NES-OPE-PR-024) y de vegetación seca por riesgo de incendio (NES-OPE-PR-026).

#### 8.2.4.12. Gestión de repuestos

- Definir con [PROPIETARIO] el listado de repuestos críticos: módulos de la misma referencia, conectores y cable, fusibles DC, DPS, tarjetas y módulos de potencia del inversor, ventiladores y filtros, controladores y motores del tracker, relés y elementos de MT, componentes de comunicación.
- Fijar mínimos considerando el tiempo de reposición del fabricante, la tasa de falla observada y el impacto en disponibilidad.
- Almacenar bajo techo, sobre estibas, en ambiente seco, con los módulos en su embalaje y en posición indicada por el fabricante; controlar humedad en tarjetas electrónicas.
- Registrar entradas, salidas, seriales y devoluciones a garantía en NES-OPE-F-187.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Ejecución del preventivo | Todas las tareas del plan del periodo ejecutadas o reprogramadas con justificación | Este procedimiento / contrato |
| Termografía | Sin anomalías de las clases que la IEC TS 62446-3 asocia a acción inmediata; condiciones de medida registradas | IEC TS 62446-3 |
| Curvas I-V | Potencia y forma de curva coherentes con la línea base y con strings vecinos; desvío según criterio del diseñador [____] % | IEC 62446-1 / Proyecto |
| Aislamiento DC | Según la tabla de la IEC 62446-1 vigente para la tensión del sistema | IEC 62446-1 |
| Pares de apriete | Valor del fabricante, con torquímetro calibrado | NES-OPE-INS-001 / ISO 6789 |
| Puesta a tierra | Resistencia y continuidad dentro de los valores de diseño y del RETIE | RETIE / IEEE 81 |
| Aceite del transformador | Dentro de los límites del fabricante y de la norma de referencia que este indique | IEC 60076 / fabricante |
| Equipos tras intervención | Normalizados, sin alarmas y generando según el SCADA | Este procedimiento |
| KPI | Según metas del contrato de O&M | Contrato |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-180 a NES-OPE-F-188 de este procedimiento.
- OT cerradas en el CMMS con su evidencia fotográfica.
- Certificados de calibración de instrumentos y torquímetros.
- Informes de termografía, curvas I-V, análisis de aceite y medición de puesta a tierra.
- Reclamaciones de garantía y su respuesta.

## 8.5. Control de calidad

El ingeniero de mantenimiento revisa el 100 % de las OT antes de cerrarlas y audita en campo una muestra mensual (criterio interno). Los hallazgos repetitivos se analizan con causa raíz. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Registro incompleto, rótulo faltante. | Corrección y cierre. |
| 2 | Tarea ejecutada fuera de método o frecuencia, sin afectar seguridad. | Repetición, reentrenamiento y verificación. |
| 3 | Intervención sin bloqueo o sin permiso, daño de equipo, afectación de garantía o de la conexión. | Suspensión, investigación, informe a [PROPIETARIO] y plan de acción. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora en el ATS y la charla diaria y verifica que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre riesgo eléctrico en DC y AC, arco eléctrico, maniobras en MT, movimiento del tracker, trabajo en alturas, fauna y uso del EPP.

## 9.1. Reglas de oro

- **SIEMPRE** aplicaré las cinco reglas de oro antes de intervenir un equipo eléctrico (Res. 5018 de 2019).
- **SIEMPRE** trataré el campo FV como energizado mientras haya luz.
- **NUNCA** intervendré un equipo sin OT, permiso de trabajo y bloqueo con mi propio candado.
- **NUNCA** abriré un inversor antes del tiempo de descarga del fabricante y de verificar ausencia de tensión.
- **SIEMPRE** usaré el EPP con la categoría de arco que indique el análisis.
- **SIEMPRE** respetaré las distancias de seguridad del RETIE.
- **NUNCA** me ubicaré en la zona de giro del tracker sin bloquear el accionamiento.
- **SIEMPRE** usaré instrumentos calibrados y de categoría adecuada.
- **SIEMPRE** suspenderé la actividad ante tormenta eléctrica y me dirigiré al refugio.
- **NUNCA** energizaré un equipo sin la autorización del responsable eléctrico.

## 9.2. Condiciones climáticas de [departamento]

- Tormenta eléctrica: ante aviso o primer trueno, suspender toda intervención, dejar los equipos en condición segura y dirigirse al refugio; reanudar con autorización del responsable SST.
- Lluvia: no abrir SCB, inversores ni celdas con lluvia o alta humedad; proteger compartimentos abiertos.
- Calor y radiación: hidratación, sombra, pausas y rotación; las tareas largas al sol se programan en las primeras horas.
- Fauna: revisar cajas, gabinetes, fosos y canaletas antes de introducir las manos; ofidios, abejas, avispas y roedores son frecuentes en equipos de campo.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado a la planta y al equipo | Colisión, volcamiento, atropellamiento. | PESV; conductores autorizados; velocidades del proyecto. |
| 2. Revisión de OT, permisos y EPP | Intervención no autorizada, EPP inadecuado. | OT y permiso eléctrico firmados; EPP dieléctrico y de arco inspeccionado. |
| 3. Maniobra, bloqueo y verificación | Choque eléctrico, arco, reenergización. | Cinco reglas de oro; candado y tarjeta personales; detector probado antes y después. |
| 4. Mantenimiento de inversores | Choque por condensadores cargados, quemaduras por superficies calientes, ruido. | Tiempo de descarga; verificación en bus DC; guantes; protección auditiva. |
| 5. Mantenimiento de CT y celdas MT | Arco eléctrico, choque, derrame de aceite, gas aislante. | Maniobra por responsable eléctrico; puesta a tierra; EPP de arco; kit antiderrame; ventilación. |
| 6. Campo FV: SCB, cables y conectores | Choque y arco en DC. | Apertura del seccionador; corriente cero verificada; NES-OPE-PR-014. |
| 7. Tracker | Atrapamiento por movimiento, golpe. | Bloqueo del accionamiento; coordinación con el centro de control. |
| 8. Termografía y curvas I-V | Exposición al sol, contacto con partes energizadas. | Distancias; herramienta aislada; puntas de prueba CAT adecuadas; hidratación. |
| 9. Uso de dron | Caída del equipo, interferencia. | Piloto certificado; zona despejada; reglamentación aeronáutica. |
| 10. Trabajo en alturas (CT, postes, cámaras) | Caída a distinto nivel. | Res. 4272 de 2021; NES-SST-PR-002; coordinador de alturas. |
| 11. Manejo de repuestos | Sobreesfuerzo, cortes. | Ayudas mecánicas; 25 kg por persona (Res. 2400 de 1979, art. 392). |
| 12. Exposición ambiental | Estrés térmico, UV, ofidios, insectos. | Hidratación, sombra, ropa manga larga, polainas, revisión de cajas. |
| 13. Tormenta eléctrica | Descarga atmosférica. | Suspensión y refugio. |

# 11. ASPECTOS AMBIENTALES

El personal recibe la inducción ambiental y la charla sobre manejo de residuos y fauna. Se cumplen las fichas del PMA del proyecto y NES-AMB-PR-001:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Suelo y agua | Derrame de aceite dieléctrico, lubricantes o refrigerantes | Bandeja y kit antiderrame; verificación del foso de contención del transformador; muestreo de aceite con recipiente cerrado; reporte inmediato de derrames. |
| Suelo | RESPEL | Aceites usados, filtros contaminados, trapos con grasa, baterías y envases de químicos en recipientes rotulados; almacenamiento temporal en zona RESPEL; entrega a gestor autorizado con certificado (Decreto 1076 de 2015). |
| Suelo | RAEE | Tarjetas, fuentes, ventiladores, medidores y módulos retirados como RAEE (Ley 1672 de 2013), separados de los que vuelven a garantía. |
| Suelo | Residuos aprovechables y ordinarios | Separación en la fuente con el código de colores de la Res. 2184 de 2019. |
| Aire | Gas aislante de celdas | No liberar a la atmósfera; recuperación solo por personal y equipos autorizados por el fabricante. |
| Aire | Emisiones y ruido | Vehículos con revisión técnico-mecánica; motores apagados en reposo; protección auditiva. |
| Fauna | Nidos y animales en equipos | No retirar sin el responsable ambiental; rescate y reubicación según PMA; sellado de entradas a gabinetes. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con NES-SST-PLN-001.

1. Detener la actividad y asegurar la zona; si hay riesgo eléctrico, cortar la fuente desde un punto seguro.
2. Notificar al responsable SST, al responsable eléctrico y al jefe de O&M de Neptuno Energy Services, al centro de control y al interlocutor de [CLIENTE]; si la emergencia afecta la conexión, el centro de control informa al [OPERADOR DE RED].
3. Brindar primeros auxilios con personal capacitado.
4. Incidente grave: línea 123, traslado al centro asistencial y notificación a la ARL.
5. Reportar e investigar según la Res. 1401 de 2007 y el SG-SST.

## 12.1. Choque eléctrico y arco

- No tocar a la víctima mientras esté en contacto; cortar la fuente o separarla con elemento aislante (pértiga de rescate en MT).
- Enfriar quemaduras con agua limpia, sin hielo ni cremas; no retirar ropa adherida.
- Toda persona que sufra choque o exposición a arco se remite a valoración médica.

## 12.2. Incendio en inversor, transformador o celda

- Activar la alarma, evacuar y cortar la alimentación desde un punto remoto si es seguro.
- Usar solo extintores aptos para equipo eléctrico energizado; nunca agua sobre equipos energizados.
- En transformadores con aceite, mantener distancia y esperar a los organismos de socorro si el fuego no es incipiente.

## 12.3. Derrame de aceite

- Contener con material absorbente, evitar que llegue a drenajes, recoger como RESPEL y reportar al responsable ambiental.

## 12.4. Accidente ofídico

- Mantener a la víctima en calma y quieta, lavar con agua y jabón; no hacer torniquete, no cortar, no succionar.
- Trasladar de inmediato al centro asistencial con suero antiofídico [__________].

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Responsable eléctrico Neptuno Energy Services | [__________] | [__________] |
| Jefe de O&M Neptuno Energy Services | [__________] | [__________] |
| Centro de control / sala de operación | [__________] | [__________] |
| [OPERADOR DE RED] — centro de control | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Plan anual de mantenimiento preventivo | NES-OPE-F-180 | Ingeniero de mantenimiento |
| Orden de trabajo | NES-OPE-F-181 | Ingeniero de mantenimiento / técnico |
| Lista de chequeo de campo FV, tracker, puesta a tierra, SCADA y obras civiles | NES-OPE-F-182 | Técnico de mantenimiento |
| Lista de chequeo de inversor, CT y celdas de MT | NES-OPE-F-183 | Técnico / responsable eléctrico |
| Informe de inspección termográfica | NES-OPE-F-184 | Termógrafo / ingeniero de mantenimiento |
| Registro de curvas I-V y aislamiento | NES-OPE-F-185 | Responsable eléctrico |
| Registro de verificación de pares de apriete | NES-OPE-F-186 | Técnico de mantenimiento |
| Control de repuestos | NES-OPE-F-187 | Almacenista |
| Informe mensual de KPI de O&M | NES-OPE-F-188 | Analista de desempeño |
| Permisos de trabajo y bloqueo | Según NES-SST-PR-001 | Responsable eléctrico / SST |

# 14. ANEXOS

## NES-OPE-F-180 — Plan anual de mantenimiento preventivo

{.plain}
| Proyecto: [__________] | Año: [____] |
|---|---|
| Documento de referencia: NES-OPE-PR-025 / manuales de fabricantes | Versión del plan: [____] |

| Sistema / equipo | Tarea | Frecuencia | Meses programados | Duración (h) | Parada requerida | Responsable |
|---|---|---|---|---|---|---|
| Módulos |  |  |  |  |  |  |
| Tracker |  |  |  |  |  |  |
| SCB y cableado DC |  |  |  |  |  |  |
| Inversores |  |  |  |  |  |  |
| CT y celdas MT |  |  |  |  |  |  |
| Puesta a tierra y SIPRA |  |  |  |  |  |  |
| SCADA y estación meteorológica |  |  |  |  |  |  |
| Cerramiento, vías y drenajes |  |  |  |  |  |  |

{.plain}
| Observaciones (temporadas, paradas coordinadas con [OPERADOR DE RED]): |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-181 — Orden de trabajo

{.plain}
| Proyecto: [__________] | OT N.º: [____] |
|---|---|
| Tipo: preventivo / correctivo / predictivo | Prioridad: 1 / 2 / 3 / 4 |
| Equipo (código CMMS y rótulo): [__________] | Documento de referencia: NES-OPE-PR-025 |

| Ítem | Dato | Registro |
|---|---|---|
| 1 | Descripción de la tarea o de la falla |  |
| 2 | Permiso de trabajo / permiso eléctrico N.º |  |
| 3 | Puntos de corte y bloqueo aplicados |  |
| 4 | Fecha y hora de aviso / inicio / fin / normalización |  |
| 5 | Personal asignado |  |
| 6 | Valores medidos |  |
| 7 | Hallazgos |  |
| 8 | Repuestos usados (referencia y serial) |  |
| 9 | Energía perdida estimada (MWh) |  |
| 10 | Correctivos derivados (OT N.º) |  |
| 11 | Equipo normalizado y verificado en SCADA |  |

{.plain}
| Observaciones: |
|---|

|  | Ejecutó | Revisó | Aprobó cierre | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-182 — Lista de chequeo de campo FV, tracker, puesta a tierra, SCADA y obras civiles

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / área: [__________] | OT N.º: [____] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Módulos sin vidrio roto, delaminación, decoloración ni caja de conexión dañada |  |  |  |
| 2 | Fijaciones de módulos completas y sin desplazamiento |  |  |  |
| 3 | Cables soportados, sin contacto con el suelo, sin roce ni daño por fauna |  |  |  |
| 4 | Conectores acoplados, sin evidencia de calentamiento |  |  |  |
| 5 | Postes, vigas y tubo de torsión sin corrosión, deformación ni tornillería faltante |  |  |  |
| 6 | Accionamiento del tracker lubricado, sin ruidos ni holguras anormales |  |  |  |
| 7 | Amortiguadores, finales de carrera y sensores del tracker en buen estado |  |  |  |
| 8 | Controlador y batería del tracker; prueba de posición de defensa conforme |  |  |  |
| 9 | SCB: envolvente, sellos, fusibles, DPS y seccionador conformes; sin agua ni fauna |  |  |  |
| 10 | Uniones de puesta a tierra y bajantes sin corrosión ni desconexión |  |  |  |
| 11 | SCADA, UPS y comunicaciones sin alarmas; respaldo de datos realizado |  |  |  |
| 12 | Piranómetros, celdas de referencia y estaciones de suciedad limpios y nivelados |  |  |  |
| 13 | Cerramiento, puertas, señalización, CCTV e iluminación conformes |  |  |  |
| 14 | Drenajes, cunetas, alcantarillas y vías sin obstrucción ni erosión |  |  |  |

{.plain}
| Observaciones y OT derivadas: |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-183 — Lista de chequeo de inversor, centro de transformación y celdas de MT

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Equipo (código y serial): [__________] | OT N.º: [____] |

| Ítem | Verificación | Cumple | No cumple | Valor / Obs. |
|---|---|---|---|---|
| 1 | Inversor: historial de alarmas revisado |  |  |  |
| 2 | Inversor: filtros limpios o reemplazados; ventiladores operando |  |  |  |
| 3 | Inversor: tiempo de descarga respetado y ausencia de tensión verificada |  |  |  |
| 4 | Inversor: conexiones DC y AC al par del fabricante; sin decoloración |  |  |  |
| 5 | Inversor: DPS, fusibles, contactores, sellos y calefactores conformes |  |  |  |
| 6 | Transformador: sin fugas; nivel y temperatura de aceite; silicagel |  |  |  |
| 7 | Transformador: muestra de aceite tomada (si corresponde) |  |  |  |
| 8 | Transformador: protecciones propias probadas |  |  |  |
| 9 | Foso de contención limpio y sin agua acumulada |  |  |  |
| 10 | Celdas MT: presión de gas, indicadores de tensión, enclavamientos |  |  |  |
| 11 | Celdas MT: relés de protección verificados; maniobra de prueba |  |  |  |
| 12 | Ventilación, iluminación, extintores y señalización del CT |  |  |  |

{.plain}
| Observaciones y OT derivadas: |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-184 — Informe de inspección termográfica

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Irradiancia en plano: [____] W/m² | Temperatura ambiente: [____] °C |
| Viento: [____] m/s | Cámara (serie / calibración): [____] |
| Documento de referencia: NES-OPE-PR-025 / IEC TS 62446-3 | Termógrafo: [__________] |

| N.º | Ubicación | Elemento | ΔT (K) | Clase de anomalía | Imagen N.º | Acción |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |

{.plain}
| Observaciones: |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-185 — Registro de curvas I-V y aislamiento

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Inversor / SCB: [__________] | Trazador (serie / calibración): [____] |
| Irradiancia: [____] W/m² | Temperatura de módulo: [____] °C |

| String | Pmax a STC (W) | Voc (V) | Isc (A) | FF | Aislamiento (MΩ) | Desvío vs. línea base (%) |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Diagnóstico y OT derivadas: |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-186 — Registro de verificación de pares de apriete

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Equipo / zona: [__________] | Torquímetro (serie / calibración): [____] |
| Documento de referencia: NES-OPE-INS-001 / manual del fabricante | OT N.º: [____] |

| Unión | Elemento | Par especificado (N·m) | Par verificado (N·m) | Conforme | Marcado | Obs. |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Observaciones: |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-187 — Control de repuestos

{.plain}
| Proyecto: [__________] | Periodo: [____] |
|---|---|
| Almacén: [__________] | Documento de referencia: NES-OPE-PR-025 |

| Repuesto | Referencia | Mínimo | Existencia | Movimiento (entrada / salida) | Serial / OT | Garantía |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Observaciones (pedidos, devoluciones, condiciones de almacenamiento): |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-188 — Informe mensual de KPI de O&M

{.plain}
| Proyecto: [__________] | Mes: [____] |
|---|---|
| Documento de referencia: NES-OPE-PR-025 / IEC 61724-1 | Potencia DC / AC: [____] MWp / [____] MW |

| Indicador | Valor del mes | Meta | Acumulado año | Observación |
|---|---|---|---|---|
| Energía producida (MWh) |  |  |  |  |
| Irradiación en plano (kWh/m²) |  |  |  |  |
| PR (%) |  |  |  |  |
| Disponibilidad técnica (%) |  |  |  |  |
| Disponibilidad contractual (%) |  |  |  |  |
| Pérdida por suciedad (%) |  |  |  |  |
| Cumplimiento del preventivo (%) |  |  |  |  |
| Tiempo medio de respuesta (h) |  |  |  |  |
| MTTR (h) |  |  |  |  |
| Energía perdida por causa (MWh) |  |  |  |  |
| Accidentes / incidentes |  |  |  |  |

{.plain}
| Análisis de desviaciones y plan de acción: |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

# 15. CONTROL DE CAMBIOS

| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
