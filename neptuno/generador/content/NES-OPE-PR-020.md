---
code: NES-OPE-PR-020
header_title: PUESTA A TIERRA Y PROTECCIÓN CONTRA RAYOS
cover_title: Procedimiento de Instalación de Puesta a Tierra y Protección contra Rayos
cover_subtitle: Malla de puesta a tierra, equipotencialización, sistema integral de protección contra rayos y mediciones en plantas fotovoltaicas
---

# 1. OBJETIVO

Definir el método de trabajo, los controles de calidad y las medidas preventivas para la instalación del sistema de puesta a tierra (SPT) y del sistema integral de protección contra rayos de la planta FV [PROYECTO]: medición de resistividad del terreno, malla de puesta a tierra de la planta y de los centros de transformación, electrodos, uniones, equipotencialización de estructuras y equipos, protección externa e interna contra rayos y mediciones de resistencia de puesta a tierra y de tensiones de paso y contacto, conforme al RETIE, a la NTC 2050, a la NTC 4552 (IEC 62305), a la IEEE 80 y a la IEEE 81.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, en especial los asociados a la soldadura exotérmica, a las excavaciones y a las tensiones transferidas durante las mediciones.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en:

- Medición de resistividad del terreno por el método de Wenner para el diseño o la verificación del diseño del SPT.
- Tendido de conductores de cobre desnudo o de acero (galvanizado o recubierto de cobre) de la malla general, de los anillos de centros de transformación, de los edificios y de las cercas.
- Instalación de electrodos de puesta a tierra (varillas) y cajas de inspección.
- Uniones por soldadura exotérmica y por conectores de compresión irreversibles; conexiones mecánicas accesibles.
- Equipotencialización de trackers, hincas, módulos, bandejas, cajas combinadoras, inversores, centros de transformación, cercas, puertas, postes y estructuras metálicas.
- Instalación del sistema de protección externa contra rayos (captadores, bajantes, puesta a tierra de bajantes) y del sistema interno (equipotencialización y dispositivos de protección contra sobretensiones, DPS).
- Mediciones de continuidad, resistencia de puesta a tierra por caída de potencial y tensiones de paso y contacto, y preparación de la documentación para el dictamen RETIE.

No incluye la excavación y el relleno de zanjas, que se rigen por NES-OPE-PR-002; el almacenamiento y la preservación de conductores, varillas, moldes y cargas de soldadura, que se rigen por NES-OPE-PR-011; las cimentaciones, que se rigen por NES-OPE-PR-012; ni la equipotencialización interna del tracker, que se rige por NES-OPE-PR-008. Este procedimiento se aplica en conjunto con NES-SST-PR-004 para la soldadura exotérmica.

> NOTA: El diseño del SPT y del sistema de protección contra rayos (memoria de cálculo, evaluación de riesgo, planos) es responsabilidad del diseñador del proyecto. Neptuno Energy Services lo construye y lo verifica; cualquier cambio de material, sección, profundidad, número de electrodos o trazado requiere aprobación escrita del diseñador.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / ART y PT | Análisis de trabajo seguro / análisis de riesgo del trabajo y permiso de trabajo. |
| SPT | Sistema de puesta a tierra: conjunto de electrodos, conductores enterrados, uniones y conductores de puesta a tierra que conectan las masas y el sistema eléctrico con el terreno. |
| Malla de puesta a tierra | Retícula de conductores desnudos enterrados, unidos entre sí y con electrodos, que controla las tensiones de paso y contacto en un área. |
| Electrodo de puesta a tierra | Elemento conductor en contacto directo con el terreno (varilla, conductor enterrado, placa, tubo) que dispersa la corriente. |
| Conductor de puesta a tierra | Conductor que une la masa, el barraje o el neutro con el electrodo o la malla. |
| Equipotencialización | Unión eléctrica de partes conductoras para llevarlas al mismo potencial. |
| Barraje equipotencial | Barra de cobre en un edificio, centro de transformación o tablero donde convergen los conductores de puesta a tierra y de equipotencialización. |
| Resistividad del terreno (ρ) | Resistencia específica del suelo, en Ω·m. Varía con la humedad, la temperatura, la composición y la profundidad. |
| Método de Wenner | Medición de resistividad con cuatro electrodos alineados y equidistantes; los exteriores inyectan corriente y los interiores miden tensión. |
| Telurómetro | Instrumento de medida de resistencia de puesta a tierra y de resistividad, de tres o cuatro terminales, que inyecta corriente a frecuencia distinta de la de red. |
| Resistencia de puesta a tierra | Resistencia entre el SPT y un punto de tierra remota, en Ω. |
| Método de caída de potencial | Medición de resistencia de puesta a tierra con un electrodo de corriente remoto y un electrodo de potencial que se desplaza entre el SPT y el electrodo de corriente (IEEE 81). |
| Elevación de potencial de tierra (GPR) | Tensión máxima que alcanza el SPT respecto de tierra remota durante una falla. |
| Tensión de paso | Diferencia de potencial entre los pies de una persona separados 1 m, sin contacto con otra parte conductora, durante una falla. |
| Tensión de contacto | Diferencia de potencial entre una estructura conectada a tierra y los pies de una persona a 1 m de ella que la toca con la mano, durante una falla. |
| Tensión transferida | Tensión trasladada fuera del área del SPT por conductores, cercas, tuberías o rieles. |
| Capa superficial | Capa de grava o material de alta resistividad sobre el terreno que reduce la corriente por el cuerpo humano. |
| Soldadura exotérmica | Unión molecular de conductores por la reacción de un polvo metálico (aluminotermia) dentro de un molde de grafito. |
| Conector de compresión irreversible | Conector que se deforma permanentemente con herramienta hidráulica y dado específicos, calificado para uso enterrado. |
| Sistema integral de protección contra rayos | Conjunto de protección externa (captación, bajantes, puesta a tierra) y protección interna (equipotencialización y DPS) según NTC 4552. |
| Nivel de protección contra rayos (NPR) | Categoría (I a IV) que define la eficiencia del sistema de protección y los parámetros de diseño. |
| Esfera rodante | Método de diseño de captación que considera protegidos los puntos que no toca una esfera de radio definido por el NPR. |
| DPS | Dispositivo de protección contra sobretensiones transitorias. Tipo 1 (corriente de rayo), tipo 2 (sobretensiones inducidas) y tipo 3 (protección fina), en BT AC y en DC fotovoltaico. |
| Descargador de sobretensión MT | DPS de óxido metálico para media tensión, instalado en celdas, transiciones o equipos. |
| Densidad de descargas a tierra (DDT) | Número de rayos a tierra por kilómetro cuadrado y por año en la zona. |
| Caja de inspección | Caja con tapa que deja accesible una unión o un electrodo para inspección y medición. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. La malla general, los anillos de centros de transformación, la subestación, los edificios y las cercas se identifican según el plano del sistema de puesta a tierra [N° de plano], el plano de protección contra rayos [N° de plano] y el plano general de implantación [N° de plano].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados. Secciones de conductor, profundidades, longitudes de electrodo, valores objetivo de resistencia y de tensiones de paso y contacto son los del diseño aprobado y del RETIE vigente.

## 5.1. Documentales

