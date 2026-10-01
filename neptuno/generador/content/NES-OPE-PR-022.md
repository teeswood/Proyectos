---
code: NES-OPE-PR-022
header_title: PROCEDIMIENTO DE PRUEBAS Y COMISIONADO DEL GENERADOR
cover_title: Procedimiento de Pruebas y Comisionado del Generador FV
cover_subtitle: Ensayos de puesta en servicio del arreglo fotovoltaico según IEC 62446-1 e IEC TS 62446-3
---

# 1. OBJETIVO

Definir el método de trabajo, la secuencia de ensayos, los criterios de aceptación y las medidas preventivas para el comisionado formal del generador fotovoltaico (arreglo de módulos, cableado DC, cajas combinadoras y entradas DC de los inversores) de la planta [PROYECTO], conforme a la IEC 62446-1 (categorías 1 y 2), a la IEC TS 62446-3 (termografía), al RETIE y a la NTC 2050 en lo que el RETIE adopta, de modo que el generador quede verificado, documentado y en condición de ser energizado y entregado.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, en especial el choque eléctrico y el arco eléctrico en corriente continua durante los ensayos.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en:

- Inspección visual del generador FV terminado, por bloque y por inversor.
- Ensayos de categoría 1 de la IEC 62446-1: continuidad de conductores de protección y de unión equipotencial, polaridad, ensayo de la caja combinadora, tensión de circuito abierto (Voc) y corriente (Isc o corriente de operación) de strings, ensayos funcionales y resistencia de aislamiento del arreglo.
- Ensayos de categoría 2 de la IEC 62446-1: curva I-V de strings y termografía infrarroja del arreglo según la IEC TS 62446-3.
- Ensayos adicionales cuando el proyecto los exija: aislamiento en húmedo, tensión a tierra en sistemas puestos a tierra por resistencia, diodos de bloqueo, evaluación de sombras.
- Tratamiento de desviaciones, repetición de ensayos y liberación por bloque.
- Compilación de la documentación del sistema exigida por la IEC 62446-1 para la entrega.

No incluye la confección de conectores ni las pruebas DC de string que liberan cada circuito durante el conexionado, que se rigen por NES-OPE-PR-014 y su formato NES-OPE-F-062: este procedimiento es el comisionado formal del generador completo y reutiliza esos registros como antecedente, sin sustituirlos. Tampoco incluye el montaje de cajas combinadoras (NES-OPE-PR-017), el montaje y la puesta en marcha del inversor (NES-OPE-PR-018), ni la energización del lado de corriente alterna y la puesta en servicio ante el [OPERADOR DE RED] (NES-OPE-PR-023).

> NOTA: Los ensayos de categoría 1 se ejecutan con el generador desconectado de la red. Los ensayos funcionales con inversor en operación, la curva I-V bajo carga cuando aplique y la termografía requieren que el inversor inyecte potencia, por lo que solo se ejecutan después de la autorización escrita de energización emitida según NES-OPE-PR-023.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| Comisionado | Conjunto de inspecciones, ensayos y verificaciones documentadas que demuestran que una instalación está construida según diseño, es segura y funciona como se espera, antes de su entrega. |
| Generador FV / arreglo | Conjunto de módulos, strings, cableado DC, cajas combinadoras y protecciones DC hasta los terminales de entrada DC del inversor. |
| String | Circuito de módulos conectados en serie. |
| Caja combinadora (SCB) | Caja que agrupa strings con fusibles o portafusibles y seccionador DC de salida. |
| Categoría 1 (IEC 62446-1) | Régimen mínimo de ensayos aplicable a todo sistema FV: continuidad, polaridad, caja combinadora, Voc, corriente, funcionales y aislamiento. |
| Categoría 2 (IEC 62446-1) | Régimen ampliado para sistemas grandes o complejos: incluye la categoría 1 más curva I-V e inspección termográfica. Solo se inicia con la categoría 1 completa y conforme. |
| Voc | Tensión de circuito abierto del string, sin carga conectada. |
| Isc | Corriente de cortocircuito del string. |
| Corriente de operación | Corriente del string con el inversor en seguimiento del punto de máxima potencia, medida con pinza DC. |
| STC | Condiciones estándar de ensayo: 1.000 W/m², temperatura de célula de 25 °C y espectro AM 1,5. |
| Irradiancia en el plano (POA) | Irradiancia medida en el plano de los módulos, en W/m². |
| Coeficiente β de Voc | Variación porcentual de la Voc por grado de temperatura de célula, declarada en la ficha técnica del módulo (negativa). |
| Curva I-V | Característica corriente-tensión de un string obtenida con trazador, de la que se extraen Isc, Voc, Pmax y factor de forma. |
| Factor de forma (FF) | Relación entre Pmax y el producto Voc × Isc. Su caída indica resistencia serie, sombreado o mismatch. |
| Termografía IR | Registro de la temperatura superficial con cámara infrarroja para detectar anomalías térmicas. |
| CoA | Clase de anomalía de la IEC TS 62446-3: CoA 1 sin anomalía, CoA 2 anomalía térmica, CoA 3 anomalía térmica relevante para la seguridad. |
| Estado térmico estable | Condición de operación sin cambios bruscos de carga ni de irradiancia, necesaria para que la termografía sea representativa. |
| Megóhmetro | Instrumento de medida de resistencia de aislamiento con tensión de ensayo DC seleccionable. |
| PTE | Permiso de trabajo eléctrico. |
| LOTO | Bloqueo y etiquetado de dispositivos de desconexión con candado y tarjeta personal. |
| Punch list | Lista de pendientes y desviaciones abiertas, con responsable y fecha de cierre. |
| Dossier de comisionado | Conjunto de registros, certificados y documentos que se entregan a [CLIENTE] al cierre del comisionado. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. Los bloques, inversores, cajas combinadoras y strings se identifican según el plano general de implantación [N° de plano], el diagrama unifilar DC [N° de plano] y el plano de distribución de strings [N° de plano]. Los ensayos se ejecutan por bloque, en la secuencia que defina el programa de comisionado aprobado por [CLIENTE].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

- Diagrama unifilar DC, plano de distribución de strings, plano del SPT y cuadro de cargas aprobados para construcción — [N° de plano].
- Ficha técnica del módulo: Voc, Isc, Pmax, coeficientes de temperatura, tolerancia de potencia y tensión máxima del sistema.
- Manual del inversor: tensión máxima de entrada DC, condiciones de ensayo de aislamiento admitidas, monitoreo de aislamiento y de corriente residual, secuencia de arranque y parada.
- Manual de la caja combinadora: fusibles, seccionador, DPS y condiciones para ensayos de aislamiento.
- Especificación técnica de comisionado del proyecto y programa de comisionado aprobado por [CLIENTE] — [__________].
- Registros de NES-OPE-PR-014 (NES-OPE-F-060 a NES-OPE-F-063), en particular NES-OPE-F-062 Registro de pruebas DC de string.
- NES-OPE-PR-010 Montaje de módulos; NES-OPE-PR-014 Conexionado DC y conectores MC4; NES-OPE-PR-015 Tendido de cables; NES-OPE-PR-017 Cajas combinadoras; NES-OPE-PR-018 Inversores; NES-OPE-PR-023 Energización y puesta en servicio.
- NES-CAL-PLN-002 Plan de calidad; NES-CAL-PLN-003 Plan de inspección y ensayos eléctrico (PIE eléctrico).
- NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-SST-PLN-001 Plan de emergencias.
- Certificados de calibración vigentes de todos los instrumentos de ensayo.

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes: requisitos de instalación, producto, señalización y dictamen de inspección de la instalación antes de su energización.
- NTC 2050 — Código Eléctrico Colombiano, artículo 690 (Sistemas solares fotovoltaicos), en los requisitos que el RETIE adopta.
- Ley 1264 de 2008 (técnicos electricistas — CONTE); Ley 51 de 1986 y Ley 842 de 2003 (ingenieros — COPNIA): competencia y matrícula profesional del personal que ejecuta y firma ensayos.
- IEC 62446-1 — Sistemas fotovoltaicos: requisitos de ensayo, documentación y mantenimiento. Parte 1: sistemas conectados a la red, documentación, ensayos de puesta en servicio e inspección (edición vigente con su enmienda).
- IEC TS 62446-3 — Termografía infrarroja en exteriores de módulos y plantas fotovoltaicas.
- IEC 62548 — Requisitos de diseño de arreglos fotovoltaicos (referencia técnica).
- IEC 60364-7-712 — Instalaciones eléctricas de baja tensión: sistemas de alimentación solar fotovoltaica (referencia técnica).
- IEC 60891 — Procedimientos de corrección por temperatura e irradiancia de curvas I-V medidas.
- IEC 61829 — Medición en sitio de la característica I-V de arreglos fotovoltaicos.
- IEC 61557 (partes 2 y 4) — Equipos de ensayo de resistencia de aislamiento y de continuidad de conductores de protección (referencia para la selección de instrumentos).
- ISO 9712 — Calificación y certificación del personal de ensayos no destructivos (termógrafos).
- NFPA 70E — Referencia técnica para análisis de riesgo de arco y selección de EPP.
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019 — estándares mínimos.
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en procesos de generación, transmisión, distribución y comercialización de energía eléctrica; cinco reglas de oro.
- Resolución 4272 de 2021 — Trabajo en alturas, cuando haya exposición a 2 m o más.
- Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo.
- Resolución 2184 de 2019 — Código de colores para separación de residuos; Decreto 1076 de 2015 — RESPEL; Ley 1672 de 2013 — RAEE.
- Ley 1715 de 2014; Resolución CREG 075 de 2021 (conexión al SIN); procedimientos del [OPERADOR DE RED] y, si aplica, de XM, para la puesta en servicio.
- Licencia ambiental y Plan de Manejo Ambiental (PMA) del proyecto — [N° de resolución].
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

