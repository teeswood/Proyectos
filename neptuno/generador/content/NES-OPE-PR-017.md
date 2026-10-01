---
code: NES-OPE-PR-017
header_title: PROCEDIMIENTO DE MONTAJE DE CAJAS COMBINADORAS
cover_title: Procedimiento de Montaje de Cajas Combinadoras y Tableros DC
cover_subtitle: Recepción, montaje, conexionado y liberación previa a energización en plantas fotovoltaicas
---

# 1. OBJETIVO

Definir el método de trabajo, los controles de calidad y las medidas preventivas para la recepción, el almacenamiento, el montaje mecánico, el conexionado y la verificación previa a energización de las cajas combinadoras de strings (SCB) y de los tableros DC de la planta FV [PROYECTO], conforme al RETIE, a la NTC 2050, a la IEC 62548, a la IEC 62446-1 y a las instrucciones del fabricante de la caja combinadora.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, en especial el arco eléctrico en corriente continua, el punto caliente por conexión floja y la pérdida de estanqueidad de la envolvente.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en:

- Recepción, inspección documental y física, almacenamiento y preservación de cajas combinadoras, tableros DC de recombinación y sus accesorios (fusibles gPV, portafusibles, seccionadores DC, dispositivos de protección contra sobretensiones DC, prensaestopas y soportes).
- Montaje mecánico de la caja sobre estructura del tracker o de mesa fija, sobre hinca dedicada, sobre poste o sobre muro de la estación de potencia.
- Preparación de entradas de cable, instalación de prensaestopas y sellado para conservar el grado IP declarado por el fabricante.
- Instalación o verificación de fusibles gPV, seccionador DC y DPS DC.
- Conexión de los cables de string, del cable de salida (principal DC) y de la puesta a tierra de la caja.
- Verificación de polaridad, medición de Voc por string, apriete controlado de bornes, rotulado y liberación de la caja previa a energización.

No incluye la conectorización de strings ni el cambio de conectores tipo MC4, que se rigen por NES-OPE-PR-014; el tendido de los cables de string y del principal DC en zanja, ducto o bandeja, que se rige por NES-OPE-PR-015; la malla de puesta a tierra y el SIPRA, que se rigen por NES-OPE-PR-020; la conexión del principal DC al inversor, que se rige por NES-OPE-PR-018; ni los ensayos de comisionado y la energización, que se rigen por NES-OPE-PR-022 y NES-OPE-PR-023.

> NOTA: La caja combinadora es el primer punto del campo donde se concentra la corriente de varios strings. Un borne flojo, un fusible mal seleccionado o un prensaestopas sin sellar no se manifiestan al montar: aparecen meses después como punto caliente, falla de aislamiento o incendio. Este procedimiento controla esas causas en el momento del montaje.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / ART y PT | Análisis de trabajo seguro / análisis de riesgo del trabajo y permiso de trabajo. |
| PTE | Permiso de trabajo eléctrico, emitido por el responsable eléctrico con alcance, puntos de corte y responsable de la maniobra. |
| SCB / caja combinadora | Envolvente de campo que conecta en paralelo varios strings, con protección por string (fusibles gPV), barraje, seccionador DC de salida y, según diseño, DPS DC y monitoreo de corriente. |
| Tablero DC de recombinación | Tablero que agrupa las salidas de varias cajas combinadoras antes del inversor central, cuando el diseño lo prevé. |
| Principal DC | Cable de salida de la caja combinadora hacia el tablero de recombinación o el inversor. |
| Fusible gPV | Fusible de rango completo para protección de circuitos fotovoltaicos en corriente continua, fabricado según IEC 60269-6. |
| Seccionador DC | Interruptor-seccionador para corriente continua fotovoltaica, fabricado según IEC 60947-3, con la categoría de utilización y la tensión DC que exige el diseño. |
| DPS DC | Dispositivo de protección contra sobretensiones para el lado DC fotovoltaico, fabricado según IEC 61643-31. Se caracteriza por su tensión máxima de operación continua (Ucpv), su corriente nominal de descarga (In) y su nivel de protección (Up). |
| Isc | Corriente de cortocircuito del módulo o del string. |
| Voc | Tensión de circuito abierto del módulo o del string, sin carga conectada. |
| Corriente inversa | Corriente que circula en sentido contrario por un string en falla, alimentada por los strings sanos en paralelo. Es la razón de ser del fusible de string. |
| Prensaestopas (racor) | Accesorio roscado que fija y sella la entrada de un cable a la envolvente. El multivía admite varios cables con un inserto de goma perforado. |
| Elemento de compensación de presión | Válvula o membrana que iguala la presión interior y exterior de la caja y reduce la condensación, sin perder el grado IP. |
| Grado IP | Grado de protección de la envolvente contra ingreso de polvo y agua, declarado por el fabricante (por ejemplo IP65 o IP66). |
| Grado IK | Grado de protección de la envolvente contra impactos mecánicos externos. |
| Terminal bimetálico | Terminal con barril de aluminio y palma de cobre, para unir un conductor de aluminio a un borne o barra de cobre sin par galvánico. |
| Torque (par de apriete) | Momento aplicado a un tornillo o borne con torquímetro calibrado, en N·m. |
| Marca de torque | Línea de pintura indeleble trazada sobre tuerca y base una vez aplicado el torque, que evidencia el apriete y permite detectar aflojamiento. |
| LOTO | Bloqueo y etiquetado de dispositivos de desconexión, con candado y tarjeta de quien ejecuta el trabajo. |
| Cinco reglas de oro | Cortar todas las fuentes, bloquear, verificar ausencia de tensión, poner a tierra cuando aplique y señalizar la zona. |
| Dictamen RETIE | Documento emitido por organismo de inspección acreditado que declara la conformidad de la instalación con el RETIE. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. Bloques, filas, cajas combinadoras, tableros DC e inversores se identifican según el plano general de implantación [N° de plano], el plano de ubicación de cajas combinadoras [N° de plano] y el diagrama unifilar DC [N° de plano].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

Diagrama unifilar DC, plano de ubicación de cajas combinadoras, plano de detalle de soporte y cuadro de strings por caja del proyecto — [N° de plano].

Manual de instalación y operación del fabricante de la caja combinadora: condiciones de transporte y almacenamiento, posición de montaje, pares de apriete, secciones admitidas, longitudes de pelado, prensaestopas y puesta en servicio.

Fichas técnicas de los fusibles gPV, del seccionador DC y del DPS DC, con tensión DC asignada, corriente asignada y categoría de utilización.

Hoja de datos del módulo: Isc, Voc, corriente inversa admisible o calibre máximo de fusible en serie, coeficientes de temperatura.

Memoria de cálculo de protecciones DC del diseñador eléctrico: calibre de fusible por string, tensión máxima del arreglo a la temperatura mínima del sitio y selección del DPS.

Certificados de conformidad de producto de la caja y de sus componentes, emitidos por organismo acreditado, en los términos que exija el RETIE, y protocolo de pruebas de fábrica (FAT) de la caja.

NES-OPE-PR-012 Obras civiles y cimentaciones; NES-OPE-PR-014 Conexionado DC y conectores MC4; NES-OPE-PR-015 Tendido de cables; NES-OPE-PR-018 Montaje y conexionado de inversores; NES-OPE-PR-020 Puesta a tierra y SIPRA; NES-OPE-PR-022 Pruebas y comisionado del generador FV; NES-OPE-PR-023 Energización y puesta en servicio.

NES-CAL-PLN-002 Plan de calidad; NES-SST-PLN-001 Plan de emergencias; NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado.

## 5.2. Normativa aplicable

RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes: requisitos de producto, instalación, distancias de seguridad, rotulado, certificación de producto y dictamen de inspección de la instalación.

NTC 2050 — Código Eléctrico Colombiano, artículo 690 (Sistemas solares fotovoltaicos), en los requisitos que el RETIE adopta.