- Memoria de cálculo del SPT (IEEE 80) con el estudio de resistividad, la corriente de falla de diseño, la resistencia esperada y las tensiones tolerables de paso y contacto — [N° de documento].
- Evaluación del riesgo por rayo (NTC 4552-2) y diseño del sistema de protección contra rayos (NTC 4552-3 y NTC 4552-4) — [N° de documento].
- Planos de puesta a tierra, de protección contra rayos, de detalles de uniones y de cajas de inspección — [N° de plano].
- Instrucciones del fabricante de la soldadura exotérmica (moldes, cargas, combinaciones) y del fabricante de los conectores de compresión (herramienta, dados, número de compresiones).
- Instrucciones de puesta a tierra del fabricante del inversor, del transformador, de las celdas, del módulo y del tracker.
- Certificados de conformidad de producto de conductores, electrodos, conectores, DPS y elementos de captación exigidos por el RETIE.
- NES-OPE-PR-002 Excavación de zanjas; NES-OPE-PR-008 Montaje de tracker; NES-OPE-PR-011 Preservación de materiales de puesta a tierra; NES-OPE-PR-012 Obras civiles y cimentaciones; NES-OPE-PR-018 Inversores; NES-OPE-PR-019 Centros de transformación; NES-OPE-PR-023 Energización.
- NES-CAL-PLN-002 Plan de calidad; NES-SST-PLN-001 Plan de emergencias; NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-SST-PR-004 Trabajos en caliente.

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes: requisitos del sistema de puesta a tierra, valores de referencia de resistencia de puesta a tierra, tensiones de contacto, materiales, protección contra rayos, certificación de producto y dictamen de inspección.
- NTC 2050 — Código Eléctrico Colombiano, sección 250 (puesta a tierra y equipotencialización) y sección 690 (sistemas solares fotovoltaicos), en los requisitos que el RETIE adopta.
- NTC 4552 (partes 1 a 4) — Protección contra descargas eléctricas atmosféricas (rayos), basada en la IEC 62305.
- IEC 62305 (partes 1 a 4) — Protección contra el rayo, como referencia técnica.
- IEEE 80 — Guía de seguridad en puesta a tierra de subestaciones de corriente alterna.
- IEEE 81 — Guía para la medición de resistividad del terreno, impedancia de puesta a tierra y potenciales de superficie.
- IEEE 837 — Calificación de conexiones permanentes usadas en puesta a tierra de subestaciones.
- IEC 62561 (serie) — Componentes del sistema de protección contra el rayo (conectores, conductores, electrodos), como referencia técnica.
- IEC 61643-11 e IEC 61643-31 — DPS para baja tensión AC y para instalaciones fotovoltaicas DC; IEC 60364-7-712 e IEC 62548 para el lado DC fotovoltaico.
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019 — Estándares mínimos.
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en el sector eléctrico; cinco reglas de oro.
- Resolución 2400 de 1979 — Estatuto de seguridad industrial; arts. 388 a 392 (manejo manual de cargas).
- Resolución 4272 de 2021 — Trabajo en alturas, para captadores y bajantes en edificios y postes a 2 m o más.
- Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo.
- Decreto 1496 de 2018 — SGA, para cargas de soldadura exotérmica y compuestos de mejoramiento del suelo.
- Decreto 1076 de 2015 (RESPEL); Resolución 2184 de 2019 (código de colores); Resolución 0472 de 2017 modificada por la Resolución 1257 de 2021 (RCD).
- Licencia ambiental y Plan de Manejo Ambiental (PMA) del proyecto — [N° de resolución].
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

- Aprobar y divulgar el presente procedimiento y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.
- Asegurar que el SPT se instale antes de que las zanjas se rellenen y antes de que los equipos se energicen, coordinando la secuencia con obras civiles, hincado y tendido de cables.
- Tramitar ante [CLIENTE] y el diseñador los RFI derivados de resistividades distintas a las de diseño, interferencias o cambios de material.
- Detener cualquier actividad que no cumpla este procedimiento, el diseño o la instrucción del fabricante.

## 6.2. Responsable eléctrico (ingeniero electricista con matrícula COPNIA vigente)

- Verificar que el diseño, los planos y los materiales estén aprobados antes de iniciar.
- Dirigir o ejecutar las mediciones de resistividad, de resistencia de puesta a tierra y de tensiones de paso y contacto, analizar los resultados frente al diseño y al RETIE y firmar los protocolos.
- Firmar la declaración de cumplimiento del constructor y preparar el expediente para el dictamen RETIE.

## 6.3. Supervisor de puesta a tierra

- Asignar tareas, dirigir la cuadrilla y verificar el cumplimiento del método descrito.
- Elaborar con los trabajadores el ATS/ART diario y la charla de inicio de turno.
- Verificar moldes, cargas, herramientas de compresión, dados e instrumentos antes de cada jornada, y diligenciar los registros del frente el mismo día.

## 6.4. Soldador de exotérmica y técnicos electricistas (matrícula CONTE vigente)

- Ejecutar uniones exotérmicas y de compresión según este procedimiento y la instrucción del fabricante, con entrenamiento certificado del fabricante del sistema de soldadura o equivalente.
- Rechazar y rehacer toda unión que no cumpla la inspección visual.

## 6.5. Responsable de calidad (QA/QC)

- Controlar el cumplimiento del PIE de NES-CAL-PLN-002 y liberar cada tramo de malla antes del relleno (punto de retención).
- Verificar la trazabilidad de lotes de conductor, varillas, cargas y conectores, y la calibración de instrumentos.
- Registrar y hacer seguimiento a las no conformidades hasta su cierre.

## 6.6. Responsable SST (con licencia en SST vigente)

- Elaborar y divulgar la matriz de peligros específica: excavaciones, trabajo en caliente, quemaduras, proyección de metal fundido, riesgo eléctrico por tensiones transferidas, trabajo en alturas.
- Verificar permisos, EPP, extintores, delimitación de áreas, competencias y afiliación vigente a ARL.
- Aplicar el protocolo de tormenta eléctrica y liderar la atención de emergencias.

## 6.7. Responsable ambiental

- Asegurar el cumplimiento del PMA, la gestión de escoria, moldes agotados, envases de carga y retazos de cobre con gestores autorizados, y el control de compuestos de mejoramiento del suelo.

## 6.8. Trabajadores

- Cumplir este procedimiento y participar en el ATS/ART.
- Usar correctamente el EPP y las herramientas asignadas y no improvisar uniones ni herramientas.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Responsable eléctrico COPNIA, supervisor de puesta a tierra, soldadores de exotérmica entrenados, técnicos electricistas CONTE, auxiliares, topógrafo, QA/QC, responsable SST. |
| Materiales | Conductores y electrodos | Conductor de cobre desnudo cableado y, cuando el diseño lo indique, acero galvanizado o recubierto de cobre, en la sección de diseño; varillas de puesta a tierra de las dimensiones y el recubrimiento de diseño, con certificado de producto; platinas y barrajes de cobre. |
| Materiales | Uniones | Moldes de grafito de la combinación exacta (conductor–conductor, conductor–varilla, conductor–platina, conductor–acero estructural), cargas de soldadura del número indicado por el molde, discos metálicos, material de sellado del molde; conectores de compresión irreversibles calificados para enterramiento; conectores mecánicos de bronce o cobre para conexiones accesibles; compuesto inhibidor de óxido. |
| Materiales | Protección contra rayos | Captadores (puntas, mástiles, conductores de captación), conductores de bajante, soportes y fijaciones, uniones de control, DPS AC, DPS DC fotovoltaicos y descargadores MT de la referencia aprobada. |
| Materiales | Obra | Cajas de inspección con tapa, relleno seleccionado sin piedras, compuesto de mejoramiento del suelo solo si el diseño lo especifica, cinta de señalización, grava para capa superficial. |
| Herramientas | Exotérmica | Pinzas o tenazas para molde, encendedor de chispa del fabricante, cepillo de alambre, lima, raspador de escoria, soplete o gas para secar el molde, kit de limpieza de molde. |
| Herramientas | Compresión y montaje | Herramienta hidráulica de compresión con los dados del fabricante del conector; cortador de cable; martillo o hincadora de varillas con cabeza de hincado; torquímetro calibrado (ISO 6789). |
| Equipos | Medida | Telurómetro de cuatro terminales con picas y carretes de cable; óhmetro de baja resistencia (miliohmímetro) para continuidad; pinza de medición de resistencia de puesta a tierra para verificaciones de lazo; equipo de inyección de corriente y voltímetros para tensiones de paso y contacto cuando se exija; GPS o estación total para el registro de coordenadas. Todos con certificado de calibración vigente. |
| EPP | Exotérmica | Careta facial o gafas de seguridad con protección lateral, guantes de cuero de soldador, peto o mangas de cuero, ropa de algodón o ignífuga sin fibras sintéticas, botas de seguridad. |
| EPP | Mediciones | Guantes dieléctricos y calzado dieléctrico al manipular cables de medición en cercanía de instalaciones energizadas o durante inyección de corriente. |
| EPP | Básico | Casco con barbuquejo, gafas con filtro UV, chaleco reflectivo, guantes de maniobra, cubrenuca, protector solar, ropa manga larga, polainas en zonas con ofidios; arnés y línea de vida para trabajos en alturas. |
| Seguridad | Trabajo en caliente | Extintor de polvo químico seco en cada punto de soldadura, recipiente metálico para escoria, lona ignífuga. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

