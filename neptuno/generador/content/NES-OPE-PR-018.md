---
code: NES-OPE-PR-018
header_title: PROCEDIMIENTO DE MONTAJE Y CONEXIONADO DE INVERSORES
cover_title: Procedimiento de Montaje y Conexionado de Inversores
cover_subtitle: Inversores string y centrales / estaciones de potencia en plantas fotovoltaicas
---

# 1. OBJETIVO

Definir el método de trabajo, los controles de calidad y las medidas preventivas para la recepción, el almacenamiento, el izaje, el montaje, el conexionado DC y AC, las comunicaciones, la puesta a tierra, las verificaciones previas al arranque y el primer arranque de los inversores string y de los inversores centrales o estaciones de potencia de la planta FV [PROYECTO], conforme al RETIE, a la NTC 2050, a las normas IEC aplicables, a los requisitos técnicos de conexión de [OPERADOR DE RED] y a las instrucciones del fabricante del inversor.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, proteger la garantía del equipo y asegurar que ningún inversor se conecte a la red sin autorización escrita.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en:

- Recepción, inspección, almacenamiento y preservación de inversores string, inversores centrales, estaciones de potencia (skid o contenedor con inversor, transformador y celdas) y sus accesorios.
- Manejo, transporte interno e izaje de inversores y estaciones de potencia.
- Montaje de inversores string sobre estructura, poste o soporte dedicado, y asentamiento de inversores centrales o estaciones de potencia sobre su fundación.
- Conexión DC (strings directos, cajas combinadoras o tableros de recombinación), conexión AC hasta el tablero de agrupamiento o el transformador, puesta a tierra y comunicaciones.
- Verificaciones previas al arranque, primer arranque con soporte del fabricante, configuración de parámetros de red aprobados, registro de números de serie y activación de garantía.

No incluye las cimentaciones, que se rigen por NES-OPE-PR-012; las cajas combinadoras, que se rigen por NES-OPE-PR-017; el tendido de cables, que se rige por NES-OPE-PR-015; el transformador y las celdas de media tensión, que se rigen por NES-OPE-PR-019; la malla de tierra y el SIPRA, que se rigen por NES-OPE-PR-020; el SCADA, que se rige por NES-OPE-PR-021; ni los ensayos de comisionado del generador y la energización de la planta, que se rigen por NES-OPE-PR-022 y NES-OPE-PR-023.

> NOTA: El inversor es el equipo de mayor valor unitario del lado de baja tensión y el que concentra las condiciones de garantía más estrictas. La mayoría de los fabricantes condicionan la garantía a la recepción documentada, al almacenamiento dentro de rango, al montaje según manual y a un primer arranque ejecutado o supervisado por su personal o por personal certificado por ellos.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / ART y PT | Análisis de trabajo seguro / análisis de riesgo del trabajo y permiso de trabajo. |
| PTE | Permiso de trabajo eléctrico, emitido por el responsable eléctrico con alcance, puntos de corte y responsable de la maniobra. |
| Inversor string | Inversor de potencia media que recibe directamente varios strings o pocas entradas DC, con varios seguidores MPPT, montado en campo cerca del arreglo. |
| Inversor central | Inversor de gran potencia que recibe las salidas de varias cajas combinadoras o tableros de recombinación, montado en sala, contenedor o skid. |
| Estación de potencia | Conjunto prefabricado en skid o contenedor que integra uno o varios inversores centrales, transformador elevador, celdas de media tensión y servicios auxiliares. |
| MPPT | Seguidor del punto de máxima potencia: circuito del inversor que ajusta la tensión de operación de un grupo de strings para extraer la máxima potencia. |
| Tensión DC máxima de entrada | Tensión que nunca debe superar la entrada del inversor, ni siquiera con la Voc del arreglo a la temperatura mínima del sitio. |
| Resistencia de aislamiento (Riso) | Resistencia entre los conductores activos DC y tierra. El inversor la mide antes de conectarse y no arranca si es inferior a su umbral. |
| Antiisla | Función del inversor que lo desconecta cuando la red se ausenta, ensayada según IEC 62116. |
| Parámetros de red | Ajustes de tensión, frecuencia, tiempos de desconexión, rampas, potencia activa y reactiva y soporte ante huecos, aprobados en el estudio de conexión. |
| Primer arranque | Primera puesta en marcha del inversor conectado a red, con la verificación de sus parámetros y el registro de su operación. |
| Desecante | Material higroscópico que el fabricante ubica en el embalaje o en el gabinete para absorber humedad durante el transporte y el almacenamiento. |
| Indicador de impacto / inclinación | Dispositivo adherido al embalaje que cambia de color si la carga sufrió un golpe o una inclinación superiores a su umbral. |
| Derrateo | Reducción automática de la potencia del inversor por temperatura, altitud o tensión fuera de rango, según curvas del fabricante. |
| Cinco reglas de oro | Cortar todas las fuentes, bloquear, verificar ausencia de tensión, poner a tierra cuando aplique y señalizar la zona. |
| LOTO | Bloqueo y etiquetado de dispositivos de desconexión, con candado y tarjeta de quien ejecuta el trabajo. |
| Dictamen RETIE | Documento emitido por organismo de inspección acreditado que declara la conformidad de la instalación con el RETIE. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento], a una altitud de [____] m s. n. m. Inversores, estaciones de potencia, cajas combinadoras y tableros se identifican según el plano general de implantación [N° de plano], el plano de estaciones de potencia [N° de plano] y los diagramas unifilares DC y AC [N° de plano].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

Manual de instalación, manual de operación y guía de puesta en marcha del fabricante del inversor y, para estaciones de potencia, manual de transporte, izaje e instalación de la estación.

Condiciones de garantía del fabricante del inversor y lista de verificación de instalación que el fabricante exige para validar la garantía.

Diagramas unifilares DC y AC, plano de fundación y de canalizaciones de la estación de potencia, plano de soporte de inversores string, arquitectura de comunicaciones — [N° de plano].

Estudio de conexión aprobado por [OPERADOR DE RED] y, si aplica, por el operador del sistema, con los parámetros de red que debe configurar el inversor — [__________].

Memoria de cálculo de dimensionamiento DC/AC: Voc máxima del string a la temperatura mínima del sitio, corriente por MPPT y relación DC/AC.

Certificados de conformidad de producto del inversor exigidos por el RETIE e informes de ensayo según IEC 62109-1, IEC 62109-2 e IEC 62116.

NES-OPE-PR-012 Obras civiles y cimentaciones; NES-OPE-PR-014 Conexionado DC y conectores MC4; NES-OPE-PR-015 Tendido de cables; NES-OPE-PR-017 Montaje de cajas combinadoras y tableros DC; NES-OPE-PR-019 Centros de transformación; NES-OPE-PR-020 Puesta a tierra y SIPRA; NES-OPE-PR-021 SCADA; NES-OPE-PR-022 Pruebas y comisionado del generador FV; NES-OPE-PR-023 Energización y puesta en servicio.

NES-CAL-PLN-002 Plan de calidad; NES-SST-PLN-001 Plan de emergencias; NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-SST-PR-003 Izaje de cargas con grúa.

## 5.2. Normativa aplicable

RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes: requisitos de producto e instalación, distancias de seguridad, certificación de producto y dictamen de inspección de la instalación antes de energizar.

NTC 2050 — Código Eléctrico Colombiano, artículo 690 (Sistemas solares fotovoltaicos), en los requisitos que el RETIE adopta.

Ley 1715 de 2014 — Integración de las energías renovables no convencionales al sistema energético nacional.

Resolución CREG 075 de 2021 — Disposiciones y procedimientos para la asignación de capacidad de transporte y la conexión al Sistema Interconectado Nacional.