IEC 62548 — Requisitos de diseño de arreglos fotovoltaicos: protección contra sobrecorriente de strings, dispositivos de seccionamiento y protección contra sobretensiones.

IEC 60364-7-712 — Instalaciones eléctricas de baja tensión: requisitos para sistemas de alimentación fotovoltaicos.

IEC 62446-1 — Documentación, ensayos de puesta en servicio e inspección de sistemas fotovoltaicos conectados a la red.

IEC 60269-6 — Fusibles de baja tensión: requisitos suplementarios para fusibles de protección de sistemas fotovoltaicos (gPV).

IEC 60947-3 — Interruptores, seccionadores e interruptores-seccionadores, incluidas las categorías de utilización para corriente continua fotovoltaica.

IEC 61643-31 — Dispositivos de protección contra sobretensiones para el lado DC de instalaciones fotovoltaicas.

IEC 61439-1 e IEC 61439-2 — Conjuntos de aparamenta de baja tensión, como referencia técnica de la envolvente y del ensamble.

IEC 62305 y NTC 4552 — Protección contra descargas eléctricas atmosféricas, en lo que el diseño del SIPRA asigne a las cajas.

ISO 6789 — Herramientas de apriete: requisitos y calibración de torquímetros.

Ley 1264 de 2008 (técnicos electricistas, CONTE); Ley 51 de 1986 y Ley 842 de 2003 (ingenieros, COPNIA).

Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019 — Estándares mínimos del SG-SST.

Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en los procesos de generación, transmisión, distribución y comercialización de energía eléctrica; cinco reglas de oro.

Resolución 2400 de 1979 — Estatuto de seguridad industrial; arts. 388 a 392 (manejo manual de cargas) y arts. 398 a 447 (manejo y transporte mecánico de materiales).

Resolución 4272 de 2021 — Trabajo en alturas, cuando haya exposición a 2 m o más.

Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo.

Decreto 1076 de 2015 (RESPEL); Resolución 2184 de 2019 (código de colores); Resolución 0472 de 2017 modificada por la Resolución 1257 de 2021 (RCD); Ley 1672 de 2013 (RAEE).

Licencia ambiental y Plan de Manejo Ambiental (PMA) del proyecto — [N° de resolución].

NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

Aprobar y divulgar el presente procedimiento y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.

Asegurar que el frente cuente con personal calificado, torquímetros calibrados, instrumentos CAT III o superior y el manual vigente del fabricante de la caja antes de autorizar el inicio.

Tramitar ante [CLIENTE] los RFI, las aprobaciones de cambio de referencia de caja, fusible, seccionador o DPS, y las desviaciones del plano de ubicación.

Detener cualquier actividad que no cumpla este procedimiento, el diseño o la instrucción del fabricante.

## 6.2. Responsable eléctrico (ingeniero con matrícula COPNIA o técnico con matrícula CONTE vigente)

Verificar antes del montaje que el calibre de los fusibles, la tensión asignada del seccionador y del DPS y las secciones de cable recibidas coinciden con la memoria de cálculo y el unifilar.

Emitir el permiso de trabajo eléctrico para toda conexión de strings y aplicar las cinco reglas de oro.

Ejecutar o supervisar la verificación de polaridad, la medición de Voc, el ensayo de aislamiento y la liberación de la caja previa a energización.

Autorizar la inserción de fusibles y el cierre del seccionador solo dentro de la secuencia de NES-OPE-PR-023.

## 6.3. Supervisor / capataz de frente de cajas combinadoras

Asignar tareas, dirigir la cuadrilla y verificar el cumplimiento del método descrito.

Elaborar con los trabajadores el ATS/ART diario y la charla de inicio de turno.

Verificar que torquímetros, pelacables, crimpadoras e instrumentos estén inspeccionados, calibrados y con el dado correcto para cada sección.

Diligenciar los registros del frente el mismo día.

## 6.4. Oficial electricista de montaje

Ejecutar el montaje mecánico, la preparación de entradas, el pelado, el crimpado de terminales y la conexión según este documento y el manual del fabricante.

Aplicar el torque especificado con torquímetro y trazar la marca de torque en cada unión apretada.

Rechazar toda caja, componente o terminal que no cumpla la inspección visual.

## 6.5. Responsable de calidad (QA/QC)

Controlar el cumplimiento del Plan de Inspección y Ensayos (PIE) definido en NES-CAL-PLN-002 y liberar cada caja mediante los formatos de este documento.

Verificar la trazabilidad entre número de serie de la caja, ubicación, strings conectados y protocolos.

Ejecutar el muestreo de verificación de torque y registrar las no conformidades hasta su cierre.

## 6.6. Responsable SST (con licencia en SST vigente)

Elaborar y divulgar la matriz de peligros específica del trabajo en cajas combinadoras.

Verificar permisos, EPP dieléctrico y de arco vigente, herramienta aislada, delimitación de áreas, competencia del personal y certificación de alturas cuando aplique.

Aplicar el protocolo de tormenta eléctrica y liderar la atención de emergencias, en especial arco eléctrico, choque eléctrico y quemaduras.

## 6.7. Coordinador de trabajo en alturas

Cuando la caja se monte a 2 m o más sobre el nivel inferior, o sobre muro de estación con exposición a caída, evaluar el sistema de acceso y emitir el permiso de alturas conforme a la Resolución 4272 de 2021.

## 6.8. Responsable ambiental

Asegurar el cumplimiento del PMA y de la licencia ambiental del proyecto.

Verificar la separación de embalajes, retazos de cable, terminales, fusibles retirados y desecantes, y su entrega a gestor autorizado.

## 6.9. Trabajadores

Cumplir este procedimiento y participar en el ATS/ART y en la charla diaria.

Usar correctamente el EPP y las herramientas asignadas; no improvisar herramienta de pelado, crimpado ni apriete.

Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS. Reportar a la ARL y al COPASST o vigía SST cualquier condición insegura.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Responsable eléctrico (COPNIA o CONTE), supervisor de frente, oficiales electricistas con matrícula CONTE, auxiliares, QA/QC, responsable SST, coordinador de alturas cuando aplique. Personal autorizado por escrito para intervenir circuitos DC. |
| Materiales | Caja y componentes | Cajas combinadoras de la referencia aprobada; fusibles gPV del calibre de diseño; portafusibles; seccionador DC; DPS DC con cartuchos de repuesto; prensaestopas y tapones de la referencia del fabricante; elemento de compensación de presión. |
| Materiales | Montaje | Soportes, abrazaderas o perfiles galvanizados del plano de detalle; tornillería de acero inoxidable o galvanizada en caliente con arandelas; arandelas de aislamiento galvánico cuando el fabricante las exija; pasta antioxidante para uniones de aluminio. |
| Materiales | Conexión | Terminales de compresión o bimetálicos de la sección de diseño; punteras (ferrules) cuando el borne lo exija; cable de tierra de la sección de diseño; marquillas y placas de identificación resistentes a UV; pintura indeleble para marca de torque. |
| Herramientas | Apriete | Torquímetros de rango adecuado (bajo para bornes de portafusibles, medio y alto para barras y principal DC) con certificado de calibración vigente según ISO 6789; destornillador dinamométrico. |
| Herramientas | Conexión | Pelacables ajustado al calibre; crimpadora hidráulica con dados de la sección y del tipo de terminal; crimpadora de punteras; llaves de apriete de prensaestopas del fabricante; juego de herramienta aislada con marcado vigente. |
| Herramientas | Montaje | Taladro con broca para metal, nivel, flexómetro, llaves mixtas, escalera o plataforma certificada cuando aplique. |
| Equipos | Medida | Multímetro CAT III o superior para la tensión DC máxima del sistema; pinza amperimétrica DC; detector de tensión DC; megóhmetro con tensión de ensayo de 1.000 V DC; telurómetro o micro-ohmímetro para continuidad de tierra. Todos con calibración vigente. |
| Equipos | LOTO | Kit LOTO (candados personales, pinzas multibloqueo, tarjetas, caja de bloqueo), tapones de fusible de bloqueo cuando el portafusibles los admita. |
| EPP | Trabajo eléctrico | Guantes dieléctricos de clase acorde con la tensión DC, con sobreguante de cuero; calzado dieléctrico; careta y ropa con la categoría que indique el análisis de riesgo de arco; sin elementos metálicos personales. |
| EPP | Básico | Casco con barbuquejo, gafas con filtro UV, botas con puntera, chaleco reflectivo, cubrenuca, protector solar, ropa manga larga, guantes anticorte, polainas en zonas con ofidios. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

