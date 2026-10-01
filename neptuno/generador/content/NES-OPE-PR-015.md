---
code: NES-OPE-PR-015
header_title: PROCEDIMIENTO DE TENDIDO DE CABLES DE POTENCIA BT Y MT
cover_title: Procedimiento de Tendido de Cables de Potencia BT y MT
cover_subtitle: Zanja, ducto y bandeja en plantas fotovoltaicas
---

# 1. OBJETIVO

Definir el método de trabajo, los cálculos de control, los criterios de aceptación y las medidas preventivas para el tendido de los cables de potencia de la planta FV [PROYECTO] — cables DC de string y de agrupamiento, cables AC de baja tensión y cables de media tensión hasta 36 kV — en zanja directamente enterrados, en ductos o banco de ductos y en bandeja, desde la recepción del carrete hasta los ensayos de recepción posteriores al tendido, conforme al RETIE, a la NTC 2050 en lo que el RETIE adopta, a las normas de producto del cable y a las instrucciones del fabricante del cable.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir el daño oculto del cable durante el tendido —la causa más frecuente de fallas tempranas de aislamiento en media tensión— y controlar los riesgos de atrapamiento, sobreesfuerzo, caída de carretes y trabajo en zanja.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en:

- Recepción, inspección, almacenamiento, traslado y manejo de carretes de cable con portabobinas, gatos de carrete y equipo de izaje.
- Verificación y liberación de zanjas, ductos, cámaras de inspección y bandejas antes del tendido.
- Cálculo previo y control en campo de la tensión de halado y de la presión lateral en curvas, y selección del método de tiro (ojo de tiro sobre conductor o manga).
- Tendido manual, con rodillos o con malacate de cables DC de string en canalización, cables DC de agrupamiento, cables AC de baja tensión (0,6/1 kV) y cables de media tensión de aislamiento extruido hasta 36 kV (Um).
- Colocación en zanja: cama y recubrimiento de arena o material seleccionado, separaciones, protección mecánica, cinta de señalización y relleno, en coordinación con NES-OPE-PR-002.
- Sellado de extremos, identificación de circuitos y fases, y ensayos de recepción tras el tendido: continuidad, resistencia de aislamiento y ensayo de cubierta.

No incluye la excavación y el relleno estructural de zanjas, que se rigen por NES-OPE-PR-002; el conexionado y la conectorización DC, que se rigen por NES-OPE-PR-014; la confección de empalmes, terminales y conectores separables de media tensión y sus ensayos VLF, tan delta y descargas parciales, que se rigen por NES-OPE-PR-016; la red de puesta a tierra y el SIPRA, que se rigen por NES-OPE-PR-020; ni el comisionado y la energización, que se rigen por NES-OPE-PR-022 y NES-OPE-PR-023.

> NOTA: Un cable de media tensión dañado durante el tendido casi nunca falla en el ensayo de aislamiento inmediato: falla meses después, en servicio. Por eso este procedimiento controla el proceso (tensión, presión lateral, radio, temperatura, estado de la canalización) y no solo el resultado de los ensayos.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / ART y PT | Análisis de trabajo seguro / análisis de riesgo del trabajo y permiso de trabajo. |
| BT | Baja tensión. En este documento, cables AC de tensión asignada 0,6/1 kV y cables DC de hasta 1.500 V. |
| MT | Media tensión. Cables de aislamiento extruido con tensión asignada U0/U (Um) hasta 18/30 (36) kV según IEC 60502-2, o clase equivalente de 15 kV, 25 kV o 35 kV según especificación del proyecto. |
| Cable de string | Cable unipolar fotovoltaico que une los strings con la caja combinadora o con el inversor string, conforme a IEC 62930 o norma de producto equivalente. |
| Cable de agrupamiento DC | Cable DC de mayor sección que une la caja combinadora con el inversor central o con el tablero de agrupamiento. |
| Carrete (bobina) | Tambor de madera o acero sobre el que el fabricante enrolla el cable. Lleva identificación de referencia, sección, longitud, lote y sentido de giro. |
| Portabobinas | Equipo (remolque, caballete con gatos o desenrollador) que sostiene el carrete por su eje y permite que gire libremente durante el tendido. |
| Ojo de tiro | Accesorio de tracción fijado al conductor por compresión o por el fabricante. Transmite la fuerza directamente al conductor. |
| Manga de tiro | Malla de acero que abraza la cubierta del cable. Transmite la fuerza a través de la cubierta y tiene un límite menor que el ojo de tiro. |
| Destorcedor y fusible mecánico | Elemento giratorio que impide que la torsión del cable de tiro pase al cable de potencia, y pieza calibrada que se rompe al superar la tensión máxima permitida. |
| Tensión de halado | Fuerza de tracción aplicada al cable durante el tendido, en kN. |
| Presión lateral (SWBP) | Fuerza por unidad de radio que el cable ejerce contra la pared interior de una curva, en kN/m. Se calcula dividiendo la tensión a la salida de la curva por el radio de la curva. |
| Coeficiente de fricción (μ) | Relación entre la fuerza de rozamiento y la fuerza normal entre cable y canalización. Depende de la cubierta, del ducto y del lubricante. |
| Factor de corrección por peso (w) | Factor que incrementa la fricción cuando se halan varios cables a la vez en un mismo ducto, según su disposición. |
| Relación de atasco (D/d) | Cociente entre el diámetro interior del ducto y el diámetro exterior de un cable. Con tres cables, ciertos valores producen atasco en curvas. |
| Radio mínimo de curvatura | Radio por debajo del cual el cable sufre daño en aislamiento, pantalla o cubierta. Lo fija el fabricante; es mayor durante el tiro que en la posición final. |
| Pantalla metálica | Capa de alambres o cintas de cobre sobre el aislamiento de un cable MT, que confina el campo eléctrico y conduce corrientes de falla. |
| Cubierta (chaqueta) | Capa exterior extruida que protege el cable contra humedad, abrasión y agentes químicos. |
| Ensayo de cubierta | Ensayo con tensión DC entre la pantalla metálica y tierra que comprueba que la cubierta no sufrió perforaciones durante el tendido (IEC 60229). |
| Banco de ductos | Conjunto de ductos agrupados, embebidos en concreto o en relleno controlado, con cámaras de inspección. |
| Cámara de inspección | Caja enterrada que permite el tiro, el cambio de dirección y la inspección de los cables en un banco de ductos. |
| Cinta de señalización | Cinta plástica de advertencia de color y leyenda normalizados, que se tiende sobre los cables enterrados para alertar a futuras excavaciones. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. Rutas de zanjas, bancos de ductos, cámaras, bandejas, inversores, centros de transformación y subestación se identifican en el plano general de implantación [N° de plano], en los planos de canalizaciones y secciones tipo de zanja [N° de plano] y en la lista de cables del proyecto [N° de documento].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