- Personal calificado, autorizado y con inducción en este procedimiento y en trabajo en caliente.
- ATS/ART, charla de inicio de turno, permiso de trabajo, permiso de trabajo en caliente (NES-SST-PR-004) y permiso de excavación diligenciados.
- Diseño del SPT y del sistema de protección contra rayos aprobado, planos vigentes en el frente.
- Materiales con certificado de conformidad de producto, inspeccionados y almacenados según NES-OPE-PR-011; cargas de soldadura secas y dentro de su vida útil.
- Moldes correctos para cada combinación de conductores y en buen estado.
- Zanjas excavadas según NES-OPE-PR-002, con profundidad y trazado verificados por topografía.
- Instrumentos con calibración vigente.
- Condiciones climáticas aptas: sin lluvia sobre la zona de soldadura y sin tormenta eléctrica.

> ALTO: Ningún tramo de malla, electrodo o unión enterrada se cubre sin la liberación escrita de QA/QC con registro fotográfico y coordenadas. Una unión tapada sin inspección se trata como no conforme y se descubre.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

El frente se organiza por sectores del plano de puesta a tierra (bloques de generación, centros de transformación, subestación, edificios y cercas). Se delimitan y señalizan: las zanjas abiertas, los puntos de soldadura exotérmica con un radio libre de material combustible, las líneas de medición (cables extendidos de telurómetro) y el punto de acopio de residuos. Durante las mediciones con inyección de corriente se señalizan los electrodos auxiliares y sus cables para que nadie los toque ni los pise.

### 8.2.2. Ingreso de personal

- Evaluar condiciones del área: estabilidad de taludes de zanja, presencia de agua, interferencias con cables ya tendidos.
- Diligenciar ATS/ART y los permisos aplicables.
- Ubicar equipos de emergencia y extintores e inspeccionar el EPP de soldadura.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional de equipos y circulación solo por rutas autorizadas.
- Los vehículos no circulan sobre zanjas abiertas ni sobre conductores tendidos sin protección, ni a menos de la distancia de seguridad del borde de la zanja definida en NES-OPE-PR-002.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Revisión del diseño y replanteo

1. Revisar la memoria de cálculo y los planos: sección y material de conductores, profundidad de enterramiento, retícula, número y longitud de electrodos, tipo de uniones, cajas de inspección, conexiones a equipos, capa superficial y valores objetivo.
2. Verificar que el diseño cubra la malla general del campo FV, los anillos de los centros de transformación, la subestación, los edificios, las cercas y las puertas.
3. Replantear con topografía los ejes de la malla, la posición de los electrodos y de las cajas de inspección y los puntos de conexión a equipos.
4. Identificar interferencias con hincas, cimentaciones, ductos y zanjas de cables; coordinar el orden de ejecución para que la malla quede a la profundidad de diseño y no sea dañada por trabajos posteriores.

#### 8.2.4.2. Medición de resistividad del terreno (método de Wenner)

La medición se ejecuta antes del diseño definitivo o, si el diseño ya existe, antes de la construcción para confirmar la resistividad de diseño. En plantas FV conviene medir antes del hincado masivo, porque las hincas y estructuras metálicas enterradas distorsionan la lectura.

1. Definir los puntos de medición según el área y la variabilidad del terreno (criterio del diseñador), distribuidos sobre todo el predio y en cada centro de transformación y subestación.
2. En cada punto, trazar dos perfiles perpendiculares entre sí.
3. Clavar cuatro picas alineadas y equidistantes a la separación a, con profundidad de hincado pequeña respecto de a (referencia usual: no mayor a un vigésimo de a).
4. Medir con separaciones crecientes, por ejemplo 1, 2, 4, 8, 16 y 32 m, o las que fije el diseñador para la profundidad que se quiere explorar.
5. Calcular la resistividad aparente con ρ = 2 × π × a × R, donde R es la lectura del telurómetro en Ω y a la separación en m.
6. Alejar los perfiles de cercas, hincas, tuberías, cables enterrados y líneas aéreas; no tender los cables de medición paralelos a conductores enterrados.
7. Registrar fecha, época (seca o de lluvias), humedad aparente del suelo, temperatura y tipo de terreno; repetir la lectura si es inestable.
8. Entregar el registro NES-OPE-F-130 al diseñador para el modelo de suelo (uniforme o estratificado).

> NOTA: Una diferencia importante entre la resistividad medida y la de diseño, o un perfil que muestre capas muy resistivas, se informa al diseñador antes de construir: puede cambiar la cantidad de electrodos, su longitud o la necesidad de capa superficial.

#### 8.2.4.3. Zanjas para la malla

- Las zanjas se excavan, se entiban si se requiere y se rellenan según NES-OPE-PR-002, a la profundidad del diseño — [____] m — verificada por topografía cada [____] m.
- El fondo queda libre de piedras, raíces y escombros. Si el terreno es rocoso, se coloca una cama de material fino seleccionado antes del conductor.
- Cuando la malla comparte zanja con cables de potencia, se respetan la posición y la separación del plano de zanjas.

#### 8.2.4.4. Tendido de conductores

1. Verificar en el carrete la sección, el material y el lote del conductor contra el diseño.
2. Desenrollar el conductor sin formar cocas ni torceduras y sin arrastrarlo sobre superficies que lo raspen.
3. Tender en el fondo de la zanja, sin tensión mecánica, en contacto pleno con el terreno, siguiendo el trazado del plano.
4. Minimizar los empalmes: se usa conductor continuo entre nodos siempre que sea posible; todo empalme es una unión exotérmica o de compresión registrada.
5. En cambios de dirección, respetar el radio mínimo de curvatura del conductor.
6. Las colas o chicotes que suben a equipos o estructuras se dejan con la longitud de diseño más holgura, protegidas contra daño mecánico y señalizadas hasta su conexión.
7. Los cruces con cables de potencia, ductos y vías se protegen según el detalle del plano.
8. Relleno inicial con material fino seleccionado y compactado manualmente alrededor del conductor, sin piedras ni escombros; el resto del relleno según NES-OPE-PR-002.
9. Compuestos de mejoramiento del suelo: solo los especificados por el diseño, con ficha técnica y hoja de seguridad, en la cantidad indicada. No se emplean sal, carbón ni productos corrosivos no certificados (criterio interno).

#### 8.2.4.5. Instalación de electrodos

1. Verificar dimensiones, recubrimiento y marcado de la varilla y su certificado de producto. Las dimensiones mínimas son las del diseño y las exigidas por el RETIE vigente.
2. Hincar la varilla en posición vertical con martillo o hincadora y cabeza de hincado, sin dañar el recubrimiento ni deformar el extremo. Si la varilla encuentra roca, no se corta ni se dobla: se informa al responsable eléctrico para reubicarla o aplicar la alternativa de diseño.
3. Dejar el extremo superior a la profundidad de diseño, por debajo del nivel del terreno y dentro de caja de inspección cuando el plano lo indique.
4. Respetar la separación entre electrodos del diseño para evitar el traslapo de sus zonas de influencia.
5. Para varillas acoplables, usar el acople del fabricante y verificar su continuidad.
6. Unir la varilla a la malla con soldadura exotérmica o conector de compresión calificado.
7. Registrar la posición con coordenadas y fotografía antes de cubrir.