Resolución CREG 174 de 2021 — Actividades de autogeneración a pequeña escala y generación distribuida, cuando el proyecto se enmarque en ella.

Procedimientos y requisitos técnicos de [OPERADOR DE RED] y, cuando aplique, del operador del sistema (XM) para pruebas, declaración y puesta en servicio.

IEC 62109-1 e IEC 62109-2 — Seguridad de los convertidores de potencia para sistemas fotovoltaicos.

IEC 62116 — Procedimiento de ensayo de las medidas de prevención de funcionamiento en isla de inversores conectados a la red.

IEC 62548 e IEC 60364-7-712 — Diseño de arreglos fotovoltaicos e instalaciones fotovoltaicas de baja tensión.

IEC 62446-1 — Documentación, ensayos de puesta en servicio e inspección de sistemas fotovoltaicos conectados a la red.

IEC 61724-1 — Monitoreo del desempeño de sistemas fotovoltaicos, para las señales del inversor hacia el SCADA.

ISO 6789 — Herramientas de apriete: requisitos y calibración de torquímetros.

Ley 1264 de 2008 (técnicos electricistas, CONTE); Ley 51 de 1986 y Ley 842 de 2003 (ingenieros, COPNIA).

Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019 — Estándares mínimos del SG-SST.

Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en el sector eléctrico; cinco reglas de oro.

Resolución 2400 de 1979 — Estatuto de seguridad industrial; arts. 388 a 392 (manejo manual de cargas) y arts. 398 a 447 (manejo y transporte mecánico de materiales).

Resolución 4272 de 2021 — Trabajo en alturas, cuando haya exposición a 2 m o más (techo de estaciones de potencia, plataformas).

Resolución 0491 de 2020 — Espacios confinados, cuando el diseño de la estación incluya fosos o sótanos de cables con esa condición.

Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo.

Decreto 1076 de 2015 (RESPEL); Resolución 2184 de 2019 (código de colores); Resolución 0472 de 2017 modificada por la Resolución 1257 de 2021 (RCD); Ley 1672 de 2013 (RAEE).

Licencia ambiental y Plan de Manejo Ambiental (PMA) del proyecto — [N° de resolución].

NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

Aprobar y divulgar el presente procedimiento y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.

Coordinar con [CLIENTE] y con el fabricante del inversor el cronograma de entregas, el soporte en sitio y la fecha del primer arranque.

Tramitar los RFI y las desviaciones frente al manual del fabricante, y obtener del fabricante la aceptación escrita de cualquier condición que pueda afectar la garantía.

Detener cualquier actividad que no cumpla este procedimiento, el diseño o la instrucción del fabricante.

## 6.2. Responsable eléctrico (ingeniero con matrícula COPNIA vigente)

Verificar que la tensión DC máxima del arreglo, las corrientes por MPPT y las secciones de cable son compatibles con la ficha del inversor antes de conectar.

Emitir los permisos de trabajo eléctrico, aplicar las cinco reglas de oro y dirigir las verificaciones previas al arranque.

Validar que los parámetros de red configurados coinciden con el estudio de conexión aprobado y firmarlos.

Autorizar por escrito el primer arranque, solo dentro de la secuencia de NES-OPE-PR-023 y con dictamen RETIE y autorización de [OPERADOR DE RED].

## 6.3. Supervisor / capataz de frente de inversores

Asignar tareas, dirigir la cuadrilla y verificar el cumplimiento del método descrito.

Elaborar con los trabajadores el ATS/ART diario y la charla de inicio de turno.

Coordinar con el supervisor de izaje las maniobras de estaciones de potencia según NES-SST-PR-003.

Diligenciar los registros del frente el mismo día.

## 6.4. Oficiales electricistas (matrícula CONTE vigente)

Ejecutar el montaje, la preparación de cables, el crimpado de terminales, el conexionado y el apriete controlado según este documento y el manual del fabricante.

Verificar polaridad y tensión antes de cada conexión DC y trazar marca de torque en cada unión.

## 6.5. Técnico del fabricante del inversor (o certificado por él)

Supervisar o ejecutar las verificaciones de instalación que exige la garantía, cargar el firmware y la configuración aprobados y ejecutar el primer arranque.

Entregar el informe de puesta en marcha y el registro de garantía.

## 6.6. Responsable de calidad (QA/QC)

Controlar el cumplimiento del PIE definido en NES-CAL-PLN-002 y liberar cada inversor mediante los formatos de este documento.

Mantener el registro de números de serie, ubicación, firmware y parámetros de cada inversor.

## 6.7. Responsable SST (con licencia en SST vigente) y supervisor de izaje

Verificar permisos, EPP dieléctrico y de arco vigente, herramienta aislada, delimitación de áreas y competencia del personal.

Verificar el plan de izaje, la certificación del operador, del aparejador y del equipo, y la delimitación del radio de maniobra según NES-SST-PR-003.

Aplicar el protocolo de tormenta eléctrica y liderar la atención de emergencias.

## 6.8. Coordinador de trabajo en alturas

Evaluar y autorizar los trabajos en techo de estación de potencia, sobre plataformas o en soportes altos, conforme a la Resolución 4272 de 2021.

## 6.9. Responsable ambiental

Asegurar el cumplimiento del PMA, la gestión de embalajes voluminosos, desecantes, RAEE y la prevención de derrames de aceite durante el izaje y el montaje.

## 6.10. Trabajadores

Cumplir este procedimiento y participar en el ATS/ART y en la charla diaria.

Usar correctamente el EPP y las herramientas asignadas; no permanecer bajo cargas suspendidas.

Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS. Reportar a la ARL y al COPASST o vigía SST cualquier condición insegura.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Responsable eléctrico (COPNIA), supervisor de frente, oficiales electricistas (CONTE), técnico del fabricante del inversor, QA/QC, responsable SST, supervisor de izaje, operador de grúa y aparejador certificados, coordinador de alturas. |
| Materiales | Montaje | Soportes y tornillería del plano de detalle o del fabricante; anclajes de la fundación; láminas de nivelación; sellos de canalización y espuma o masilla cortafuego para pasos de cable. |
| Materiales | Conexión | Terminales de compresión y bimetálicos de la sección de diseño; conectores DC de la referencia del inversor; pasta antioxidante; marquillas; pintura indeleble para marca de torque; cable de comunicaciones apantallado y conectores. |
| Herramientas | Apriete y conexión | Torquímetros y destornillador dinamométrico calibrados según ISO 6789; crimpadora hidráulica con dados; pelacables; herramienta del fabricante del conector DC; herramienta aislada con marcado vigente. |
| Herramientas | Montaje | Taladro, nivel de burbuja o nivel láser, flexómetro, llaves, gatos hidráulicos de nivelación cuando el fabricante los admita. |
| Equipos | Izaje | Grúa del tamaño del plan de izaje; balancín o viga separadora y eslingas certificadas; grilletes; vientos; montacargas o manipulador telescópico para inversores string. |
| Equipos | Medida | Multímetro CAT III o superior para la tensión DC máxima; pinza amperimétrica AC/DC; megóhmetro de 1.000 V DC o más; secuencímetro de fases; detector de tensión AC y DC; telurómetro o micro-ohmímetro; analizador de red cuando el proyecto lo exija; computador con el software del fabricante. |
| Equipos | LOTO | Kit LOTO, pinzas multibloqueo, tarjetas, caja de bloqueo. |
| EPP | Trabajo eléctrico | Guantes dieléctricos de clase acorde con la tensión, con sobreguante; calzado dieléctrico; careta, capucha y ropa con la categoría de arco del análisis de riesgo; sin elementos metálicos personales. |
| EPP | Básico e izaje | Casco con barbuquejo, gafas UV, botas con puntera, chaleco reflectivo, guantes, protección auditiva, cubrenuca, protector solar, polainas en zonas con ofidios, arnés y línea de vida para alturas. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