- Aprobar y divulgar el presente procedimiento y el programa de comisionado por bloque, y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.
- Coordinar con [CLIENTE] los puntos de espera (H) y de testigo (W) del PIE eléctrico y la asistencia de su representante a los ensayos.
- Asegurar que no se energice ningún circuito sin la autorización escrita prevista en NES-OPE-PR-023.
- Detener cualquier ensayo que no cumpla este procedimiento, el diseño o las instrucciones de los fabricantes.

## 6.2. Ingeniero de comisionado (ingeniero electricista con matrícula COPNIA vigente)

- Planificar los ensayos, calcular los valores esperados (Voc corregida, Isc corregida, tensión de ensayo de aislamiento) y preparar las plantillas de registro por bloque.
- Emitir o validar el permiso de trabajo eléctrico de cada sesión de ensayo y definir los puntos de corte.
- Analizar los resultados, clasificar las desviaciones, decidir la repetición de ensayos y firmar los protocolos y el certificado de comisionado del generador.
- Compilar el dossier de comisionado con la documentación del sistema exigida por la IEC 62446-1.

## 6.3. Técnico de pruebas (técnico electricista con matrícula CONTE vigente)

- Ejecutar los ensayos con instrumentos calibrados y según la secuencia de este procedimiento.
- Aplicar el bloqueo y etiquetado, verificar ausencia de tensión cuando aplique y descargar los circuitos después de cada ensayo de aislamiento.
- Registrar los valores medidos en el mismo momento de la medición, con hora, irradiancia y temperatura.

## 6.4. Termógrafo

- Ejecutar la inspección termográfica conforme a la IEC TS 62446-3 con certificación ISO 9712 nivel 1 como mínimo para inspección simplificada, y nivel 2 en termografía eléctrica para inspección detallada y análisis.
- Verificar y registrar las condiciones ambientales y de operación que hacen válida la inspección.
- Clasificar las anomalías según las clases CoA y emitir el informe termográfico.
- Si la termografía es aérea, operar la aeronave no tripulada según la reglamentación de la Aeronáutica Civil de Colombia vigente y el plan de vuelo aprobado por [CLIENTE].

## 6.5. Responsable de calidad (QA/QC)

- Verificar que cada bloque cuente con los registros de NES-OPE-PR-014, NES-OPE-PR-017 y NES-OPE-PR-018 cerrados antes de iniciar el comisionado.
- Controlar los puntos H/W/R del PIE eléctrico (NES-CAL-PLN-003), la trazabilidad instrumento–ensayo–string y el cierre de no conformidades.
- Custodiar los registros originales y los archivos electrónicos de los instrumentos.

## 6.6. Responsable SST

- Elaborar y divulgar la matriz de peligros de los ensayos eléctricos en DC, incluido el riesgo de la tensión de ensayo del megóhmetro.
- Verificar permisos, EPP dieléctrico y de arco, delimitación de la zona de ensayo y competencia del personal.
- Aplicar el protocolo de tormenta eléctrica y liderar la atención de emergencias.

## 6.7. Responsable ambiental

- Asegurar el cumplimiento del PMA y la gestión de los residuos generados (fusibles, conectores, baterías de instrumentos, empaques).

## 6.8. Representante de [CLIENTE]

- Presenciar los ensayos definidos como punto de testigo o de espera, firmar los protocolos y comunicar por escrito sus observaciones.

## 6.9. Trabajadores

- Cumplir este procedimiento y participar en el ATS/ART.
- Usar correctamente el EPP y no tocar conductores, bornes ni estructura durante un ensayo de aislamiento en curso.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Ingeniero de comisionado (COPNIA), técnicos de pruebas (CONTE), termógrafo certificado ISO 9712, auxiliar de registro, QA/QC, responsable SST. Mínimo dos personas por equipo de ensayo. |
| Equipos | Ensayo multifunción FV | Instrumento de ensayo de instalaciones FV, o combinación equivalente, para Voc, Isc, continuidad y aislamiento, con categoría de medida CAT III o superior para la tensión DC máxima del sistema. |
| Equipos | Megóhmetro | Tensiones de ensayo de 250 V, 500 V y 1.000 V DC como mínimo, y la que fije el proyecto para sistemas de 1.500 V; descarga automática del circuito al terminar; conforme a IEC 61557-2. |
| Equipos | Continuidad | Óhmetro de baja resistencia con corriente de ensayo no menor de 200 mA, conforme a IEC 61557-4, con compensación de puntas. |
| Equipos | Corriente | Pinza amperimétrica DC con rango suficiente para la corriente de string y del circuito de salida de la caja combinadora. |
| Equipos | Trazador I-V | Trazador de curva I-V para la tensión y la corriente de string del proyecto, con sensor de irradiancia de referencia y sensor de temperatura de módulo sincronizados. |
| Equipos | Irradiancia y temperatura | Medidor de irradiancia calibrado o célula de referencia montada en el plano de los módulos; termómetro de contacto o sensor de temperatura de módulo; anemómetro portátil. |
| Equipos | Termografía | Cámara infrarroja con sensibilidad térmica (NETD) no mayor de 0,1 K a 30 °C, emisividad y temperatura reflejada ajustables, y resolución suficiente para 5 × 5 píxeles por célula; aeronave no tripulada con cámara radiométrica cuando se use inspección aérea. |
| Equipos | Seguridad del ensayo | Detector de tensión DC, dispositivo de cortocircuito de string apto para la tensión y la Isc del string cuando el método lo exija, kit LOTO, cinta y conos de delimitación, señal de ensayo en curso. |
| Materiales | Registro | Tabletas o planillas impresas de los formatos NES-OPE-F-150 a NES-OPE-F-159, rótulos de ensayado, marcadores indelebles. |
| EPP | Trabajo eléctrico | Guantes dieléctricos de clase acorde con la tensión DC con sobreguante de cuero, verificados antes de cada uso; careta y ropa con la categoría que indique el análisis de riesgo de arco; calzado dieléctrico; sin elementos metálicos personales. |
| EPP | Básico | Casco con barbuquejo, gafas con filtro UV, botas con puntera, chaleco reflectivo, cubrenuca, protector solar, ropa manga larga, polainas en zonas con presencia de ofidios. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