#### 8.2.4.6. Uniones por soldadura exotérmica

La soldadura exotérmica es un trabajo en caliente: requiere permiso según NES-SST-PR-004, extintor en el punto, retiro de combustibles en el radio de seguridad y EPP de soldador.

1. Seleccionar el molde de la combinación exacta (tipo de unión, sección y material de cada conductor) y la carga indicada en el molde. No se usa un molde de otra combinación ni una carga de otro tamaño.
2. Inspeccionar el molde: sin grietas, sin desgaste del orificio de colada, cierre hermético. Un molde con fuga de metal o desgastado se retira.
3. Secar el molde precalentándolo antes de la primera soldadura de la jornada y siempre que haya estado expuesto a humedad; la humedad produce porosidad y proyección de metal.
4. Limpiar los conductores hasta metal brillante con cepillo de alambre o lima, sin grasa, barro, óxido ni humedad. Secar con calor los conductores húmedos.
5. Cortar y posicionar los conductores según el molde, sin deformarlos, y cerrar el molde con las pinzas; sellar las holguras con el material de sellado del fabricante si la combinación lo requiere.
6. Colocar el disco metálico en el fondo de la cámara de reacción, verter la carga de soldadura y el polvo de ignición sobre ella según la instrucción del fabricante.
7. Cerrar la tapa del molde, retirarse del frente del molde y encender con el encendedor de chispa del fabricante. Nunca con fósforo, encendedor de bolsillo ni llama directa.
8. Esperar el tiempo de enfriamiento del fabricante antes de abrir el molde; retirar la escoria con el raspador y limpiar el molde para la siguiente unión.
9. Inspeccionar la unión (formato NES-OPE-F-132).
10. Registrar el número de soldaduras por molde y retirarlo al alcanzar la vida útil indicada por el fabricante.

| Condición de la unión | Disposición |
|---|---|
| Superficie lisa, conductores totalmente embebidos, sin cavidades, sin porosidad excesiva, tamaño completo | Aceptada |
| Porosidad superficial menor sin cavidades ni conductores expuestos | Aceptada si el criterio del fabricante lo admite; registrar |
| Conductor no fundido o visible dentro de la unión, unión incompleta, cavidades, fisuras | Rechazada: cortar y rehacer |
| Fuga de metal por el molde, rebaba que impide el cierre de la siguiente unión | Revisar el molde y el sellado; rehacer |
| Unión que se suelta al golpe moderado con martillo | Rechazada: cortar y rehacer |

> ALTO: Nunca se suelda sobre conductores mojados ni con el molde húmedo: el vapor proyecta metal fundido a más de un metro. El soldador y los ayudantes se ubican fuera de la línea del orificio de colada durante la reacción.

#### 8.2.4.7. Uniones por conectores de compresión

1. Usar solo conectores irreversibles calificados para enterramiento (IEEE 837 o la calificación que exija el diseño) cuando la unión vaya enterrada o embebida en concreto.
2. Verificar que el conector corresponde a la sección y combinación de conductores y que la herramienta y el dado son los indicados por el fabricante del conector.
3. Limpiar los conductores hasta metal brillante y aplicar compuesto inhibidor si el conector no lo trae.
4. Insertar los conductores hasta el tope y ejecutar el número de compresiones y la secuencia del fabricante, hasta que el cabezal cierre completamente.
5. Verificar la marca o el número del dado estampado en el conector y la ausencia de fisuras.
6. Los conectores mecánicos (perno, abrazadera) se usan solo en conexiones accesibles para inspección y mantenimiento, con el par del fabricante y protección contra corrosión.
7. Registrar en el formato NES-OPE-F-133.

#### 8.2.4.8. Equipotencialización de estructuras y equipos

Todas las partes conductoras expuestas de la planta se unen al SPT de modo que no existan diferencias peligrosas de potencial. Conexiones típicas a verificar contra el plano:

| Elemento | Conexión |
|---|---|
| Tracker y estructura fija | Según NES-OPE-PR-008 y el diseño: continuidad entre tramos, conexión de la estructura a la malla en los puntos y con el conductor del plano. |
| Marcos de módulos | Según la instrucción de puesta a tierra del fabricante del módulo y del tracker: arandelas de unión certificadas, tornillería o conductor; no se perforan marcos fuera de los puntos permitidos. |
| Hincas | Solo cuando el diseño las use como electrodo o exija su unión; conexión con el elemento calificado. |
| Bandejas y canalizaciones metálicas | Continuidad entre tramos con puentes de unión y conexión a tierra en los extremos y en los puntos de diseño. |
| Cajas combinadoras | Barra de tierra conectada a la malla y a la estructura; DPS DC con conductor de tierra corto. |
| Inversores | Barra o borne de puesta a tierra del inversor conectado a la malla con la sección y el número de puntos que indique el fabricante del inversor (NES-OPE-PR-018). |
| Centros de transformación | Según NES-OPE-PR-019: tanque, base, celdas, cuadros, puertas y neutro según diseño. |
| Cercas perimetrales y puertas | Puesta a tierra según el diseño (intervalos, esquinas, puertas, cruces de líneas); puertas con puente flexible a su poste; secciones aisladas cuando el diseño lo exija para controlar tensiones transferidas. |
| Postes de iluminación, CCTV y estaciones meteorológicas | Conectados a la malla con conductor y unión del plano. |
| Contenedores, edificios y tuberías metálicas | Conectados al barraje equipotencial del edificio y a la malla. |

Reglas comunes:

- Las conexiones a equipos se hacen en superficies limpias, sin pintura, con terminales adecuados al conductor y el par del fabricante; las superficies galvanizadas raspadas se protegen después de la conexión.
- No se conectan equipos en serie a través de otros equipos: cada masa tiene su propia conexión al SPT, salvo que el diseño indique lo contrario.
- Los conductores de puesta a tierra visibles se fijan, se protegen contra daño mecánico y se identifican.

#### 8.2.4.9. Puesta a tierra de centros de transformación y subestación

- Construir el anillo perimetral y la retícula del diseño alrededor y bajo el centro de transformación, con electrodos en las esquinas o donde indique el plano, y unirlo a la malla general en el número de puntos de diseño (al menos dos, en lados opuestos, si el diseño así lo indica).
- Dejar las colas para el tanque, la base, las celdas y los cuadros en posición, antes del vaciado de la fundación (NES-OPE-PR-012).
- Instalar la capa superficial de grava con el espesor y la granulometría de diseño, sin mezclarla con tierra.
- Verificar que las cercas metálicas próximas al CT o a la subestación estén conectadas o aisladas según el diseño, para que no transfieran tensiones fuera del área de la malla.

#### 8.2.4.10. Protección externa contra rayos

1. Verificar que la evaluación del riesgo (NTC 4552-2) definió el nivel de protección y las estructuras que requieren protección externa: edificios de control y de O&M, subestación, almacenes, torres de comunicación, estación meteorológica y, si el diseño lo exige, el campo FV.
2. Instalar los captadores (puntas, mástiles, conductores de captación) en la posición del diseño realizado por el método de la esfera rodante, del ángulo de protección o de la malla (NTC 4552-3), sin generar sombras sobre los módulos que no hayan sido consideradas en el diseño.
3. Instalar las bajantes por el recorrido más corto y recto posible, sin bucles ni curvas cerradas, con el número y la separación del diseño, fijadas con soportes adecuados al material.
4. Instalar uniones de control (desconectables) accesibles para medición en la base de cada bajante cuando el diseño lo indique, y protección mecánica en el tramo inferior.
5. Conectar cada bajante a su puesta a tierra y esta a la malla general, de modo que todo el sistema quede equipotencializado.
6. Mantener la distancia de separación del diseño entre bajantes y conductores eléctricos o de comunicaciones, o equipotencializarlos donde el diseño lo indique.
7. Verificar que todos los componentes (captadores, conductores, conectores) tengan el material y la sección del diseño y certificado de producto, y que no se mezclen metales que produzcan corrosión galvánica sin la unión bimetálica adecuada.