Personal calificado, autorizado y con inducción en riesgo eléctrico y en este procedimiento; técnico del fabricante programado para las etapas que exige la garantía.

ATS/ART, charla de inicio de turno, permiso de trabajo, permiso de trabajo eléctrico, permiso de izaje y permiso de alturas, según la tarea.

Manual vigente del fabricante del inversor en el frente y lista de verificación de garantía del fabricante.

Fundaciones o soportes terminados y liberados según NES-OPE-PR-012, con concreto a la resistencia de diseño para recibir carga.

Canalizaciones de llegada DC, AC, tierra y comunicaciones terminadas y despejadas según NES-OPE-PR-015.

Malla de tierra con punto de conexión disponible según NES-OPE-PR-020.

Compatibilidad verificada por el responsable eléctrico: Voc máxima del string a la temperatura mínima de [municipio] menor que la tensión DC máxima de entrada del inversor; corriente por MPPT dentro del límite; derrateo por altitud y temperatura del sitio revisado contra las curvas del fabricante.

Torquímetros e instrumentos con calibración vigente.

Condiciones climáticas aptas para izaje (viento dentro del límite del plan de izaje) y para abrir gabinetes (sin lluvia).

> ALTO: Si la Voc máxima calculada del arreglo, a la temperatura mínima registrada del sitio, supera la tensión DC máxima de entrada del inversor, no se conecta. La sobretensión DC destruye la etapa de entrada y no la cubre la garantía.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

Se delimitan y señalizan: el patio de almacenamiento de inversores, la zona de descargue, el radio de maniobra de la grúa con su zona de exclusión, la fundación de cada estación, los puntos de montaje de inversores string y el punto de acopio de residuos. Todo inversor o estación con algún circuito conectado se trata como energizado y su zona se demarca con señal de riesgo eléctrico.

### 8.2.2. Ingreso de personal

Evaluar condiciones del área y verificar que no haya trabajos simultáneos incompatibles bajo la carga o en el mismo circuito.

Diligenciar los permisos que exige la tarea.

Ubicar equipos de emergencia e inspeccionar el EPP.

### 8.2.3. Ingreso de vehículos y equipos

Preoperacional de grúa, montacargas, camabaja y vehículos; certificados vigentes del equipo y del operador.

Verificar la capacidad portante del terreno de apoyo de la grúa y de la vía de acceso a la fundación; usar placas de apoyo bajo los estabilizadores.

Circulación solo por rutas autorizadas; no transitar sobre canalizaciones abiertas ni sobre cables tendidos.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Recepción e inspección

La recepción se registra en el formato NES-OPE-F-110 y, cuando el fabricante lo exija, en su propio formato de recepción.

1. Antes de descargar, inspeccionar embalaje, contenedor o skid: golpes, deformaciones, humedad, sellos de transporte e indicadores de impacto y de inclinación. Si un indicador está activado, fotografiar, dejar constancia en la remisión del transportador antes de firmar y notificar al fabricante en el plazo que fije su contrato.
2. Verificar la placa de características: referencia, número de serie, potencia, tensión DC máxima, tensión y frecuencia AC (60 Hz), grado IP y fecha de fabricación.
3. Verificar los documentos de entrega: certificado de conformidad de producto exigido por el RETIE, protocolo de pruebas de fábrica, manuales, lista de empaque, llaves y accesorios.
4. Inspeccionar el exterior sin abrir el gabinete en ambiente húmedo: pintura, puertas, rejillas de ventilación, ventiladores visibles, prensaestopas y tapas de conectores DC.
5. En estaciones de potencia, verificar además el estado del transformador (nivel y fugas de aceite, indicadores), de las celdas y del contenedor, en coordinación con NES-OPE-PR-019.
6. Registrar números de serie del inversor y de sus módulos o tarjetas principales cuando la placa los exponga, para el registro de NES-OPE-F-119.
7. Rotular el estado: aceptado, en cuarentena o rechazado.

#### 8.2.4.2. Almacenamiento y preservación

| Aspecto | Requisito |
|---|---|
| Lugar | Bodega cerrada o contenedor seco, ventilado, sobre estibas o superficie firme y nivelada, fuera de zonas inundables. Las estaciones de potencia se almacenan sobre apoyos nivelados o sobre su fundación, cerradas. |
| Posición | La que indique el embalaje; los inversores string en su caja, sin apoyarlos sobre los conectores. |
| Apilado | Máximo número de niveles indicado en el embalaje. |
| Condiciones | Temperatura y humedad dentro del rango del fabricante. Valores típicos de fabricante: entre -40 °C y +65 °C, y humedad relativa entre 5% y 90% sin condensación, en ambiente sin polvo ni gases corrosivos; verificar contra el manual del equipo del proyecto. |
| Desecante | Se conserva el desecante de fábrica y se reemplaza en el intervalo del fabricante; valor de referencia: cada 6 a 12 meses o cuando cambie el indicador de saturación. |
| Calefacción | En estaciones de potencia almacenadas largo tiempo, energizar la calefacción anticondensación con fuente auxiliar si el fabricante lo exige. |
| Inspección | Mensual (criterio interno), con registro en NES-OPE-F-111: embalaje, humedad, condensación, plagas, ofidios, roedores y estado del desecante. |
| Tiempo máximo | El que fije el fabricante sin acciones adicionales; superado, se ejecuta la inspección previa al montaje que él indique — [__________]. |

En [departamento] con alta humedad o ambiente salino (costa Caribe y Pacífico), se evita abrir los gabinetes en patio y se verifica la categoría de corrosividad del sitio prevista en el diseño (ISO 9223) contra la especificación del equipo.

#### 8.2.4.3. Izaje y manejo

El izaje de inversores centrales y estaciones de potencia se rige por NES-SST-PR-003 y por el manual de transporte e izaje del fabricante. Se registra en NES-OPE-F-112.

1. Elaborar el plan de izaje con la masa del equipo de la placa o del manual, la posición del centro de gravedad marcada en el equipo, el radio de trabajo, la configuración de la grúa y el factor de utilización.
2. Izar solo desde los puntos de izaje del fabricante, con el balancín o la viga separadora y las eslingas que él indique. Ángulo de eslinga respecto de la horizontal no menor a 60° cuando no se usa balancín, o el que indique el fabricante (valor de referencia de práctica de izaje).
3. No izar ni empujar desde rejillas, puertas, techos, bandejas de cables, radiadores del transformador ni aisladores.
4. Usar vientos para controlar el giro; nadie bajo la carga ni entre la carga y un objeto fijo.
5. Los inversores string se manejan en su embalaje con montacargas o entre dos o más personas sin superar 25 kg por persona (Res. 2400 de 1979, art. 392); para su montaje se usan las asas o los puntos de izaje del fabricante.
6. Mantener la verticalidad que exige el fabricante durante todo el transporte interno; no inclinar ni voltear el equipo.
7. Suspender el izaje con viento por encima del límite del plan, con lluvia intensa o ante tormenta eléctrica.

> ALTO: Ningún izaje de estación de potencia o inversor central sin plan de izaje aprobado, operador y aparejador certificados, área delimitada y supervisor de izaje presente.

#### 8.2.4.4. Fundación, soporte y asentamiento

Inversor central y estación de potencia:

1. Verificar la fundación contra el plano: cotas, dimensiones, nivelación, posición de anclajes, ventanas y ductos de cables, foso o bandeja de contención de aceite del transformador y drenaje.
2. Verificar la planitud del apoyo. Valor típico de fabricante: los apoyos estándar compensan desniveles de hasta ±20 mm; verificar contra el manual del equipo del proyecto.
3. Asentar el equipo de modo que su peso quede repartido por igual en todos los apoyos, con el equipo horizontal, y ajustar los apoyos o las láminas de nivelación según el fabricante.
4. Verificar la altura libre entre el equipo y el terreno que exige el fabricante para ventilación, inundación y entrada de cables.
5. Fijar el equipo a la fundación con los anclajes y el torque del plano; trazar marca de torque.
6. Sellar los pasos de cables entre la fundación y el equipo contra agua, polvo, roedores y ofidios.

Inversor string:

1. Montar sobre el soporte del plano (estructura, poste o bastidor dedicado), en posición vertical. Si el fabricante lo admite, inclinación hacia atrás hasta el límite de su manual; valor típico de fabricante: no menos de 15° respecto de la horizontal y nunca inclinado hacia adelante; verificar contra el manual del equipo del proyecto.
2. Fijar el soporte del fabricante con la tornillería y el torque indicados, colgar el inversor y asegurar los tornillos o pasadores antirrobo y antilevantamiento.
3. Proteger el inversor del sol directo y de la lluvia directa cuando el fabricante lo recomiende, con techo o con la sombra de la estructura, sin obstruir la ventilación.
4. Ubicar el inversor a la altura que permita leer el indicador, operar el seccionador y mantenerlo, y por encima del nivel de inundación.
5. Registrar en NES-OPE-F-113 (string) o NES-OPE-F-114 (central o estación).

#### 8.2.4.5. Distancias de ventilación y entorno

Las distancias las fija el manual del fabricante y se verifican en campo con flexómetro. Como referencia, los manuales de inversores string consultados indican:

| Aspecto | Valor típico de fabricante (verificar contra el manual del equipo del proyecto) |
|---|---|
| Separación entre inversores contiguos | 500 mm o más |
| Espacio libre arriba y abajo del inversor | 500 mm o más |
| Espacio lateral mínimo con restricción de sitio | 200 mm, cuando el fabricante lo admite |
| Temperatura ambiente alta | Por encima de 45 °C se aumentan las separaciones según el fabricante |
| Humedad de operación | Hasta 90% a 95% sin condensación, según fabricante |
| Disposición en filas | No montar un inversor encima de otro de modo que el aire caliente de uno entre al otro |

Para inversores centrales y estaciones de potencia, se respetan las distancias a otros equipos, a cercas y a la vegetación que indique el fabricante para la entrada y salida de aire, para la apertura completa de puertas y para el acceso de mantenimiento, además de las distancias de seguridad del RETIE.

Altitud: en plantas ubicadas en zonas altas de Colombia se verifica la curva de derateo por altitud del fabricante y, para equipos de media tensión integrados, la corrección por altitud del aislamiento. Temperatura: en zonas cálidas se verifica la curva de derateo por temperatura y que la orientación de la estación no dirija la descarga de aire caliente hacia la toma de otra estación.

#### 8.2.4.6. Conexión DC

1. Abrir el seccionador DC del inversor y bloquearlo; abrir el seccionador de cada caja combinadora o tablero aguas arriba, según NES-OPE-PR-017, y verificar ausencia de corriente.
2. Verificar la identificación de cada string o principal DC contra el unifilar y contra la asignación de entradas y MPPT del inversor. Los strings de un mismo MPPT deben tener igual número de módulos, igual orientación e igual tipo, salvo que el diseño indique otra cosa.
3. Medir en el extremo del cable, antes de conectar, la polaridad y la Voc de cada string o principal. Comparar con el valor esperado y con los vecinos; verificar que ninguna Voc supera la tensión DC máxima de entrada.
4. Medir la tensión entre cada polo y tierra: una lectura anormal indica falla de aislamiento o polo a tierra, y no se conecta.
5. Inversor string: conectar con los conectores DC de la referencia compatible con el inversor, confeccionados según NES-OPE-PR-014. Los conectores no compatibles se reemplazan; no se acoplan referencias distintas.
6. Inversor central: conectar los principales DC a las barras o bornes de entrada con terminales de compresión o bimetálicos, tornillería del fabricante y torque calibrado; trazar marca de torque.
7. Sellar los prensaestopas o las entradas de cable; tapar las entradas DC sin uso con los tapones del fabricante.
8. Ejecutar el ensayo de resistencia de aislamiento del circuito DC por el método de la IEC 62446-1, con el inversor desconectado del circuito ensayado. Para tensión de sistema mayor a 500 V la norma establece ensayo a 1.000 V con valor mínimo de 1 MΩ; se confirma la tabla de la edición vigente.
9. Registrar en NES-OPE-F-115.

> ALTO: Una polaridad invertida en una entrada DC puede dañar el inversor de forma permanente. Toda entrada se mide antes de conectar, aunque el string ya haya sido medido en la caja combinadora.

#### 8.2.4.7. Conexión AC

1. Verificar que el interruptor AC aguas abajo (tablero de agrupamiento o celda del transformador) está abierto, bloqueado y etiquetado, y que el lado de media tensión del transformador está desenergizado y bloqueado según NES-OPE-PR-019 y NES-SST-PR-001.
2. Verificar sección, material, número de conductores por fase y tensión asignada contra el unifilar AC.
3. Preparar los cables respetando el radio de curvatura y sin tensión sobre los bornes; crimpar terminales con el dado y la herramienta de la sección; en aluminio, terminal bimetálico o el que indique el fabricante del inversor.
4. Conectar las fases en la secuencia del unifilar, el neutro si el diseño lo usa y el conductor de protección (PE).
5. Apretar al torque del fabricante. Valores de bornes AC en inversores string varían con el modelo y la sección; se transcriben del manual a la tabla de torques del proyecto antes de iniciar — [__________].
6. Verificar la secuencia de fases con secuencímetro en la primera energización del lado AC, antes de cerrar el interruptor del inversor.
7. Ensayar la resistencia de aislamiento del cable AC con el inversor desconectado, con la tensión de ensayo que fije el procedimiento de cables del proyecto (NES-OPE-PR-015).
8. Sellar las entradas, trazar marcas de torque y registrar en NES-OPE-F-116.

#### 8.2.4.8. Puesta a tierra

1. Conectar el borne de tierra del inversor o de la estación al conductor de tierra que viene de la malla, con la sección del diseño, terminal de compresión y torque del fabricante.
2. En inversores string, conectar además el conductor PE del cable AC. Los manuales de fabricante consultados indican que el punto de tierra adicional del chasis no reemplaza al PE del cable AC: ambos se conectan.
3. En estaciones de potencia, verificar la unión equipotencial entre inversor, transformador, celdas, contenedor o skid y malla, según el diseño del SPT y NES-OPE-PR-020.
4. Verificar la puesta a tierra del arreglo DC que exija el diseño (funcional o de protección) y que coincide con la configuración del inversor.
5. Medir continuidad y registrar en NES-OPE-F-117.

#### 8.2.4.9. Comunicaciones

1. Tender el cable de comunicaciones por canalización separada de los cables de potencia, o con la separación del diseño, según NES-OPE-PR-021.
2. Usar cable apantallado para buses seriales (por ejemplo RS-485) y conectar la pantalla a tierra en un solo extremo, salvo que el fabricante indique otra cosa; respetar la resistencia de terminación al final del bus.
3. En fibra óptica, respetar el radio de curvatura y proteger los conectores con tapón hasta la conexión.
4. Asignar direcciones o IP de cada inversor según la arquitectura aprobada y registrarlas en NES-OPE-F-117 y NES-OPE-F-119.
5. Verificar comunicación con el controlador de planta o el registrador antes del primer arranque: lectura de estado, alarmas y medidas.