- Bloque mecánicamente terminado: módulos montados (NES-OPE-PR-010), trackers en condición de operación o asegurados en posición de ensayo, cableado DC soportado y conectorizado (NES-OPE-PR-014).
- Registros de construcción del bloque cerrados: NES-OPE-F-060 a NES-OPE-F-063, protocolos de cajas combinadoras (NES-OPE-PR-017) y de montaje del inversor (NES-OPE-PR-018), y protocolos de tendido de cables (NES-OPE-PR-015).
- Sistema de puesta a tierra del bloque terminado y medido según el diseño del SPT del proyecto.
- Unifilar DC y plano de strings vigentes en el frente, con rotulación física verificada.
- Valores esperados calculados por string tipo: Voc y Isc a STC, coeficientes de temperatura, número de módulos en serie, tensión de ensayo de aislamiento.
- Instrumentos con certificado de calibración vigente, baterías cargadas y verificación funcional del megóhmetro y del óhmetro en un patrón o resistencia conocida al inicio de la jornada.
- PTE, ATS/ART y charla de inicio de turno diligenciados; LOTO disponible para cada ejecutante.
- Condiciones climáticas aptas: sin lluvia, sin humedad sobre conectores y bornes, sin tormenta eléctrica. Para ensayos de corriente, I-V y termografía, irradiancia estable y suficiente según el ensayo.
- Inversores del bloque en parada y seccionados del lado DC, salvo en los ensayos funcionales que exijan su operación.

> ALTO: No se inicia el comisionado de un bloque con registros de construcción abiertos, con conectores sin enclavar o con cajas combinadoras sin tapa. Lo que no está terminado no se ensaya.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

El comisionado se organiza por bloque, inversor y caja combinadora. Se delimitan y señalizan: el punto de ensayo (caja combinadora o entrada del inversor), el tramo de strings bajo ensayo y la zona de exclusión durante los ensayos de aislamiento. Durante un ensayo de aislamiento todo el circuito ensayado, incluidos los módulos y la estructura asociada, se considera zona de peligro y solo permanece el personal de ensayo.

### 8.2.2. Ingreso de personal

- Evaluar las condiciones del área y verificar que no haya trabajos simultáneos en el mismo circuito ni en circuitos adyacentes del mismo inversor.
- Diligenciar ATS/ART, permiso de trabajo y PTE; verificar matrícula profesional vigente de quien ejecuta y firma.
- Ubicar equipos de emergencia e inspeccionar el EPP dieléctrico y de arco.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional de vehículos y equipos y circulación solo por rutas autorizadas.
- Los vehículos no estacionan sobre cableado, cajas de paso ni zanjas abiertas, ni dentro de la zona de exclusión del ensayo.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Principios del comisionado del generador

El comisionado sigue tres principios:

1. Secuencia: primero la inspección, luego los ensayos de categoría 1 y solo con estos conformes los de categoría 2. Un ensayo posterior no compensa uno anterior fallido.
2. Comparación: en un generador con muchos strings idénticos, el mejor detector de defectos es la comparación entre strings del mismo tipo medidos en las mismas condiciones, además de la comparación contra el valor esperado.
3. Trazabilidad: cada valor queda asociado a un string, un instrumento calibrado, una hora, una irradiancia y una temperatura. Un valor sin condiciones de medida no es evidencia de comisionado.

La IEC 62446-1 admite que en arreglos grandes ciertos ensayos se ejecuten sobre subarreglos o agrupaciones de strings en lugar de string por string, cuando el diseño y la especificación del proyecto lo permitan. El nivel de desagregación se define en el programa de comisionado aprobado por [CLIENTE].

#### 8.2.4.2. Seguridad del ensayo en corriente continua

- El arreglo genera tensión siempre que recibe luz. Todo ensayo se ejecuta tratando el circuito como energizado.
- La corriente continua no pasa por cero: ningún conector, portafusibles ni borne se abre bajo corriente. La apertura de strings se hace con el seccionador de la caja combinadora o del inversor y con corriente verificada en 0,0 A, según NES-OPE-PR-014.
- La Isc se mide solo con el instrumento de ensayo, con el trazador I-V o con un dispositivo de cortocircuito apto para la tensión y la corriente del string. Prohibido cortocircuitar con puentes, cables o pinzas improvisadas.
- El ensayo de aislamiento inyecta una tensión DC adicional: se delimita la zona, nadie toca el circuito ni la estructura mientras dura y el circuito se descarga con el instrumento antes de desconectar las puntas.
- Las puntas de prueba se conectan primero al instrumento y luego al circuito, y se retiran en orden inverso. Las puntas tienen protección contra contacto y categoría de medida acorde.
- Un ensayo de aislamiento no se ejecuta con humedad sobre conectores o bornes, salvo el ensayo en húmedo específico, ni con personal sobre las mesas.
- Las cinco reglas de oro del RETIE y de la Res. 5018 de 2019 se aplican a toda intervención en la caja combinadora y en el inversor, con LOTO según NES-SST-PR-001.

> ALTO: Prohibido medir Isc cerrando un cortocircuito con conectores o puentes improvisados, y prohibido abrir el cortocircuito de un string sin antes reducir la corriente a cero con el dispositivo de ensayo. Abrir un string en cortocircuito bajo luz produce un arco DC sostenido.

#### 8.2.4.3. Inspección visual

Se ejecuta antes de cualquier ensayo, por bloque, y se registra en NES-OPE-F-151. Cubre como mínimo:

| Elemento | Verificación |
|---|---|
| Sistema DC general | Instalación conforme al diseño aprobado y al unifilar; componentes DC con tensión y corriente nominales aptas para la tensión máxima del sistema y la corriente de diseño. |
| Protección contra choque | Partes activas protegidas por envolvente o aislamiento; cajas cerradas con tapa y grado IP de diseño. |
| Módulos | Sin vidrio roto, sin marcos deformados, sin cajas de conexión abiertas, sin suciedad o sombras anómalas; fijación conforme a NES-OPE-PR-010. |
| Cableado DC | Cable solar de la sección de diseño, soportado, sin contacto con suelo, agua ni bordes vivos, con radio de curvatura respetado y holgura para el giro del tracker. |
| Conectores | Pares macho-hembra de la misma referencia, acoplados y enclavados, con sello presente; sin conectores abiertos ni sin tapón. |
| Cajas combinadoras | Fusibles de la capacidad de diseño, seccionador operativo, DPS instalados y señalizados, entradas estancas, rótulos de strings legibles. |
| Puesta a tierra y equipotencialidad | Conductores de protección y de unión equipotencial instalados según diseño, con terminales apretados y marcados. |
| Protección contra sobretensiones | DPS del tipo y la tensión de diseño, con indicador de estado en verde y conductor de tierra corto y directo. |
| Inversor | Entradas DC correctamente polarizadas y rotuladas, seccionador DC operativo, ventilación libre. |
| Señalización | Rótulos de advertencia de tensión DC y de doble alimentación en cajas combinadoras, inversores y puntos de desconexión, según el RETIE; identificación del seccionador DC principal. |

#### 8.2.4.4. Continuidad de conductores de protección y de unión equipotencial

1. Identificar en el plano del SPT los conductores de protección y de unión equipotencial del bloque: estructura de tracker, marcos de módulo cuando el diseño lo exija, cajas combinadoras, bandejas, inversor y barra de tierra.
2. Verificar ausencia de tensión entre la parte a ensayar y la tierra antes de conectar el óhmetro.
3. Compensar la resistencia de las puntas del óhmetro de baja resistencia (corriente de ensayo no menor de 200 mA).
4. Medir la continuidad entre cada elemento y la barra o punto de tierra de referencia del bloque, incluyendo las uniones entre secciones de estructura y entre mesas.
5. Registrar el valor en NES-OPE-F-152. El valor debe ser coherente con la longitud y la sección del conductor y con los valores de elementos similares; el valor límite lo fija la especificación del proyecto — [__________].
6. Toda lectura anómala o inestable obliga a inspeccionar el terminal, la arandela, la superficie de contacto y la tornillería antes de repetir.

> NOTA: La continuidad de protección es requisito previo del ensayo de aislamiento: sin una referencia de tierra continua y medida, el resultado del aislamiento no es válido.