#### 8.2.4.11. Protección interna: equipotencialización y DPS

- Equipotencializar en el punto de entrada a cada edificio o recinto todas las instalaciones metálicas entrantes: pantallas de cables, tuberías, elementos metálicos de cables de comunicaciones.
- Instalar los DPS en la posición, tipo, tensión y corriente de descarga del diseño: DPS DC fotovoltaicos en cajas combinadoras e inversores (IEC 61643-31), DPS AC en tableros de BT y servicios auxiliares (IEC 61643-11), DPS de comunicaciones y descargadores MT donde indique el unifilar.
- Conectar el DPS con conductores lo más cortos y rectos posible, entre fase y barra de tierra local; una conexión larga suma la caída de tensión inductiva al nivel de protección. Referencia usual de la literatura técnica: longitud total de conexión no mayor a 0,5 m; verificar contra la instrucción del fabricante del DPS y el diseño.
- Instalar la protección de respaldo (fusible o interruptor) del DPS que indique el fabricante.
- Verificar el indicador de estado de cada DPS y, si tiene, el contacto de señalización remota hacia el SCADA.
- Coordinar los tipos de DPS en cascada según el diseño (tipo 1 en la acometida o en estructuras con protección externa, tipo 2 aguas abajo).

#### 8.2.4.12. Inspección antes de tapar (punto de retención)

Antes de rellenar cada tramo, QA/QC verifica con el formato NES-OPE-F-131:

- Trazado, profundidad y sección del conductor conforme al plano.
- Electrodos en número y posición de diseño.
- 100 % de las uniones inspeccionadas y aceptadas.
- Colas a equipos en posición y protegidas.
- Registro fotográfico de cada unión y electrodo, con coordenadas.
- Continuidad del tramo con óhmetro de baja resistencia.

#### 8.2.4.13. Mediciones de continuidad

1. Medir con óhmetro de baja resistencia de cuatro hilos la resistencia entre la malla (punto de referencia en caja de inspección o barraje) y cada masa conectada: estructuras, inversores, cajas combinadoras, tanques, celdas, cercas, puertas, postes.
2. Registrar el valor en el formato NES-OPE-F-134.
3. Criterio de referencia: valores bajos y homogéneos entre elementos similares; como referencia de práctica de ensayos de aceptación, investigar todo valor punto a punto superior a 0,5 Ω (criterio interno; verificar contra la especificación del proyecto). Un valor elevado indica unión defectuosa, conductor cortado o conexión pintada.

#### 8.2.4.14. Medición de resistencia de puesta a tierra (caída de potencial)

Se mide la resistencia del SPT completo y, cuando el diseño lo exija, de cada subsistema (anillos de CT, subestación, edificios) antes de interconectarlos, siguiendo la IEEE 81:

1. Medir preferiblemente en época seca o registrar la época y la humedad del suelo; una medición en época de lluvias da valores optimistas.
2. Si se mide un subsistema aislado, desconectar temporalmente las uniones que lo enlazan con el resto, con autorización del responsable eléctrico y nunca en una instalación energizada.
3. Ubicar el electrodo de corriente a una distancia suficiente para estar fuera de la zona de influencia del SPT: para mallas grandes, varias veces la mayor dimensión de la malla (referencia usual: cinco veces o más). Tender el cable en una dirección libre de estructuras, cercas y conductores enterrados.
4. Ubicar el electrodo de potencial en la misma línea, en posiciones sucesivas entre el SPT y el electrodo de corriente (por ejemplo cada 10 % de la distancia), y registrar la resistencia en cada posición.
5. Graficar la curva de resistencia contra distancia. El valor válido es el de la zona plana de la curva; en suelo homogéneo coincide con el electrodo de potencial a aproximadamente el 62 % de la distancia al electrodo de corriente. Si la curva no presenta zona plana, el electrodo de corriente está demasiado cerca: alejarlo o aplicar un método alternativo de la IEEE 81 (método de la pendiente, método de intersección) definido por el responsable eléctrico.
6. Repetir en una segunda dirección para confirmar.
7. Verificar que el instrumento no indique ruido ni resistencia excesiva de los electrodos auxiliares; mojar las picas auxiliares si es necesario.
8. Registrar en el formato NES-OPE-F-135 con el método, distancias, curva y condiciones.

> NOTA: La pinza de medición de resistencia de lazo solo sirve para verificaciones en sistemas con múltiples trayectorias a tierra y no reemplaza la medición por caída de potencial para la aceptación del SPT.

Criterio: valor no mayor que el de diseño y que el máximo aplicable según la tabla de valores de referencia de resistencia de puesta a tierra del RETIE vigente para cada tipo de instalación (subestaciones de media tensión, protección contra rayos, neutro de acometida en BT u otros que apliquen). El cumplimiento del valor de referencia no exime de verificar que las tensiones de paso y de contacto no superen las tolerables.

#### 8.2.4.15. Tensiones de paso y contacto

Cuando la memoria de cálculo, el RETIE o [CLIENTE] lo exijan, en particular en subestaciones y centros de transformación, se verifican las tensiones de paso y de contacto:

1. El método, los puntos de medición y la corriente de inyección los define el responsable eléctrico conforme a la IEEE 81, de modo que el resultado pueda escalarse a la corriente de falla de diseño.
2. Inyectar corriente entre el SPT y un electrodo remoto; medir la tensión entre la estructura y los electrodos que simulan los pies (contacto) y entre dos puntos separados 1 m (paso), en los puntos críticos: puertas, esquinas, manijas de equipos, cercas, zonas de maniobra.
3. Escalar los valores medidos a la corriente de falla de diseño y compararlos con las tensiones tolerables calculadas en la memoria (IEEE 80) y con los valores máximos de tensión de contacto del RETIE vigente.
4. Registrar en el formato NES-OPE-F-136. Un valor por encima del tolerable se informa al diseñador antes de energizar.

> ALTO: Durante la inyección de corriente nadie toca los electrodos auxiliares, los cables de medición ni las estructuras bajo ensayo. Los cables se señalizan en todo su recorrido y el personal de medición usa guantes y calzado dieléctrico.

#### 8.2.4.16. Cajas de inspección, rotulación y planos récord

- Instalar las cajas de inspección en los puntos del plano, con tapa identificada, a nivel del terreno y libres de relleno dentro.
- Rotular los conductores de puesta a tierra en los barrajes y en las conexiones a equipos.
- Elaborar el plano récord con las coordenadas de nodos, electrodos, uniones, colas y cajas de inspección y entregar el registro fotográfico asociado.

#### 8.2.4.17. Documentación para el dictamen RETIE

El SPT y el sistema de protección contra rayos forman parte de la inspección RETIE de la instalación, que la ejecuta un organismo de inspección acreditado por el ONAC. Antes de solicitarla, el responsable eléctrico reúne con el formato NES-OPE-F-139:

- Memoria de cálculo y planos aprobados, y planos récord.
- Mediciones de resistividad, continuidad, resistencia de puesta a tierra y, cuando aplique, tensiones de paso y contacto.
- Certificados de conformidad de producto de los materiales.
- Protocolos de uniones y registros fotográficos.
- Evaluación de riesgo por rayo y diseño del sistema de protección contra rayos.
- Declaración de cumplimiento del RETIE suscrita por el constructor responsable (con matrícula profesional vigente), en el formato que exija el reglamento.

> ALTO: Ninguna parte de la instalación se energiza sin el SPT completo, medido y aceptado, sin el dictamen de inspección RETIE y sin autorización escrita de energización según NES-OPE-PR-023.

#### 8.2.4.18. No conformidades