Personal calificado, autorizado y con inducción en riesgo eléctrico DC y en este procedimiento.

ATS/ART, charla de inicio de turno y permiso de trabajo diligenciados; permiso de trabajo eléctrico cuando se conecten strings.

Plano de ubicación de cajas, plano de detalle de soporte y unifilar DC vigentes en el frente, con revisión aprobada para construcción.

Manual del fabricante de la caja disponible en el frente, en español o con traducción técnica de los pasos críticos.

Memoria de protecciones DC aprobada: calibre de fusible por string, tensión asignada del seccionador y del DPS.

Soportes, hincas o postes de montaje terminados y liberados según NES-OPE-PR-012, y punto de conexión a la malla de tierra disponible según NES-OPE-PR-020.

Torquímetros e instrumentos con calibración vigente; detector de tensión probado en fuente conocida.

Condiciones climáticas aptas: sin lluvia y sin tormenta eléctrica para abrir la caja o conectar.

> ALTO: No se abre una caja combinadora ni se conecta un string con lluvia, llovizna o rocío. La humedad que entra a la envolvente queda atrapada, condensa y produce corrosión de bornes y falla de aislamiento.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

El frente se organiza por bloque e inversor. Se delimitan y señalizan: el patio de almacenamiento de cajas, el punto de montaje en fila o en estación, el tramo de strings que llega a la caja y el punto de acopio de residuos. Toda caja con strings conectados se trata como energizada y su zona se demarca con señal de riesgo eléctrico; solo ingresa personal autorizado.

### 8.2.2. Ingreso de personal

Evaluar condiciones del área y verificar que no haya trabajos simultáneos incompatibles en el mismo circuito o bajo la misma fila.

Diligenciar ATS/ART, permiso de trabajo y, cuando aplique, permiso de trabajo eléctrico y permiso de alturas.

Ubicar equipos de emergencia e inspeccionar el EPP, en especial guantes dieléctricos y careta.

### 8.2.3. Ingreso de vehículos y equipos

Preoperacional de vehículos, montacargas y equipos de distribución; circulación solo por rutas autorizadas.

La distribución de las cajas a lo largo de las filas se hace con máquina y con la caja dentro de su embalaje, apoyada sobre la cara posterior.

Los vehículos no estacionan sobre cableado tendido ni sobre zanjas o canalizaciones abiertas.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Recepción e inspección

Toda caja combinadora y todo componente se recibe contra la orden de compra, la ficha aprobada (submittal) y la lista de empaque. La inspección se registra en el formato NES-OPE-F-100.

1. Inspeccionar el embalaje antes de descargar: golpes, perforaciones, humedad, indicadores de impacto o de inclinación activados. Fotografiar y dejar constancia en la remisión del transportador antes de firmar.
2. Verificar la placa de características de cada caja: referencia, número de serie, tensión DC máxima, corriente asignada, número de entradas, grado IP, grado IK y año de fabricación.
3. Verificar que la caja trae el certificado de conformidad de producto exigido por el RETIE y el protocolo de pruebas de fábrica.
4. Abrir la caja solo bajo techo y en ambiente seco. Verificar interior: ausencia de humedad, polvo o cuerpos extraños; barraje y bornes sin daño; portafusibles, seccionador y DPS de la referencia aprobada.
5. Verificar que los fusibles suministrados son gPV según IEC 60269-6, con la tensión DC asignada igual o superior a la del sistema y con el calibre de la memoria de cálculo. Un fusible no gPV, o de tensión inferior, se rechaza.
6. Verificar el estado de prensaestopas, insertos multivía, tapones y elemento de compensación de presión; que la junta de la puerta esté completa y sin cortes y que las cerraduras funcionen.
7. Cerrar de nuevo la caja, conservarla en su embalaje y rotular con estado: aceptada, en cuarentena o rechazada.

> NOTA: Si tras el almacenamiento se encuentra ingreso de polvo, contaminantes o líquido, condensación o cualquier daño, la caja no se instala hasta que el fabricante apruebe por escrito el procedimiento de corrección. Así lo exigen los manuales de fabricante consultados y es condición de garantía.

#### 8.2.4.2. Almacenamiento y preservación

| Aspecto | Requisito |
|---|---|
| Posición | Caja en su embalaje, apoyada sobre la cara posterior. No se apoya sobre la cara inferior, donde están los prensaestopas y conectores, porque se dañan. |
| Lugar | Bodega o contenedor cerrado, seco, ventilado, sobre estibas, fuera de zonas inundables y protegido del sol directo. |
| Condiciones | Temperatura y humedad dentro del rango del fabricante. Valor típico de fabricante para almacenamiento prolongado: -25 °C a +40 °C y humedad relativa baja, sin condensación; verificar contra el manual del equipo del proyecto. |
| Apilado | Máximo número de niveles que indique el embalaje; nunca apilar cajas fuera de su embalaje. |
| Fusibles, DPS y repuestos | En su empaque original, en estantería bajo llave, separados por calibre y rotulados. |
| Inspección | Mensual (criterio interno), con registro en NES-OPE-F-101: estado de embalaje, humedad, plagas y ofidios, fecha de ingreso. |

En [departamento] con humedad relativa alta o ambiente salino, se mantiene el desecante de fábrica dentro de la caja hasta el montaje y se evita abrirla en patio.

#### 8.2.4.3. Ubicación, orientación y sombreado

La ubicación de cada caja la fija el plano aprobado. En campo se verifica y se aplica lo siguiente:

- Montar la caja en posición vertical, con prensaestopas y conectores hacia abajo. Algunos fabricantes admiten inclinación positiva limitada; valor típico de fabricante: entre 15° y 90° respecto de la horizontal, nunca con la puerta hacia arriba ni con las entradas hacia arriba; verificar contra el manual del equipo del proyecto.
- Buscar la sombra de la propia estructura o de la fila: el calentamiento solar de la envolvente reduce la capacidad de los fusibles y acelera el envejecimiento de juntas y DPS. En la latitud de Colombia el sol pasa cerca del cenit, por lo que la cara superior y las caras este y oeste reciben radiación fuerte; si el fabricante o el diseño prevén techo o parasol, se instala.
- Respetar el rango de temperatura de operación del fabricante. Valor típico de fabricante: -20 °C a +50 °C de temperatura ambiente; verificar contra el manual del equipo del proyecto y contra la temperatura máxima del sitio.
- Dejar libre el giro completo de la puerta y un espacio frontal de trabajo suficiente para operar el seccionador y medir con EPP de arco, según las distancias del RETIE y el plano.
- La base de la caja queda por encima del nivel de inundación del diseño y lejos de canales de drenaje, cunetas o zonas de empozamiento. Altura típica de montaje para operación y mantenimiento: entre 1,5 m y 2,0 m del suelo al eje de la caja, salvo que el plano indique otra (valor de referencia de guías de instalación; verificar contra el plano).
- En tracker, la caja se monta sobre una parte fija (hinca, poste dedicado o perfil fijo indicado por el fabricante del tracker), nunca sobre una parte giratoria salvo que el diseño lo prevea con holguras de cable para todo el recorrido.
- No montar la caja donde reciba escorrentía de los módulos, salpicadura del lavado ni golpes de maquinaria de desbroce.

#### 8.2.4.4. Montaje mecánico