#### 8.2.4.10. Verificaciones previas al arranque

Antes del primer arranque se ejecutan y registran en NES-OPE-F-118, como mínimo:

1. Montaje mecánico, fijación, distancias de ventilación y sellos conformes.
2. Ausencia de herramientas, residuos, desecante suelto y polvo dentro del gabinete; filtros y rejillas despejados; ventiladores giran libres.
3. Torques aplicados y marcados en DC, AC y tierra; muestra QA/QC conforme.
4. Polaridad y Voc de todas las entradas DC conformes; ninguna supera la tensión DC máxima.
5. Resistencia de aislamiento DC y AC conforme.
6. Puesta a tierra conforme y continuidad medida.
7. Tensión de red en bornes AC dentro del rango del inversor y secuencia de fases correcta, medida con el lado AC energizado y el inversor aún desconectado.
8. Comunicaciones operativas.
9. Fusibles internos y protecciones del inversor verificados según el fabricante.
10. Parámetros de red cargados y verificados contra el estudio de conexión (numeral 8.2.4.12).
11. Rotulado y señalización de riesgo eléctrico según el RETIE.
12. Lista de verificación de garantía del fabricante diligenciada.

#### 8.2.4.11. Primer arranque con soporte del fabricante

El primer arranque se ejecuta solo dentro de la secuencia de energización de NES-OPE-PR-023, con la autorización escrita del responsable eléctrico y de [CLIENTE], con dictamen de inspección RETIE de la instalación y con la autorización de [OPERADOR DE RED] para inyectar.

1. Confirmar la presencia del técnico del fabricante o la autorización escrita del fabricante para que lo ejecute personal certificado por él.
2. Cargar o verificar el firmware aprobado para el proyecto.
3. Cerrar el lado AC (red disponible) y verificar en el inversor la lectura de tensión y frecuencia de red.
4. Cerrar los circuitos DC de forma gradual, entrada por entrada o MPPT por MPPT cuando el diseño lo permita, observando en el inversor la tensión de cada entrada, la resistencia de aislamiento medida por el equipo y la ausencia de alarmas.
5. Dar la orden de arranque. El inversor ejecuta sus autoverificaciones (aislamiento, red) y se sincroniza. Registrar hora, tiempo de conexión y potencia inicial.
6. Verificar con pinza las corrientes de entrada por MPPT y de salida por fase; comparar entre inversores del mismo tipo en las mismas condiciones.
7. Verificar el registro de eventos: sin alarmas activas ni advertencias repetidas.
8. Mantener el inversor en observación durante [____] horas de operación continua (criterio a definir con el fabricante y [CLIENTE]), con revisión termográfica de las conexiones cuando el proyecto lo exija.
9. Firmar el acta de primer arranque en NES-OPE-F-118 y obtener el informe del fabricante.

> NOTA: Los ensayos de desempeño del generador, las curvas I-V, la termografía de campo y las pruebas de la planta con el controlador se rigen por NES-OPE-PR-022 y NES-OPE-PR-023.

#### 8.2.4.12. Parámetros de red

Los parámetros de red del inversor no se eligen en campo. Se toman del estudio de conexión aprobado y de los requisitos técnicos de [OPERADOR DE RED], en el marco de la Resolución CREG 075 de 2021 o de la Resolución CREG 174 de 2021 según el tipo de proyecto, y, cuando aplique, de los requisitos del operador del sistema.

1. El responsable eléctrico entrega al técnico del fabricante la tabla de parámetros aprobada — [__________] — con: tensión y frecuencia nominales (60 Hz), límites y tiempos de desconexión por tensión y frecuencia, tiempo de reconexión, rampas de potencia, límite de potencia activa, modo de control de potencia reactiva o factor de potencia, soporte ante huecos de tensión y protección antiisla.
2. Cuando el inversor no tenga un perfil de red preconfigurado que coincida, se configura un perfil personalizado con los valores aprobados; no se usa el perfil de otro país sin verificar cada valor.
3. Se protege la configuración con contraseña de instalador y se exporta el archivo de parámetros de cada inversor.
4. El responsable eléctrico compara parámetro por parámetro el archivo exportado contra la tabla aprobada y firma la verificación en NES-OPE-F-119.
5. Todo cambio posterior de parámetros requiere solicitud escrita, aprobación del responsable eléctrico y de [CLIENTE] y nuevo registro.

#### 8.2.4.13. Registro de números de serie y garantía

1. Registrar en NES-OPE-F-119, por inversor: ubicación (bloque, estación, posición), referencia, número de serie, firmware, dirección de comunicación, fecha de primer arranque y técnico del fabricante.
2. Registrar el equipo en el sistema de garantía del fabricante en el plazo que él fije, con los datos del [PROPIETARIO].
3. Archivar fotografías del equipo instalado, de la placa, de las conexiones con marca de torque y de las distancias de ventilación.
4. Entregar a [CLIENTE] el dossier del inversor: recepción, almacenamiento, montaje, conexiones, parámetros, acta de arranque, informe del fabricante y certificado de garantía.

#### 8.2.4.14. No conformidades

Equipo con indicador de impacto o inclinación activado, daño de transporte o humedad interna: cuarentena y disposición escrita del fabricante antes de montar.

Almacenamiento fuera de rango o por encima del tiempo máximo: inspección del fabricante antes de energizar.

Voc por encima de la tensión DC máxima, polaridad invertida o aislamiento bajo: no se conecta; se corrige y se repite la medición.

Distancias de ventilación o posición de montaje fuera del manual: corrección o aceptación escrita del fabricante.

Parámetros de red distintos de los aprobados: el inversor se detiene y se reconfigura antes de seguir inyectando.

Cambio de referencia de inversor, firmware o perfil de red: requiere aprobación escrita del ingeniero responsable del diseño eléctrico y queda en el RFI log.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Certificación del inversor | Certificado de conformidad de producto; ensayos IEC 62109-1, IEC 62109-2 e IEC 62116 | RETIE / IEC |
| Estado a la recepción | Sin daño, indicadores sin activar, sin humedad; placa conforme (60 Hz) | Manual del fabricante |
| Almacenamiento | Dentro del rango de temperatura, humedad y tiempo del fabricante | Manual del fabricante |
| Izaje | Solo por puntos del fabricante, con plan de izaje aprobado | NES-SST-PR-003 / fabricante |
| Asentamiento | Equipo horizontal; carga repartida; desnivel dentro de lo que compensan los apoyos | Manual del fabricante |
| Posición del inversor string | Vertical o inclinado hacia atrás dentro del límite del fabricante; nunca hacia adelante | Manual del fabricante |
| Distancias de ventilación | Las del manual del fabricante, medidas en campo | Manual del fabricante |
| Tensión DC por entrada | Voc máxima a la temperatura mínima del sitio menor que la tensión DC máxima de entrada | Ficha técnica / memoria |
| Polaridad DC | 100% de entradas coincidentes con el unifilar antes de conectar | IEC 62446-1 |
| Resistencia de aislamiento DC | Según tabla de la IEC 62446-1 vigente; tensión de sistema mayor a 500 V: ensayo a 1.000 V y mínimo 1 MΩ | IEC 62446-1 |
| Torques DC, AC y tierra | Valor del fabricante en el 100% de uniones; marca de torque | Manual del fabricante |
| Secuencia de fases | Coincidente con el unifilar AC | Unifilar AC |
| Puesta a tierra | PE del cable AC y tierra de chasis conectados; continuidad conforme | Manual del fabricante / NES-OPE-PR-020 |
| Comunicaciones | Inversor visible en el controlador con estado, alarmas y medidas | NES-OPE-PR-021 |
| Parámetros de red | Idénticos a la tabla aprobada del estudio de conexión, verificados parámetro por parámetro | [OPERADOR DE RED] / CREG 075 de 2021 o CREG 174 de 2021 |
| Primer arranque | Sincronización sin alarmas; corrientes coherentes entre inversores del mismo tipo | Fabricante / este procedimiento |