#### 8.2.4.5. Polaridad y ensayo de la caja combinadora

1. Con los fusibles retirados y el seccionador de salida abierto, medir en cada entrada de la caja combinadora la tensión de cada string con multímetro CAT III o superior.
2. Verificar que la polaridad coincide con la rotulación y con el unifilar: positivo al borne positivo y negativo al borne negativo.
3. Verificar que ningún string presenta tensión invertida respecto de los demás. Una polaridad invertida dentro de una caja combinadora con fusibles insertados provoca circulación de corriente inversa a través del string invertido.
4. Verificar que no hay tensión entre cada polo y tierra superior a la esperada para el esquema de tierra del sistema; una lectura franca a tierra indica falla de aislamiento y suspende la secuencia.
5. Comparar las tensiones de los strings de la misma caja: deben ser del mismo orden. Una diferencia equivalente a la tensión de uno o más módulos indica error en el número de módulos en serie, un módulo en cortocircuito o un diodo de bypass conduciendo.
6. Registrar en NES-OPE-F-153 y no insertar fusibles mientras haya una desviación abierta.

#### 8.2.4.6. Tensión de circuito abierto (Voc) de strings

1. Medir la Voc de cada string en la caja combinadora o en la entrada del inversor, con el string abierto y sin carga.
2. Registrar simultáneamente la irradiancia en el plano, la temperatura de módulo (o la ambiente y la estimación de temperatura de célula) y la hora.
3. Calcular la Voc esperada: Voc esperada = N × Voc STC × [1 + β × (T célula − 25 °C)], donde N es el número de módulos en serie y β el coeficiente de Voc de la ficha técnica en por unidad por °C.
4. Comparar el valor medido contra la Voc esperada y contra los strings del mismo tipo medidos en las mismas condiciones.
5. Criterio: en strings idénticos y con irradiancia estable, las Voc deben ser iguales dentro de la tolerancia de comparación; la referencia habitual de la IEC 62446-1 es una diferencia típica no mayor de 5 %. El criterio definitivo lo fija la especificación del proyecto.
6. Una Voc baja en una cantidad próxima a la Voc de un módulo indica módulo faltante, conexión errónea o diodo de bypass en cortocircuito; una Voc nula indica circuito abierto; una Voc mayor que la esperada indica módulos de más en el string. Se registra como desviación y se investiga.

> NOTA: La Voc depende poco de la irradiancia y mucho de la temperatura de célula. Los strings que se comparan entre sí se miden en un intervalo corto, sin cambio apreciable de nubosidad, para que la temperatura sea comparable.

#### 8.2.4.7. Corriente de strings (Isc o corriente de operación)

La IEC 62446-1 admite dos métodos; el programa de comisionado define cuál se aplica:

| Método | Ejecución | Condiciones |
|---|---|---|
| Cortocircuito (Isc) | Con el instrumento de ensayo FV, el trazador I-V o un dispositivo de cortocircuito apto para la tensión y la Isc del string, con el string aislado de los demás. | String abierto del resto; fusibles retirados; nunca con puentes improvisados; irradiancia estable registrada. |
| Corriente de operación | Con el inversor operando en seguimiento del punto de máxima potencia, medir con pinza DC la corriente de cada string. | Solo con autorización de energización (NES-OPE-PR-023); irradiancia estable; inversor fuera de limitación de potencia. |

1. Registrar la irradiancia en el plano en el momento de cada medida.
2. Calcular la Isc esperada: Isc esperada ≈ Isc STC × (G medida / 1.000 W/m²), con la corrección por temperatura que indique la ficha técnica (coeficiente α, de efecto menor).
3. Comparar contra la Isc esperada y, sobre todo, contra los strings del mismo tipo medidos en las mismas condiciones.
4. Criterio de referencia: en strings idénticos y con irradiancia estable, las corrientes deben ser iguales dentro de la tolerancia de comparación; se adopta una diferencia no mayor de 5 % respecto de la media de los strings del mismo tipo (criterio interno; el valor definitivo lo fija la especificación del proyecto).
5. Las medidas de corriente se ejecutan con irradiancia suficiente y estable para que la comparación sea significativa; el umbral de irradiancia mínima lo fija el programa de comisionado — [____] W/m².
6. Corriente baja en un string con Voc normal indica sombreado, suciedad, módulo degradado, conector con alta resistencia o fusible fundido; se registra y se investiga.

#### 8.2.4.8. Ensayos funcionales

1. Seccionadores DC de cajas combinadoras y del inversor: maniobra mecánica completa, enclavamiento, indicación de posición y bloqueo con candado.
2. Fusibles y portafusibles: capacidad conforme al diseño y apertura del portafusibles solo sin carga.
3. DPS: indicador de estado conforme y conexión a tierra verificada.
4. Inversor: con autorización de energización, arranque y parada según el protocolo del fabricante, verificación de la medida de aislamiento DC y de la vigilancia de corriente residual que informe el equipo, y comportamiento ante apertura del seccionador DC.
5. Monitoreo: comunicación de las medidas de string o de caja combinadora con el sistema de supervisión, cuando el proyecto lo incluya (ver NES-OPE-PR-021).
6. Parada de emergencia y desconexión remota cuando el diseño las incluya.
7. Registrar en NES-OPE-F-155.

#### 8.2.4.9. Resistencia de aislamiento del arreglo

Se ejecuta con el arreglo desconectado del inversor y de cualquier equipo que pueda dañarse o falsear la medida, por el método que defina el programa de comisionado entre los dos de la IEC 62446-1:

| Método | Descripción |
|---|---|
| Método 1 | Ensayo entre el polo negativo del arreglo y tierra, seguido del ensayo entre el polo positivo y tierra. |
| Método 2 | Ensayo entre tierra y el polo positivo y el negativo del arreglo cortocircuitados entre sí mediante un dispositivo de cortocircuito apto para la tensión y la corriente del arreglo. |

Tensiones de ensayo y valores mínimos de la IEC 62446-1 (tabla de la edición 2016 con su enmienda de 2018; confirmar contra la copia vigente adquirida por el proyecto antes de ensayar):

| Tensión del sistema (Voc STC × 1,25) | Tensión de ensayo | Resistencia mínima |
|---|---|---|
| Menor de 120 V | 250 V DC | 0,5 MΩ |
| De 120 V a 500 V | 500 V DC | 1 MΩ |
| Mayor de 500 V hasta 1.000 V | 1.000 V DC | 1 MΩ |
| Mayor de 1.000 V (sistemas de 1.500 V) | Según especificación del proyecto y edición vigente de la norma — [____] V DC | Según especificación del proyecto — [____] MΩ |

> NOTA: La enmienda de 2018 ajustó el ámbito de la tabla de valores mínimos (arreglos pequeños) e introdujo flexibilidad para ensayar arreglos grandes por subarreglos. En plantas utility-scale con sistemas de 1.500 V, la tensión de ensayo, el valor mínimo y el nivel de agrupación se fijan en la especificación de comisionado del proyecto con base en la edición vigente de la IEC 62446-1 y en lo que admitan el fabricante del módulo, del inversor y de la caja combinadora. No se aplica una tensión de ensayo mayor que la admitida por los equipos conectados.

Secuencia:

1. Emitir el PTE, aplicar LOTO en el seccionador DC del inversor y en la caja combinadora y verificar corriente 0,0 A.
2. Desconectar o aislar los DPS y cualquier equipo de vigilancia de aislamiento que puedan afectar la medida o dañarse, según el manual de la caja combinadora.
3. Delimitar la zona de exclusión y avisar por radio el inicio del ensayo.
4. Para el método 2, instalar el dispositivo de cortocircuito con el seccionador abierto y cerrarlo solo con el dispositivo previsto; nunca con puentes.
5. Conectar el megóhmetro: borne de tierra a la barra de tierra del bloque, borne de ensayo al polo o al punto común de cortocircuito.
6. Aplicar la tensión de ensayo durante el tiempo que fije el instrumento o el programa de comisionado, hasta lectura estable, y registrar el valor.
7. Descargar el circuito con el propio instrumento y verificar ausencia de tensión de ensayo antes de desconectar las puntas.
8. Para el método 2, abrir el cortocircuito solo con la corriente reducida a cero mediante el dispositivo de ensayo.
9. Reconectar DPS y equipos aislados y registrar en NES-OPE-F-154 el método, la tensión de ensayo, la temperatura, la humedad relativa y el valor.