1. Verificar en el soporte, hinca o poste: verticalidad, altura, orientación y estado del galvanizado. Reparar daños del galvanizado con el método aprobado antes de montar.
2. Instalar el soporte, la placa o las abrazaderas de la caja según el plano de detalle, con la tornillería especificada y arandelas.
3. Izar la caja a su posición entre dos personas cuando su masa supere el límite de manejo manual de la Resolución 2400 de 1979, o con equipo mecánico. Nunca levantar la caja de los prensaestopas, de la puerta ni de las manijas del seccionador.
4. Fijar la caja usando solo los puntos de fijación del fabricante. No se perfora la envolvente para nuevas fijaciones: se pierde el grado IP y la certificación.
5. Cuando la caja sea metálica y el soporte de otro metal, instalar las arandelas de aislamiento galvánico que indique el fabricante.
6. Nivelar y apretar la tornillería de fijación al torque del plano o del fabricante; trazar marca de torque.
7. Verificar que la caja no vibra, no gira y que la puerta abre y cierra sin interferencia.
8. Registrar en NES-OPE-F-102.

#### 8.2.4.5. Entradas de cable, prensaestopas y sellado IP

1. Usar únicamente los prensaestopas y los insertos multivía del fabricante, del diámetro exterior del cable empleado. Un prensaestopas de rango distinto no sella.
2. Cuando el fabricante entregue entradas sin mecanizar, la perforación solo se hace en la zona y con la herramienta que indique su manual, retirando la viruta y protegiendo el interior. Toda perforación no prevista requiere aprobación escrita del fabricante.
3. Pasar cada cable por su orificio del inserto multivía; no se pasan dos cables por un mismo orificio ni se corta el inserto para agrandarlo.
4. Dejar en el interior una holgura de cable que permita reconectar, sin tensión mecánica sobre el borne.
5. Apretar la tuerca del prensaestopas al torque del fabricante, con la llave indicada. Ni flojo ni sobreapretado: el inserto debe abrazar la cubierta del cable sin deformarla.
6. Instalar tapones en todos los orificios del inserto y en todas las entradas sin uso. Ninguna entrada queda abierta, ni siquiera de forma provisional al final de la jornada.
7. Verificar que el elemento de compensación de presión está instalado y libre. No se tapa ni se pinta.
8. Formar bajo la caja un bucle de goteo en cada cable, para que el agua escurra antes de llegar al prensaestopas.
9. Verificar que la junta de la puerta queda limpia y completa y que la puerta cierra con todos sus cierres.

> ALTO: Un prensaestopas flojo o una entrada sin tapón anulan el grado IP de la caja. El agua y el polvo que entran producen corrosión del barraje, pérdida de aislamiento y arco interno. La caja no se libera con una sola entrada sin sellar.

#### 8.2.4.6. Fusibles gPV y protección de strings

La selección de los fusibles es responsabilidad del diseñador eléctrico. En campo se verifica que lo instalado coincide con la memoria de cálculo y con los criterios técnicos siguientes, tomados de la IEC 62548 y de la IEC 60364-7-712:

| Aspecto | Criterio de verificación |
|---|---|
| Necesidad de protección | Se requiere protección de sobrecorriente por string cuando la corriente inversa que pueden aportar los demás strings en paralelo supera la que el módulo soporta. La IEC 60364-7-712 la expresa como 1,35 · IRM menor que (Ns − 1) · Isc máx., donde IRM es la corriente inversa admisible del módulo y Ns el número de strings en paralelo. Con uno o dos strings en paralelo no se requiere. |
| Calibre | Corriente asignada mayor que 1,5 veces la Isc del string y menor que 2,4 veces la Isc, y no superior al calibre máximo de fusible en serie declarado por el fabricante del módulo. El valor definitivo lo fija la memoria de cálculo. |
| Tipo | gPV según IEC 60269-6. No se admiten fusibles gG, aM ni de corriente alterna. |
| Tensión asignada | Igual o superior a la tensión máxima del arreglo calculada a la temperatura mínima del sitio. |
| Polos | Fusible en el polo o en los polos que indique el diseño según el esquema de puesta a tierra del arreglo. Un fusible ubicado en el polo equivocado deja el string sin protección. |
| Portafusibles | De la referencia del fabricante, con la tensión DC del sistema, apretado al torque del fabricante. |

Procedimiento en campo:

1. Durante el montaje y la conexión de strings, los fusibles permanecen fuera del portafusibles o con el portafusibles abierto y el seccionador en posición abierta.
2. Verificar el calibre y la referencia impresos en el cuerpo de cada fusible contra el cuadro de strings de la caja. No se mezclan calibres dentro de una caja salvo que el diseño lo indique.
3. Apretar los bornes del portafusibles al torque del fabricante. Valor típico de fabricante para bornes de portafusibles de 10 × 85 mm: 2,0 N·m a 2,5 N·m; verificar contra el manual del equipo del proyecto.
4. La inserción de fusibles se hace solo después de la verificación de polaridad y Voc de todos los strings de la caja (numeral 8.2.4.9), con el seccionador abierto, con la autorización del responsable eléctrico y dentro de la secuencia de energización de NES-OPE-PR-023.
5. Los portafusibles nunca se abren ni se cierran bajo carga. El portafusibles no es un dispositivo de maniobra.

#### 8.2.4.7. Seccionador DC

Verificar que el seccionador DC es de la referencia aprobada, fabricado según IEC 60947-3, con la tensión DC asignada y la categoría de utilización para corriente continua fotovoltaica que exige el diseño, y con la corriente asignada a la temperatura interna de la caja.

Verificar el funcionamiento mecánico en vacío: apertura y cierre completos, indicación de posición visible y coherente, y capacidad de bloqueo con candado en posición abierta.

Apretar los bornes al torque del fabricante y trazar marca de torque.

Dejar el seccionador abierto, con candado y tarjeta del responsable eléctrico, desde la conexión del primer string hasta la autorización de energización.

> NOTA: Algunos seccionadores DC tienen terminales de entrada y salida definidos por el fabricante. Una conexión invertida puede impedir la extinción del arco al abrir bajo carga. Se verifica contra el manual antes de conectar.

#### 8.2.4.8. DPS DC

1. Verificar que el DPS es del tipo y la referencia del diseño, fabricado según IEC 61643-31, con tensión máxima de operación continua (Ucpv) igual o superior a la tensión máxima del arreglo y con la corriente de descarga que fije el diseño del SIPRA.
2. Verificar que los cartuchos están completamente insertados y que la ventana de estado indica condición sana.
3. Conectar el conductor de tierra del DPS a la barra de tierra de la caja con la menor longitud posible y sin bucles. Valor de referencia técnica para DPS tipo 2: longitud total de conexión no mayor a 0,5 m y conductor de cobre de sección no inferior a 6 mm², salvo que el diseño o el fabricante exijan otra; verificar contra el manual y el diseño del SIPRA.
4. Si la caja tiene contacto auxiliar de señalización del DPS, conectarlo al sistema de monitoreo según NES-OPE-PR-021.
5. Durante el ensayo de aislamiento del circuito DC, retirar los cartuchos del DPS o aislarlo según indique el fabricante, para no dañarlo ni falsear la lectura, y reponerlo al terminar.

#### 8.2.4.9. Conexión de strings, polaridad y Voc

Los cables de string llegan a la caja tendidos, identificados y conectorizados según NES-OPE-PR-014 y NES-OPE-PR-015. La conexión se hace con permiso de trabajo eléctrico.