- Lista de cables (cable schedule) del proyecto: identificación, origen, destino, referencia, sección, longitud y carrete asignado — [N° de documento].
- Planos de canalizaciones, secciones tipo de zanja, banco de ductos, cámaras de inspección y bandejas — [N° de plano].
- Diagramas unifilares DC, BT y MT del proyecto — [N° de plano].
- Fichas técnicas e instrucciones de instalación del fabricante del cable: tensión máxima de halado, presión lateral admisible, radio mínimo de curvatura durante el tiro y en reposo, temperatura mínima de instalación, peso por metro y diámetro exterior.
- Protocolos de ensayo de rutina en fábrica por carrete y certificados de conformidad de producto exigidos por el RETIE.
- Ficha técnica y hoja de datos de seguridad del lubricante de tendido, compatible con la cubierta del cable.
- NES-OPE-PR-002 Excavación de zanjas y movimiento de tierras; NES-OPE-PR-014 Conexionado DC y conectores MC4; NES-OPE-PR-011 Preservación de materiales de puesta a tierra; NES-OPE-PR-016 Empalmes y terminales de media tensión; NES-OPE-PR-020 Puesta a tierra y SIPRA; NES-OPE-PR-022 Pruebas y comisionado del generador FV.
- NES-CAL-PLN-002 Plan de calidad; NES-SST-PLN-001 Plan de emergencias; NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-SST-PR-003 Izaje de cargas con grúa.

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes: requisitos de producto, de instalación, de identificación y de certificación de conductores y canalizaciones; dictamen de inspección de la instalación.
- NTC 2050 — Código Eléctrico Colombiano, en los requisitos que el RETIE adopta: métodos de alambrado e instalaciones subterráneas (capítulo 3), ocupación de canalizaciones (capítulo 9) y sistemas solares fotovoltaicos (artículo 690).
- IEC 60502-1 e IEC 60502-2 — Cables de potencia con aislamiento extruido de 1 kV a 30 kV (Um 36 kV): construcción, ensayos y radios de curvatura de referencia.
- IEC 62930 — Cables eléctricos para sistemas fotovoltaicos con tensión nominal de 1,5 kV DC.
- IEC 60229 — Ensayos eléctricos de cubiertas extruidas de cables con función protectora especial.
- IEC 60364-6 — Verificación de instalaciones de baja tensión (resistencia de aislamiento de circuitos BT).
- IEC 62446-1 — Ensayos de puesta en servicio de sistemas fotovoltaicos (circuitos DC).
- IEEE 1185 — Práctica recomendada para la instalación de cables en centrales de generación e instalaciones industriales (tensión de halado, presión lateral, factor de corrección por peso). Referencia técnica.
- IEEE 400 e IEEE 400.2 — Ensayos en campo de sistemas de cables apantallados, aplicables una vez confeccionados los accesorios (NES-OPE-PR-016).
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST. Resolución 0312 de 2019 — Estándares mínimos del SG-SST.
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en el sector eléctrico; cinco reglas de oro.
- Resolución 2400 de 1979 — Estatuto de seguridad industrial; arts. 388 a 392 (manejo manual de cargas) y arts. 398 a 447 (manejo y transporte mecánico de materiales).
- Resolución 4272 de 2021 — Trabajo en alturas, para bandejas elevadas a 2 m o más. Resolución 0491 de 2020 — Espacios confinados, para cámaras de inspección que lo sean.
- Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo. Resolución 2844 de 2007 — GATI ruido.
- Decreto 1496 de 2018 — Sistema Globalmente Armonizado (SGA) para el lubricante y los solventes.
- Ley 1503 de 2011 y Resolución 40595 de 2022 (MinTransporte) — PESV, para el transporte interno de carretes.
- Decreto 1076 de 2015 y sus modificaciones vigentes (RESPEL); Resolución 2184 de 2019 (código de colores); Resolución 0472 de 2017 modificada por la Resolución 1257 de 2021 (RCD); licencia ambiental y PMA del proyecto — [N° de resolución].
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

- Aprobar y divulgar el presente procedimiento y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.
- Aprobar el plan de tendido (secuencia de circuitos, asignación de carretes, puntos de tiro y equipos) antes de iniciar cada frente.
- Tramitar ante [CLIENTE] los RFI, los cambios de ruta, de referencia de cable o de longitud de carrete.
- Detener cualquier tendido que no cumpla este procedimiento, el diseño o la instrucción del fabricante del cable.

## 6.2. Responsable eléctrico (ingeniero con matrícula COPNIA vigente)

- Elaborar o revisar el cálculo de tensión de halado y presión lateral de cada tiro de MT y de los tiros críticos de BT, y fijar la tensión máxima y el fusible mecánico.
- Verificar la coincidencia entre lista de cables, carrete asignado y longitud real, y aprobar los cortes.
- Ejecutar o supervisar los ensayos de recepción tras el tendido y firmar los registros.
- Coordinar con el área de puesta a tierra (NES-OPE-PR-020) el tendido del conductor de tierra que acompaña a los circuitos.

## 6.3. Supervisor / capataz de tendido

- Dirigir la cuadrilla, asignar posiciones (carrete, boca de ducto, curvas, malacate) y mantener la comunicación por radio entre extremos.
- Elaborar con los trabajadores el ATS/ART diario y la charla de inicio de turno.
- Verificar el estado de rodillos, poleas, malacate, dinamómetro, destorcedor y manga antes de cada tiro.
- Diligenciar los registros del frente el mismo día.

## 6.4. Operador de malacate y de portabobinas

- Operar el equipo según su manual, a velocidad constante, con el dinamómetro a la vista y con orden de parada inmediata ante cualquier aviso.
- Frenar el carrete para evitar que gire libre y forme bucles o que el cable se desenrolle sobre el terreno.
- Realizar el preoperacional diario del equipo.

## 6.5. Oficiales electricistas (técnicos con matrícula CONTE vigente)

- Guiar el cable en la boca del ducto, en curvas y en la zanja, controlar el radio de curvatura y aplicar el lubricante.
- Sellar los extremos, identificar cables y fases y acomodar el cable en su posición final.
- Ejecutar los ensayos de recepción bajo la supervisión del responsable eléctrico.

## 6.6. Responsable de calidad (QA/QC)

- Controlar el cumplimiento del Plan de Inspección y Ensayos derivado de NES-CAL-PLN-002 y liberar cada circuito con los formatos de este documento.
- Mantener la trazabilidad entre carrete, lote, circuito, longitud cortada y ensayos.
- Registrar y hacer seguimiento a las no conformidades hasta su cierre.

## 6.7. Responsable SST (con licencia en SST vigente)

- Elaborar y divulgar la matriz de peligros del tendido: atrapamiento, sobreesfuerzo, caída de carretes, trabajo en zanja, izaje y, cuando aplique, trabajo en alturas o en espacio confinado.
- Verificar permisos, EPP, estado de la zanja según NES-OPE-PR-002 y competencia del personal; coordinar con el coordinador de alturas cuando aplique.
- Aplicar el protocolo de tormenta eléctrica y liderar la atención de emergencias.

## 6.8. Responsable ambiental

- Asegurar el cumplimiento del PMA y de la licencia ambiental del proyecto.
- Verificar la gestión de carretes, retazos de cable, lubricante, embalajes y residuos peligrosos con gestores autorizados.

## 6.9. Trabajadores

- Cumplir este procedimiento, participar en el ATS/ART y obedecer las señales del supervisor durante el tiro.
- Usar correctamente el EPP y no ubicarse nunca dentro del seno del cable de tiro ni en la línea de retroceso de un cable o manga.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Responsable eléctrico, supervisor de tendido, operador de malacate y de portabobinas, oficiales electricistas, auxiliares de tendido (uno por cada boca, curva o cámara relevante), QA/QC, responsable SST. Señalero certificado cuando se ice el carrete con grúa. |
| Materiales | Cables | Cables de la referencia, sección y tensión de la lista de cables, con certificado de conformidad de producto y protocolo de ensayo de fábrica por carrete. |
| Materiales | Accesorios de tendido | Capuchones termocontráctiles o capuchones de sellado para extremos; lubricante de tendido compatible con la cubierta; cinta de señalización; arena lavada o material de cama de la especificación; losetas o placas de protección mecánica cuando el plano las exija; amarres no metálicos resistentes a UV; rótulos de identificación indelebles. |
| Herramientas | Tendido | Rodillos rectos y de curva, poleas de esquina con el radio mínimo de curvatura, embudo o boquilla de entrada al ducto, mangas de tiro del diámetro del cable, ojos de tiro, destorcedor, fusible mecánico calibrado, cuerda o cable de tiro de baja elongación. |
| Herramientas | Preparación | Mandril o sonda de limpieza de ductos, guía de alambre o cinta pasacables, cepillo de ducto, cortacables de trinquete, cinta métrica y odómetro de rueda. |
| Equipos | Manejo de carretes | Remolque portabobinas, caballetes con gatos y eje de acero del diámetro del agujero del carrete, freno de carrete, grúa o montacargas con eslinga y barra separadora según NES-SST-PR-003. |
| Equipos | Tracción | Malacate de cables con dinamómetro de lectura continua y, preferiblemente, registro de tensión; empujador de cables (cable pusher) para tiros largos de BT cuando se use. |
| Equipos | Medida | Megóhmetro con tensiones de ensayo de 500 V, 1.000 V y 5.000 V DC; fuente de ensayo DC hasta 10 kV para ensayo de cubierta; multímetro y equipo de continuidad; todos con certificado de calibración vigente. Torquímetro según ISO 6789 si se fijan accesorios. |
| Equipos | Apoyo | Radios de comunicación (uno por cada punto de control), conos y cinta de demarcación, iluminación, carpa para equipos de medida, extintor y botiquín por frente. |
| EPP | Básico | Casco con barbuquejo, gafas de seguridad con filtro UV, botas con puntera, chaleco reflectivo, guantes de vaqueta o anticorte para manipular cable y manga, protección auditiva cerca del malacate, cubrenuca, protector solar, ropa manga larga, polainas en zonas con ofidios. |
| EPP | Eléctrico | Para ensayos y para trabajo cerca de circuitos energizados: guantes dieléctricos de clase acorde con la tensión, protección facial y ropa con la categoría que indique el análisis de riesgo de arco; detector de tensión. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