Un valor inferior al mínimo o claramente inferior al de circuitos similares indica conector húmedo o mal sellado, cable dañado por roce o por roedores, módulo con falla de aislamiento o caja con ingreso de agua. Se localiza la falla subdividiendo el circuito, se corrige y se repite el ensayo.

> ALTO: Durante el ensayo de aislamiento nadie toca el circuito, la estructura ni los módulos ensayados. Al terminar, el circuito puede quedar cargado: se descarga con el instrumento antes de retirar las puntas.

#### 8.2.4.10. Ensayos adicionales

Se ejecutan cuando la especificación del proyecto los exija o cuando los resultados de categoría 1 lo justifiquen:

- Aislamiento en húmedo: para localizar fallas de aislamiento que solo aparecen con humedad, mojando la parte del arreglo bajo ensayo con agua y agente humectante según el método de la IEC 62446-1. Se coordina con el área ambiental el manejo del agua.
- Tensión a tierra en sistemas puestos a tierra por resistencia: verificación según la documentación del fabricante del módulo y del inversor.
- Diodos de bloqueo, cuando el diseño los incluya: verificación de conexión y de ausencia de sobrecalentamiento.
- Evaluación de sombras: registro de obstáculos y sombras mutuas entre filas que afecten el rendimiento, en especial al inicio y al final del día con trackers.

#### 8.2.4.11. Curva I-V de strings (categoría 2)

1. Ejecutar solo sobre strings con categoría 1 conforme y con el string aislado del inversor.
2. Montar el sensor de irradiancia de referencia en el plano de los módulos del string ensayado y el sensor de temperatura en la cara posterior de un módulo representativo, lejos de los bordes y de la caja de conexión.
3. Ejecutar con irradiancia estable no menor de 400 W/m² en el plano, que es el mínimo de la IEC 62446-1 para mediciones de desempeño de string. Cuando los resultados se trasladen a STC se busca irradiancia no menor de 700 W/m², que es la recomendación de la IEC 61829.
4. Trazar la curva, verificar que no presenta escalones, inflexiones ni pendientes anómalas y registrar Isc, Voc, Imp, Vmp, Pmax y factor de forma.
5. Trasladar a STC con los procedimientos de la IEC 60891 y comparar contra el valor nominal del string, considerando la tolerancia de potencia del módulo, las pérdidas de cableado y la incertidumbre del instrumento.
6. Comparar las curvas de strings del mismo tipo. Escalones en la curva indican diodos de bypass activos por sombreado, suciedad o célula dañada; pendiente reducida en la zona de tensión indica resistencia serie elevada (conector o crimpado deficiente); pendiente en la zona de corriente indica resistencia en paralelo baja.
7. Criterio de aceptación: el que fije la especificación del proyecto para la desviación de Pmax trasladada a STC y para el factor de forma — [__________]. A falta de criterio del proyecto, toda curva con forma anómala o con Pmax claramente inferior a la de los strings vecinos se investiga antes de liberar (criterio interno).
8. Registrar en NES-OPE-F-156 y conservar el archivo electrónico de cada curva con identificación del string.

#### 8.2.4.12. Inspección termográfica (categoría 2, IEC TS 62446-3)

Condiciones que hacen válida la inspección, según la IEC TS 62446-3:

| Parámetro | Condición |
|---|---|
| Irradiancia en el plano | No menor de 600 W/m² para la inspección de módulos. |
| Estabilidad | Parte inspeccionada en estado térmico estable. Tras un cambio de carga o de irradiancia mayor de 10 % por minuto, esperar 15 minutos antes de registrar. |
| Nubosidad | No mayor de 2 octas de nubes cúmulos. |
| Viento | No mayor de 4 en la escala Beaufort (28 km/h como máximo). |
| Operación | Inversor operando y generador bajo carga normal; registrar la condición de operación de cada string inspeccionado. |
| Suciedad y sombras | Módulos sin suciedad apreciable y sin sombras parciales durante la inspección, en lo posible. |
| Cámara | NETD no mayor de 0,1 K a 30 °C; resolución mínima de 5 × 5 píxeles por célula; emisividad y temperatura reflejada ajustadas. |
| Ángulo de observación | El que indica la norma para limitar la reflexión del entorno sobre el vidrio; verificar en la edición vigente y registrar el ángulo usado. |

Tipos de inspección:

- Inspección simplificada: verifica que módulos y componentes funcionan e identifica anomalías evidentes. Puede ejecutarla personal con certificación ISO 9712 nivel 1. No permite conclusiones de calidad del módulo.
- Inspección detallada: incluye análisis de las firmas térmicas y, cuando aplica, mediciones de temperatura absolutas. La ejecuta o supervisa un termógrafo con certificación ISO 9712 nivel 2 en termografía eléctrica.

Secuencia:

1. Verificar y registrar irradiancia, temperatura ambiente, viento, nubosidad y hora al inicio y periódicamente durante la inspección.
2. Inspeccionar módulos (cara frontal), cajas de conexión de módulo cuando sean accesibles, conectores y cableado, cajas combinadoras con la tapa retirada por personal autorizado y con EPP de arco, y entradas DC del inversor.
3. Clasificar cada anomalía según la matriz de la IEC TS 62446-3: CoA 1 sin anomalía; CoA 2 anomalía térmica, que se investiga y se planifica su corrección; CoA 3 anomalía térmica relevante para la seguridad, que exige acción inmediata.
4. Para conectores, fusibles y bornes, comparar contra componentes iguales con la misma carga. Un conector claramente más caliente que el cable adyacente o que sus pares indica crimpado deficiente o acople incompleto y se interviene según NES-OPE-PR-014.
5. Registrar cada anomalía con imagen térmica y visual, ubicación (bloque, fila, mesa, posición del módulo, número de serie si es accesible), condiciones de medida y clase; resumir en NES-OPE-F-157.
6. Emitir el informe termográfico con el contenido que exige la norma: datos del sitio y del sistema, condiciones ambientales, equipo y su calibración, personal y su certificación, método, lista de anomalías clasificadas y recomendaciones.

> NOTA: En inspección aérea, la altura y la velocidad de vuelo se fijan para cumplir la resolución mínima por célula de la norma; el plan de vuelo, los permisos y la coordinación con la operación del sitio se tramitan antes de la jornada.

#### 8.2.4.13. Tratamiento de desviaciones

1. Toda medida fuera de criterio se registra en el formato del ensayo y se abre en el registro de desviaciones NES-OPE-F-158 con número, string, valor, criterio, causa probable y acción.
2. La desviación se investiga en campo: inspección visual dirigida, repetición de la medida, subdivisión del circuito, comparación con strings vecinos.
3. La corrección se ejecuta con el procedimiento que corresponda (NES-OPE-PR-010 para módulos, NES-OPE-PR-014 para conectores y cableado, NES-OPE-PR-017 para cajas combinadoras) y con su propio PTE.
4. Tras la corrección se repiten el ensayo fallido y todos los ensayos que la intervención pudo afectar; como mínimo polaridad, Voc y aislamiento del circuito intervenido.
5. Las desviaciones que no afectan la seguridad ni el desempeño pueden aceptarse como pendientes de entrega con aprobación escrita de [CLIENTE] y se incluyen en el punch list con fecha de cierre.
6. Los módulos con defecto confirmado se tramitan como reclamación ante el fabricante del módulo con la evidencia del ensayo (curva I-V, termografía, fotografía, número de serie).

| Clasificación | Ejemplos | Tratamiento |
|---|---|---|
| A — Bloqueante | Falla de aislamiento, polaridad invertida, CoA 3, conector con evidencia de arco, continuidad de protección ausente. | El circuito no se energiza ni se libera hasta corregir y repetir el ensayo. |
| B — Corregir antes de la entrega | Voc o corriente fuera de criterio, CoA 2, curva I-V anómala, rotulación incompleta. | Corrección planificada y repetición del ensayo antes del certificado de comisionado. |
| C — Observación | Desviación documental o estética sin efecto en seguridad ni desempeño. | Registro en punch list y cierre en la fecha acordada. |