- Resistividad o resistencia de puesta a tierra fuera de lo previsto: informe al diseñador; ninguna medida correctiva (electrodos adicionales, compuestos de mejoramiento) se ejecuta sin su aprobación escrita.
- Unión rechazada, conductor dañado o sección inferior a la de diseño: corrección inmediata y reinspección del 100 % del tramo.
- Tramo tapado sin liberación: descubrir e inspeccionar.
- Material sin certificado de producto: cuarentena y consulta a QA/QC.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Materiales | Material, sección y dimensiones de diseño, con certificado de conformidad de producto | Diseño / RETIE |
| Profundidad del conductor de malla | La del diseño — [____] m — verificada por topografía | Diseño |
| Electrodos | Número, posición, longitud y separación de diseño; verticales y sin daño del recubrimiento | Diseño / RETIE |
| Soldadura exotérmica | Molde y carga de la combinación exacta; superficie lisa, conductores embebidos, sin cavidades ni fisuras | Fabricante del sistema de soldadura |
| Conector de compresión | Calificado para enterramiento; dado y número de compresiones del fabricante; marca del dado visible | IEEE 837 / fabricante |
| Conexiones mecánicas | Solo en puntos accesibles; par del fabricante | Fabricante |
| Continuidad punto a punto | Valores bajos y homogéneos; investigar valores mayores de 0,5 Ω (criterio interno) | Especificación del proyecto |
| Resistividad del terreno | Registrada en dos direcciones por punto; diferencias con el diseño informadas al diseñador | IEEE 81 |
| Resistencia de puesta a tierra | No mayor que la de diseño ni que el valor de la tabla de valores de referencia de resistencia de puesta a tierra del RETIE vigente para el tipo de instalación | Diseño / RETIE |
| Curva de caída de potencial | Con zona plana identificable; medición confirmada en dos direcciones | IEEE 81 |
| Tensiones de paso y contacto | No mayores que las tolerables de la memoria (IEEE 80) ni que los máximos del RETIE vigente, escaladas a la corriente de falla de diseño | IEEE 80 / RETIE |
| Captadores y bajantes | Posición, material, sección y número del diseño; recorrido corto sin bucles; uniones de control accesibles | NTC 4552-3 / diseño |
| DPS | Tipo y valores del diseño; conexión corta; protección de respaldo del fabricante; indicador en estado normal | IEC 61643-11 / IEC 61643-31 / fabricante |
| Capa superficial | Espesor y material del diseño, sin contaminar con tierra | Diseño / IEEE 80 |
| Liberación antes de tapar | 100 % de tramos con formato firmado, fotos y coordenadas | Este procedimiento |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-130 a NES-OPE-F-139 de este procedimiento.
- Permisos de trabajo en caliente y de excavación, ATS/ART del frente.
- Certificados de calibración de telurómetros, óhmetros e instrumentos de medición.
- Certificados de conformidad de producto y fichas técnicas por lote.
- Planos récord con coordenadas y registro fotográfico.

## 8.5. Control de calidad

QA/QC verifica el 100 % de las uniones y de los tramos antes del relleno (punto de retención H), el 100 % de las conexiones a equipos mediante la medición de continuidad y la totalidad de las mediciones de resistencia de puesta a tierra. Si una unión exotérmica es rechazada, se inspeccionan de nuevo todas las uniones hechas con el mismo molde en la jornada. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación que no afecta calidad, prestación ni seguridad, por ejemplo rótulo faltante o caja de inspección sin tapa identificada. | Registro y cierre. |
| 2 | Requiere rehacer con el método de este procedimiento: unión rechazada, conexión a equipo floja, profundidad insuficiente localizada. | Corrección por la cuadrilla y reinspección. |
| 3 | Afecta la seguridad de las personas o el cumplimiento del RETIE: resistencia o tensiones fuera de criterio, material no certificado, tramo enterrado sin inspección. | Suspensión del frente, consulta al diseñador y aprobación escrita antes de actuar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS/ART y la charla diaria, verifica que las áreas estén señalizadas y demarcadas y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre características del proyecto, trabajo en caliente con soldadura exotérmica, excavaciones, tensiones transferidas, medidas de control, puntos de encuentro y uso correcto del EPP.

## 9.1. Reglas de oro

- **SIEMPRE** soldaré con permiso de trabajo en caliente, extintor a mano y EPP de soldador completo.
- **NUNCA** soldaré con el molde o los conductores húmedos.
- **NUNCA** encenderé una carga con llama directa: solo con el encendedor de chispa del fabricante.
- **SIEMPRE** me ubicaré fuera de la línea del orificio de colada durante la reacción.
- **NUNCA** ingresaré a una zanja sin verificar su estabilidad y el entibado requerido (NES-OPE-PR-002).
- **NUNCA** desconectaré una unión del SPT en una instalación energizada.
- **NUNCA** tocaré cables ni electrodos de medición durante la inyección de corriente.
- **SIEMPRE** suspenderé la actividad ante tormenta eléctrica: la malla, las cercas y los cables de medición conducen la corriente del rayo.
- **SIEMPRE** dejaré cada unión inspeccionada y fotografiada antes de taparla.
- **SIEMPRE** ejecutaré el trabajo con ATS/ART y permisos diligenciados.

## 9.2. Condiciones climáticas de [departamento]