- Plan de tendido aprobado: secuencia de circuitos, carretes asignados con su longitud, dirección de tiro, ubicación del portabobinas y del malacate, y cálculo de tensión y presión lateral firmado por el responsable eléctrico (formato NES-OPE-F-082).
- Zanja, ducto o bandeja liberados por QA/QC con el formato NES-OPE-F-081: profundidad, ancho, fondo nivelado y limpio, cama de arena colocada, ductos limpios y mandrilados, bandeja completa y aterrizada.
- Excavación con permiso vigente y taludes o entibado conforme a NES-OPE-PR-002; sin agua estancada en el fondo.
- Carretes recibidos e inspeccionados con el formato NES-OPE-F-080, con extremos sellados y protocolo de fábrica disponible.
- Equipos de tendido inspeccionados: malacate con dinamómetro calibrado, rodillos completos y que giran libremente, poleas de curva con el radio requerido, manga del diámetro del cable, destorcedor y fusible mecánico del valor calculado.
- Personal suficiente, con radio, en cada punto de control.
- ATS/ART, charla de inicio de turno y permiso de trabajo diligenciados; permiso de izaje si el carrete se iza con grúa.
- Condiciones climáticas aptas: sin tormenta eléctrica, sin lluvia que inunde la zanja y, si la ficha técnica lo exige, temperatura del cable por encima de la mínima de instalación del fabricante.

> ALTO: No se inicia ningún tiro de MT sin el cálculo de tensión y presión lateral firmado, sin dinamómetro funcionando y sin comunicación por radio entre el carrete y el malacate. Un tiro sin control de tensión es un tiro sin control de daño.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

El frente se organiza por circuito y por tramo entre puntos de tiro. Se delimitan y señalizan: la zona del portabobinas, la boca de entrada al ducto o a la zanja, cada cámara de inspección abierta, la zona del malacate con su anclaje y la línea del cable de tiro, el área de acopio de carretes y el punto de acopio de residuos. Toda zanja abierta se protege con baranda o cinta y señal de peligro conforme a NES-OPE-PR-002, y las cámaras abiertas se cubren o se vallan cuando no haya personal en ellas.

### 8.2.2. Ingreso de personal

- Evaluar el estado de la zanja (taludes, agua, material suelto en los bordes) y confirmar que no haya trabajos simultáneos incompatibles en la misma ruta.
- Diligenciar ATS/ART y permiso de trabajo; permiso de espacio confinado si alguna cámara lo es (Resolución 0491 de 2020).
- Ingresar a la zanja solo por escaleras o rampas previstas; nunca saltar ni descender por el talud.
- Ubicar equipos de emergencia y asignar el punto de encuentro.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional de vehículos, portabobinas, malacate y grúa; circulación solo por rutas autorizadas, a la velocidad del proyecto.
- Ningún vehículo ni equipo se estaciona a menos de la distancia al borde de zanja que fije NES-OPE-PR-002, ni pasa sobre cables tendidos sin protección.
- El malacate se ancla a un punto calculado para la tensión máxima del tiro, nunca a la estructura de los trackers ni a un vehículo sin freno.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Recepción e inspección de carretes

Al recibir cada carrete se verifica, y se registra en el formato NES-OPE-F-080:

1. Identificación del rótulo: fabricante, referencia, sección, tensión asignada, longitud, número de carrete, lote y fecha de fabricación; coincidencia con la orden de compra y con la lista de cables.
2. Estado del carrete: tablas o duelas de protección completas, sin flanges rotos, sin clavos que sobresalgan hacia el cable y sin golpes de montacargas.
3. Estado de los extremos: ambos extremos con capuchón de sellado íntegro y firmemente adherido. Un extremo sin capuchón puede haber dejado entrar agua al conductor o bajo la pantalla.
4. Estado visible del cable: sin aplastamientos, cortes, abrasión ni deformación de la cubierta en las vueltas exteriores.
5. Documentos: protocolo de ensayos de rutina del fabricante y certificado de conformidad de producto.
6. Medida de resistencia de aislamiento de recepción en los cables MT y en los carretes que presenten algún daño, con el método del numeral 8.2.4.13.

Un carrete con extremo abierto, con golpe que llegue al cable o con rótulo ilegible pasa a cuarentena y no se tiende hasta la decisión de QA/QC y del responsable eléctrico. Si el extremo estuvo expuesto a agua, el fabricante del cable define si se corta y cuánto.

#### 8.2.4.2. Almacenamiento y manejo de carretes

- Almacenar los carretes sobre terreno firme, nivelado y drenado, en posición vertical (apoyados sobre ambos flanges), calzados por ambos lados y con separación que permita el paso para inspección. Nunca se acuestan sobre un flange.
- Proteger los carretes de la radiación solar directa cuando el fabricante lo indique, y nunca dejar el cable expuesto sin sus duelas hasta el momento del tendido.
- Rodar el carrete solo en el sentido de la flecha marcada en el flange y en distancias cortas; en otros casos se traslada con montacargas o grúa.
- Izar el carrete con un eje de acero que pase por el agujero central y una barra separadora que evite que las eslingas aprieten los flanges, conforme a NES-SST-PR-003. Nunca se iza por las duelas ni se toma con las uñas del montacargas por el tambor del cable.
- No dejar caer el carrete desde la plataforma del vehículo. La descarga se hace con equipo de izaje o con rampa y control de descenso.
- Llevar un registro de existencias por carrete: longitud inicial, cortes, remanente y ubicación.

> ALTO: Un carrete de cable MT puede pesar varias toneladas. Nadie se ubica en la dirección en que el carrete podría rodar ni bajo una carga suspendida. Las cuñas se colocan antes de soltar el equipo de izaje.

#### 8.2.4.3. Preparación de la ruta

Zanja directamente enterrada:

- Verificar profundidad, ancho y trazado contra la sección tipo del plano; la profundidad de los cables no será menor que la del plano aprobado ni que la mínima de la NTC 2050 adoptada por el RETIE para la tensión del circuito.
- Fondo nivelado, sin piedras, raíces, escombros ni puntas de roca; cuando el terreno sea rocoso se sobreexcava y se repone con material seleccionado según NES-OPE-PR-002.
- Colocar la cama de arena o de material seleccionado con el espesor del plano — [____] mm — y nivelarla antes del tendido.
- Instalar rodillos a la separación necesaria para que el cable no arrastre por el fondo ni se apoye en los bordes; en los cambios de dirección, rodillos de curva con el radio mínimo de tendido.

Ductos y banco de ductos:

- Comprobar continuidad, alineación y limpieza de cada ducto pasando un mandril de diámetro cercano al interior del ducto y luego un cepillo o escobillón. Un mandril que no pasa indica ducto aplastado, desalineado o con concreto: el ducto no se libera.
- Retirar el agua y el lodo de ductos y cámaras.
- Verificar que las bocas de los ductos tengan campana o boquilla sin filos; instalar embudo o boquilla de entrada para el tiro.
- Dejar guía de tiro (cuerda o cinta) en cada ducto liberado y tapar los extremos hasta el tendido.
- Verificar la ocupación: no se excede la de diseño ni la permitida por la NTC 2050 (capítulo 9) — 53% para un conductor, 31% para dos y 40% para tres o más — y se revisa la relación de atasco (numeral 8.2.4.5).

Bandeja:

- Bandeja completa, alineada, con uniones y soportes apretados, con la continuidad equipotencial y la puesta a tierra del diseño (NES-OPE-PR-020).
- Sin rebabas, cantos vivos ni tornillería que sobresalga hacia el interior; protección de borde en los puntos de salida.
- Rodillos de bandeja instalados en los tramos rectos y poleas de curva en los cambios de dirección, con el radio mínimo de tendido.
- En bandejas a 2 m o más, trabajo conforme a la Resolución 4272 de 2021 con el coordinador de alturas.

#### 8.2.4.4. Radio mínimo de curvatura

El radio mínimo lo fija la ficha técnica del fabricante del cable y prevalece sobre cualquier valor de este documento. Como referencia, para verificar que la ficha y las poleas son coherentes:

| Tipo de cable | Radio mínimo durante el tiro | Radio mínimo en posición final | Fuente |
|---|---|---|---|
| MT unipolar apantallado, aislamiento extruido | 20 × D (valor típico de fabricante) | 15 × D (valor típico de fabricante) | Guías de instalación de fabricantes; verificar contra la ficha del cable del proyecto |
| MT tripolar apantallado | Según fabricante | 12 × D (valor típico de fabricante) | Guías de instalación de fabricantes; verificar contra la ficha |
| MT armado | Según fabricante | 15 × D (valor típico de fabricante) | Guías de instalación de fabricantes; verificar contra la ficha |
| BT 0,6/1 kV y DC de agrupamiento | Según fabricante | Según fabricante | Ficha técnica del cable |
| Cable de string (IEC 62930) | Según fabricante | Según fabricante | Ficha técnica del cable |

D es el diámetro exterior del cable. El radio de la polea o del rodillo de curva se mide hasta el eje del cable. En las bocas de ducto, en las entradas a cámaras, en las subidas a celdas y en las salidas de zanja a equipo se verifica el radio real con plantilla o cinta antes de fijar el cable.

> NOTA: La curva más severa de un tendido suele estar fuera del ducto: en la salida del carrete, en la boca de entrada y en la subida al equipo. Son los puntos que más se vigilan durante el tiro.

#### 8.2.4.5. Cálculo y control de la tensión de halado y de la presión lateral

Antes de cada tiro de MT, y de los tiros de BT largos o con varias curvas, el responsable eléctrico calcula la tensión acumulada tramo por tramo y la presión lateral en cada curva, y la registra en el formato NES-OPE-F-082. El método es el de IEEE 1185 y de las guías de instalación de los fabricantes:

1. Tramo recto horizontal: T salida = T entrada + μ × w × W × L, donde μ es el coeficiente de fricción, w el factor de corrección por peso, W el peso del cable o del conjunto de cables en N/m y L la longitud del tramo en m.
2. Curva horizontal: T salida = T entrada × e elevado a (μ × w × θ), con θ en radianes (90° = 1,571 rad). Una curva multiplica la tensión que trae: por eso se halará, cuando sea posible, desde el extremo más cercano a las curvas, de modo que las curvas queden al inicio del tiro.
3. Tramos inclinados y curvas verticales: se aplican las expresiones de IEEE 1185 que incluyen la componente del peso; en pendientes descendentes la tensión puede disminuir y el carrete requiere freno.
4. Presión lateral en cada curva: SWBP = T salida de la curva / R, con R el radio de la curva en m. Con tres cables en un ducto, el cable central o el cable inferior soporta una presión mayor; se usan los factores de disposición de IEEE 1185 o de la guía del fabricante.
5. Factor de corrección por peso, tres cables iguales en un ducto: disposición acunada w = 1 + (4/3) × [d / (D − d)]²; disposición triangular w = 1 / raíz de {1 − [d / (D − d)]²}, con d el diámetro del cable y D el diámetro interior del ducto. Para un solo cable, w = 1.
6. Relación de atasco: con tres cables, si D/d está entre 2,8 y 3,2 aproximadamente existe riesgo de atasco en curvas; se cambia el diámetro de ducto, se halan los cables triplexados o se consulta al fabricante.

Valores de referencia para el cálculo, que se reemplazan por los del fabricante del cable y del lubricante del proyecto:

| Parámetro | Valor de referencia | Fuente |
|---|---|---|
| Coeficiente de fricción con lubricante, ducto PVC o PEAD | 0,15 a 0,50 según cubierta, ducto y lubricante; usar 0,5 cuando no se tenga dato del fabricante del lubricante | Guías de fabricantes de lubricante y de cable |
| Tensión máxima con ojo de tiro sobre conductor de cobre | 50 N/mm² de sección de conductor (guías europeas); 0,008 lbf/cmil ≈ 70 N/mm² (guías norteamericanas). Se usa el menor salvo indicación escrita del fabricante del cable | Valor típico de fabricante; verificar contra la ficha del cable del proyecto |
| Tensión máxima con ojo de tiro sobre conductor de aluminio | 30 N/mm² (guías europeas); 0,006 lbf/cmil ≈ 52 N/mm² (guías norteamericanas). Se usa el menor salvo indicación escrita del fabricante | Valor típico de fabricante; verificar contra la ficha del cable del proyecto |
| Tensión máxima con manga de tiro | La que fije el fabricante del cable, siempre menor o igual que la de ojo de tiro | Ficha técnica del cable |
| Presión lateral admisible | Del orden de 7,3 kN/m (500 lbf/ft) para tres cables unipolares en un ducto, y valores mayores para un solo cable MT, según cubierta y construcción | Valor típico de fabricante e IEEE 1185; verificar contra la ficha del cable del proyecto |
| Temperatura mínima de instalación | La de la ficha técnica; para cubiertas de PVC las guías indican del orden de −10 °C | Ficha técnica; en la mayor parte de Colombia no es limitante, salvo zonas de alta montaña |

La tensión de trabajo del tiro se fija como la menor entre: la tensión máxima del método de tiro, la tensión que produce la presión lateral admisible en la curva más severa y la capacidad del malacate y del anclaje. El fusible mecánico se calibra a ese valor.

En campo:

- El operador del malacate lee el dinamómetro de forma continua; si el registro es automático, se archiva con el formato NES-OPE-F-083.
- Al alcanzar el 80% de la tensión de trabajo (criterio interno), se detiene el tiro, se revisan rodillos, lubricación y curvas, y se decide con el responsable eléctrico si se continúa.
- Si la tensión real supera la calculada en más de un 20% (criterio interno) sin causa identificada, el tiro se detiene y se investiga: rodillo bloqueado, cable fuera de la polea, ducto obstruido o cable enganchado en el carrete.
- Un tiro que superó la tensión máxima admisible o la presión lateral admisible se declara no conforme: el tramo se marca y se decide con el fabricante del cable si se acepta, se ensaya de forma adicional o se reemplaza.

> ALTO: La tensión máxima de un cable se aplica al conductor, no al aislamiento ni a la pantalla. Con manga sobre la cubierta, el límite es menor porque la cubierta se desliza y el esfuerzo se transmite por fricción a las capas internas. Nunca se hala un cable MT desde la pantalla o desde la cubierta pelada.

#### 8.2.4.6. Montaje del carrete y preparación del extremo de tiro

1. Ubicar el portabobinas alineado con la boca del ducto o el eje de la zanja, de modo que el cable salga por la parte superior del carrete y entre al ducto sin invertir su curvatura.
2. Nivelar el portabobinas, calzar las ruedas, colocar el eje y elevar el carrete con los gatos hasta que gire libre; verificar el freno.
3. Retirar las duelas de protección y revisar las vueltas exteriores; recoger los clavos y la madera.
4. Preparar el extremo de tiro:
  - Ojo de tiro: instalarlo sobre el conductor con la herramienta y el dado del fabricante del accesorio y sellarlo contra el ingreso de agua.
  - Manga: elegir la del diámetro del cable, deslizarla sobre la cubierta, fijar su extremo con cinta y abrazadera para que no se suelte, y no superar la tensión de manga del fabricante.
  - En tiros de varios cables, sujetar todos los extremos a un mismo dispositivo de tiro, con los extremos desfasados para no formar un nudo rígido de gran diámetro.
5. Instalar el destorcedor y el fusible mecánico entre la cuerda de tiro y el dispositivo.
6. Marcar en el cable, cerca del extremo, el número de circuito y la fase o polaridad.

#### 8.2.4.7. Tendido en ducto o banco de ductos

1. Pasar la cuerda de tiro por el ducto con la guía dejada en la liberación y conectarla al destorcedor.
2. Confirmar por radio que todos los puntos de control están listos: carrete, boca de entrada, cámaras intermedias y malacate.
3. Lubricar el cable a la entrada del ducto de forma continua durante todo el tiro, con el lubricante aprobado y en la cantidad que recomiende su fabricante; prelubricar el ducto en los tiros largos.
4. Iniciar el tiro de forma progresiva, sin tirones, y mantener una velocidad constante y moderada — [____] m/min según el fabricante del cable y el equipo —. Las paradas y arranques bruscos generan picos de tensión.
5. En la boca de entrada, un oficial guía el cable con la mano a través del embudo para que no roce el borde ni forme ángulo; en el carrete, otro oficial controla el giro y el freno.
6. En cada cámara intermedia, un auxiliar verifica que el cable avance sin rozar los bordes y sin formar seno; en las cámaras donde el cable cambia de dirección, se usan poleas con el radio de tendido.
7. Detener el tiro de inmediato ante: orden de cualquier punto de control, tensión cercana al límite, cable que se sale de un rodillo, daño visible de la cubierta, carrete que se traba o pérdida de comunicación.
8. Al llegar el extremo al punto final, dejar la longitud de reserva para la conexión y el empalme o terminal indicada en el plano — [____] m — más la longitud que se cortará por haber estado bajo la manga.
9. Cortar el extremo que estuvo dentro de la manga o con el ojo de tiro; esa zona no forma parte del cable definitivo.
10. Sellar de inmediato ambos extremos con capuchón (numeral 8.2.4.11).