#### 8.2.4.14. Documentación del sistema y cierre del comisionado

La IEC 62446-1 exige que, al terminar la instalación, se entregue documentación que permita operar, mantener e inspeccionar el sistema. El dossier de comisionado del generador contiene como mínimo:

- Datos básicos del sistema: potencia nominal DC y AC, cantidad y referencia de módulos e inversores, fechas de instalación y de comisionado, [PROPIETARIO], ubicación, y datos de Neptuno Energy Services como instalador y del diseñador.
- Diagrama unifilar actualizado según lo construido, con tipo y cantidad de módulos, conformación de strings y subarreglos, secciones de conductores, capacidad de protecciones, DPS y puntos de desconexión.
- Plano de distribución de strings (obligatorio cuando el sistema tiene tres o más strings), con la identificación de cada string.
- Fichas técnicas de módulos, inversores, cajas combinadoras, conectores y cables.
- Información del sistema de montaje (tracker o estructura) y de su puesta a tierra.
- Información de operación y mantenimiento: verificación del funcionamiento, actuación ante falla, procedimiento de parada y desconexión de emergencia.
- Resultados de todos los ensayos de este procedimiento, con identificación y calibración de los instrumentos.
- Informe termográfico y archivos de curvas I-V cuando se ejecuten.
- Registro de desviaciones cerrado y punch list aceptado.
- Certificado de comisionado del generador NES-OPE-F-159 firmado.

El certificado de comisionado del generador es requisito de entrada para la inspección RETIE del lado DC y para la secuencia de energización de NES-OPE-PR-023. El dictamen de inspección RETIE y la autorización del [OPERADOR DE RED] y, si aplica, de XM, se tramitan en ese procedimiento.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Inspección visual | Sin hallazgos bloqueantes; lista NES-OPE-F-151 completa | IEC 62446-1 / Este procedimiento |
| Continuidad de protección | Continuidad en todos los elementos; valor coherente con longitud y sección y no superior al límite del proyecto — [__________] | IEC 62446-1 / Especificación del proyecto |
| Polaridad | Coincidente con el unifilar en el 100 % de los strings, antes de insertar fusibles | IEC 62446-1 |
| Voc de string | Coherente con la Voc esperada corregida por temperatura; diferencia entre strings idénticos típicamente no mayor de 5 % | IEC 62446-1 / Especificación del proyecto |
| Corriente de string | Coherente con la Isc esperada corregida por irradiancia; diferencia no mayor de 5 % respecto de la media de strings idénticos (criterio interno) | IEC 62446-1 / Criterio interno |
| Resistencia de aislamiento hasta 1.000 V | Tensión de ensayo y mínimo según la tabla de la IEC 62446-1 vigente (sistemas mayores de 500 V hasta 1.000 V: ensayo a 1.000 V, mínimo 1 MΩ) | IEC 62446-1 |
| Resistencia de aislamiento en sistemas de 1.500 V | Tensión de ensayo y mínimo fijados en la especificación del proyecto — [__________] | Especificación del proyecto / IEC 62446-1 |
| Ensayos funcionales | Seccionadores, protecciones, DPS e inversor operan según diseño y manual | IEC 62446-1 / Manuales de fabricante |
| Curva I-V | Irradiancia estable no menor de 400 W/m²; forma sin anomalías; Pmax trasladada a STC dentro del criterio del proyecto — [__________] | IEC 62446-1 / IEC 60891 / IEC 61829 |
| Termografía | Condiciones válidas de la IEC TS 62446-3; ninguna anomalía CoA 3 abierta; CoA 2 con plan de corrección aceptado | IEC TS 62446-3 |
| Documentación | Dossier completo según la IEC 62446-1 | IEC 62446-1 |
| Personal | Ejecuta técnico CONTE; firma ingeniero COPNIA; termógrafo con certificación ISO 9712 | Ley 1264 de 2008 / Ley 842 de 2003 / IEC TS 62446-3 |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-150 a NES-OPE-F-159 de este procedimiento.
- Registros de construcción del bloque (NES-OPE-F-060 a NES-OPE-F-063 y los de NES-OPE-PR-015, NES-OPE-PR-017 y NES-OPE-PR-018).
- PTE, ATS/ART y registros de LOTO de cada sesión de ensayo.
- Certificados de calibración de instrumentos y certificados ISO 9712 de los termógrafos.
- Archivos electrónicos de los instrumentos (curvas I-V, imágenes térmicas, registros de aislamiento) con identificación del string.

## 8.5. Control de calidad

QA/QC verifica el 100 % de los strings en los ensayos de categoría 1 y la muestra o la totalidad de categoría 2 que defina el programa de comisionado. Los puntos de espera y de testigo de [CLIENTE] son los del PIE eléctrico NES-CAL-PLN-003. QA/QC revisa al cierre de cada jornada que los registros estén completos, con condiciones de medida y firmas, y que cada valor fuera de criterio tenga su desviación abierta. Un ensayo ejecutado con instrumento de calibración vencida se anula y se repite. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación documental o de registro que no afecta la validez del ensayo. | Corrección del registro y cierre. |
| 2 | Ensayo fuera de criterio corregible con los procedimientos de construcción. | Corrección, repetición del ensayo y cierre por QA/QC. |
| 3 | Afecta la seguridad eléctrica, la garantía o la conformidad RETIE: falla de aislamiento recurrente, CoA 3, defecto de serie de módulos, polaridad invertida con daño. | Suspensión del bloque, consulta al diseñador eléctrico y al fabricante, y aprobación escrita antes de actuar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS/ART y la charla diaria, verifica que las zonas de ensayo estén señalizadas y demarcadas y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre riesgo eléctrico en corriente continua, arco eléctrico, riesgo de la tensión de ensayo, puntos de encuentro y uso del EPP dieléctrico y de arco.

## 9.1. Reglas de oro

- **SIEMPRE** trataré todo string y todo arreglo como energizados mientras reciban luz.
- **SIEMPRE** aplicaré las cinco reglas de oro y el bloqueo y etiquetado antes de intervenir una caja combinadora o un inversor (Res. 5018 de 2019).
- **NUNCA** mediré Isc con puentes o cortocircuitos improvisados.
- **NUNCA** abriré un conector, un portafusibles o un cortocircuito de ensayo con corriente circulando.
- **NUNCA** tocaré el circuito, los módulos ni la estructura durante un ensayo de aislamiento.
- **SIEMPRE** descargaré el circuito con el instrumento al terminar un ensayo de aislamiento.
- **SIEMPRE** usaré instrumentos calibrados, con categoría de medida acorde a la tensión del sistema y puntas en buen estado.
- **SIEMPRE** trabajaré acompañado y con radio.
- **SIEMPRE** suspenderé los ensayos ante lluvia o tormenta eléctrica y me dirigiré al refugio.
- **SIEMPRE** ejecutaré los ensayos con ATS/ART y PTE diligenciados.

## 9.2. Condiciones climáticas de [departamento]