1. Confirmar que el seccionador DC está abierto y bloqueado y que no hay fusibles insertados.
2. Identificar cada par de cables contra el cuadro de strings de la caja: número de string, polo positivo y polo negativo. Un cable sin identificación no se conecta.
3. Pelar a la longitud que indique el fabricante del borne. Valor típico de fabricante para bornes de string con punteras: 18 mm; verificar contra el manual del equipo del proyecto. Sin hilos cortados ni degollados.
4. Cuando el borne lo exija, crimpar puntera o terminal con la herramienta y el dado de la sección; inspección visual del 100% del crimpado y prueba de tracción manual.
5. Antes de conectar, medir con multímetro CAT III o superior la tensión y la polaridad de cada string en el extremo del cable: el positivo al borne positivo del portafusibles y el negativo al borne negativo, según el unifilar. Una polaridad invertida en una caja con strings en paralelo produce cortocircuito franco al insertar los fusibles.
6. Conectar al borne correspondiente y apretar al torque del fabricante con destornillador dinamométrico; trazar marca de torque.
7. Con todos los strings conectados y los fusibles fuera, medir en cada portafusibles la polaridad y la Voc de cada string, y registrar en NES-OPE-F-105 junto con irradiancia, hora y temperatura.
8. Comparar cada Voc con la media de los strings de la misma caja medidos en las mismas condiciones. Desviación de referencia no mayor a ±5% respecto de la media (criterio interno, coherente con NES-OPE-PR-014); un string fuera de rango indica módulo faltante, módulo invertido, conector abierto o polaridad equivocada y no se le inserta fusible hasta aclararlo.
9. Verificar que el número de strings conectados coincide con el cuadro de la caja y que las entradas de reserva quedan sin cable, con tapón y rotuladas como reserva.

> ALTO: Prohibido cerrar un string sobre una caja con fusibles insertados o con el seccionador cerrado. Con luz, cada string tiene tensión plena desde el momento del armado; el error de polaridad entre strings en paralelo no da segunda oportunidad.

#### 8.2.4.10. Conexión del cable de salida (principal DC)

1. Verificar sección, material (cobre o aluminio) y tensión asignada del principal DC contra el unifilar.
2. Preparar el cable respetando el radio mínimo de curvatura del fabricante del cable y sin tensión mecánica sobre la barra.
3. Crimpar el terminal de compresión con crimpadora hidráulica, dado de la sección y número de compresiones del fabricante del terminal. En conductor de aluminio sobre barra de cobre, usar terminal bimetálico y pasta antioxidante; nunca se une aluminio directamente a cobre.
4. Colocar el terminal sobre la barra con la tornillería, arandela plana y arandela de presión o elástica que indique el fabricante, sin pintura ni óxido en la superficie de contacto.
5. Apretar al torque del fabricante con torquímetro calibrado. Rangos típicos de uniones atornilladas en barra: M10 de 28 N·m a 40 N·m y M12 de 45 N·m a 70 N·m, según material y lubricación de la rosca; valor típico de fabricante, verificar contra el manual del equipo del proyecto.
6. Trazar marca de torque y registrar en NES-OPE-F-103 y NES-OPE-F-106.
7. Verificar polaridad del principal en ambos extremos antes de conectar el extremo del inversor o del tablero de recombinación (NES-OPE-PR-018).

#### 8.2.4.11. Torques de bornes

Todo borne y toda unión atornillada de la caja se aprieta con herramienta dinamométrica al valor del manual del fabricante. Los valores se transcriben antes de iniciar en la tabla de torques del proyecto y se verifican en el frente.

| Unión | Torque | Fuente |
|---|---|---|
| Bornes de portafusibles (entrada de string) | [____] N·m (típico 2,0 N·m a 2,5 N·m) | Manual del fabricante de la caja |
| Bornes de barraje o de borne de paso | [____] N·m | Manual del fabricante de la caja |
| Bornes del seccionador DC | [____] N·m | Manual del fabricante del seccionador |
| Bornes del DPS | [____] N·m | Manual del fabricante del DPS |
| Terminal del principal DC en barra | [____] N·m (típico M10: 28 a 40 N·m; M12: 45 a 70 N·m) | Manual del fabricante de la caja |
| Barra o borne de tierra | [____] N·m | Manual del fabricante de la caja |
| Prensaestopas | [____] N·m | Manual del fabricante del prensaestopas |
| Fijación de la caja al soporte | [____] N·m | Plano de detalle |

Control:

- Torquímetros calibrados según ISO 6789, con verificación diaria contra un patrón o probador de torque (criterio interno).
- Marca de torque en el 100% de las uniones apretadas.
- Verificación por QA/QC en una muestra de cajas por bloque, re-aplicando el torque nominal: si la marca se desplaza, la unión estaba floja. Muestra de referencia: 10% de las cajas de cada bloque y el 100% de los principales DC (criterio interno). Una unión floja en la muestra obliga a revisar el 100% de las cajas de esa cuadrilla en el bloque.

#### 8.2.4.12. Puesta a tierra y equipotencialidad

1. Conectar la envolvente metálica, la placa de montaje y la barra de tierra de la caja al conductor de tierra del diseño, que llega desde la malla del SPT según NES-OPE-PR-020.
2. Usar terminal de compresión de la sección del conductor y apretar al torque del fabricante; en puertas metálicas, verificar la trenza de tierra entre puerta y cuerpo.
3. Conectar el conductor de tierra del DPS a la barra de tierra de la caja (numeral 8.2.4.8).
4. No usar la tornillería de fijación ni el soporte como único camino de tierra, salvo que el diseño lo prevea y la continuidad se mida.
5. Medir la continuidad entre la barra de tierra de la caja y el punto de conexión a la malla, y registrar en NES-OPE-F-107. Criterio de continuidad según el diseño del SPT; valor de referencia de baja resistencia que fije el diseñador — [__________].

#### 8.2.4.13. Rotulado y señalización

Toda caja se rotula antes de su liberación, con elementos resistentes a UV, a la intemperie y legibles a la distancia de operación:

- Código de la caja según el unifilar (bloque, inversor, entrada) en el exterior de la puerta.
- Señal de riesgo eléctrico conforme al RETIE y advertencia permanente: "Tensión DC presente mientras haya luz solar. Ambos lados del seccionador pueden estar energizados".
- Advertencia de no abrir portafusibles ni conectores bajo carga.
- Tensión DC máxima y corriente máxima de la caja.
- Identificación de cada string en su borne y en su cable, en coherencia con el cuadro de strings.
- Polaridad de barras y bornes.
- Copia plastificada del cuadro de strings y del esquema de la caja dentro de la puerta.
- Identificación del principal DC en ambos extremos.

Registrar en NES-OPE-F-108.

#### 8.2.4.14. Verificación previa a energización

La caja se libera para energización solo cuando cumple todos los puntos siguientes, registrados en NES-OPE-F-109:

1. Inspección visual completa: montaje, sellado, entradas taponadas, puerta y junta, ausencia de herramientas, viruta, retazos o desecante suelto dentro de la caja.
2. Torques aplicados y marcados en el 100% de las uniones, con la muestra de QA/QC conforme.
3. Polaridad y Voc de todos los strings registradas y conformes.
4. Resistencia de aislamiento del circuito DC con megóhmetro, por el método de la IEC 62446-1 vigente, con el DPS aislado. Para tensión de sistema mayor a 500 V la norma establece ensayo a 1.000 V con valor mínimo de 1 MΩ; se confirma la tabla de la edición vigente antes de ensayar y se registra el método empleado.
5. Continuidad de puesta a tierra conforme.
6. Fusibles del calibre correcto disponibles en la caja, aún sin insertar.
7. Seccionador abierto, bloqueado y con tarjeta.
8. Rotulado completo.
9. Principal DC conectado y verificado en polaridad en ambos extremos.
10. Firma del responsable eléctrico y de QA/QC y entrega a comisionado según NES-OPE-PR-022.

> ALTO: Ninguna caja combinadora se energiza sin dictamen de inspección RETIE de la instalación, sin la autorización escrita del responsable eléctrico y de [CLIENTE] y sin seguir la secuencia de NES-OPE-PR-023. Liberar la caja no es autorizar su energización.

#### 8.2.4.15. No conformidades

Caja o componente dañado, sin certificado o de referencia distinta a la aprobada: cuarentena y consulta a QA/QC y al fabricante antes de usar.