> NOTA: Los cables de una misma terna se halan juntos en el mismo ducto. Si el diseño prevé una terna por ducto, nunca se pasa una fase sola por un ducto metálico ni por un ducto rodeado de material ferromagnético: la corriente inducida calienta el ducto.

#### 8.2.4.8. Tendido en zanja directamente enterrado

1. Instalar el portabobinas en un extremo de la zanja o, en tendidos largos, en un punto intermedio, tendiendo primero en una dirección y luego desenrollando el resto en forma de ocho sobre superficie limpia para tender en la otra dirección, sin arrastrarlo y respetando el radio mínimo.
2. Tender el cable sobre rodillos colocados en el fondo de la zanja; nunca arrastrarlo por el fondo ni por el borde.
3. En tendido manual, distribuir a los auxiliares a lo largo de la zanja a una separación tal que ninguno cargue más de 25 kg (Resolución 2400 de 1979, art. 392); el cable se toma por debajo y no se jala en ángulo.
4. Terminado el tiro, retirar los rodillos y bajar el cable a la cama de arena a mano, de forma progresiva desde un extremo, sin dejarlo caer.
5. Ubicar los cables en la posición del plano: formación en trébol o en plano, separación entre circuitos — [____] mm — y separación con otros servicios (comunicaciones, tierra) según la sección tipo. La separación entre circuitos de MT afecta su capacidad de corriente: no se modifica sin aprobación del diseñador.
6. Atar las ternas en trébol con amarres no metálicos a la distancia del plano, cuando el diseño lo indique.
7. Dejar el cable ondulado de forma suave en la zanja, sin tensión, con la holgura del plano en extremos y en puntos de empalme.
8. Tender el conductor de tierra desnudo que acompaña a los circuitos según NES-OPE-PR-020, en la posición del plano.
9. Para los cables DC de string y de agrupamiento enterrados, mantener los polos positivo y negativo identificados y en la disposición del plano; si el diseño exige ducto para los cables de string, no se entierran directamente.

> ALTO: Ningún trabajador se ubica dentro de la zanja en el tramo donde se está bajando el cable o donde opera el portabobinas. Antes de bajar a la zanja se verifica su estabilidad según NES-OPE-PR-002.

#### 8.2.4.9. Tendido en bandeja

1. Tender sobre rodillos de bandeja y poleas de curva; nunca arrastrar el cable sobre los peldaños o el fondo de la bandeja.
2. Acomodar los cables en la posición del plano: ternas en trébol o cables separados según el diseño, sin superar la ocupación de la bandeja.
3. Sujetar los cables a la bandeja con amarres o abrazaderas a la separación del plano — [____] m — en tramos horizontales y más próximos en tramos verticales; en MT, abrazaderas para esfuerzos de cortocircuito si el diseño las exige.
4. Usar amarres no metálicos resistentes a UV en bandejas a la intemperie; no se usa alambre ni amarres sin protección UV.
5. Mantener la separación entre bandejas de MT, de BT, de DC y de comunicaciones que fije el diseño.
6. En las subidas y bajadas, verificar el radio de curvatura y soportar el peso del cable vertical para que no cuelgue del terminal.

#### 8.2.4.10. Cables DC de string y de agrupamiento

- Los cables de string se tienden según NES-OPE-PR-014 en lo que respecta al tracker y a la caja combinadora; este procedimiento cubre su tramo en canalización enterrada o en bandeja.
- Los cables DC se tienden sin conexión a los strings ni a la caja combinadora. Si un extremo ya está conectado a los módulos, el cable se trata como energizado y se aplica NES-OPE-PR-014.
- Mantener los extremos con capuchón o tapón hasta su conectorización, sin contacto con el suelo ni con agua.
- Identificar cada cable en ambos extremos y en las cámaras con número de string o de circuito y polaridad, con rótulo indeleble y resistente a UV.
- Los cables de agrupamiento DC de aluminio se manejan con las mismas reglas de radio, tensión y presión lateral, con los límites de aluminio del fabricante.

#### 8.2.4.11. Sellado de extremos

- Sellar ambos extremos de cada cable MT inmediatamente después de cortarlo, con capuchón termocontráctil con adhesivo interior o capuchón de sellado del fabricante. La cinta aislante sola no es un sello.
- En BT y DC, sellar los extremos que queden en zanja, cámara o intemperie hasta su conexión.
- Revisar el sello de todos los extremos tendidos al final de cada jornada y después de lluvias; un sello roto en MT se reporta a QA/QC.
- El extremo remanente en el carrete se sella antes de devolver el carrete al acopio.

> ALTO: El agua que entra por un extremo abierto de un cable MT migra por el conductor y bajo la pantalla a lo largo de decenas de metros y produce arborescencias en el aislamiento. Un extremo MT sin sello en zanja o en cámara es una no conformidad grado 3.

#### 8.2.4.12. Recubrimiento, protección, señalización y relleno

1. Antes de tapar, QA/QC inspecciona el 100% del tramo: posición, separaciones, ausencia de daño en la cubierta, holguras, identificación y sellos; se registra en el formato NES-OPE-F-084 y, si el plan de calidad lo establece, se toma registro fotográfico georreferenciado del tramo antes de cubrir.
2. Cubrir los cables con arena o material seleccionado de la especificación, con el espesor del plano — [____] mm — sobre la generatriz superior del cable, colocado a mano y sin compactación mecánica directa sobre el cable.
3. Colocar la protección mecánica (losetas, placas o ladrillo) cuando el plano la exija.
4. Colocar la cinta de señalización a la profundidad del plano — [____] mm por encima de los cables —, centrada sobre cada circuito o sobre cada grupo de ternas, con el color y la leyenda que exija el RETIE para cables enterrados de la tensión correspondiente.
5. Rellenar y compactar por capas según NES-OPE-PR-002; la compactación mecánica se inicia solo cuando haya sobre los cables el espesor mínimo de material que fije NES-OPE-PR-002 — [____] mm —.
6. Instalar los mojones o hitos de señalización de la ruta en superficie, en cambios de dirección, cruces y a la separación del plano.
7. Actualizar el plano de registro (as-built) con la ruta real, profundidad, posición de empalmes y cruces.

#### 8.2.4.13. Identificación de cables

- Rotular cada cable en ambos extremos, en cada cámara de inspección, en las entradas y salidas de bandeja y en los empalmes, con el código de la lista de cables.
- Identificar las fases de MT (L1, L2, L3) y la polaridad DC con el código de colores o marcas del proyecto, conforme al RETIE.
- Los rótulos son indelebles, resistentes a UV y a humedad, y no se fijan con adhesivo sobre la cubierta en zonas calientes.

#### 8.2.4.14. Ensayos de recepción tras el tendido

Terminado el tendido y antes de confeccionar empalmes o terminales, se ejecutan los siguientes ensayos y se registran en el formato NES-OPE-F-085. Los ensayos de MT con alta tensión (VLF, tan delta, descargas parciales) se ejecutan con los accesorios ya confeccionados, según NES-OPE-PR-016.

Antes de cada ensayo: cable desconectado en ambos extremos, extremos separados y señalizados, personal fuera del alcance de los extremos y comunicación por radio entre ambos puntos. Al terminar, descargar el cable a tierra durante un tiempo al menos igual al de aplicación de la tensión, o el que indique el fabricante del instrumento.