- Tormenta eléctrica: ante el aviso o el primer trueno, suspender todo ensayo, dejar los circuitos abiertos y bloqueados, retirar las puntas y alejarse de estructuras metálicas y conductores. Se reanuda solo con autorización del responsable SST.
- Lluvia y rocío: no ejecutar ensayos de aislamiento ni abrir cajas combinadoras con humedad; la humedad falsea el resultado y aumenta el riesgo.
- Calor y radiación: los ensayos de corriente, I-V y termografía exigen alta irradiancia, que coincide con la mayor carga térmica. Hidratación, sombra, pausas y rotación; la estructura y las cajas expuestas al sol se manipulan con guante.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado al bloque | Colisión, volcamiento, caídas al mismo nivel. | Conductores autorizados; vías y velocidades del proyecto; cinturón obligatorio. |
| 2. Preparación de instrumentos y EPP | Instrumento descalibrado o con puntas dañadas; EPP vencido. | Verificación funcional diaria; certificados vigentes; inspección de guantes y careta. |
| 3. Inspección visual | Contacto con partes activas, cortes con bordes, caídas. | No abrir envolventes sin PTE; guantes; atención al terreno. |
| 4. Apertura de cajas combinadoras y seccionamiento | Choque eléctrico, arco al maniobrar bajo carga. | PTE; inversor en parada; seccionador abierto; 0,0 A verificados; LOTO; EPP de arco. |
| 5. Continuidad de protección | Contacto con elemento energizado por falla. | Verificar ausencia de tensión antes de conectar el óhmetro. |
| 6. Polaridad y Voc | Choque eléctrico, cortocircuito con las puntas. | Multímetro CAT III o superior; puntas con protección; una mano cuando sea posible; fusibles retirados. |
| 7. Medida de Isc | Arco DC al abrir el cortocircuito, quemaduras. | Solo instrumento o dispositivo de cortocircuito apto; prohibidos los puentes; EPP de arco. |
| 8. Ensayo de aislamiento | Choque por tensión de ensayo, carga residual, daño a equipos. | Zona de exclusión; aviso por radio; DPS y equipos sensibles aislados; descarga con el instrumento. |
| 9. Ensayos funcionales con inversor operando | Choque eléctrico, arco, energización imprevista. | Solo con autorización de energización (NES-OPE-PR-023); maniobras según manual; personal autorizado. |
| 10. Curva I-V | Choque al conectar el trazador, quemaduras por superficies calientes. | String aislado del inversor; conexión con seccionador abierto; guantes. |
| 11. Termografía terrestre o aérea | Arco al retirar tapas de cajas bajo carga; caída de aeronave; atropellamiento. | Tapas retiradas solo por personal autorizado con EPP de arco; plan de vuelo; zona de despegue delimitada. |
| 12. Trabajo sobre mesas altas o plataformas | Caída a distinto nivel. | Plataforma o escalera certificada; Res. 4272 de 2021 cuando haya exposición a 2 m o más. |
| 13. Exposición ambiental | Radiación UV, estrés térmico, deshidratación, ofidios. | Ropa manga larga, cubrenuca, protector solar, hidratación, sombra, pausas; polainas. |
| 14. Tormenta eléctrica y lluvia | Descarga atmosférica, choque eléctrico. | Suspender; circuitos abiertos y bloqueados; refugio o punto de encuentro. |
| 15. Cierre de jornada | Circuito dejado en estado inseguro. | Registro del estado de cada circuito; bloqueos que permanecen con tarjeta; cajas cerradas. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Aire | Emisiones y ruido | Vehículos con revisión técnico-mecánica al día; motores apagados en reposo; humectación de vías en época seca. |
| Suelo | Residuos sólidos | Separación en la fuente con el código de colores de la Res. 2184 de 2019; empaques y papelería a aprovechamiento; entrega a gestores autorizados. |
| Suelo | Fusibles, conectores y componentes retirados | Recolección en recipiente rotulado y gestión como RAEE según la Ley 1672 de 2013. |
| Suelo | Baterías de instrumentos | Recolección separada y entrega a programa posconsumo o gestor autorizado. |
| Suelo | RESPEL | Trapos y absorbentes contaminados, en recipientes rotulados y entregados a gestor autorizado (Decreto 1076 de 2015). |
| Agua | Ensayo de aislamiento en húmedo | Uso mínimo de agua; agente humectante biodegradable aprobado por el área ambiental; sin vertimiento a cuerpos de agua. |
| Flora y fauna | Intervención de hábitat | Trabajar solo en áreas liberadas; revisar fauna dentro de cajas combinadoras antes de abrirlas; reporte para rescate según PMA. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con el Plan de emergencias NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener el ensayo y asegurar la zona: apagar el instrumento, abrir el seccionador DC del circuito desde un punto seguro y alejar al personal.
2. Notificar al responsable SST, al ingeniero de comisionado y al interlocutor de [CLIENTE].
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, extintor en cada frente).
4. Incidente grave: activar ambulancia y traslado al centro asistencial definido; notificar a la ARL.
5. Reportar el evento e investigarlo según la Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Arco eléctrico en corriente continua durante un ensayo

- No intentar apagar el arco separando conectores o retirando puntas: el arco DC no se autoextingue.
- Cortar la corriente desde el seccionador de la caja combinadora o del inversor, fuera de la línea de proyección del arco.
- Conato de incendio en circuito energizado: extintor apto para equipo eléctrico energizado; nunca agua. Si el fuego avanza, evacuar y activar la emergencia.
- Delimitar la zona y no reenergizar hasta la inspección del ingeniero de comisionado.

## 12.2. Choque eléctrico por tensión de ensayo o del arreglo

- No tocar a la víctima mientras siga en contacto con el circuito; apagar el instrumento, abrir el seccionador o separarla con elemento aislante.
- Activar la emergencia y aplicar reanimación si el personal está capacitado.
- Toda persona que sufra un choque eléctrico se remite a valoración médica aunque se sienta bien.
- Quemaduras: enfriar con agua limpia a temperatura ambiente, no retirar ropa adherida, cubrir con apósito estéril y remitir a valoración.

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Ingeniero de comisionado Neptuno Energy Services | [__________] | [__________] |
| Residente de obra Neptuno Energy Services | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| Centro de control / sala de operación | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Permiso de ensayo y control de riesgos DC | NES-OPE-F-150 | Ingeniero de comisionado |
| Inspección visual del generador FV | NES-OPE-F-151 | Técnico de pruebas / QA/QC |
| Continuidad de conductores de protección y equipotencialidad | NES-OPE-F-152 | Técnico de pruebas |
| Polaridad, Voc y corriente de strings | NES-OPE-F-153 | Técnico de pruebas |
| Resistencia de aislamiento del arreglo | NES-OPE-F-154 | Técnico de pruebas |
| Ensayos funcionales | NES-OPE-F-155 | Ingeniero de comisionado |
| Curva I-V de strings | NES-OPE-F-156 | Técnico de pruebas |
| Resumen de inspección termográfica | NES-OPE-F-157 | Termógrafo |
| Registro de desviaciones y repetición de ensayos | NES-OPE-F-158 | QA/QC |
| Certificado de comisionado del generador FV | NES-OPE-F-159 | Ingeniero de comisionado |
| Registro de pruebas DC de string (antecedente) | NES-OPE-F-062 | Responsable eléctrico |
| PTE, ATS/ART y LOTO | Según NES-SST-PR-001 | Responsable SST |
| Certificados de calibración e ISO 9712 | — | QA/QC |

\pagebreak

# 14. ANEXOS

## NES-OPE-F-150 — Permiso de ensayo y control de riesgos DC

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / inversor / caja combinadora: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-022 / NES-SST-PR-001 | PTE asociado N.º: [____] |
| Ensayos autorizados: [__________] | Horario: [____] a [____] |