Fusible de calibre, tipo o tensión distinto al de diseño: retiro inmediato y reposición; se revisa el 100% de las cajas del lote.

Polaridad invertida, entrada sin sellar, unión floja o terminal mal crimpado: corrección inmediata y reinspección del 100% de la caja.

Perforación no autorizada de la envolvente: se reporta al fabricante; la caja no se libera sin su disposición escrita.

Evidencia de humedad, condensación o corrosión interna: no se energiza; se seca, se investiga la causa (sello, compensación de presión, perforación) y se documenta.

Cambio de referencia de caja, fusible, seccionador o DPS: requiere aprobación escrita del ingeniero responsable del diseño eléctrico y queda en el RFI log.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Certificación de la caja y componentes | Certificado de conformidad de producto vigente y protocolo FAT | RETIE Res. 40117 de 2024 |
| Estado a la recepción | Sin daño, humedad, polvo ni condensación; placa legible y conforme | Manual del fabricante |
| Posición de montaje | Vertical, entradas hacia abajo; inclinación dentro del rango del fabricante | Manual del fabricante |
| Ubicación | Según plano; en sombra o con protección solar si se exige; sobre nivel de inundación; espacio de trabajo libre | Plano / RETIE |
| Fijación | Solo en puntos del fabricante; sin perforaciones no autorizadas; tornillería al torque del plano | Manual del fabricante / plano |
| Sellado | Prensaestopas del rango del cable, apretados; entradas sin uso taponadas; compensación de presión libre; junta íntegra | Manual del fabricante |
| Fusibles | gPV IEC 60269-6; calibre entre 1,5 y 2,4 veces Isc y no mayor al máximo del módulo; tensión mayor o igual a la máxima del arreglo | IEC 62548 / memoria de cálculo |
| Seccionador DC | IEC 60947-3, tensión y categoría DC de diseño; bloqueable en abierto | IEC 60947-3 / diseño |
| DPS DC | IEC 61643-31; Ucpv mayor o igual a la tensión máxima del arreglo; indicador sano; conexión corta | IEC 61643-31 / diseño SIPRA |
| Polaridad | 100% de strings coincidentes con el unifilar antes de insertar fusibles | IEC 62446-1 |
| Voc por string | Desviación no mayor a ±5% respecto de la media de la caja (criterio interno); valor definitivo del diseñador | IEC 62446-1 / Proyecto |
| Torques | Valor del fabricante en el 100% de uniones; marca de torque; muestra QA/QC sin desplazamiento | Manual del fabricante |
| Resistencia de aislamiento DC | Según tabla de la IEC 62446-1 vigente; tensión de sistema mayor a 500 V: ensayo a 1.000 V y mínimo 1 MΩ | IEC 62446-1 |
| Puesta a tierra | Continuidad conforme al diseño del SPT | NES-OPE-PR-020 / diseño |
| Rotulado | Completo, legible, resistente a UV; señal de riesgo eléctrico RETIE | RETIE |

## 8.4. Documentación para mantener y registrar

Anexos NES-OPE-F-100 a NES-OPE-F-109 de este procedimiento.

Permisos de trabajo, permisos de trabajo eléctrico y ATS/ART del frente.

Certificados de calibración de torquímetros, multímetros, pinzas, megóhmetros y detectores de tensión.

Certificados de conformidad de producto, protocolos FAT, fichas técnicas y manuales de instalación de cajas, fusibles, seccionadores y DPS.

Tabla de torques del proyecto aprobada por el responsable eléctrico.

Cuadro de strings por caja, actualizado como construido.

## 8.5. Control de calidad

QA/QC verifica el 100% de las cajas en recepción, montaje, sellado, rotulado y liberación, y aplica el muestreo de torque del numeral 8.2.4.11. Las cajas liberadas se marcan en el plano de seguimiento del bloque. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación que no afecta calidad, prestación ni seguridad, por ejemplo rótulo incompleto o marca de torque faltante en unión verificada. | Registro y cierre. |
| 2 | Requiere rehacer una conexión, reponer un componente o resellar una entrada con el método de este procedimiento. | Corrección por la cuadrilla y reinspección. |
| 3 | Afecta la seguridad eléctrica, la certificación o la garantía: fusible de calibre o tipo erróneo, polaridad invertida con fusibles insertados, perforación no autorizada, humedad interna, evidencia de arco. | Suspensión del frente, consulta al diseñador eléctrico y al fabricante, aprobación escrita antes de actuar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS/ART y la charla diaria, verifica que las áreas intervenidas estén señalizadas y demarcadas y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre características del proyecto, riesgo eléctrico en corriente continua, arco eléctrico, medidas de control, puntos de encuentro y uso correcto del EPP dieléctrico y de arco.

## 9.1. Reglas de oro

**SIEMPRE** trataré toda caja con strings conectados como energizada mientras haya luz solar.

**SIEMPRE** aplicaré las cinco reglas de oro antes de intervenir una caja (Res. 5018 de 2019).

**NUNCA** abriré un portafusibles ni un conector bajo carga: primero abro el seccionador y verifico 0,0 A.

**NUNCA** insertaré fusibles sin haber verificado la polaridad y la Voc de todos los strings de la caja.

**SIEMPRE** apretaré con torquímetro calibrado y marcaré la unión.

**NUNCA** dejaré una entrada de cable sin sellar ni una caja abierta al terminar la jornada.

**NUNCA** perforaré la envolvente sin aprobación escrita del fabricante.

**SIEMPRE** usaré guantes dieléctricos vigentes, careta y herramienta aislada al intervenir circuitos DC.

**SIEMPRE** trabajaré acompañado y con radio cuando intervenga una caja con strings conectados.

**SIEMPRE** suspenderé la actividad ante lluvia o tormenta eléctrica y me dirigiré al refugio o punto de encuentro.

## 9.2. Distancias de seguridad y riesgo de arco

Se respetan las distancias de seguridad y los espacios de trabajo frente a equipos energizados que fija el RETIE. La categoría del EPP de arco para operar el seccionador y medir dentro de la caja la define el análisis de riesgo de arco del proyecto, con referencia técnica en NFPA 70E; no se interviene una caja con strings conectados sin ese EPP.

## 9.3. Condiciones climáticas de [departamento]

Tormenta eléctrica: ante el aviso o el primer trueno, suspender toda intervención, cerrar las cajas, alejarse de estructuras metálicas, cajas y conductores y dirigirse al refugio. Se reanuda solo con autorización del responsable SST.

Lluvia: no abrir cajas; cerrar y asegurar las abiertas; proteger extremos de cable con tapón y bolsa sellada.

Calor y radiación: hidratación, sombra, pausas activas y rotación; la envolvente y la estructura expuestas al sol se manipulan con guante.