| Ensayo | Cable | Método | Criterio |
|---|---|---|---|
| Continuidad y correspondencia | Todos | Continuidad de cada conductor de extremo a extremo y verificación de que el extremo identificado corresponde al mismo cable (identificación de fases y polaridad). | Continuidad y correspondencia con la lista de cables. |
| Continuidad de pantalla | MT | Continuidad de la pantalla metálica de extremo a extremo con óhmetro. | Continuidad; valor coherente con la longitud y la sección de la pantalla. |
| Resistencia de aislamiento BT AC | 0,6/1 kV | Megóhmetro a 1.000 V DC durante 1 min, entre cada conductor y los demás unidos a tierra. | IEC 60364-6: para circuitos de más de 500 V, mínimo 1 MΩ; criterio del proyecto o del fabricante si es mayor — [____] MΩ. |
| Resistencia de aislamiento DC | String y agrupamiento | Según IEC 62446-1 y NES-OPE-PR-014. | IEC 62446-1: para tensión de sistema superior a 500 V, ensayo a 1.000 V y mínimo 1 MΩ, o lo que fije la edición vigente y el proyecto. |
| Resistencia de aislamiento MT | MT | Megóhmetro a 5.000 V DC durante 1 min (o la tensión que fije el fabricante o la especificación), entre conductor y pantalla puesta a tierra; registrar también 10 min si se calcula índice de polarización. | El que fije el fabricante del cable o la especificación — [____] MΩ —; valores de las tres fases coherentes entre sí y con los de carretes similares. |
| Ensayo de cubierta | MT con cubierta extruida | Tensión DC entre la pantalla metálica y tierra (o el electrodo exterior), de 4 kV por mm de espesor especificado de cubierta, con un máximo de 10 kV, durante 1 min (IEC 60229). | Sin perforación durante el minuto de ensayo. |

> NOTA: El ensayo de cubierta solo es representativo si el cable está enterrado o en contacto con un medio conductor en toda su longitud; en bandeja o en ducto seco, la cubierta no está rodeada de un electrodo. El método se acuerda con el fabricante y con [CLIENTE]. Una perforación de cubierta se localiza y repara con el kit del fabricante antes de cubrir.

> ALTO: Durante cualquier ensayo con megóhmetro o con fuente DC, el extremo remoto es un punto con tensión peligrosa. Se custodia con una persona y señalización, y el cable se descarga a tierra antes de que nadie lo toque. Un cable MT largo acumula carga suficiente para producir un choque grave.

#### 8.2.4.15. Cruces, paralelismos y trabajos cerca de redes existentes

- Antes de excavar o de tender cerca de redes existentes, confirmar su ubicación con planos, detector de redes y apiques manuales según NES-OPE-PR-002.
- Cruces con vías internas: en ducto protegido o banco de ductos según el plano; nunca cable directamente enterrado bajo vía sin protección.
- Paralelismos y cruces con circuitos energizados, con comunicaciones o con tuberías: respetar las separaciones del plano y del RETIE; si un circuito existente está energizado en la zona de trabajo, aplicar NES-SST-PR-001 y las distancias de seguridad del RETIE.
- Cruces con cuerpos de agua o drenajes: solo según el diseño aprobado y el permiso ambiental correspondiente.

#### 8.2.4.16. No conformidades

- Daño de cubierta visible durante el tendido: se detiene el tiro, se marca la zona y se decide con el responsable eléctrico la reparación con kit del fabricante o el corte y empalme. En MT, un daño que llegue a la pantalla o al aislamiento obliga a cortar o a empalmar.
- Tensión o presión lateral superior a la admisible: tramo no conforme hasta decisión documentada con el fabricante del cable.
- Radio de curvatura inferior al mínimo: se corrige; si el cable fue doblado bajo tensión por debajo del radio de tendido, se evalúa como daño.
- Extremo MT sin sello o con agua: cuarentena y consulta al fabricante del cable.
- Resultado de ensayo fuera de criterio: el circuito no se libera; se localiza la falla, se repara y se repite el ensayo.
- Cambio de ruta, de sección o de referencia de cable: requiere aprobación escrita del diseñador eléctrico y queda en el registro de RFI.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Carrete recibido | Rótulo legible y coincidente con la lista de cables; extremos sellados; sin daño que llegue al cable; protocolo de fábrica y certificado de producto | RETIE / Este procedimiento |
| Ductos | Mandril pasa en toda la longitud; ducto limpio, seco y con guía | Este procedimiento |
| Ocupación de ductos | No mayor que la del diseño ni que la de la NTC 2050, capítulo 9 (53% / 31% / 40%) | NTC 2050 |
| Relación de atasco (tres cables) | Fuera del intervalo aproximado de 2,8 a 3,2, o medida correctiva aprobada | IEEE 1185 / Guías de fabricante |
| Tensión de halado | Menor o igual que la tensión de trabajo calculada; nunca mayor que la máxima del fabricante para el método de tiro | Ficha del cable / IEEE 1185 |
| Presión lateral | Menor o igual que la admisible del fabricante en cada curva | Ficha del cable / IEEE 1185 |
| Radio de curvatura | No menor que el mínimo del fabricante durante el tiro y en la posición final | Ficha del cable / IEC 60502 |
| Zona de manga u ojo de tiro | Cortada y descartada | Este procedimiento |
| Extremos | Sellados con capuchón en MT desde el corte hasta la confección del accesorio | Este procedimiento |
| Profundidad y posición | Según sección tipo del plano y no menor que la mínima de la NTC 2050 adoptada por el RETIE | Plano / NTC 2050 / RETIE |
| Cama, recubrimiento y cinta | Espesores y altura de cinta del plano; cinta continua sobre cada circuito | Plano / RETIE |
| Identificación | Rótulo en ambos extremos, cámaras y empalmes; fases y polaridad identificadas | RETIE / Este procedimiento |
| Aislamiento BT AC | Mínimo 1 MΩ a 1.000 V DC o el valor mayor del proyecto | IEC 60364-6 |
| Aislamiento DC | Según tabla de IEC 62446-1 vigente | IEC 62446-1 |
| Aislamiento MT | Valor del fabricante o de la especificación; fases coherentes entre sí | Fabricante / Especificación |
| Cubierta MT | Sin perforación a 4 kV/mm de espesor (máx. 10 kV DC) durante 1 min | IEC 60229 |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-080 a NES-OPE-F-085 de este procedimiento.
- Plan de tendido aprobado y cálculos de tensión y presión lateral.
- Registros del dinamómetro o del malacate, cuando sean automáticos.
- Protocolos de fábrica, certificados de conformidad de producto y fichas técnicas por carrete.
- Certificados de calibración de dinamómetro, megóhmetro, fuente DC y demás instrumentos.
- Registro fotográfico de los tramos antes de tapar y plano de registro (as-built) de rutas.

## 8.5. Control de calidad

QA/QC verifica el 100% de los carretes en su recepción, el 100% de los tramos antes de tapar y el 100% de los circuitos mediante los ensayos del numeral 8.2.4.14 antes de su liberación para la confección de accesorios. Asiste como punto de espera (H) a todos los tiros de MT y como punto de testigo (W) a los tiros de BT y DC. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación que no afecta calidad, prestación ni seguridad, por ejemplo rótulo incompleto o registro tardío. | Registro y cierre. |
| 2 | Requiere corregir con el método de este procedimiento: posición en zanja, sujeción en bandeja, reparación de cubierta BT con kit del fabricante, sello de extremo BT. | Corrección por la cuadrilla y reinspección. |
| 3 | Afecta la vida útil o la seguridad del circuito: exceso de tensión o de presión lateral, radio por debajo del mínimo bajo tensión, daño de pantalla o aislamiento MT, extremo MT con agua, ensayo fuera de criterio. | Suspensión del circuito, consulta al fabricante del cable y al diseñador, y aprobación escrita antes de actuar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS/ART y la charla diaria, verifica que las zanjas, cámaras y zonas de tiro estén señalizadas y demarcadas y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre características del proyecto, riesgos de atrapamiento y de rotura del cable de tiro, manejo de cargas, trabajo en zanja, riesgo eléctrico en los ensayos, puntos de encuentro y uso correcto del EPP.

## 9.1. Reglas de oro

- **SIEMPRE** me ubicaré fuera de la línea del cable de tiro y nunca dentro del seno de un cable o cuerda en tensión.
- **NUNCA** pondré las manos entre el cable y un rodillo, una polea, el carrete o la boca del ducto mientras el cable esté en movimiento.
- **SIEMPRE** detendré el tiro ante cualquier duda y daré la orden por radio de forma clara.
- **NUNCA** me ubicaré en la dirección en que puede rodar un carrete ni bajo una carga suspendida.
- **SIEMPRE** verificaré la estabilidad de la zanja antes de entrar y usaré la escalera o rampa prevista.
- **NUNCA** cargaré más de 25 kg de cable por persona (Res. 2400 de 1979, art. 392).
- **SIEMPRE** trataré el extremo remoto de un cable en ensayo como energizado y lo descargaré a tierra antes de tocarlo.
- **SIEMPRE** aplicaré las cinco reglas de oro y el bloqueo y etiquetado de NES-SST-PR-001 cuando trabaje cerca de un circuito energizado.
- **SIEMPRE** suspenderé la actividad ante tormenta eléctrica y me dirigiré al refugio o punto de encuentro.
- **SIEMPRE** ejecutaré el trabajo con ATS/ART y permiso de trabajo diligenciados.