## 8.4. Documentación para mantener y registrar

Anexos NES-OPE-F-110 a NES-OPE-F-119 de este procedimiento.

Plan de izaje, permisos de trabajo, permisos de trabajo eléctrico, permisos de alturas y ATS/ART.

Certificados de calibración de torquímetros, instrumentos y equipos de medida; certificados de grúa, eslingas, operador y aparejador.

Certificados de producto, protocolos FAT, manuales, informe de puesta en marcha del fabricante, archivos de parámetros exportados y certificados de garantía.

Tabla de torques del proyecto aprobada por el responsable eléctrico.

## 8.5. Control de calidad

QA/QC verifica el 100% de los inversores en recepción, montaje, conexiones, puesta a tierra, comunicaciones, verificaciones previas y parámetros, y aplica muestreo de torque en el 10% de las uniones DC y AC de inversores string por bloque y en el 100% de las uniones de potencia de inversores centrales (criterio interno). Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación que no afecta calidad, prestación ni seguridad, por ejemplo rótulo incompleto. | Registro y cierre. |
| 2 | Requiere rehacer una conexión, resellar una entrada o corregir una distancia con el método de este procedimiento. | Corrección por la cuadrilla y reinspección. |
| 3 | Afecta la seguridad eléctrica, la conexión a la red o la garantía: daño de transporte, humedad interna, sobretensión DC, polaridad invertida, parámetros de red no aprobados. | Suspensión, consulta al diseñador eléctrico y al fabricante, aprobación escrita antes de actuar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS/ART y la charla diaria, verifica que las áreas intervenidas estén señalizadas y demarcadas y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre características del proyecto, riesgo eléctrico en DC y AC, arco eléctrico, izaje de cargas, medidas de control, puntos de encuentro y uso correcto del EPP.

## 9.1. Reglas de oro

**SIEMPRE** trataré todo inversor con strings o red conectados como energizado por ambos lados.

**SIEMPRE** aplicaré las cinco reglas de oro antes de intervenir un inversor (Res. 5018 de 2019).

**NUNCA** abriré un gabinete de inversor sin esperar el tiempo de descarga de condensadores que indica el fabricante y sin verificar ausencia de tensión.

**NUNCA** conectaré una entrada DC sin medir antes su polaridad y su tensión.

**NUNCA** me ubicaré bajo una carga suspendida ni entre la carga y un objeto fijo.

**NUNCA** cambiaré un parámetro de red sin autorización escrita.

**NUNCA** arrancaré un inversor sin dictamen RETIE, sin autorización escrita del responsable eléctrico y de [CLIENTE] y sin la autorización de [OPERADOR DE RED].

**SIEMPRE** usaré guantes dieléctricos vigentes, careta y ropa de arco al intervenir circuitos energizados.

**SIEMPRE** suspenderé la actividad ante lluvia o tormenta eléctrica y me dirigiré al refugio o punto de encuentro.

## 9.2. Energía almacenada y riesgo de arco

Los inversores tienen condensadores en el bus DC que conservan tensión peligrosa después de desconectar ambos lados. Antes de abrir el gabinete se espera el tiempo indicado en la placa o el manual del fabricante y se verifica ausencia de tensión en el bus DC y en los bornes AC con detector probado. Se respetan las distancias de seguridad del RETIE, y la categoría del EPP de arco la define el análisis de riesgo de arco del proyecto, con referencia técnica en NFPA 70E.

## 9.3. Condiciones climáticas de [departamento]

Tormenta eléctrica: ante el aviso o el primer trueno, suspender izajes y toda intervención eléctrica, cerrar gabinetes, alejarse de estaciones, estructuras y conductores y dirigirse al refugio. Se reanuda solo con autorización del responsable SST.

Viento: suspender el izaje cuando la velocidad supere el límite del plan de izaje o de la tabla de carga de la grúa.

Lluvia: no abrir gabinetes; proteger cables y entradas con tapón y bolsa sellada.

Calor y radiación: hidratación, sombra, pausas activas y rotación; las superficies metálicas expuestas al sol se manipulan con guante.

Ofidios y roedores: antes de abrir embalajes, gabinetes, fosos o canalizaciones, inspeccionar con linterna y herramienta, sin introducir las manos.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado al frente | Colisión, volcamiento, caídas al mismo nivel. | Conductores autorizados; vías y velocidades del proyecto; cinturón obligatorio. |
| 2. Descargue y recepción | Caída de la carga, atrapamiento, golpes. | Plan de izaje; equipo certificado; área delimitada; nadie bajo la carga; vientos. |
| 3. Izaje de inversor central o estación | Volcamiento de grúa, caída de la carga, contacto con líneas energizadas. | NES-SST-PR-003; terreno verificado; placas de apoyo; distancias a líneas según RETIE; supervisor de izaje; límite de viento. |
| 4. Manejo de inversores string | Sobreesfuerzo, atrapamiento de manos. | Montacargas o dos personas; máximo 25 kg por persona (Res. 2400 de 1979, art. 392); guantes. |
| 5. Montaje en soporte o asentamiento | Golpes, atrapamiento, caída del equipo. | Equipo asegurado antes de soltar; herramienta en buen estado; manos fuera de puntos de pellizco. |
| 6. Trabajo en techo de estación o plataforma | Caída a distinto nivel. | Permiso de alturas; arnés y punto de anclaje certificado (Res. 4272 de 2021). |
| 7. Conexión DC | Choque eléctrico, arco, polaridad invertida. | PTE; seccionadores abiertos y bloqueados; corriente cero verificada; polaridad y Voc medidas; EPP dieléctrico y careta. |
| 8. Conexión AC | Choque eléctrico, retorno de tensión desde la red o el transformador. | LOTO en el interruptor AC y en el lado MT; verificación de ausencia de tensión; puesta a tierra temporal cuando aplique. |
| 9. Apertura de gabinetes | Descarga de condensadores, arco. | Tiempo de descarga del fabricante; detector probado antes y después; EPP de arco. |
| 10. Ensayos de aislamiento | Choque eléctrico, descarga capacitiva. | Inversor desconectado del circuito ensayado; descargar el circuito al terminar; área delimitada. |
| 11. Primer arranque | Arco, falla de equipo, reenergización con personal en zona. | Zona despejada; secuencia de NES-OPE-PR-023; técnico del fabricante; EPP de arco; comunicación por radio. |
| 12. Exposición ambiental | Radiación UV, estrés térmico, ofidios. | Ropa manga larga, cubrenuca, protector solar, hidratación, sombra, pausas; polainas. |
| 13. Tormenta eléctrica, lluvia y viento | Descarga atmosférica, choque eléctrico, caída de la carga. | Suspender; cerrar gabinetes; refugio o punto de encuentro. |
| 14. Orden, aseo y residuos | Tropiezos, cortes, contaminación. | Embalajes retirados el mismo día; separación de residuos; área despejada al cierre. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Aire | Emisiones y ruido de grúas y vehículos | Equipos con revisión técnico-mecánica y mantenimiento al día; motores apagados en reposo; humectación de vías. |
| Suelo | Embalajes voluminosos | Madera, cartón, plásticos, espumas y zunchos separados con el código de colores de la Res. 2184 de 2019 y entregados a gestor autorizado para aprovechamiento; la madera tratada se gestiona según su condición. |
| Suelo | Retazos de cable y terminales | Recogidos el mismo día, pesados y almacenados como aprovechable; entrega a gestor autorizado. |
| Suelo | Equipos o tarjetas retirados | Componentes electrónicos sustituidos que no devuelva el fabricante se gestionan como RAEE según la Ley 1672 de 2013. |
| Suelo | Aceite del transformador de la estación | Inspección de fugas en recepción; kit antiderrame durante el izaje; foso o bandeja de contención operativo; derrames gestionados como RESPEL según el Decreto 1076 de 2015. |
| Suelo | RESPEL | Trapos con grasa o pasta antioxidante, aerosoles, envases de pintura y desecantes contaminados en recipientes rotulados; entrega a gestor autorizado con certificado. |
| Suelo | RCD | Gestión según Res. 0472 de 2017 modificada por Res. 1257 de 2021. |
| Flora y fauna | Intervención de hábitat | Trabajar solo en áreas liberadas; sellar pasos de cables contra fauna; reporte de fauna para rescate según PMA. |
| Agua | Escorrentía | Drenaje de la fundación operativo; sin vertimientos de aceite ni de lavado de equipos. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener la actividad y asegurar la zona: detener el izaje y bajar la carga si es seguro; desconectar el inversor por los dispositivos de maniobra AC y DC desde una posición segura; alejar al personal.
2. Notificar al responsable SST y al responsable eléctrico de Neptuno Energy Services y al interlocutor de [CLIENTE]; si hay energía en la red de media tensión, notificar a la sala de control.
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, extintor en cada frente).
4. Incidente grave: activar la línea 123 y el traslado al centro asistencial definido; notificar a la ARL.
5. Reportar el evento y realizar la investigación según Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Incendio o humo en inversor o estación de potencia