Ofidios e insectos: antes de abrir una caja almacenada o montada, golpear suavemente y abrir con la puerta como escudo; revisar el interior y las canalizaciones.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado al frente | Colisión, volcamiento, caídas al mismo nivel. | Conductores autorizados; vías y velocidades del proyecto; cinturón obligatorio. |
| 2. Descargue y recepción | Golpes, atrapamiento, sobreesfuerzo, caída de la carga. | Equipo mecánico para cargas pesadas; dos personas como mínimo; máximo 25 kg por persona (Res. 2400 de 1979, art. 392); guantes. |
| 3. Distribución en fila con máquina | Atropellamiento, caída de la carga. | Operador certificado; señalero; carga asegurada; nadie bajo la carga. |
| 4. Montaje de soporte y caja | Golpes, cortes, atrapamiento de manos, caída de la caja. | Herramienta en buen estado; guantes anticorte; caja asegurada antes de soltar; no levantar de prensaestopas o puerta. |
| 5. Trabajo en altura en muro o soporte alto | Caída a distinto nivel. | Plataforma o escalera certificada; permiso de alturas cuando haya exposición a 2 m o más (Res. 4272 de 2021). |
| 6. Perforación y preparación de entradas (si aplica) | Proyección de partículas, cortes, ruido. | Gafas, careta, guantes; retirar viruta; protección auditiva. |
| 7. Conexión de strings | Choque eléctrico, arco, cortocircuito por polaridad invertida. | PTE; seccionador abierto y bloqueado; fusibles fuera; polaridad medida antes de conectar; EPP dieléctrico y careta; trabajo en pareja. |
| 8. Crimpado de terminales | Atrapamiento de dedos, proyección por falla hidráulica. | Herramienta y dado correctos; manos fuera de la matriz; inspección de mangueras. |
| 9. Apriete de bornes | Contacto con partes energizadas, sobreesfuerzo de muñeca. | Herramienta aislada; torquímetro del rango; postura adecuada. |
| 10. Medición de Voc y aislamiento | Choque eléctrico, lectura falsa, descarga capacitiva tras el megado. | Instrumento CAT III o superior; detector probado antes y después; descargar el circuito al terminar el ensayo; DPS aislado. |
| 11. Rotulado | Cortes, contacto con partes energizadas. | Rotular con la caja cerrada o con el circuito bloqueado. |
| 12. Exposición ambiental | Radiación UV, estrés térmico, deshidratación, ofidios. | Ropa manga larga, cubrenuca, protector solar, hidratación, sombra, pausas; polainas. |
| 13. Tormenta eléctrica y lluvia | Descarga atmosférica, choque eléctrico, ingreso de agua a la caja. | Suspender; cerrar cajas; refugio o punto de encuentro. |
| 14. Orden, aseo y residuos | Tropiezos, cortes, contaminación del suelo. | Retazos y terminales en recipiente; área despejada al cierre; separación de residuos. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Aire | Emisiones y ruido | Vehículos y equipos con revisión técnico-mecánica y mantenimiento al día; motores apagados en reposo; humectación de vías en época seca. |
| Suelo | Embalajes | Cartón, madera de estibas, plásticos y espumas separados en la fuente con el código de colores de la Res. 2184 de 2019 y entregados a gestor autorizado para aprovechamiento. |
| Suelo | Retazos de cable y cobre | Recogidos el mismo día, pesados y almacenados como aprovechable; entrega a gestor autorizado con acta y certificado. |
| Suelo | Fusibles, DPS y componentes retirados | Componentes eléctricos retirados, quemados o no conformes en recipiente rotulado, gestionados como RAEE según la Ley 1672 de 2013. |
| Suelo | Residuos peligrosos (RESPEL) | Trapos con pasta antioxidante o grasa, envases de pintura de marca de torque y aerosoles en recipientes rotulados; almacenamiento en zona RESPEL y entrega a gestor autorizado según el Decreto 1076 de 2015. |
| Suelo | Desecantes | Bolsas de desecante retiradas de las cajas se recogen y se disponen según su ficha de datos de seguridad. |
| Suelo | Derrames | Kit antiderrame en cada frente y vehículo; bandeja bajo equipos hidráulicos estacionados. |
| Suelo | RCD | Gestión según Res. 0472 de 2017 modificada por Res. 1257 de 2021. |
| Flora y fauna | Intervención de hábitat | Trabajar solo en áreas liberadas; revisar fauna dentro de cajas y canalizaciones antes de intervenir; reporte de fauna para rescate según PMA. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener la actividad y asegurar la zona: abrir el seccionador DC de la caja afectada desde una posición fuera de la línea de proyección, alejar al personal y no manipular fusibles ni conectores.
2. Notificar al responsable SST y al responsable eléctrico de Neptuno Energy Services y al interlocutor de [CLIENTE].
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, extintor en cada frente).
4. Incidente grave: activar la línea 123 y el traslado al centro asistencial definido; notificar a la ARL.
5. Reportar el evento y realizar la investigación según Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Arco o incendio dentro de una caja combinadora

No abrir la puerta de una caja con humo, olor a quemado o ruido de arco: la apertura aporta oxígeno y expone al trabajador al arco.

Abrir el seccionador o el dispositivo aguas abajo solo si se puede hacer desde fuera y sin exponerse; recuerde que los strings siguen alimentando la caja mientras haya luz.

Conato de incendio: usar extintor apto para equipo eléctrico energizado. Nunca agua sobre un circuito DC energizado. Si el fuego avanza, evacuar y activar la emergencia.

Delimitar la zona, no reenergizar y no manipular la caja hasta la inspección del responsable eléctrico.

## 12.2. Choque eléctrico y quemaduras

No tocar a la víctima mientras siga en contacto con el circuito; separarla con elemento aislante; activar la emergencia y aplicar reanimación si el personal está capacitado.

Enfriar la quemadura con agua limpia a temperatura ambiente; no aplicar hielo, cremas ni remedios caseros; no retirar ropa adherida; cubrir con apósito estéril.

Toda persona que sufra un choque eléctrico o una quemadura por arco se remite a valoración médica aunque se sienta bien.

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Responsable eléctrico Neptuno Energy Services | [__________] | [__________] |
| Residente de obra Neptuno Energy Services | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Recepción e inspección de cajas combinadoras y tableros DC | NES-OPE-F-100 | QA/QC |
| Control de almacenamiento y preservación | NES-OPE-F-101 | Almacenista / QA/QC |
| Protocolo de montaje mecánico | NES-OPE-F-102 | Supervisor de frente |
| Registro de torques de bornes y uniones | NES-OPE-F-103 | Oficial electricista / QA/QC |
| Verificación de fusibles gPV, seccionador y DPS | NES-OPE-F-104 | Responsable eléctrico |
| Registro de polaridad y Voc de strings en caja | NES-OPE-F-105 | Responsable eléctrico |
| Protocolo de conexión del principal DC | NES-OPE-F-106 | Responsable eléctrico |
| Verificación de puesta a tierra de la caja | NES-OPE-F-107 | Responsable eléctrico / QA/QC |
| Lista de verificación de rotulado y señalización | NES-OPE-F-108 | QA/QC |
| Liberación de caja combinadora previa a energización | NES-OPE-F-109 | Responsable eléctrico / QA/QC |
| ATS/ART, permisos de trabajo y permisos de trabajo eléctrico | Según NES-SST-PR-001 | Supervisor / Responsable SST |
| Certificados de calibración y de producto | — | QA/QC |

# 14. ANEXOS

## NES-OPE-F-100 — Recepción e inspección de cajas combinadoras y tableros DC

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Remisión / orden de compra: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-017 | Transportador / placa: [__________] |

| N.º de serie | Referencia | Embalaje sin daño | Placa conforme | Interior seco y limpio | Certificado producto / FAT | Estado (A / C / R) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Indicadores de impacto o inclinación sin activar | | | |
| 2 | Tensión DC máxima, corriente y n.º de entradas según submittal | | | |
| 3 | Grado IP e IK según especificación | | | |
| 4 | Fusibles gPV IEC 60269-6, calibre y tensión de diseño | | | |
| 5 | Seccionador DC y DPS de la referencia aprobada | | | |
| 6 | Prensaestopas, insertos, tapones y compensación de presión completos | | | |
| 7 | Junta de puerta íntegra; cerraduras operativas | | | |
| 8 | Manual de instalación y llaves entregados | | | |

{.plain}
| Observaciones (A: aceptada; C: cuarentena; R: rechazada): |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-101 — Control de almacenamiento y preservación de cajas combinadoras

{.plain}
| Proyecto: [__________] | Mes: [____] |
|---|---|
| Bodega / contenedor: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-017 | Condiciones del fabricante: [____] °C / [____] % HR |

| Fecha | Temp. (°C) | HR (%) | Embalajes íntegros | Posición correcta (cara posterior) | Sin humedad, plagas ni ofidios | Responsable |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