## 9.2. Riesgos específicos del tendido

- Rotura del cable de tiro o de la manga: la energía almacenada provoca un latigazo. Se usan cables de tiro de baja elongación, fusible mecánico calibrado y zona de exclusión alrededor del malacate y de la línea de tiro.
- Atrapamiento: en el carrete, en los rodillos, en las poleas y en la boca del ducto. Ropa ajustada, sin guantes sueltos cerca de partes en giro y guardas en el malacate.
- Sobreesfuerzo: el cable MT pesa varios kilogramos por metro; los auxiliares se distribuyen para no superar 25 kg por persona y se usan rodillos en lugar de cargar el cable.
- Trabajo en zanja: derrumbe, caída al mismo y a distinto nivel; se aplica NES-OPE-PR-002.
- Espacio confinado: cámaras de inspección que cumplan la definición de la Resolución 0491 de 2020; medición de atmósfera y permiso específico.
- Riesgo eléctrico: ensayos de aislamiento y de cubierta, y cercanía de circuitos existentes energizados; distancias de seguridad del RETIE y EPP con categoría de arco cuando aplique.

## 9.3. Condiciones climáticas de [departamento]

- Tormenta eléctrica: ante el aviso o el primer trueno, detener el tiro, asegurar el carrete con freno y cuñas, salir de la zanja, alejarse de cables, bandejas y estructuras metálicas y dirigirse al refugio. Se reanuda solo con autorización del responsable SST.
- Lluvias intensas: suspender el tendido en zanja si hay acumulación de agua o inestabilidad de taludes; sellar extremos y cubrir carretes y cámaras abiertas.
- Calor y radiación: hidratación, sombra, pausas y rotación; el cable y el carrete expuestos al sol se manipulan con guante. La cubierta de algunos cables se ablanda con temperatura alta y es más sensible a la abrasión: se intensifica la lubricación y la vigilancia.
- Fauna: revisar zanjas, cámaras y carretes antes de intervenir; presencia de ofidios en zanjas y bajo duelas; polainas y reporte al área ambiental.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado al frente | Colisión, volcamiento, caídas al mismo nivel. | Conductores autorizados; vías y velocidades del proyecto; PESV. |
| 2. Recepción y descarga de carretes | Caída o rodadura del carrete, aplastamiento, golpe por carga suspendida. | Izaje con eje y barra separadora según NES-SST-PR-003; señalero; cuñas; nadie en la dirección de rodadura. |
| 3. Montaje del carrete en portabobinas | Atrapamiento, volcamiento del portabobinas, caída del eje. | Terreno nivelado; calzas; gatos inspeccionados; dos personas; freno verificado. |
| 4. Preparación de ductos y zanja | Derrumbe, caída a la zanja, espacio confinado en cámaras. | NES-OPE-PR-002; entibado o taludes; escaleras; permiso de espacio confinado cuando aplique; medición de atmósfera. |
| 5. Instalación de rodillos y poleas | Golpes, cortes, sobreesfuerzo. | Guantes; manipulación entre dos personas; inspección de rodillos. |
| 6. Tiro con malacate | Latigazo por rotura de cuerda o manga, atrapamiento en carrete y rodillos, ruido. | Fusible mecánico; zona de exclusión; radio en cada punto; dinamómetro; protección auditiva; guardas. |
| 7. Tendido manual en zanja | Sobreesfuerzo, caída en la zanja, atrapamiento de manos. | Máximo 25 kg por persona (Res. 2400 de 1979, art. 392); rodillos; tomar el cable por debajo; no caminar por el borde inestable. |
| 8. Tendido en bandeja elevada | Caída a distinto nivel, caída de objetos. | Res. 4272 de 2021; coordinador de alturas; andamio o plataforma certificada; zona inferior demarcada. |
| 9. Corte y sellado de extremos | Cortes, quemaduras con pistola de calor o soplete. | Cortacables de trinquete; guantes; pistola de calor preferida sobre soplete; permiso de trabajo en caliente si se usa llama. |
| 10. Recubrimiento y relleno | Atrapamiento por maquinaria, golpes, daño al cable. | Señalero; nadie en la zanja durante el vertido; compactación mecánica solo sobre el espesor mínimo. |
| 11. Ensayos de aislamiento y de cubierta | Choque eléctrico, descarga de cable cargado. | Extremos custodiados y señalizados; radio; descarga a tierra; guantes dieléctricos; instrumento calibrado; personal calificado. |
| 12. Trabajo cerca de redes existentes | Contacto eléctrico, daño a redes. | Planos y detector de redes; apiques manuales; NES-SST-PR-001; distancias de seguridad del RETIE. |
| 13. Exposición ambiental | Radiación UV, estrés térmico, ofidios, tormenta eléctrica. | Ropa manga larga, cubrenuca, protector solar, hidratación, pausas; polainas; protocolo de tormenta. |
| 14. Orden, aseo y residuos | Tropiezos, cortes con clavos y duelas, contaminación del suelo. | Retiro diario de duelas y clavos; retazos en recipiente; separación de residuos. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Aire | Emisiones, material particulado y ruido | Vehículos, malacate y grúa con mantenimiento al día; motores apagados en reposo; humectación de vías en época seca. |
| Suelo | Residuos sólidos | Separación en la fuente con el código de colores de la Res. 2184 de 2019; duelas, carretes de madera, cartón y plásticos a su corriente de aprovechamiento; carretes retornables devueltos al fabricante cuando el contrato lo prevea. |
| Suelo | Retazos de cable | Recogidos el mismo día, pesados y almacenados bajo llave como aprovechables; entrega a gestor autorizado con acta y certificado. |
| Suelo | Lubricante y solventes | Uso de la cantidad necesaria; envases y trapos contaminados como RESPEL según Decreto 1076 de 2015; hoja de seguridad en el frente (Decreto 1496 de 2018). |
| Suelo | Derrames de hidrocarburos | Kit antiderrame en cada frente; bandeja bajo malacate y generadores; tanqueo solo en zonas autorizadas. |
| Suelo | RCD y material sobrante de excavación | Gestión según Res. 0472 de 2017 modificada por Res. 1257 de 2021 y NES-OPE-PR-002. |
| Flora y fauna | Intervención de hábitat y atrapamiento de fauna en zanjas | Trabajar en áreas liberadas; revisar zanjas al inicio de la jornada y retirar fauna atrapada según PMA; rampas de escape en zanjas largas abiertas; prohibido cazar o alimentar fauna. |
| Agua | Escorrentía y sedimentos | Control de sedimentos en zanjas abiertas en temporada de lluvias; prohibido intervenir cuerpos de agua sin permiso. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener el tiro por radio, frenar el carrete y el malacate y asegurar la zona.
2. Notificar al responsable SST y al residente de obra de Neptuno Energy Services y al interlocutor de [CLIENTE].
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, extintor en cada frente).
4. Incidente grave: activar ambulancia por la línea 123 y traslado al centro asistencial definido; notificar a la ARL.
5. Reportar el evento y realizar la investigación según Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Atrapamiento en carrete, rodillo o malacate

- Ordenar la parada inmediata del malacate y frenar el carrete; no invertir el giro sin evaluar si eso agrava la lesión.
- Liberar la tensión del cable de forma controlada antes de intentar liberar a la víctima.
- No retirar a la víctima atrapada si hay sospecha de lesión grave sin el apoyo de personal de emergencias.

## 12.2. Derrumbe de zanja

- Sacar al personal de la zanja y alejar equipos y cargas del borde.
- No ingresar a rescatar sin evaluar la estabilidad; seguir el plan de rescate de NES-OPE-PR-002 y NES-SST-PLN-001.

## 12.3. Choque eléctrico durante ensayos

- No tocar a la víctima mientras siga en contacto con el cable; cortar la fuente de ensayo y descargar el cable con la pértiga de descarga.
- Activar la emergencia y aplicar reanimación si el personal está capacitado. Toda persona que sufra un choque eléctrico se remite a valoración médica aunque se sienta bien.

## 12.4. Mordedura de ofidio