No abrir puertas del gabinete ni del contenedor con humo en su interior.

Desconectar el lado AC desde el interruptor aguas abajo o la celda de media tensión y los seccionadores DC aguas arriba, desde fuera del equipo; recordar que el lado DC sigue con tensión mientras haya luz.

Usar extintor apto para equipo eléctrico energizado solo en conato; nunca agua sobre equipo energizado. Si el fuego avanza o involucra el transformador, evacuar a la distancia del plan de emergencias y activar el apoyo externo.

## 12.2. Caída o volcamiento de carga durante el izaje

Detener la maniobra, alejar al personal del radio de la grúa y no intentar sostener la carga. Asegurar la grúa, evaluar daños y lesionados y no reanudar sin investigación y nuevo plan de izaje. Notificar al fabricante si el equipo cayó o golpeó.

## 12.3. Choque eléctrico, arco y quemaduras

No tocar a la víctima mientras siga en contacto con el circuito; separarla con elemento aislante; activar la emergencia y aplicar reanimación si el personal está capacitado.

Enfriar la quemadura con agua limpia a temperatura ambiente; no aplicar hielo, cremas ni remedios caseros; cubrir con apósito estéril. Toda persona que sufra un choque eléctrico o una quemadura por arco se remite a valoración médica aunque se sienta bien.

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Responsable eléctrico Neptuno Energy Services | [__________] | [__________] |
| Residente de obra Neptuno Energy Services | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| Soporte técnico del fabricante del inversor | [__________] | [__________] |
| Centro de control / [OPERADOR DE RED] | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Recepción e inspección de inversores y estaciones de potencia | NES-OPE-F-110 | QA/QC |
| Control de almacenamiento y preservación de inversores | NES-OPE-F-111 | Almacenista / QA/QC |
| Lista de verificación de izaje de inversor o estación de potencia | NES-OPE-F-112 | Supervisor de izaje |
| Protocolo de montaje de inversor string | NES-OPE-F-113 | Supervisor de frente |
| Protocolo de asentamiento de inversor central o estación de potencia | NES-OPE-F-114 | Supervisor de frente / QA/QC |
| Registro de conexión DC al inversor | NES-OPE-F-115 | Responsable eléctrico |
| Registro de conexión AC y torques | NES-OPE-F-116 | Responsable eléctrico |
| Verificación de puesta a tierra y comunicaciones | NES-OPE-F-117 | Responsable eléctrico / QA/QC |
| Verificaciones previas y acta de primer arranque | NES-OPE-F-118 | Responsable eléctrico / técnico del fabricante |
| Registro de números de serie, parámetros de red y garantía | NES-OPE-F-119 | QA/QC / Responsable eléctrico |
| Plan de izaje, permisos y ATS/ART | Según NES-SST-PR-001 y NES-SST-PR-003 | Supervisor / Responsable SST |
| Certificados de calibración, de producto y de garantía | — | QA/QC |

# 14. ANEXOS

## NES-OPE-F-110 — Recepción e inspección de inversores y estaciones de potencia

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Remisión / orden de compra: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-018 | Transportador / placa: [__________] |

| Equipo (tipo) | Referencia | N.º de serie | Indicadores impacto / inclinación sin activar | Embalaje y exterior sin daño | Placa conforme (60 Hz) | Estado (A / C / R) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Certificado de conformidad de producto (RETIE) | | | |
| 2 | Protocolo de pruebas de fábrica | | | |
| 3 | Manuales, llaves y accesorios según lista de empaque | | | |
| 4 | Rejillas, ventiladores, prensaestopas y tapas DC sin daño | | | |
| 5 | Sin humedad ni condensación visible | | | |
| 6 | Estación: transformador sin fugas, indicadores conformes | | | |
| 7 | Estación: celdas y contenedor sin daño | | | |
| 8 | Fotografías y constancia en remisión del transportador | | | |
| 9 | Notificación al fabricante si hubo novedad | | | |

{.plain}
| Observaciones (A: aceptado; C: cuarentena; R: rechazado): |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-111 — Control de almacenamiento y preservación de inversores

{.plain}
| Proyecto: [__________] | Mes: [____] |
|---|---|
| Bodega / patio: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-018 | Rango del fabricante: [____] °C / [____] % HR / [____] meses |

| Fecha | Temp. (°C) | HR (%) | Embalaje o gabinete íntegro | Desecante en buen estado | Sin condensación, plagas ni ofidios | Responsable |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

{.plain}
| Fecha de ingreso más antigua: [____] | Calefacción anticondensación energizada (si aplica): Sí / No |
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

## NES-OPE-F-112 — Lista de verificación de izaje de inversor o estación de potencia

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Equipo (n.º de serie / ubicación): [__________] | Consecutivo: [____] |
| Masa del equipo: [____] kg | Plan de izaje N.º: [__________] |
| Grúa (capacidad / configuración): [__________] | Radio de trabajo: [____] m |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Plan de izaje aprobado según NES-SST-PR-003 | | | |
| 2 | Operador y aparejador certificados; supervisor de izaje presente | | | |
| 3 | Grúa, eslingas, grilletes y balancín certificados e inspeccionados | | | |
| 4 | Terreno verificado y placas de apoyo bajo estabilizadores | | | |
| 5 | Puntos de izaje del fabricante; centro de gravedad identificado | | | |
| 6 | Ángulo de eslinga o balancín según fabricante | | | |
| 7 | Vientos instalados; zona de exclusión delimitada | | | |
| 8 | Distancias a líneas energizadas según RETIE | | | |
| 9 | Viento dentro del límite del plan: [____] km/h | | | |
| 10 | Kit antiderrame disponible (estación con transformador) | | | |
| 11 | Equipo asentado y asegurado antes de liberar eslingas | | | |

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

## NES-OPE-F-113 — Protocolo de montaje de inversor string

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Inversor (código / n.º de serie): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-018 | Plano de soporte: [__________] |