{.plain}
| Cantidad en bodega: [____] | Cantidad despachada a campo: [____] |
|---|---|
| Fusibles y DPS bajo llave: Sí / No | Desecantes en buen estado: Sí / No |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-102 — Protocolo de montaje mecánico de caja combinadora

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja (código / n.º de serie): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-017 | Plano de detalle: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Soporte, hinca o poste liberado (NES-OPE-PR-012) y galvanizado sin daño | | | |
| 2 | Ubicación según plano; no sobre parte giratoria del tracker | | | |
| 3 | Altura de montaje: [____] m (plano: [____] m) | | | |
| 4 | Posición vertical, entradas hacia abajo | | | |
| 5 | Sombra o protección solar según diseño | | | |
| 6 | Sobre nivel de inundación; sin escorrentía de módulos | | | |
| 7 | Fijación solo en puntos del fabricante; sin perforaciones no autorizadas | | | |
| 8 | Aislamiento galvánico instalado cuando se exige | | | |
| 9 | Tornillería de fijación al torque del plano y con marca | | | |
| 10 | Caja firme, sin vibración; puerta abre y cierra sin interferencia | | | |
| 11 | Espacio frontal de trabajo libre | | | |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-103 — Registro de torques de bornes y uniones

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja (código / n.º de serie): [__________] | Consecutivo: [____] |
| Torquímetro (serie / calibración): [__________] | Destornillador dinamométrico (serie / calibración): [__________] |

| Unión | Cantidad | Torque especificado (N·m) | Torque aplicado (N·m) | Marca de torque | Verificación QA/QC | Obs. |
|---|---|---|---|---|---|---|
| Bornes de portafusibles | | | | | | |
| Barraje / bornes de paso | | | | | | |
| Seccionador DC | | | | | | |
| DPS DC | | | | | | |
| Principal DC en barra (+) | | | | | | |
| Principal DC en barra (−) | | | | | | |
| Barra de tierra | | | | | | |
| Prensaestopas | | | | | | |
| Fijación al soporte | | | | | | |

{.plain}
| Ejecutante (oficial): [__________] | Verificó (QA/QC): [__________] |
|---|---|

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-104 — Verificación de fusibles gPV, seccionador DC y DPS DC

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja (código / n.º de serie): [__________] | Consecutivo: [____] |
| Isc del módulo: [____] A | Calibre máximo de fusible del módulo: [____] A |
| Tensión máxima del arreglo: [____] V | Memoria de cálculo: [__________] |

| Ítem | Verificación | Valor | Cumple | No cumple |
|---|---|---|---|---|
| 1 | Fusibles gPV según IEC 60269-6 | Ref.: | | |
| 2 | Calibre del fusible (entre 1,5 y 2,4 Isc y no mayor al máximo del módulo) | ____ A | | |
| 3 | Tensión asignada del fusible mayor o igual a la máxima del arreglo | ____ V | | |
| 4 | Fusibles en el polo o los polos de diseño | + / − / ambos | | |
| 5 | Mismo calibre en toda la caja, salvo indicación de diseño | — | | |
| 6 | Fusibles fuera del portafusibles hasta autorización | — | | |
| 7 | Seccionador IEC 60947-3, tensión y categoría DC de diseño | ____ V / ____ A | | |
| 8 | Seccionador opera en vacío; indicación de posición correcta | — | | |
| 9 | Seccionador abierto, bloqueado y con tarjeta | — | | |
| 10 | DPS IEC 61643-31; Ucpv mayor o igual a la tensión máxima del arreglo | ____ V | | |
| 11 | Cartuchos del DPS insertados; indicador sano | — | | |
| 12 | Conexión a tierra del DPS corta y sin bucles | ____ m | | |
| 13 | Contacto de señalización del DPS conectado (si aplica) | — | | |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-105 — Registro de polaridad y Voc de strings en caja combinadora

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja (código / n.º de serie): [__________] | Consecutivo: [____] |
| Irradiancia: [____] W/m² | Temperatura ambiente: [____] °C |
| Hora de medición: [____] | Instrumento (serie / calibración): [__________] |

| Entrada | String (código) | Polaridad OK | Voc (V) | Desviación vs. media (%) | Cumple | Obs. |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

{.plain}
| Voc media de la caja: [____] V | Entradas de reserva taponadas y rotuladas: Sí / No |
|---|---|

{.plain}
| Observaciones y strings no conformes: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-106 — Protocolo de conexión del principal DC

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja de origen: [__________] | Destino (tablero DC / inversor): [__________] |
| Cable: [____] mm², Cu / Al, [____] V | Consecutivo: [____] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Sección, material y tensión según unifilar | | | |
| 2 | Radio de curvatura respetado; sin tensión sobre la barra | | | |
| 3 | Terminal de la sección; bimetálico si conductor de aluminio | | | |
| 4 | Crimpado con dado y n.º de compresiones del fabricante | | | |
| 5 | Pasta antioxidante en unión de aluminio | | | |
| 6 | Superficie de contacto limpia, sin pintura ni óxido | | | |
| 7 | Tornillería y arandelas según fabricante | | | |
| 8 | Torque aplicado y marcado | | | |
| 9 | Polaridad verificada en ambos extremos | | | |
| 10 | Prensaestopas sellado y bucle de goteo | | | |
| 11 | Identificación del principal en ambos extremos | | | |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-107 — Verificación de puesta a tierra de caja combinadora

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque: [__________] | Consecutivo: [____] |
| Instrumento (serie / calibración): [__________] | Criterio de diseño: [____] Ω |

| Caja (código) | Conductor de tierra (mm²) | Envolvente y placa conectadas | Trenza de puerta | Tierra del DPS | Continuidad medida (Ω) | Cumple |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-108 — Lista de verificación de rotulado y señalización de cajas combinadoras

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / cajas: [__________] | Consecutivo: [____] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Código de caja en el exterior, según unifilar | | | |
| 2 | Señal de riesgo eléctrico conforme al RETIE | | | |
| 3 | Advertencia de tensión DC con luz solar en ambos lados del seccionador | | | |
| 4 | Advertencia de no abrir portafusibles ni conectores bajo carga | | | |
| 5 | Tensión y corriente máximas de la caja | | | |
| 6 | Identificación de cada string en borne y cable | | | |
| 7 | Polaridad de barras y bornes | | | |
| 8 | Cuadro de strings y esquema plastificado dentro de la puerta | | | |
| 9 | Principal DC identificado en ambos extremos | | | |
| 10 | Rótulos resistentes a UV y legibles | | | |

{.plain}
| Observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-109 — Liberación de caja combinadora previa a energización

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja (código / n.º de serie): [__________] | Consecutivo: [____] |
| Inversor asociado: [__________] | Plano unifilar: [__________] |

| Ítem | Verificación | Registro | Cumple | No cumple |
|---|---|---|---|---|
| 1 | Recepción y almacenamiento conformes | F-100 / F-101 | | |
| 2 | Montaje mecánico conforme | F-102 | | |
| 3 | Torques aplicados, marcados y muestra QA/QC conforme | F-103 | | |
| 4 | Fusibles, seccionador y DPS conformes | F-104 | | |
| 5 | Polaridad y Voc de todos los strings conformes | F-105 | | |
| 6 | Principal DC conectado y verificado | F-106 | | |
| 7 | Puesta a tierra conforme | F-107 | | |
| 8 | Rotulado completo | F-108 | | |
| 9 | Entradas selladas, sin viruta, herramienta ni residuos dentro | — | | |
| 10 | Seccionador abierto y bloqueado; fusibles disponibles sin insertar | — | | |

{.plain}
| Ensayo de aislamiento DC — método: [__________] | Tensión de ensayo: [____] V |
|---|---|
| Polo (+) a tierra: [____] MΩ | Polo (−) a tierra: [____] MΩ |
| DPS aislado durante el ensayo: Sí / No | Circuito descargado al terminar: Sí / No |

{.plain}
| Resultado: Caja liberada para comisionado / No liberada. Esta liberación no autoriza la energización, que se rige por NES-OPE-PR-023. |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

# 15. CONTROL DE CAMBIOS

| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