- Mantener a la víctima en reposo, retirar anillos y elementos que compriman, no hacer torniquete ni succionar la herida; trasladar de inmediato al centro asistencial con capacidad de aplicar suero antiofídico; si es posible y seguro, registrar una fotografía del animal sin acercarse.

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
| Recepción e inspección de carretes de cable | NES-OPE-F-080 | QA/QC |
| Liberación de zanja, ducto o bandeja previa al tendido | NES-OPE-F-081 | QA/QC |
| Cálculo de tensión de halado y presión lateral | NES-OPE-F-082 | Responsable eléctrico |
| Registro de tendido por circuito | NES-OPE-F-083 | Supervisor de tendido |
| Inspección antes de tapar zanja y señalización | NES-OPE-F-084 | QA/QC |
| Ensayos de recepción tras el tendido | NES-OPE-F-085 | Responsable eléctrico |
| ATS/ART y permisos de trabajo | Según SG-SST | Supervisor / Responsable SST |
| Permisos de izaje | NES-SST-PR-003 | Responsable SST |
| Certificados de calibración y de producto | Según NES-CAL-PLN-002 | QA/QC |

\pagebreak

# 14. ANEXOS

## NES-OPE-F-080 — Recepción e inspección de carretes de cable

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Remisión / orden de compra: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-015 | Lugar de acopio: [__________] |

| Carrete N.º | Referencia y sección | Tensión asignada | Longitud (m) | Lote | Extremos sellados | Estado / decisión |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Rótulo legible y coincidente con orden de compra y lista de cables |  |  |  |
| 2 | Duelas y flanges íntegros, sin clavos hacia el cable |  |  |  |
| 3 | Cable sin aplastamiento, corte ni abrasión en vueltas exteriores |  |  |  |
| 4 | Ambos extremos con capuchón de sellado íntegro |  |  |  |
| 5 | Protocolo de ensayo de fábrica del carrete recibido |  |  |  |
| 6 | Certificado de conformidad de producto (RETIE) recibido |  |  |  |
| 7 | Descarga con equipo de izaje, sin caída del carrete |  |  |  |
| 8 | Almacenado vertical, calzado, sobre terreno firme y drenado |  |  |  |
| 9 | Resistencia de aislamiento de recepción (MT o carrete con daño): [____] MΩ a [____] V |  |  |  |

{.plain}
| Observaciones y carretes en cuarentena: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-081 — Liberación de zanja, ducto o bandeja previa al tendido

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Tramo (desde / hasta): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-015 / NES-OPE-PR-002 | Plano: [__________] |

{.plain}
| Tipo de canalización: zanja / ducto / banco de ductos / bandeja | Circuitos previstos: [__________] |
|---|---|
| Longitud del tramo: [____] m | Profundidad medida: [____] m (plano: [____] m) |

| Ítem | Verificación | Cumple | No cumple | N/A |
|---|---|---|---|---|
| 1 | Zanja con permiso de excavación vigente y taludes o entibado conformes |  |  |  |
| 2 | Profundidad y ancho según sección tipo del plano |  |  |  |
| 3 | Fondo nivelado, sin piedras, raíces ni escombros; sin agua estancada |  |  |  |
| 4 | Cama de arena colocada y nivelada, espesor [____] mm |  |  |  |
| 5 | Ductos: mandril pasado en toda la longitud |  |  |  |
| 6 | Ductos limpios, secos, con boquilla sin filos y guía de tiro |  |  |  |
| 7 | Ocupación de ducto y relación de atasco verificadas |  |  |  |
| 8 | Cámaras limpias, sin agua, con acceso seguro |  |  |  |
| 9 | Bandeja completa, sin rebabas, aterrizada según NES-OPE-PR-020 |  |  |  |
| 10 | Rodillos y poleas de curva instalados con el radio de tendido |  |  |  |
| 11 | Cruces y paralelismos con otras redes identificados y protegidos |  |  |  |

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-082 — Cálculo de tensión de halado y presión lateral

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito / tiro: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-015 / IEEE 1185 | Plano de ruta: [__________] |

{.plain}
| Cable (referencia, sección, material): [__________] | N.º de cables por ducto: [____] |
|---|---|
| Diámetro exterior d: [____] mm | Diámetro interior de ducto D: [____] mm |
| Peso por metro W: [____] N/m | Relación de atasco D/d: [____] |
| Coeficiente de fricción μ: [____] | Factor de corrección w: [____] |
| Método de tiro: ojo sobre conductor / manga | Tensión máxima del método: [____] kN |
| Presión lateral admisible: [____] kN/m | Radio mínimo durante el tiro: [____] mm |

| Tramo | Tipo (recto / curva / pendiente) | Longitud (m) o ángulo (°) | Radio de curva (m) | T entrada (kN) | T salida (kN) | SWBP (kN/m) |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |

{.plain}
| Tensión de trabajo fijada: [____] kN | Fusible mecánico calibrado a: [____] kN |
|---|---|
| Dirección de tiro elegida: [__________] | Tensión calculada en sentido inverso: [____] kN |

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-083 — Registro de tendido por circuito

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito (código de lista de cables): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-015 | Cálculo NES-OPE-F-082 N.º: [____] |

{.plain}
| Origen: [__________] | Destino: [__________] |
|---|---|
| Carrete N.º: [____] | Longitud cortada: [____] m (diseño: [____] m) |
| Marca métrica inicial: [____] | Marca métrica final: [____] |
| Hora de inicio: [____] | Hora de fin: [____] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Puntos de control con radio y personal asignado |  |  |  |
| 2 | Destorcedor y fusible mecánico instalados |  |  |  |
| 3 | Lubricación continua en la boca de entrada |  |  |  |
| 4 | Tensión máxima registrada: [____] kN (trabajo: [____] kN) |  |  |  |
| 5 | Velocidad constante, sin tirones |  |  |  |
| 6 | Radio de curvatura respetado en salida de carrete, bocas y curvas |  |  |  |
| 7 | Sin daño visible de cubierta durante el tiro |  |  |  |
| 8 | Zona de manga u ojo de tiro cortada y descartada |  |  |  |
| 9 | Longitud de reserva dejada en extremos: [____] m |  |  |  |
| 10 | Extremos sellados con capuchón inmediatamente |  |  |  |
| 11 | Cables identificados con circuito y fase o polaridad |  |  |  |
| 12 | Posición final y sujeción según plano (zanja o bandeja) |  |  |  |

{.plain}
| Observaciones (paradas, incidencias, registro del dinamómetro adjunto): |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-084 — Inspección antes de tapar zanja y señalización

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Tramo (desde / hasta): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-015 / NES-OPE-PR-002 | Plano: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Cables en la posición y formación del plano (trébol / plano) |  |  |  |
| 2 | Separación entre circuitos según plano: [____] mm |  |  |  |
| 3 | Separación con comunicaciones y otros servicios según plano |  |  |  |
| 4 | Conductor de tierra en la posición del plano (NES-OPE-PR-020) |  |  |  |
| 5 | Cubierta sin daño en todo el tramo |  |  |  |
| 6 | Holgura en extremos y empalmes; cable sin tensión |  |  |  |
| 7 | Identificación en extremos, cámaras y empalmes |  |  |  |
| 8 | Extremos sellados |  |  |  |
| 9 | Registro fotográfico georreferenciado tomado |  |  |  |
| 10 | Recubrimiento de arena colocado a mano, espesor [____] mm |  |  |  |
| 11 | Protección mecánica colocada (si el plano la exige) |  |  |  |
| 12 | Cinta de señalización continua a [____] mm sobre los cables |  |  |  |
| 13 | Compactación mecánica solo sobre el espesor mínimo de NES-OPE-PR-002 |  |  |  |
| 14 | Hitos de señalización instalados y ruta actualizada en as-built |  |  |  |

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-085 — Ensayos de recepción tras el tendido

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-015 / IEC 60229 / IEC 60364-6 | Temperatura ambiente / HR: [____] °C / [____] % |
| Instrumentos (serie / calibración): [__________] | Longitud del circuito: [____] m |

| Fase / polo | Continuidad conductor | Continuidad pantalla | Tensión de ensayo aislamiento (V) | Aislamiento 1 min (MΩ) | Ensayo de cubierta (kV / 1 min) | Cumple |
|---|---|---|---|---|---|---|
| L1 / + |  |  |  |  |  |  |
| L2 / − |  |  |  |  |  |  |
| L3 |  |  |  |  |  |  |

{.plain}
| Correspondencia de fases o polaridad verificada: Sí / No | Espesor especificado de cubierta: [____] mm |
|---|---|
| Criterio de aislamiento aplicado: [____] MΩ | Descarga a tierra del cable al terminar: Sí / No |

{.plain}
| Observaciones y circuitos no liberados: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

# 15. CONTROL DE CAMBIOS

| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