- Tormenta eléctrica: ante el aviso o el primer trueno, suspender todo trabajo en zanjas, sobre conductores de la malla, cercas, bajantes y mediciones con cables extendidos; alejarse de estructuras metálicas y dirigirse al refugio. Se reanuda solo con autorización del responsable SST.
- Lluvia: suspender la soldadura exotérmica y las mediciones; proteger moldes y cargas; revisar la estabilidad de las zanjas antes de reingresar.
- Calor y radiación: hidratación, sombra, pausas activas y rotación, en especial del soldador por el calor adicional de la reacción.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado de materiales y carretes | Sobreesfuerzo, atrapamiento, golpes. | Ayudas mecánicas para carretes; carga manual dentro de los límites de la Res. 2400 de 1979; guantes de maniobra. |
| 2. Medición de resistividad | Tropiezos con cables, golpes al hincar picas, tensión inducida en cables largos. | Cables señalizados; martillo en buen estado; suspensión ante tormenta; alejamiento de líneas energizadas. |
| 3. Trabajo en zanjas | Derrumbe, caída al mismo y distinto nivel, golpes por equipos. | NES-OPE-PR-002; entibado cuando aplique; escaleras de acceso; material de excavación retirado del borde. |
| 4. Tendido del conductor | Cortes y punzadas con hilos de cobre, latigazo del conductor. | Guantes de maniobra; desenrollado controlado; nadie en la línea del conductor bajo tensión mecánica. |
| 5. Hincado de electrodos | Golpes en manos, proyección de partículas, ruido. | Guía o sujetador de varilla; gafas; protección auditiva; cabeza de hincado. |
| 6. Soldadura exotérmica | Quemaduras, proyección de metal fundido, incendio, humos. | Permiso de trabajo en caliente (NES-SST-PR-004); molde seco; encendedor de chispa; EPP de soldador; extintor; zona libre de combustibles; trabajo con viento a favor. |
| 7. Manejo de cargas de soldadura | Ignición accidental, contacto con sustancia química. | Almacenamiento según NES-OPE-PR-011 y SGA; lejos de fuentes de calor; cantidades de la jornada. |
| 8. Conectores de compresión | Atrapamiento de dedos, falla de la herramienta hidráulica. | Herramienta inspeccionada; manos fuera del cabezal; mangueras sin fugas. |
| 9. Conexión a equipos e inversores | Choque eléctrico si el equipo está energizado o tiene fuentes de retorno. | Cinco reglas de oro; LOTO según NES-SST-PR-001; conexión al SPT antes de cualquier energización. |
| 10. Captadores y bajantes en altura | Caída a distinto nivel, caída de objetos. | Res. 4272 de 2021; arnés y punto de anclaje; herramientas amarradas; zona inferior delimitada. |
| 11. Instalación de DPS en tableros | Choque eléctrico, arco eléctrico. | Tablero desenergizado y bloqueado; verificación de ausencia de tensión; EPP con categoría de arco. |
| 12. Medición de resistencia y tensiones de paso y contacto | Choque eléctrico por tensiones transferidas o por la inyección, tropiezos. | Señalización de cables y picas; guantes y calzado dieléctrico; nadie toca la instalación bajo ensayo; suspensión ante tormenta. |
| 13. Exposición ambiental | Radiación UV, estrés térmico, ofidios, picaduras. | Ropa manga larga, cubrenuca, protector solar, hidratación, sombra, pausas; polainas; revisar zanjas y cajas antes de ingresar las manos. |
| 14. Tormenta eléctrica y lluvia | Descarga atmosférica, derrumbe de zanjas. | Suspender la actividad; refugio o punto de encuentro; inspección de zanjas antes de reanudar. |
| 15. Orden, aseo y residuos | Tropiezos, cortes, contaminación del suelo. | Escoria y retazos en recipientes; área despejada al cierre; separación de residuos. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Suelo | Escoria y moldes agotados | Escoria fría recogida en recipiente metálico; moldes agotados, envases de cargas y residuos de la reacción gestionados según la hoja de seguridad del fabricante; si se clasifican como peligrosos, se entregan a gestor RESPEL autorizado (Decreto 1076 de 2015). |
| Suelo | Retazos de cobre y acero | Recogidos el mismo día, pesados y almacenados bajo llave como aprovechables; entrega a gestor autorizado con acta y certificado. |
| Suelo y agua | Compuestos de mejoramiento del suelo | Solo los especificados en el diseño, con hoja de seguridad; sin uso de sal ni productos que contaminen el suelo o el agua subterránea; sobrantes devueltos o gestionados según la hoja de seguridad. |
| Suelo | Residuos sólidos y embalajes | Separación en la fuente según Res. 2184 de 2019; carretes de madera, cartón y plásticos a su corriente de aprovechamiento. |
| Suelo | RCD y excedentes de excavación | Gestión según Res. 0472 de 2017 modificada por Res. 1257 de 2021 y NES-OPE-PR-002. |
| Aire | Humos de la reacción exotérmica y polvo | Soldadura al aire libre con viento a favor; humectación de vías en época seca. |
| Flora y fauna | Intervención de hábitat y caída de fauna en zanjas | Trabajar solo en áreas liberadas; rampas de escape o revisión diaria de zanjas abiertas; reporte de fauna para rescate según PMA; prohibido hacer fuego fuera del punto de soldadura autorizado. |
| Suelo | Incendio de cobertura vegetal | Despeje de vegetación seca en el radio de la soldadura; extintor y agua disponibles; vigilancia posterior al trabajo en caliente. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener la actividad y asegurar la zona: suspender la soldadura, apagar fuentes de ignición, detener la inyección de corriente, retirar al personal de la zanja.
2. Notificar al responsable SST y al responsable eléctrico de Neptuno Energy Services y al interlocutor de [CLIENTE].
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, extintor en el frente).
4. Incidente grave: activar ambulancia (línea 123) y traslado al centro asistencial definido; notificar a la ARL.
5. Reportar el evento y realizar la investigación según Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Responsable eléctrico Neptuno Energy Services | [__________] | [__________] |
| Residente de obra Neptuno Energy Services | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Bomberos / Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

## 12.1. Quemaduras por metal fundido

- Retirar al lesionado de la fuente de calor; si la ropa arde, cubrir y hacer rodar a la persona en el suelo.
- Enfriar la quemadura con agua limpia a temperatura ambiente durante varios minutos; no aplicar hielo, cremas ni remedios caseros.
- No retirar la ropa adherida ni partículas de metal incrustadas; cubrir con apósito estéril.
- Lesión ocular por proyección: no frotar, cubrir ambos ojos y remitir a valoración oftalmológica.

## 12.2. Incendio de vegetación o de material combustible

- Atacar el conato con extintor si es seguro; si el fuego avanza, evacuar en dirección contraria al viento y activar la emergencia (123).
- Mantener vigilancia del área de soldadura después de terminar, según el permiso de trabajo en caliente.

## 12.3. Derrumbe de zanja o atrapamiento

- No ingresar a rescatar sin asegurar las paredes; activar la emergencia de inmediato.
- Retirar material manualmente con cuidado alrededor de la cabeza y el tórax del atrapado y mantener contacto verbal.

## 12.4. Descarga eléctrica o choque eléctrico

- No tocar a la víctima mientras siga en contacto con la fuente; cortar la fuente o separarla con elemento aislante.
- Activar la emergencia y aplicar reanimación si el personal está capacitado; toda persona que sufra un choque eléctrico o una descarga atmosférica cercana se remite a valoración médica aunque se sienta bien.

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Registro de medición de resistividad del terreno (método de Wenner) | NES-OPE-F-130 | Responsable eléctrico |
| Lista de verificación de malla y electrodos antes de tapar | NES-OPE-F-131 | QA/QC |
| Registro de uniones por soldadura exotérmica | NES-OPE-F-132 | Supervisor / soldador |
| Registro de uniones por conectores de compresión | NES-OPE-F-133 | Supervisor |
| Protocolo de continuidad y equipotencialización | NES-OPE-F-134 | Responsable eléctrico |
| Registro de medición de resistencia de puesta a tierra (caída de potencial) | NES-OPE-F-135 | Responsable eléctrico |
| Registro de medición de tensiones de paso y contacto | NES-OPE-F-136 | Responsable eléctrico |
| Lista de verificación de protección externa contra rayos | NES-OPE-F-137 | QA/QC |
| Lista de verificación de instalación de DPS | NES-OPE-F-138 | Responsable eléctrico |
| Lista de documentos para el dictamen RETIE del SPT y de la protección contra rayos | NES-OPE-F-139 | Responsable eléctrico |
| Permisos de trabajo en caliente y de excavación | NES-SST-PR-004 / NES-OPE-PR-002 | Supervisor / SST |
| Planos récord, fotografías y certificados | — | QA/QC |

# 14. ANEXOS

## NES-OPE-F-130 — Registro de medición de resistividad del terreno (método de Wenner)

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Punto de medición / coordenadas: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / IEEE 81 | Telurómetro (serie / calibración): [__________] |

{.plain}
| Época: seca / lluvias | Estado del suelo: seco / húmedo / saturado |
|---|---|
| Tipo de terreno: [__________] | Temperatura ambiente: [____] °C |
| Profundidad de hincado de picas: [____] m | Interferencias cercanas: [__________] |

| Separación a (m) | Perfil 1 — R (Ω) | Perfil 1 — ρ (Ω·m) | Perfil 2 — R (Ω) | Perfil 2 — ρ (Ω·m) | ρ promedio (Ω·m) |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 8 |  |  |  |  |  |
| 16 |  |  |  |  |  |
| 32 |  |  |  |  |  |

{.plain}
| Fórmula aplicada: ρ = 2 × π × a × R | Orientación perfil 1 / perfil 2: [____] / [____] |
|---|---|

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

## NES-OPE-F-131 — Lista de verificación de malla y electrodos antes de tapar

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Sector / tramo (desde – hasta): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 | Plano de puesta a tierra: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Trazado conforme al plano |  |  |  |
| 2 | Profundidad de diseño verificada por topografía ([____] m) |  |  |  |
| 3 | Conductor de material y sección de diseño (lote [____]) |  |  |  |
| 4 | Fondo de zanja sin piedras ni escombros; cama de material fino si aplica |  |  |  |
| 5 | Conductor sin tensión, sin cocas ni daños |  |  |  |
| 6 | Electrodos en número y posición de diseño, verticales y sin daño |  |  |  |
| 7 | 100 % de uniones inspeccionadas y aceptadas (F-132 / F-133) |  |  |  |
| 8 | Colas a equipos en posición, con longitud y protección |  |  |  |
| 9 | Cruces con cables y ductos protegidos según detalle |  |  |  |
| 10 | Cajas de inspección en posición |  |  |  |
| 11 | Continuidad del tramo verificada |  |  |  |
| 12 | Registro fotográfico y coordenadas de uniones y electrodos |  |  |  |
| 13 | Relleno inicial con material seleccionado autorizado |  |  |  |