| Ítem | Verificación | Valor medido | Cumple | No cumple |
|---|---|---|---|---|
| 1 | Soporte según plano, galvanizado sin daño | — | | |
| 2 | Posición vertical o inclinación hacia atrás dentro del límite del fabricante | ____ ° | | |
| 3 | Soporte del fabricante fijado al torque indicado | ____ N·m | | |
| 4 | Tornillos o pasadores antirrobo y antilevantamiento instalados | — | | |
| 5 | Separación a inversor contiguo | ____ mm | | |
| 6 | Espacio libre arriba | ____ mm | | |
| 7 | Espacio libre abajo | ____ mm | | |
| 8 | Espacio libre lateral | ____ mm | | |
| 9 | Protección solar y de lluvia según fabricante, sin obstruir ventilación | — | | |
| 10 | Altura de operación y sobre nivel de inundación | ____ m | | |
| 11 | Sin descarga de aire caliente hacia otro inversor | — | | |

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

## NES-OPE-F-114 — Protocolo de asentamiento de inversor central o estación de potencia

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Estación (código / n.º de serie): [__________] | Consecutivo: [____] |
| Fundación liberada (NES-OPE-PR-012): [__________] | Plano de fundación: [__________] |

| Ítem | Verificación | Valor medido | Cumple | No cumple |
|---|---|---|---|---|
| 1 | Cotas y dimensiones de la fundación según plano | — | | |
| 2 | Desnivel del apoyo dentro de lo que compensan los apoyos del fabricante | ____ mm | | |
| 3 | Equipo horizontal; carga repartida en todos los apoyos | ____ mm/m | | |
| 4 | Altura libre al terreno según fabricante | ____ mm | | |
| 5 | Anclajes al torque del plano y con marca | ____ N·m | | |
| 6 | Ventanas y ductos de cables alineados con las entradas | — | | |
| 7 | Foso o bandeja de contención de aceite y drenaje operativos | — | | |
| 8 | Distancias de ventilación y de apertura de puertas | ____ m | | |
| 9 | Pasos de cables sellados contra agua, polvo y fauna | — | | |
| 10 | Derrateo por altitud y temperatura revisado | ____ m s. n. m. | | |

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

## NES-OPE-F-115 — Registro de conexión DC al inversor

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Inversor (código / n.º de serie): [__________] | Consecutivo: [____] |
| Tensión DC máxima de entrada: [____] V | Voc máxima calculada del string (T mín. del sitio): [____] V |
| Irradiancia: [____] W/m² / Temp.: [____] °C | Instrumentos (serie / calibración): [__________] |

| Entrada / MPPT | String o principal (código) | Polaridad OK | Voc (V) | Tensión polo-tierra (+ / −) (V) | Aislamiento (MΩ) | Cumple |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

{.plain}
| Método de ensayo de aislamiento: [__________] | Tensión de ensayo: [____] V |
|---|---|
| Conectores DC compatibles con el inversor: Sí / No | Torques de barras DC (central): [____] N·m |

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

## NES-OPE-F-116 — Registro de conexión AC y torques

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Inversor (código / n.º de serie): [__________] | Consecutivo: [____] |
| Cable AC: [____] × [____] mm², Cu / Al | Torquímetro (serie / calibración): [__________] |

| Unión | Torque especificado (N·m) | Torque aplicado (N·m) | Marca de torque | Verificación QA/QC | Obs. |
|---|---|---|---|---|---|
| Fase L1 | | | | | |
| Fase L2 | | | | | |
| Fase L3 | | | | | |
| Neutro (si aplica) | | | | | |
| PE del cable AC | | | | | |
| Tierra de chasis | | | | | |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Interruptor AC aguas abajo y lado MT bloqueados y etiquetados | | | |
| 2 | Sección, material y número de conductores según unifilar | | | |
| 3 | Terminales y crimpado conformes; bimetálico si aluminio | | | |
| 4 | Aislamiento del cable AC ensayado: ____ MΩ a ____ V | | | |
| 5 | Secuencia de fases verificada | | | |
| 6 | Entradas selladas | | | |

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

## NES-OPE-F-117 — Verificación de puesta a tierra y comunicaciones del inversor

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Inversor / estación (código): [__________] | Consecutivo: [____] |
| Instrumento (serie / calibración): [__________] | Criterio de continuidad de diseño: [____] Ω |

| Ítem | Verificación | Valor | Cumple | No cumple |
|---|---|---|---|---|
| 1 | Borne de tierra del inversor conectado a la malla | ____ Ω | | |
| 2 | PE del cable AC conectado además de la tierra de chasis | — | | |
| 3 | Equipotencialidad inversor, transformador, celdas y skid | ____ Ω | | |
| 4 | Configuración de tierra del arreglo DC coincide con el inversor | — | | |
| 5 | Cable de comunicaciones separado de potencia | — | | |
| 6 | Pantalla a tierra en un extremo; terminación de bus instalada | — | | |
| 7 | Dirección o IP asignada según arquitectura | ____ | | |
| 8 | Inversor visible en el controlador con estado, alarmas y medidas | — | | |
| 9 | Señal de DPS y de alarmas llega al SCADA (si aplica) | — | | |

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

## NES-OPE-F-118 — Verificaciones previas y acta de primer arranque del inversor

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Inversor (código / n.º de serie): [__________] | Consecutivo: [____] |
| Dictamen RETIE N.º: [__________] | Autorización de [OPERADOR DE RED]: [__________] |

| Ítem | Verificación previa | Registro | Cumple | No cumple |
|---|---|---|---|---|
| 1 | Montaje, distancias y sellos conformes | F-113 / F-114 | | |
| 2 | Gabinete limpio; ventiladores y filtros libres | — | | |
| 3 | Conexión DC conforme; ninguna Voc supera el máximo | F-115 | | |
| 4 | Conexión AC, torques y secuencia de fases conformes | F-116 | | |
| 5 | Puesta a tierra y comunicaciones conformes | F-117 | | |
| 6 | Tensión de red en bornes dentro de rango: ____ V / ____ Hz | — | | |
| 7 | Parámetros de red cargados y verificados | F-119 | | |
| 8 | Lista de verificación de garantía del fabricante diligenciada | — | | |
| 9 | Autorización escrita del responsable eléctrico y de [CLIENTE] | — | | |

{.plain}
| Firmware: [__________] | Hora de sincronización: [____] |
|---|---|
| Riso medida por el inversor: [____] kΩ | Potencia inicial: [____] kW |
| Alarmas en registro de eventos: [__________] | Horas de observación: [____] h |
| Técnico del fabricante: [__________] | Informe del fabricante N.º: [__________] |

{.plain}
| Resultado del primer arranque y observaciones: |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] | |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-119 — Registro de números de serie, parámetros de red y garantía

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / estación: [__________] | Consecutivo: [____] |
| Estudio de conexión / tabla de parámetros aprobada: [__________] | Marco regulatorio: CREG 075 de 2021 / CREG 174 de 2021 |

| Posición | Referencia | N.º de serie | Firmware | Dirección / IP | Fecha primer arranque | Registro de garantía N.º |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

| Parámetro de red | Valor aprobado | Valor configurado | Conforme |
|---|---|---|---|
| Tensión y frecuencia nominales | | | |
| Límites y tiempos de desconexión por tensión | | | |
| Límites y tiempos de desconexión por frecuencia | | | |
| Tiempo de reconexión | | | |
| Rampas de potencia | | | |
| Límite de potencia activa | | | |
| Modo de potencia reactiva / factor de potencia | | | |
| Soporte ante huecos de tensión | | | |
| Protección antiisla | | | |

{.plain}
| Archivo de parámetros exportado: [__________] | Contraseña de instalador custodiada por: [__________] |
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

# 15. CONTROL DE CAMBIOS

| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