| Paso | Control | Verificado | Responsable | Firma |
|---|---|---|---|---|
| 1 | Registros de construcción del bloque cerrados |  |  |  |
| 2 | Circuitos identificados contra unifilar y rótulos |  |  |  |
| 3 | Inversor en parada y seccionador DC abierto |  |  |  |
| 4 | Corriente 0,0 A verificada con pinza DC |  |  |  |
| 5 | Candado y tarjeta de cada ejecutante |  |  |  |
| 6 | Detector de tensión probado antes y después |  |  |  |
| 7 | Instrumentos calibrados y verificados en la jornada |  |  |  |
| 8 | Zona de exclusión delimitada y señalizada |  |  |  |
| 9 | DPS y equipos sensibles aislados para aislamiento |  |  |  |
| 10 | EPP dieléctrico y de arco inspeccionado |  |  |  |
| 11 | Condiciones climáticas aptas (sin lluvia ni tormenta) |  |  |  |
| 12 | Cierre: circuitos descargados, estado documentado, bloqueos retirados por sus dueños |  |  |  |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-151 — Inspección visual del generador FV (IEC 62446-1)

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / inversor: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-022 / IEC 62446-1 | Plano: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Instalación conforme al diseño y al unifilar aprobado |  |  |  |
| 2 | Componentes DC aptos para la tensión máxima del sistema |  |  |  |
| 3 | Módulos sin daño, fijación conforme, sin sombras anómalas |  |  |  |
| 4 | Cableado DC soportado, sin contacto con suelo ni bordes vivos |  |  |  |
| 5 | Conectores de la misma referencia, acoplados y enclavados |  |  |  |
| 6 | Cajas combinadoras cerradas, estancas y rotuladas |  |  |  |
| 7 | Fusibles de la capacidad de diseño |  |  |  |
| 8 | DPS instalados, indicador conforme, tierra corta y directa |  |  |  |
| 9 | Conductores de protección y equipotenciales instalados y marcados |  |  |  |
| 10 | Entradas DC del inversor polarizadas y rotuladas |  |  |  |
| 11 | Señalización de advertencia DC y doble alimentación según RETIE |  |  |  |
| 12 | Seccionador DC principal identificado y accesible |  |  |  |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-152 — Continuidad de conductores de protección y equipotencialidad

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / inversor: [__________] | Consecutivo: [____] |
| Instrumento (serie / calibración): [__________] | Corriente de ensayo: [____] mA |
| Punto de tierra de referencia: [__________] | Límite del proyecto: [____] Ω |

| N.º | Elemento ensayado | Desde | Hasta | Valor (Ω) | Cumple | Obs. |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-153 — Polaridad, Voc y corriente de strings

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja combinadora / inversor: [__________] | Consecutivo: [____] |
| Módulo (referencia): [__________] | Módulos en serie (N): [____] |
| Voc STC módulo: [____] V | Isc STC módulo: [____] A |
| Coeficiente β de Voc: [____] %/°C | Método de corriente: Isc / operación |
| Irradiancia POA: [____] W/m² | Temperatura de módulo: [____] °C |
| Voc esperada: [____] V | Isc esperada: [____] A |
| Instrumentos (serie / calibración): [__________] | Hora inicio / fin: [____] |

| String | Polaridad OK | Voc (V) | Desv. Voc (%) | I (A) | Desv. I (%) | Cumple |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Media Voc strings idénticos: [____] V | Media corriente strings idénticos: [____] A |
|---|---|
| Tensión polo-tierra sin anomalía: Sí / No | Fusibles insertados tras conformidad: Sí / No |

{.plain}
| Observaciones y strings no liberados: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-154 — Resistencia de aislamiento del arreglo

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / inversor / caja: [__________] | Consecutivo: [____] |
| Tensión del sistema: [____] V | Tensión de ensayo: [____] V DC |
| Método: 1 (polo a tierra por separado) / 2 (polos cortocircuitados) | Mínimo exigido: [____] MΩ |
| Temperatura ambiente: [____] °C | Humedad relativa: [____] % |
| Megóhmetro (serie / calibración): [__________] | DPS aislados: Sí / No |

| Circuito / string | R (+) a tierra (MΩ) | R (−) a tierra (MΩ) | R polos unidos a tierra (MΩ) | Tiempo (s) | Descargado | Cumple |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-155 — Ensayos funcionales del generador

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / inversor: [__________] | Consecutivo: [____] |
| Autorización de energización (NES-OPE-PR-023) N.º: [____] | Documento de referencia: NES-OPE-PR-022 |

| Ítem | Ensayo | Resultado | Cumple | No cumple | Obs. |
|---|---|---|---|---|---|
| 1 | Maniobra y enclavamiento de seccionadores DC de cajas combinadoras |  |  |  |  |
| 2 | Bloqueo con candado de seccionadores |  |  |  |  |
| 3 | Fusibles de capacidad de diseño |  |  |  |  |
| 4 | Indicador de estado de DPS |  |  |  |  |
| 5 | Seccionador DC del inversor |  |  |  |  |
| 6 | Arranque y parada del inversor según manual |  |  |  |  |
| 7 | Medida de aislamiento DC informada por el inversor |  |  |  |  |
| 8 | Vigilancia de corriente residual / falla a tierra |  |  |  |  |
| 9 | Comunicación de medidas al sistema de supervisión |  |  |  |  |
| 10 | Parada de emergencia y desconexión remota |  |  |  |  |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-156 — Curva I-V de strings

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja combinadora / inversor: [__________] | Consecutivo: [____] |
| Trazador (serie / calibración): [__________] | Sensor de irradiancia (serie): [__________] |
| Método de traslado a STC: IEC 60891 procedimiento [____] | Criterio Pmax del proyecto: [____] % |
| Pmax nominal del string a STC: [____] W | Tolerancia de potencia del módulo: [____] |

| String | G POA (W/m²) | T módulo (°C) | Pmax medida (W) | Pmax a STC (W) | FF | Forma conforme |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Observaciones (escalones, pendientes anómalas, strings a investigar): |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-157 — Resumen de inspección termográfica (IEC TS 62446-3)

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloques inspeccionados: [__________] | Consecutivo: [____] |
| Tipo: simplificada / detallada | Modalidad: terrestre / aérea |
| Termógrafo y nivel ISO 9712: [__________] | Cámara (serie / NETD / calibración): [__________] |
| Irradiancia POA mín. / máx.: [____] W/m² | Viento máx.: [____] km/h |
| Nubosidad: [____] octas | Temperatura ambiente: [____] °C |
| Emisividad ajustada: [____] | Resolución lograda: [____] píxeles por célula |

| N.º | Ubicación (bloque / fila / mesa / módulo) | Componente | Descripción de la anomalía | ΔT (K) | Clase (CoA) | Acción |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |

{.plain}
| Total CoA 2: [____] | Total CoA 3: [____] |
|---|---|
| Condiciones válidas durante toda la inspección: Sí / No | Informe termográfico N.º: [____] |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-158 — Registro de desviaciones y repetición de ensayos

{.plain}
| Proyecto: [__________] | Fecha de apertura: [____] |
|---|---|
| Bloque / inversor: [__________] | Consecutivo: [____] |

| N.º | String / equipo | Ensayo y valor medido | Criterio | Clasificación (A/B/C) | Acción correctiva | Reensayo y fecha de cierre |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |

{.plain}
| Observaciones y pendientes aceptados por [CLIENTE]: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-159 — Certificado de comisionado del generador FV

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / inversores incluidos: [__________] | Consecutivo: [____] |
| Potencia DC del alcance: [____] kWp | Cantidad de strings: [____] |
| Documento de referencia: NES-OPE-PR-022 / IEC 62446-1 | Categoría ejecutada: 1 / 1 y 2 |

| Ítem | Requisito | Registro | Conforme | Obs. |
|---|---|---|---|---|
| 1 | Inspección visual sin hallazgos bloqueantes | NES-OPE-F-151 |  |  |
| 2 | Continuidad de protección y equipotencialidad | NES-OPE-F-152 |  |  |
| 3 | Polaridad, Voc y corriente del 100 % de strings | NES-OPE-F-153 |  |  |
| 4 | Resistencia de aislamiento conforme | NES-OPE-F-154 |  |  |
| 5 | Ensayos funcionales conformes | NES-OPE-F-155 |  |  |
| 6 | Curvas I-V conformes (si aplica) | NES-OPE-F-156 |  |  |
| 7 | Termografía sin CoA 3 abiertas (si aplica) | NES-OPE-F-157 |  |  |
| 8 | Desviaciones A y B cerradas; C en punch list aceptado | NES-OPE-F-158 |  |  |
| 9 | Unifilar y plano de strings según lo construido | Dossier |  |  |
| 10 | Fichas técnicas e información de O&M | Dossier |  |  |
| 11 | Certificados de calibración y de personal | Dossier |  |  |

{.plain}
| Declaración: el generador FV del alcance indicado fue inspeccionado y ensayado según NES-OPE-PR-022 y la IEC 62446-1, y se encuentra en condición de continuar con la inspección RETIE y la secuencia de energización de NES-OPE-PR-023. Este certificado no autoriza por sí mismo la energización. |
|---|

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

# 15. CONTROL DE CAMBIOS

| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