{.plain}
| Tramo liberado para relleno: Sí / No | Punto de retención (H) firmado por QA/QC: [____] |
|---|---|

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

## NES-OPE-F-132 — Registro de uniones por soldadura exotérmica

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Sector / tramo: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / NES-SST-PR-004 | Permiso de trabajo en caliente N.º: [____] |

{.plain}
| Soldador: [__________] | Lote de cargas: [__________] |
|---|---|
| Molde (referencia / combinación): [__________] | Soldaduras acumuladas del molde: [____] |
| Molde precalentado al inicio: Sí / No | Condición del clima: [__________] |

| N.º unión | Tipo (cable–cable, cable–varilla, cable–estructura) | Coordenadas / ubicación | Carga N.º | Inspección visual | Foto N.º | Acepta / rechaza |
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
| Uniones ejecutadas: [____] | Rechazadas y rehechas: [____] |
|---|---|

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

## NES-OPE-F-133 — Registro de uniones por conectores de compresión

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Sector / tramo: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / IEEE 837 | Herramienta (serie): [__________] |

| N.º unión | Referencia del conector | Conductores (sección) | Dado | N.º de compresiones | Marca del dado visible | Acepta / rechaza |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |

{.plain}
| Conector calificado para enterramiento: Sí / No | Compuesto inhibidor aplicado: Sí / No |
|---|---|

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

## NES-OPE-F-134 — Protocolo de continuidad y equipotencialización

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Sector / bloque: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 | Óhmetro (serie / calibración): [__________] |

{.plain}
| Punto de referencia de la malla: [__________] | Corriente de ensayo: [____] A |
|---|---|

| Elemento | Identificación | Tipo de conexión | Resistencia (Ω) | Cumple | Obs. |
|---|---|---|---|---|---|
| Estructura de tracker / mesa |  |  |  |  |  |
| Caja combinadora |  |  |  |  |  |
| Inversor |  |  |  |  |  |
| Centro de transformación |  |  |  |  |  |
| Bandeja / canalización |  |  |  |  |  |
| Cerca / puerta |  |  |  |  |  |
| Poste de iluminación / CCTV |  |  |  |  |  |
| Edificio / contenedor |  |  |  |  |  |

{.plain}
| Criterio aplicado: [____] Ω | Resultado: conforme / no conforme |
|---|---|

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

## NES-OPE-F-135 — Registro de medición de resistencia de puesta a tierra (caída de potencial)

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Sistema medido (malla general / CT / subestación / edificio): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / IEEE 81 | Telurómetro (serie / calibración): [__________] |

{.plain}
| Mayor dimensión del SPT: [____] m | Distancia al electrodo de corriente: [____] m |
|---|---|
| Dirección del perfil 1 / perfil 2: [____] / [____] | Época y estado del suelo: [__________] |
| Subsistema aislado para la medición: Sí / No | Valor de diseño: [____] Ω |

| Posición del electrodo de potencial (% de la distancia) | 10 | 20 | 30 | 40 | 50 | 62 |
|---|---|---|---|---|---|---|
| Perfil 1 — R (Ω) |  |  |  |  |  |  |
| Perfil 2 — R (Ω) |  |  |  |  |  |  |

| Posición del electrodo de potencial (% de la distancia) | 70 | 80 | 90 | Zona plana identificada | Valor adoptado (Ω) |
|---|---|---|---|---|---|
| Perfil 1 — R (Ω) |  |  |  |  |  |
| Perfil 2 — R (Ω) |  |  |  |  |  |

{.plain}
| Valor de referencia RETIE aplicable (tipo de instalación): [__________] | Resultado: conforme / no conforme |
|---|---|

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

## NES-OPE-F-136 — Registro de medición de tensiones de paso y contacto

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Instalación (CT / subestación): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / IEEE 81 / IEEE 80 | Equipos (serie / calibración): [__________] |

{.plain}
| Corriente inyectada: [____] A | Corriente de falla de diseño: [____] A |
|---|---|
| Factor de escala: [____] | Resistividad de la capa superficial: [____] Ω·m |

| Punto | Tipo (paso / contacto) | Descripción del punto | Tensión medida (V) | Tensión escalada (V) | Tensión tolerable (V) | Cumple |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |

{.plain}
| Método aplicado: [__________] | Resultado: conforme / no conforme |
|---|---|

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

## NES-OPE-F-137 — Lista de verificación de protección externa contra rayos

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Estructura protegida: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / NTC 4552 | Nivel de protección de diseño: [____] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Captadores en posición, altura y número de diseño |  |  |  |
| 2 | Material y sección de captadores y conductores según diseño |  |  |  |
| 3 | Sin sombras no previstas sobre módulos |  |  |  |
| 4 | Bajantes en número y separación de diseño |  |  |  |
| 5 | Recorrido de bajantes corto, recto, sin bucles |  |  |  |
| 6 | Fijaciones a la separación de diseño |  |  |  |
| 7 | Uniones de control accesibles y protección mecánica inferior |  |  |  |
| 8 | Puesta a tierra de cada bajante unida a la malla |  |  |  |
| 9 | Distancia de separación o equipotencialización según diseño |  |  |  |
| 10 | Sin pares galvánicos sin unión bimetálica |  |  |  |
| 11 | Certificados de producto de los componentes |  |  |  |

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

## NES-OPE-F-138 — Lista de verificación de instalación de DPS

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Tablero / caja / equipo: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / IEC 61643-11 / IEC 61643-31 | Unifilar: [__________] |

| Ubicación | Tipo (1 / 2 / 3, AC / DC / MT) | Tensión máx. de servicio | Corriente de descarga | Longitud de conexión (m) | Indicador de estado | Cumple |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Referencia y valores conforme al diseño y certificado de producto |  |  |  |
| 2 | Conexión corta y recta a la barra de tierra local |  |  |  |
| 3 | Protección de respaldo del fabricante instalada |  |  |  |
| 4 | Señalización remota al SCADA (si aplica) verificada |  |  |  |
| 5 | Coordinación en cascada según diseño |  |  |  |

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

## NES-OPE-F-139 — Lista de documentos para el dictamen RETIE del SPT y de la protección contra rayos

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Alcance de la inspección: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-020 / RETIE | Organismo de inspección acreditado: [__________] |

| Ítem | Documento | Disponible | Referencia / N.º | Obs. |
|---|---|---|---|---|
| 1 | Memoria de cálculo del SPT y planos aprobados |  |  |  |
| 2 | Evaluación de riesgo por rayo y diseño de protección (NTC 4552) |  |  |  |
| 3 | Planos récord con coordenadas |  |  |  |
| 4 | Registros de resistividad (F-130) |  |  |  |
| 5 | Liberaciones antes de tapar (F-131) y protocolos de uniones (F-132 / F-133) |  |  |  |
| 6 | Protocolos de continuidad (F-134) |  |  |  |
| 7 | Mediciones de resistencia de puesta a tierra (F-135) |  |  |  |
| 8 | Mediciones de tensiones de paso y contacto (F-136), si aplica |  |  |  |
| 9 | Listas de protección externa (F-137) y DPS (F-138) |  |  |  |
| 10 | Certificados de conformidad de producto de materiales |  |  |  |
| 11 | Certificados de calibración de instrumentos |  |  |  |
| 12 | Declaración de cumplimiento del constructor, con matrícula profesional vigente |  |  |  |
| 13 | Registro fotográfico |  |  |  |

{.plain}
| Expediente completo y entregado a NES-OPE-PR-023: Sí / No | Fecha de solicitud de inspección: [____] |
|---|---|

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
