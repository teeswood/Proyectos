---
code: NES-OPE-PR-021
header_title: PROCEDIMIENTO DE INSTALACIÓN DE SCADA Y FIBRA ÓPTICA
cover_title: Procedimiento de Instalación de SCADA, Comunicaciones y Fibra Óptica
cover_subtitle: Fibra óptica, red de planta, controlador de planta y estación meteorológica en plantas fotovoltaicas
---

# 1. OBJETIVO

Definir el método de trabajo, los controles de calidad, los ensayos y las medidas preventivas para la instalación del sistema de supervisión, control y adquisición de datos (SCADA) de la planta [PROYECTO]: tendido, empalme, terminación y ensayo de la red de fibra óptica; montaje de tableros de comunicación y de la red Ethernet de planta; instalación del controlador de planta (PPC), de la estación meteorológica y de los sensores de irradiancia y temperatura según la IEC 61724-1; integración de inversores, trackers y equipos eléctricos; pruebas punto a punto de señales y medidas básicas de ciberseguridad.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, en especial las lesiones por fragmentos de fibra, la exposición a radiación láser y el contacto con partes energizadas en tableros.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en:

- Recepción, almacenamiento y manejo de cable de fibra óptica, cable de cobre de datos, equipos de red y sensores.
- Tendido de cable de fibra óptica en ducto, subducto y zanja, y de cable de cobre de datos en bandeja y canalización.
- Empalmes por fusión, cajas de empalme, distribuidores ópticos (ODF), pigtails y cordones de conexión.
- Ensayos de la red de fibra: inspección de conectores, reflectometría (OTDR) y pérdida de inserción con fuente y medidor.
- Montaje y conexionado de tableros de comunicación, switches, convertidores de medio, fuentes y sistemas de respaldo de energía.
- Configuración de la red Ethernet de planta en anillo, segmentación y sincronización de tiempo.
- Instalación del controlador de planta (PPC) y de la estación meteorológica con piranómetros en el plano y horizontales, sensores de temperatura de módulo, de temperatura ambiente, de viento y demás variables del diseño.
- Integración de inversores, trackers, cajas combinadoras monitoreadas, medidores y relés al SCADA; pruebas punto a punto; pruebas funcionales en frío.
- Medidas básicas de ciberseguridad en la puesta en marcha del sistema.

No incluye la canalización civil de ductos y zanjas, que se rige por el procedimiento civil del proyecto [__________] y por NES-OPE-PR-015 en lo que corresponde al tendido; el montaje eléctrico de inversores (NES-OPE-PR-018) y de cajas combinadoras (NES-OPE-PR-017); ni las pruebas del PPC con inyección de potencia a la red y las pruebas exigidas por el [OPERADOR DE RED] y por XM, que se ejecutan dentro de NES-OPE-PR-023.

> NOTA: Las pruebas de lazo cerrado del controlador de planta que modifican la potencia inyectada solo se ejecutan con la planta energizada y con autorización escrita según NES-OPE-PR-023. Este procedimiento deja el sistema probado en frío: señales verificadas punto a punto y comunicaciones operativas.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| SCADA | Sistema de supervisión, control y adquisición de datos de la planta: servidores, estaciones de operación, red, controladores y software de supervisión. |
| PPC | Controlador de planta: equipo que recibe las consignas del operador y la medida en el punto de conexión y distribuye consignas de potencia activa, reactiva, tensión o factor de potencia a los inversores. |
| RTU / controlador de bloque | Equipo que concentra señales de campo de un bloque o subestación y las comunica al SCADA. |
| Fibra monomodo (SM) | Fibra con núcleo de diámetro pequeño que propaga un solo modo; usada en distancias de planta. Tipo habitual según ITU-T G.652.D o G.657. |
| Fibra multimodo (MM) | Fibra con núcleo de mayor diámetro, para distancias cortas dentro de tableros o edificios. |
| Cable dieléctrico | Cable de fibra sin elementos metálicos; no conduce tensiones inducidas ni descargas atmosféricas. |
| Tubo holgado (loose tube) | Tubo que aloja varias fibras con gel o material bloqueante de agua dentro del cable. |
| Empalme por fusión | Unión permanente de dos fibras por arco eléctrico, con equipo de alineación. |
| Caja de empalme | Envolvente estanca que aloja y protege los empalmes y las reservas de fibra en campo. |
| ODF | Distribuidor óptico: bandeja o chasis en tablero donde se terminan las fibras en pigtails y adaptadores. |
| Pigtail | Tramo corto de fibra con un conector en un extremo, que se empalma a la fibra del cable. |
| UPC / APC | Tipos de pulido del conector: contacto físico ultra pulido (cara plana) o en ángulo (cara inclinada). No se acoplan entre sí. |
| OTDR | Reflectómetro óptico en el dominio del tiempo: inyecta pulsos y analiza la luz retrodispersada para medir longitud, atenuación, empalmes, conectores y fallas. |
| Bobina de lanzamiento / recepción | Tramo de fibra de longitud conocida que se conecta antes y después del enlace ensayado para que el OTDR pueda medir el primer y el último conector. |
| Zona muerta | Distancia después de un evento reflectivo en la que el OTDR no puede detectar o medir otro evento. |
| Pérdida de inserción | Atenuación total de un enlace medida con fuente de luz y medidor de potencia, en dB. |
| Presupuesto de pérdidas | Pérdida máxima calculada de un enlace: atenuación del cable más pérdida de empalmes y conectores. |
| Anillo | Topología en la que los switches se conectan en lazo cerrado con un protocolo de redundancia que bloquea un enlace y lo habilita ante una falla. |
| VLAN | Red lógica separada dentro de la misma infraestructura física. |
| POA | Irradiancia en el plano del arreglo. |
| GHI | Irradiancia global horizontal. |
| Piranómetro | Sensor de irradiancia solar hemisférica, clasificado según la ISO 9060. |
| Lista de señales (I/O list) | Relación de todas las señales del sistema con origen, tipo, dirección de registro, escalamiento, unidades y destino. |
| Prueba punto a punto | Verificación de cada señal desde el equipo de origen hasta la pantalla de operación, incluyendo valor, escala, alarma y comando. |
| FAT / SAT | Pruebas de aceptación en fábrica / en sitio. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. El recorrido de la red de fibra óptica, las cajas de empalme, los tableros de comunicación por bloque, la sala de control, la ubicación del PPC y de las estaciones meteorológicas se identifican en el plano de arquitectura de comunicaciones [N° de plano], el plano de rutas de fibra [N° de plano] y el plano de implantación de estaciones meteorológicas [N° de plano].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

- Arquitectura de comunicaciones del SCADA, plano de rutas de fibra, diagrama de empalmes (asignación de fibras por enlace) y plano de tableros — [N° de plano].
- Lista de señales del proyecto, mapas de registros de inversores, trackers, medidores y relés, y plan de direccionamiento IP — [__________].
- Especificación funcional del SCADA y del PPC, y requisitos de supervisión del [OPERADOR DE RED] y, si aplica, de XM — [__________].
- Ficha técnica del cable de fibra: tipo de fibra, número de fibras, diámetro, tensión máxima de tracción en instalación y en servicio, radio mínimo de curvatura con y sin carga, rango de temperatura y protección antirroedores.
- Manuales de los fabricantes de la empalmadora, el OTDR, los switches, el PPC, los sensores meteorológicos y el registrador de datos.
- NES-OPE-PR-015 Tendido de cables; NES-OPE-PR-017 Cajas combinadoras; NES-OPE-PR-018 Inversores; NES-OPE-PR-022 Pruebas y comisionado del generador FV; NES-OPE-PR-023 Energización y puesta en servicio.
- NES-CAL-PLN-002 Plan de calidad; NES-CAL-PLN-003 Plan de inspección y ensayos eléctrico.
- NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-SST-PLN-001 Plan de emergencias.
- Manual del fabricante del tracker del proyecto, en lo relativo a la comunicación del controlador de tracker y a la señal de viento para la posición de defensa.

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes: requisitos de instalación de tableros, puesta a tierra, protección contra sobretensiones y trabajo en instalaciones eléctricas.
- NTC 2050 — Código Eléctrico Colombiano, en los requisitos que el RETIE adopta.
- Ley 1264 de 2008 (técnicos electricistas — CONTE); Ley 51 de 1986 y Ley 842 de 2003 (ingenieros — COPNIA).
- Resolución CREG 075 de 2021 (conexión al SIN) y procedimientos del [OPERADOR DE RED] y de XM en lo relativo a supervisión e intercambio de información, cuando apliquen.
- IEC 61724-1 — Desempeño de sistemas fotovoltaicos. Parte 1: monitoreo.
- ISO 9060 — Especificación y clasificación de instrumentos de medida de radiación solar hemisférica y directa.
- IEC 61850 — Redes y sistemas de comunicación para la automatización de sistemas de potencia, cuando el diseño la adopte.
- IEC 62439-2 — Redes de automatización de alta disponibilidad: protocolo de redundancia en anillo (MRP), cuando el diseño lo adopte; IEEE 802.1 para RSTP y VLAN.
- IEC 62443 — Seguridad de sistemas de automatización y control industrial (referencia técnica de ciberseguridad).
- ITU-T G.652 y G.657 — Características de la fibra monomodo.
- IEC 60794 — Cables de fibra óptica (especificaciones de producto).
- IEC 61280-4-2 — Medición de atenuación de planta de cable instalada con fibra monomodo.
- IEC 61300-3-35 — Inspección visual de la cara de conectores de fibra óptica.
- IEC 60825-1 y IEC 60825-2 — Seguridad de productos láser y de sistemas de comunicación por fibra óptica.
- ANSI/TIA-568 (series .2 y .3) y ANSI/TIA-598 — Cableado de cobre y de fibra, y código de colores de fibras (referencia técnica).
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019.
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en el sector eléctrico; cinco reglas de oro.
- Resolución 4272 de 2021 — Trabajo en alturas (mástiles de estación meteorológica, postes, bandejas altas).
- Resolución 0491 de 2020 — Espacios confinados (cámaras de inspección y cajas de paso que lo sean).
- Resolución 2400 de 1979 — Estatuto de seguridad industrial; arts. 388 a 392 (manejo manual de cargas) y arts. 398 a 447 (manejo y transporte mecánico de materiales).
- Decreto 1496 de 2018 — Sistema Globalmente Armonizado (alcohol isopropílico, geles, limpiadores).
- Resolución 2184 de 2019; Decreto 1076 de 2015 (RESPEL); Ley 1672 de 2013 (RAEE); Resolución 0472 de 2017 modificada por la Resolución 1257 de 2021 (RCD).
- Licencia ambiental y Plan de Manejo Ambiental (PMA) del proyecto — [N° de resolución].
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

- Aprobar y divulgar el presente procedimiento y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.
- Coordinar con [CLIENTE], con el integrador del SCADA y con los fabricantes de inversores y trackers el programa de integración y de pruebas.
- Tramitar los RFI de cambios de ruta, de cantidad de fibras o de arquitectura de red.
- Detener cualquier actividad que no cumpla este procedimiento, el diseño o la instrucción del fabricante.

## 6.2. Ingeniero de SCADA y comunicaciones (ingeniero con matrícula COPNIA vigente)

- Controlar la ejecución según la arquitectura, la lista de señales y el plan de direccionamiento aprobados.
- Calcular el presupuesto de pérdidas de cada enlace óptico, aprobar los resultados de OTDR y pérdida de inserción y firmar los protocolos.
- Dirigir la configuración de la red, la integración de equipos, las pruebas punto a punto y las medidas de ciberseguridad.
- Custodiar las contraseñas y los respaldos de configuración y entregarlos a [CLIENTE] por el medio seguro acordado.

## 6.3. Supervisor de frente de comunicaciones

- Asignar tareas, dirigir la cuadrilla de tendido y empalme y verificar el cumplimiento del método.
- Elaborar con los trabajadores el ATS/ART diario y la charla de inicio de turno.
- Verificar la tensión de tracción, el radio de curvatura y las reservas durante el tendido.
- Diligenciar los registros del frente el mismo día.

## 6.4. Técnico empalmador de fibra óptica

- Preparar cables, ejecutar empalmes por fusión, organizar bandejas y cerrar cajas de empalme y ODF según el diagrama de empalmes.
- Ejecutar la inspección y limpieza de conectores y los ensayos de OTDR y pérdida de inserción.
- Recoger y disponer los fragmentos de fibra en el recipiente previsto.

## 6.5. Técnico electricista de tableros e instrumentación (matrícula CONTE vigente)

- Montar y conexionar tableros de comunicación, fuentes, sistemas de respaldo, DPS de señal y puesta a tierra.
- Instalar la estación meteorológica y los sensores de campo y conexionarlos al registrador o al controlador.
- Aplicar el bloqueo y etiquetado en todo tablero alimentado.

## 6.6. Responsable de calidad (QA/QC)

- Controlar el PIE eléctrico (NES-CAL-PLN-003) en lo relativo a comunicaciones, la trazabilidad de bobinas, cajas de empalme y enlaces, y la vigencia de calibración de OTDR, medidores de potencia y sensores.
- Registrar y hacer seguimiento a las no conformidades hasta su cierre.

## 6.7. Responsable SST

- Elaborar y divulgar la matriz de peligros específica: fragmentos de fibra, radiación láser, sustancias químicas, zanjas, alturas, espacios confinados y riesgo eléctrico en tableros.
- Verificar permisos, EPP, delimitación de áreas y competencia del personal.
- Aplicar el protocolo de tormenta eléctrica y liderar la atención de emergencias.

## 6.8. Responsable ambiental

- Asegurar el cumplimiento del PMA y la gestión de retazos de cable, fragmentos de fibra, envases de químicos, carretes y embalajes.

## 6.9. Trabajadores

- Cumplir este procedimiento y participar en el ATS/ART.
- Usar correctamente el EPP y no mirar nunca el extremo de una fibra ni de un conector, ni a simple vista ni con microscopio sin filtro, sin confirmar que no está iluminada.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Ingeniero de SCADA y comunicaciones, supervisor, técnicos empalmadores, técnicos electricistas de tableros e instrumentación, auxiliares de tendido, QA/QC, responsable SST; coordinador de alturas cuando haya trabajo en mástiles o postes. |
| Materiales | Fibra óptica | Cable de fibra de la especificación del proyecto, preferiblemente dieléctrico y con protección antirroedores en tendido enterrado; cajas de empalme estancas; ODF; pigtails; adaptadores; cordones de conexión del tipo de pulido del proyecto; manguitos termocontráctiles de protección de empalme. |
| Materiales | Red y tableros | Switches industriales gestionables, convertidores de medio, transceptores ópticos, cable de cobre de datos apantallado de la categoría de diseño, fuentes DC, sistema de respaldo (UPS), DPS de alimentación y de señal, borneras, rótulos. |
| Materiales | Meteorología | Piranómetros en el plano y horizontales de la clase de diseño, sensores de temperatura de módulo, sensor de temperatura y humedad ambiente con protector de radiación, anemómetro y veleta, pluviómetro y sensor de suciedad si el diseño los incluye, registrador de datos, mástil, soportes y cable apantallado. |
| Herramientas | Tendido | Cinta o guía de tendido, mandril de verificación de ducto, lubricante de tendido compatible con la cubierta, destorcedor, malla de tracción, dinamómetro o fusible mecánico de tracción, rodillos y poleas de radio adecuado, malacate con limitador de tensión cuando aplique. |
| Herramientas | Empalme | Empalmadora por fusión con alineación por núcleo o por revestimiento según especificación, cortadora de precisión, peladores de cubierta, de tubo y de recubrimiento, alcohol isopropílico de alta pureza, paños sin pelusa, recipiente para fragmentos, horno de manguitos. |
| Equipos | Ensayo óptico | OTDR con longitudes de onda de 1.310 nm y 1.550 nm como mínimo, bobinas de lanzamiento y recepción, fuente de luz y medidor de potencia, cordones de referencia, microscopio de inspección de conectores con filtro, localizador visual de fallas; todos con calibración vigente. |
| Equipos | Ensayo de red y señales | Computador de configuración, probador de cable de cobre, calibrador de lazo de corriente y de señales, multímetro CAT III o superior, irradiancímetro o célula de referencia calibrada para contraste, nivel de burbuja e inclinómetro digital, brújula o equipo de orientación. |
| EPP | Fibra y químicos | Gafas de seguridad con protección lateral, guantes de nitrilo para limpieza, delantal o tapete de trabajo oscuro para ver fragmentos. |
| EPP | Trabajo eléctrico | Guantes dieléctricos de la clase acorde a la tensión del tablero, careta y ropa con la categoría que indique el análisis de riesgo de arco, calzado dieléctrico. |
| EPP | Básico | Casco con barbuquejo, botas con puntera, chaleco reflectivo, cubrenuca, protector solar, ropa manga larga, guantes de manipulación, polainas en zonas con presencia de ofidios; arnés y línea de vida certificados para trabajo en alturas. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

- Planos de arquitectura, rutas, diagrama de empalmes, lista de señales y plan IP vigentes y aprobados en el frente.
- Ductos y zanjas recibidos del frente civil: continuidad del ducto verificada con mandril, cinta guía instalada, cajas de paso terminadas, sin agua ni sedimentos.
- Bobinas de fibra inspeccionadas a la recepción: sin golpes en la bobina, extremos sellados, certificado de ensayo de fábrica de cada bobina; ensayo de OTDR de la bobina antes de tender cuando la especificación lo exija.
- Equipos de red, PPC y sensores con certificado de conformidad y FAT, cuando aplique, y con firmware de la versión aprobada.
- Instrumentos con calibración vigente; empalmadora con mantenimiento y electrodos dentro de vida útil.
- Tableros con alimentación definitiva o provisional aprobada y puesta a tierra conforme.
- ATS/ART, permiso de trabajo, y permiso de trabajo en alturas, en excavaciones o en espacio confinado cuando apliquen.
- Condiciones climáticas aptas: sin tormenta eléctrica; sin lluvia para empalmes, apertura de cajas y montaje de sensores.

> ALTO: No se empalma ni se abre una caja de empalme o un ODF con lluvia, polvo en suspensión o viento que no permita controlar los fragmentos de fibra. El empalme se ejecuta dentro de carpa o vehículo taller.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

El frente se organiza por tramo de ruta, caja de empalme, tablero de bloque y sala de control. Se delimitan: el punto de alimentación de la bobina, el punto de tracción, las cajas de paso intermedias con personal de vigilancia, el puesto de empalme bajo carpa, los tableros intervenidos y el mástil de la estación meteorológica durante su montaje. Las zanjas y cajas abiertas se señalizan y protegen contra caídas.

### 8.2.2. Ingreso de personal

- Evaluar condiciones del área y verificar que no haya trabajos simultáneos incompatibles (excavación, izaje, energización del tablero).
- Diligenciar ATS/ART y los permisos que correspondan.
- Ubicar equipos de emergencia, botiquín, lavaojos portátil y extintor.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional de vehículos, malacates y equipos; circulación solo por rutas autorizadas.
- Las bobinas se transportan y descargan con equipo mecánico, con la bobina en posición vertical sobre su eje y nunca rodándola desde la plataforma (Res. 2400 de 1979, manejo mecánico de materiales).
- Los vehículos no transitan sobre ductos sin protección ni a menos de la distancia de seguridad del borde de zanjas abiertas.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Recepción y almacenamiento de materiales

1. Verificar referencia, cantidad de fibras, tipo de fibra, longitud y número de bobina contra la orden de compra y la especificación.
2. Inspeccionar la bobina: sin daño en las alas, cubierta del cable sin cortes, extremos con capuchón de sellado.
3. Archivar el certificado de fábrica de cada bobina (atenuación por fibra y longitud).
4. Almacenar las bobinas en posición vertical, calzadas, sobre superficie firme, protegidas del sol directo prolongado y de la maquinaria.
5. Almacenar switches, PPC, sensores y piranómetros en lugar cerrado, seco y bajo llave, en su empaque original.
6. Registrar la recepción en NES-OPE-F-140.

#### 8.2.4.2. Preparación de la ruta

1. Verificar el ducto con mandril de diámetro acorde: un ducto aplastado o con obstrucción no se usa hasta repararlo.
2. Limpiar el ducto con escobillón o pistón si hay sedimentos; retirar agua de las cajas de paso.
3. Confirmar la cinta guía y su resistencia; si no existe, instalarla con el método del frente civil.
4. Definir en el plano los puntos de alimentación y tracción, el sentido del tendido y las cajas intermedias donde se hace tendido en figura de ocho cuando el tramo supera la longitud que se puede halar con la tensión admitida.
5. Instalar rodillos y poleas en cambios de dirección y en la boca del ducto, con radio no menor que el radio mínimo de curvatura con carga del cable.

#### 8.2.4.3. Tendido de fibra óptica en ducto y zanja

| Parámetro | Requisito |
|---|---|
| Tensión de tracción | No superar la tensión máxima de instalación de la ficha técnica del cable — [____] N. Controlar con dinamómetro, fusible mecánico de tracción o malacate con limitador. |
| Radio de curvatura con carga | No menor que el de la ficha técnica; valor típico de referencia 20 veces el diámetro exterior del cable — verificar contra la ficha. |
| Radio de curvatura sin carga | No menor que el de la ficha técnica; valor típico de referencia 10 veces el diámetro exterior del cable — verificar contra la ficha. |
| Tracción | Por los elementos de tracción del cable (aramida o varilla central) con malla o terminal de tracción y destorcedor; nunca por la cubierta sola ni por las fibras. |
| Lubricación | Lubricante compatible con la cubierta, aplicado en la boca del ducto en tramos largos o con curvas. |
| Velocidad | Constante y sin tirones; detener ante cualquier aumento brusco de tensión. |
| Figura de ocho | En el punto intermedio, el cable se dispone en figura de ocho sobre superficie limpia para invertir el sentido sin torsión; nunca en espiral. |
| Torsión | Prohibido torcer el cable; el destorcedor absorbe la rotación. |
| Reservas | Dejar reserva enrollada en cada caja de empalme y en cada extremo, según el diseño — [____] m. |
| Sellado | Sellar los extremos del cable y las bocas de ducto el mismo día. |

1. Asignar personal con radio en el punto de alimentación, en el de tracción y en cada caja intermedia; nadie se ubica en la línea de la cinta o del cable bajo tensión.
2. Desenrollar la bobina desde un portabobinas, con freno, para que el cable salga sin tensión excesiva ni roce contra el borde.
3. Halar de forma continua controlando tensión y radio en cada caja.
4. En zanja directa, cuando el diseño lo admita, tender el cable sobre lecho de material seleccionado sin piedras, sin tensión y con la holgura de diseño; aplicar la profundidad, el relleno y la cinta de advertencia del plano.
5. Mantener la separación con cables de potencia definida en el diseño; aunque el cable dieléctrico no se ve afectado por campos electromagnéticos, la separación protege contra daño mecánico y facilita el mantenimiento.
6. Rotular el cable en cada caja de paso y en cada extremo con identificación del enlace.
7. Registrar longitud tendida (marcas métricas de la cubierta al inicio y al final), tensión máxima registrada y novedades en NES-OPE-F-141.

> ALTO: Un cable de fibra que se ha halado por encima de su tensión máxima, se ha torcido o se ha doblado por debajo de su radio mínimo puede quedar con microfisuras que no se ven y que aparecen como atenuación o como rotura meses después. Ante cualquiera de estas situaciones se detiene el tendido, se informa y se ensaya el tramo con OTDR antes de continuar.

#### 8.2.4.4. Cable de cobre de datos

- Respetar la longitud máxima del canal de cobre Ethernet de la norma de cableado aplicable (100 m en la práctica habitual de ANSI/TIA-568) y usar fibra o convertidor de medio para distancias mayores o entre tableros con referencias de tierra distintas.
- Usar cable apantallado de la categoría de diseño en ambientes con interferencia y aterrizar la pantalla según el criterio del diseño.
- Separar el cable de datos de los cables de potencia según el diseño; cruzarlos en ángulo recto cuando sea inevitable.
- Instalar DPS de señal en líneas de cobre que salen del tablero hacia campo (sensores, RS-485), con la tierra del tablero.
- Respetar el radio de curvatura del fabricante y no apretar los amarres hasta deformar el cable.

#### 8.2.4.5. Preparación del cable y empalme por fusión

1. Ingresar el cable a la caja de empalme o al ODF por su prensaestopas, fijar el elemento de tracción al anclaje previsto y aterrizar la armadura metálica solo si el cable la tiene y el diseño lo indica.
2. Retirar la cubierta la longitud que indique el fabricante de la caja, sin dañar los tubos; cortar el hilo de rasgado y la aramida a la longitud del anclaje.
3. Limpiar el gel de los tubos y de las fibras con el limpiador indicado por el fabricante del cable, nunca con solventes no aprobados.
4. Pasar las fibras a la bandeja de empalme con su tubo de transporte, respetando el radio mínimo de la fibra en la bandeja.
5. Identificar cada fibra por el código de colores del cable (ANSI/TIA-598 o el que declare el fabricante) y verificarla contra el diagrama de empalmes.
6. Deslizar el manguito termocontráctil de protección sobre una de las fibras antes de empalmar.
7. Retirar el recubrimiento primario con el pelador de precisión y limpiar la fibra desnuda con alcohol isopropílico de alta pureza y paño sin pelusa, en una sola pasada.
8. Cortar con la cortadora de precisión a la longitud que fija la empalmadora. Depositar de inmediato el fragmento en el recipiente.
9. Colocar las fibras en la empalmadora; verificar en la pantalla el ángulo y la calidad del corte; si el equipo lo rechaza, repetir pelado, limpieza y corte.
10. Ejecutar la fusión y anotar la pérdida estimada por la empalmadora. La estimación es una ayuda: la aceptación del empalme se hace con OTDR.
11. Centrar el manguito sobre el empalme y contraerlo en el horno.
12. Acomodar el empalme en su posición de la bandeja y la reserva de fibra en las guías, sin cruces ni curvas cerradas.
13. Registrar cada empalme (bandeja, posición, fibra de entrada, fibra de salida, pérdida estimada) en NES-OPE-F-142.

> NOTA: La fibra desnuda limpia no se toca ni se apoya sobre ninguna superficie antes del corte y la fusión. Una fibra contaminada produce empalmes con pérdida alta o con burbujas que fallan con el tiempo.

#### 8.2.4.6. Cajas de empalme y ODF

- Caja de empalme: verificar sello de entradas y de tapa según el fabricante, instalar el desecante si lo trae, cerrar al par indicado y ubicarla en la caja de paso por encima del nivel de agua previsible, con la reserva de cable enrollada y fijada.
- ODF: fijar en el tablero, ingresar el cable con su anclaje, empalmar pigtails del tipo de conector y pulido del proyecto, instalar adaptadores y rotular cada puerto con el enlace y la fibra.
- Las fibras de reserva (no usadas) también se empalman o se dejan organizadas y rotuladas según el diseño.
- Instalar tapas antipolvo en todos los adaptadores y conectores no usados.
- No mezclar conectores UPC y APC: se identifican por color de cuerpo según la convención del fabricante y del proyecto.

#### 8.2.4.7. Inspección y limpieza de conectores

1. Confirmar que la fibra no está iluminada antes de inspeccionar.
2. Inspeccionar cada cara de conector y cada adaptador con el microscopio con filtro, con el criterio de la IEC 61300-3-35 (zonas de núcleo, revestimiento y contacto).
3. Si hay contaminación, limpiar con el limpiador en seco del fabricante (cassette o lápiz); si persiste, limpieza húmeda y seca; volver a inspeccionar.
4. No conectar ningún conector sin inspeccionar: un conector contaminado contamina al adaptador y al conector opuesto.
5. Rechazar el conector con rayas o picaduras en el núcleo y reemplazar el pigtail.

#### 8.2.4.8. Ensayo de reflectometría (OTDR)

1. Conectar la bobina de lanzamiento entre el OTDR y el enlace y la bobina de recepción en el extremo opuesto, para que el primer y el último conector del enlace sean medibles fuera de la zona muerta.
2. Configurar longitudes de onda de 1.310 nm y 1.550 nm (y otras si la especificación lo exige), índice de refracción del cable de la ficha técnica, ancho de pulso y tiempo de promediado acordes con la longitud del enlace.
3. Medir cada fibra en ambos sentidos. La pérdida de cada empalme es el promedio de las lecturas en los dos sentidos: una lectura en un solo sentido puede mostrar ganancia aparente o pérdida exagerada por diferencias del diámetro de campo modal entre fibras.
4. Verificar en la traza: longitud total coherente con el tendido, atenuación de cada tramo, ubicación y pérdida de cada empalme y conector, ausencia de eventos no previstos y reflectancia de los conectores.
5. Comparar la diferencia de pérdida entre 1.310 nm y 1.550 nm en cada evento: una pérdida mayor en 1.550 nm que en 1.310 nm indica macrocurvatura (fibra doblada en bandeja, caja o tendido).
6. Guardar los archivos de traza con identificación del enlace, la fibra, la longitud de onda y el sentido, y resumir en NES-OPE-F-143.

#### 8.2.4.9. Ensayo de pérdida de inserción

1. Referenciar la fuente y el medidor con el método de cordones de referencia que fije la IEC 61280-4-2 para el tipo de enlace y registrar el método.
2. Medir la pérdida de cada fibra del enlace en 1.310 nm y 1.550 nm.
3. Calcular el presupuesto de pérdidas del enlace: pérdida máxima = (coeficiente de atenuación × longitud) + (número de empalmes × pérdida máxima por empalme) + (número de pares de conectores × pérdida máxima por par).
4. Comparar la pérdida medida contra el presupuesto y contra la sensibilidad y la potencia de los transceptores con su margen de diseño.
5. Registrar en NES-OPE-F-143.

| Parámetro | Valor de referencia | Fuente |
|---|---|---|
| Pérdida por empalme por fusión | No mayor de 0,3 dB (máximo de la norma de cableado); el proyecto suele fijar un valor más exigente — [____] dB | ANSI/TIA-568.3 / Especificación del proyecto |
| Pérdida por par de conectores acoplados | No mayor de 0,75 dB (máximo de la norma de cableado); valor del proyecto — [____] dB | ANSI/TIA-568.3 / Especificación del proyecto |
| Atenuación del cable monomodo de planta externa | No mayor de 0,5 dB/km en 1.310 nm y 1.550 nm (máximo de la norma de cableado); valor de la ficha del cable — [____] dB/km | ANSI/TIA-568.3 / Ficha técnica |
| Pérdida de inserción del enlace | No mayor que el presupuesto calculado del enlace | Este procedimiento |
| Reflectancia de conectores | Según el tipo de pulido y la especificación del proyecto — [____] dB | Especificación del proyecto |

> NOTA: Los valores de la tabla son los máximos de referencia de la norma de cableado. La especificación técnica del proyecto o del integrador del SCADA puede fijar criterios más exigentes: en ese caso, manda la especificación del proyecto.

#### 8.2.4.10. Tableros de comunicación

1. Montar el tablero según el plano, nivelado, con anclaje y grado IP de diseño, protegido de la radiación directa cuando el diseño lo indique.
2. Conectar la puesta a tierra del tablero a la red de tierra del bloque y las pantallas de los cables según el criterio de diseño.
3. Instalar fuente, sistema de respaldo, DPS de alimentación y de señal, switches, convertidores, ODF y borneras según el plano de disposición.
4. Verificar la ventilación o climatización y que la temperatura interior esperada no supere el rango de los equipos.
5. Antes de energizar: revisar conexionado, apriete de bornes, polaridad de fuentes DC y aislamiento; aplicar la secuencia de energización del tablero con permiso de trabajo y LOTO según NES-SST-PR-001.
6. Verificar autonomía del sistema de respaldo de energía frente al valor de diseño — [____] min.
7. Rotular equipos, puertos y cables y dejar dentro del tablero el plano de disposición y conexionado.
8. Registrar en NES-OPE-F-144.

#### 8.2.4.11. Red Ethernet de planta

1. Cargar en cada switch la configuración aprobada: nombre, dirección IP de gestión, VLAN, protocolo de redundancia en anillo, sincronización de tiempo y registro de eventos.
2. Segmentar la red según el diseño; como mínimo separar control y supervisión de la planta, videovigilancia y seguridad física, y acceso corporativo o remoto.
3. Verificar la topología: cada anillo cerrado, un único enlace bloqueado por el protocolo y sin bucles fuera de los anillos.
4. Prueba de redundancia: desconectar un enlace del anillo y verificar que la comunicación con los equipos se mantiene y que el tiempo de recuperación cumple la especificación — [____] ms; reponer el enlace y verificar el retorno.
5. Verificar la sincronización de tiempo de servidores, PPC, inversores, medidores y relés desde la fuente de tiempo del diseño (receptor satelital con NTP o PTP), con diferencia dentro de la especificación.
6. Verificar el ancho de banda y la latencia de los enlaces críticos (PPC a inversores, PPC a medidor del punto de conexión) contra la especificación del PPC.
7. Respaldar la configuración final de cada equipo y registrar en NES-OPE-F-145.

#### 8.2.4.12. Controlador de planta (PPC)

- Instalar el PPC en el tablero previsto, con alimentación respaldada y sincronización de tiempo.
- Verificar la medida del punto de conexión que recibe el PPC (tensión, corriente, potencia activa y reactiva, frecuencia) contra el medidor o el relé de origen y contra los transformadores de medida del diseño, con relación y polaridad correctas.
- Verificar la comunicación con cada inversor: lectura de estado y de potencia, y escritura de consignas en frío o en modo de prueba sin inyección.
- Verificar las entradas de consigna del operador y del centro de control, las señales de habilitación y las alarmas de pérdida de comunicación.
- Verificar el comportamiento de seguridad del PPC ante pérdida de comunicación con los inversores o con la medida, según la especificación funcional.
- Las pruebas de lazo cerrado (control de potencia activa y reactiva, factor de potencia, tensión, rampas, respuesta a frecuencia) se ejecutan en NES-OPE-PR-023 con la planta energizada y con la coordinación del [OPERADOR DE RED] y, si aplica, de XM.

#### 8.2.4.13. Estación meteorológica y sensores (IEC 61724-1)

La clase de monitoreo (Clase A o Clase B de la IEC 61724-1) la fija la especificación del proyecto. Para la Clase A, la norma exige, entre otros, intervalo de muestreo no mayor de 3 s y registro a intervalos no mayores de 1 minuto, y define la cantidad mínima de estaciones y de sensores de temperatura de módulo según la potencia de la planta:

| Potencia de la planta | Estaciones de monitoreo (Clase A) | Sensores de temperatura de módulo (Clase A) |
|---|---|---|
| Menor de 5 MW | 2 | 6 |
| De 5 MW a menos de 40 MW | 2 | 12 |
| De 40 MW a menos de 100 MW | 3 | 18 |
| De 100 MW a menos de 200 MW | 4 | 24 |
| 200 MW o más | Según tabla de la norma — [____] | Según tabla de la norma — [____] |

> NOTA: Las cantidades de la tabla se tomaron de guías técnicas públicas que resumen la IEC 61724-1:2021. Se confirman contra la edición vigente de la norma y contra la especificación del proyecto antes de la compra de sensores.

Ubicación y montaje:

1. Ubicar cada estación en un punto representativo del bloque asignado, sin sombras de estructuras, mástiles, edificaciones ni vegetación durante el día, y sin reflexiones anómalas.
2. Piranómetro en el plano (POA): montarlo en el mismo plano de los módulos. En trackers, sobre el tubo de torsión o sobre un soporte solidario que siga el giro, de modo que mida la irradiancia que reciben los módulos; verificar con inclinómetro digital que su inclinación coincide con la de los módulos en varias posiciones del tracker.
3. Piranómetro horizontal (GHI): nivelar con el nivel de burbuja del propio sensor; orientar el conector y el cable según el fabricante; fijar sin esfuerzos sobre la base.
4. Irradiancia posterior o albedo: cuando los módulos son bifaciales y la especificación lo exige, instalar los sensores de irradiancia posterior o albedómetro en la posición definida por el diseño.
5. Temperatura de módulo: fijar el sensor en la cara posterior del módulo, detrás de una célula próxima al centro del módulo, lejos del marco y de la caja de conexión, con el adhesivo o la cinta térmica del fabricante del sensor; distribuir los sensores en módulos representativos de distintas posiciones del arreglo según el diseño; asegurar el cable para que no tire del sensor con el giro del tracker.
6. Temperatura y humedad ambiente: dentro del protector de radiación, a la altura y en la posición del diseño.
7. Viento: anemómetro y veleta en la parte alta del mástil, orientando la veleta al norte de referencia según el fabricante; la señal de viento que usa el sistema de trackers para la posición de defensa se cablea o comunica según el manual del tracker y se prueba en 8.2.4.15.
8. Mástil: anclado y aterrizado; montaje con permiso de trabajo en alturas cuando aplique (Res. 4272 de 2021).
9. Registrar números de serie, certificados de calibración, clase ISO 9060, orientación e inclinación verificadas en NES-OPE-F-146.

Verificación de medidas:

- Contrastar la lectura de cada piranómetro con un irradiancímetro o célula de referencia calibrada en las mismas condiciones y con los demás sensores de la planta; una diferencia significativa indica error de montaje, de configuración (constante de calibración) o de cableado.
- Verificar que la constante de calibración cargada en el registrador coincide con el certificado de cada piranómetro.
- Verificar la lectura nocturna del piranómetro (cercana a cero) y la coherencia de la curva diaria.
- Verificar la temperatura de módulo frente a un termómetro de contacto y entre sensores.
- Definir con [CLIENTE] el programa de limpieza y de recalibración de los sensores conforme a la clase de monitoreo y al fabricante.

#### 8.2.4.14. Integración de inversores, trackers y equipos eléctricos

1. Verificar la comunicación con cada equipo según el mapa de registros de su fabricante y el protocolo del diseño (por ejemplo Modbus TCP, Modbus RTU, IEC 61850 o el que se especifique).
2. Inversores: estado, alarmas, potencias, energías, medidas DC por entrada o por string si el equipo las ofrece, y consignas del PPC.
3. Trackers: comunicación con el controlador de cada fila o de red, ángulo real frente a ángulo objetivo, modo de operación, alarmas, estado de batería si aplica y comando de posición de defensa, según el manual del tracker del proyecto.
4. Cajas combinadoras monitoreadas: corrientes por string o por entrada y estado del seccionador.
5. Medidores, relés de protección y centros de transformación: medidas, estados de interruptores y seccionadores, alarmas y disparos que el diseño incluya en el SCADA.
6. Verificar que el SCADA detecta y alarma la pérdida de comunicación de cada equipo.

#### 8.2.4.15. Pruebas punto a punto

Cada señal de la lista de señales se prueba desde su origen hasta la pantalla de operación y el histórico:

| Tipo de señal | Método de prueba | Criterio |
|---|---|---|
| Estado digital | Cambiar el estado real en el equipo o simularlo en su bornera. | Cambio correcto en la pantalla, con texto y marca de tiempo coherentes. |
| Alarma | Provocar la condición o simularla. | Alarma con prioridad, texto y registro según la especificación. |
| Medida analógica | Comparar con instrumento patrón o inyectar señal con calibrador en varios puntos de la escala. | Valor, unidad y escala correctos dentro de la exactitud de la especificación. |
| Medida por comunicación | Comparar el valor en pantalla con la pantalla local del equipo. | Igualdad de valor, unidad y signo. |
| Comando | Emitir el comando desde el SCADA en condición segura y verificar la acción en el equipo. | Ejecución correcta y retroaviso del estado. Los comandos que afectan equipos de potencia solo con permiso de maniobra. |

1. Marcar cada señal probada en la lista de señales con fecha y firma.
2. Registrar las señales no conformes y su corrección en NES-OPE-F-147.
3. Para el tracker del proyecto, probar en frío la señal de viento y el comando de posición de defensa con el procedimiento del fabricante y con la zona de las filas despejada.

> ALTO: Un comando de prueba sobre un interruptor, un inversor o un tracker mueve equipos reales. Antes de emitirlo, el ingeniero de SCADA confirma con el responsable del equipo que el área está despejada, que existe permiso de maniobra y que el equipo está en la condición prevista.

#### 8.2.4.16. Ciberseguridad básica

Medidas mínimas en la puesta en marcha, tomando como referencia técnica la IEC 62443:

- Cambiar todas las contraseñas por defecto de switches, PPC, registradores, inversores, servidores y estaciones antes de conectarlos a la red de planta.
- Crear cuentas nominales con el mínimo privilegio necesario; eliminar cuentas genéricas o de prueba al terminar la puesta en marcha.
- Deshabilitar puertos físicos no usados de los switches y servicios no necesarios (por ejemplo, gestión por protocolos no cifrados) cuando el equipo lo permita.
- Mantener la segmentación de 8.2.4.11 y ubicar un cortafuegos en la frontera entre la red de planta y cualquier red externa, con reglas explícitas y documentadas.
- Acceso remoto solo por el medio aprobado por [CLIENTE] (por ejemplo, red privada virtual con autenticación de doble factor), habilitado únicamente cuando se necesite.
- Prohibido conectar a la red de planta computadores o memorias no autorizados; los equipos de configuración se revisan con antivirus actualizado.
- Registrar la versión de firmware de cada equipo y respaldar las configuraciones finales.
- Entregar las credenciales a [CLIENTE] por el medio seguro acordado, nunca escritas en el tablero ni en el dossier impreso.
- Registrar en NES-OPE-F-145.

#### 8.2.4.17. No conformidades

- Cable halado por encima de su tensión máxima, torcido o doblado por debajo del radio mínimo: ensayo OTDR del tramo y decisión del ingeniero de SCADA; si hay daño, reemplazo del tramo y nuevos empalmes.
- Empalme o conector fuera de criterio: rehacer el empalme o reemplazar el pigtail y repetir el ensayo de la fibra completa.
- Enlace fuera del presupuesto de pérdidas: localizar el evento con OTDR, corregir y repetir.
- Sensor fuera de tolerancia o mal montado: corregir montaje o configuración; si persiste, devolución al fabricante con certificado.
- Señal no conforme en la prueba punto a punto: corrección en el origen, en la base de datos o en la pantalla, y repetición de la prueba.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Tensión de tracción del cable | No superior a la máxima de instalación de la ficha técnica — [____] N | Ficha técnica |
| Radio de curvatura | No inferior al de la ficha técnica con y sin carga (referencia típica 20 y 10 veces el diámetro) | Ficha técnica |
| Reserva de cable | La del diseño en cada caja y extremo — [____] m | Diseño |
| Pérdida por empalme (OTDR bidireccional) | No mayor de 0,3 dB o el valor más exigente del proyecto — [____] dB | ANSI/TIA-568.3 / Especificación del proyecto |
| Pérdida por par de conectores | No mayor de 0,75 dB o el valor del proyecto — [____] dB | ANSI/TIA-568.3 / Especificación del proyecto |
| Pérdida de inserción del enlace | No mayor que el presupuesto calculado | IEC 61280-4-2 / Este procedimiento |
| Cara de conectores | Conforme a la IEC 61300-3-35 antes de conectar | IEC 61300-3-35 |
| Redundancia del anillo | Comunicación mantenida ante apertura de un enlace; recuperación dentro de la especificación — [____] ms | Especificación del proyecto |
| Sincronización de tiempo | Todos los equipos sincronizados con la fuente de diseño, dentro de la tolerancia especificada | Especificación del proyecto |
| Monitoreo meteorológico | Clase de la IEC 61724-1 cumplida: sensores, cantidad, muestreo y registro | IEC 61724-1 |
| Piranómetro POA | Inclinación coincidente con el plano de los módulos; constante de calibración del certificado cargada | IEC 61724-1 / Fabricante |
| Piranómetro horizontal | Nivelado con su nivel de burbuja | Fabricante |
| Sensor de temperatura de módulo | Fijado detrás de célula, lejos de marco y caja de conexión, con adhesivo del fabricante | IEC 61724-1 / Fabricante |
| Pruebas punto a punto | 100 % de las señales de la lista probadas y conformes | Especificación del proyecto |
| Ciberseguridad | Contraseñas por defecto cambiadas, puertos no usados deshabilitados, segmentación y respaldo de configuraciones | IEC 62443 (referencia) / Especificación del proyecto |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-140 a NES-OPE-F-149 de este procedimiento.
- Certificados de fábrica de bobinas de fibra; archivos de traza de OTDR y resultados de pérdida de inserción por fibra.
- Diagrama de empalmes y planos de tableros según lo construido.
- Lista de señales firmada con el resultado de las pruebas punto a punto.
- Respaldos de configuración y versiones de firmware, entregados por medio seguro.
- Certificados de calibración de piranómetros, sensores, OTDR, medidores y calibradores.

## 8.5. Control de calidad

QA/QC verifica el 100 % de las fibras de cada enlace con OTDR bidireccional y pérdida de inserción, el 100 % de los conectores con inspección de cara antes de conectar y el 100 % de las señales de la lista con prueba punto a punto. Los puntos de espera y de testigo de [CLIENTE] son los del PIE eléctrico NES-CAL-PLN-003. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación que no afecta funcionamiento ni seguridad, por ejemplo rotulación incompleta. | Registro y cierre. |
| 2 | Empalme, conector, señal o sensor fuera de criterio, corregible con el método de este procedimiento. | Corrección y repetición del ensayo. |
| 3 | Afecta la disponibilidad del control de la planta, la ciberseguridad o los requisitos del operador: cable dañado en tramo largo, anillo sin redundancia, PPC sin medida válida. | Suspensión del frente, consulta al diseñador y aprobación escrita antes de actuar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS/ART y la charla diaria, verifica que las áreas intervenidas estén señalizadas y demarcadas y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre fragmentos de fibra, radiación láser, sustancias químicas, zanjas y cajas de paso, trabajo en alturas y riesgo eléctrico en tableros.

## 9.1. Reglas de oro

- **NUNCA** miraré el extremo de una fibra o de un conector sin confirmar que no está iluminada; usaré microscopio con filtro.
- **SIEMPRE** depositaré cada fragmento de fibra en el recipiente previsto y nunca lo dejaré sobre la mesa, la ropa o el suelo.
- **NUNCA** comeré, beberé ni fumaré en el puesto de empalme.
- **SIEMPRE** usaré gafas de seguridad al pelar, cortar y empalmar fibra.
- **NUNCA** me ubicaré en la línea de la cinta o del cable bajo tensión durante el tendido.
- **SIEMPRE** aplicaré las cinco reglas de oro y el bloqueo y etiquetado antes de intervenir un tablero alimentado (Res. 5018 de 2019).
- **NUNCA** emitiré un comando de prueba sobre un equipo de potencia o un tracker sin permiso de maniobra y área despejada.
- **SIEMPRE** usaré arnés y línea de vida certificados al trabajar en mástiles o postes a 2 m o más.
- **SIEMPRE** suspenderé la actividad ante tormenta eléctrica y me alejaré de mástiles, estructuras y tableros.
- **SIEMPRE** ejecutaré el trabajo con ATS/ART y los permisos que correspondan diligenciados.

## 9.2. Condiciones climáticas de [departamento]

- Tormenta eléctrica: el mástil de la estación meteorológica, los tableros y los trackers atraen descargas. Ante el aviso o el primer trueno, suspender, bajar del mástil y dirigirse al refugio. Se reanuda solo con autorización del responsable SST.
- Lluvia: suspender empalmes, apertura de cajas de empalme y ODF y montaje de sensores; sellar extremos de cable y cajas abiertas; no ingresar a cajas de paso inundadas.
- Calor y radiación: el puesto de empalme se instala bajo carpa; hidratación, sombra, pausas y rotación; los equipos de ensayo se protegen del sol directo para evitar su sobrecalentamiento.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado y descargue de bobinas | Volcamiento de bobina, atrapamiento, sobreesfuerzo. | Equipo mecánico; bobina vertical sobre su eje; prohibido rodarla desde la plataforma; 25 kg máximo por persona (Res. 2400 de 1979, art. 392). |
| 2. Preparación de ruta y cajas de paso | Caída a zanja o caja, atmósfera peligrosa en cámaras, ofidios. | Señalización y protección de bordes; evaluación de espacio confinado y medición de atmósfera (Res. 0491 de 2020); revisión previa de fauna. |
| 3. Tendido del cable | Latigazo de cinta o cable, atrapamiento en rodillos y malacate, sobreesfuerzo. | Nadie en la línea de tracción; guardas en rodillos; radios de comunicación; tensión limitada. |
| 4. Preparación del cable | Cortes con herramientas, contacto con gel. | Herramienta de pelado adecuada; guantes de nitrilo; corte alejándose del cuerpo. |
| 5. Pelado, corte y empalme | Fragmentos de fibra en piel, ojos o ingestión; quemadura con horno. | Gafas; recipiente para fragmentos; tapete oscuro; prohibido comer; lavado de manos; no tocar el horno caliente. |
| 6. Uso de alcohol isopropílico y limpiadores | Incendio, irritación, inhalación. | Hoja de seguridad y etiqueta SGA (Decreto 1496 de 2018); envase pequeño y cerrado; lejos de chispas y del arco de la empalmadora en uso. |
| 7. Ensayos ópticos | Exposición del ojo a radiación láser invisible. | No mirar extremos; microscopio con filtro; tapas en conectores; fuente apagada al desconectar (IEC 60825-2). |
| 8. Montaje y energización de tableros | Choque eléctrico, arco, cortes. | Permiso de trabajo; LOTO; verificación de ausencia de tensión; EPP dieléctrico y de arco; personal con matrícula. |
| 9. Montaje de mástil y sensores | Caída de altura, caída de objetos, descarga atmosférica. | Res. 4272 de 2021; arnés y línea de vida; zona inferior delimitada; herramienta amarrada; no trabajar con tormenta. |
| 10. Montaje de sensores sobre trackers | Atrapamiento por movimiento del tracker, cortes con bordes. | Tracker bloqueado o en modo manual según el manual del fabricante; LOTO del controlador; guantes. |
| 11. Pruebas punto a punto y de comandos | Movimiento imprevisto de equipos, maniobra no autorizada. | Permiso de maniobra; área despejada confirmada por radio; coordinación con el responsable del equipo. |
| 12. Configuración y ciberseguridad | Acceso no autorizado, pérdida de configuración. | Equipos autorizados; cuentas nominales; respaldo; credenciales por medio seguro. |
| 13. Exposición ambiental | Radiación UV, estrés térmico, deshidratación, ofidios. | Ropa manga larga, cubrenuca, protector solar, hidratación, sombra, pausas; polainas. |
| 14. Tormenta eléctrica y lluvia | Descarga atmosférica, choque eléctrico, ingreso de agua a cajas. | Suspender; bajar de mástiles; sellar cables y cajas; refugio o punto de encuentro. |
| 15. Orden, aseo y residuos | Fragmentos de fibra en el área, tropiezos, contaminación. | Recipientes rotulados; limpieza del puesto de empalme con cinta adhesiva; área despejada al cierre. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Aire | Emisiones y ruido | Vehículos y malacates con revisión técnico-mecánica y mantenimiento al día; motores apagados en reposo; humectación de vías en época seca. |
| Suelo | Residuos sólidos | Separación en la fuente con el código de colores de la Res. 2184 de 2019; carretes, cartón, plásticos y embalajes de equipos a aprovechamiento; entrega a gestores autorizados. |
| Suelo | Fragmentos de fibra | Recipiente rígido rotulado con tapa; disposición como residuo no aprovechable cortopunzante con gestor autorizado; nunca en el terreno ni en la basura común abierta. |
| Suelo | Retazos de cable | Recolección diaria; retazos con elementos metálicos a aprovechamiento; entrega a gestor autorizado. |
| Suelo | RESPEL | Envases de alcohol isopropílico y limpiadores, paños con gel o solvente, en recipientes rotulados; almacenamiento temporal en zona RESPEL y entrega a gestor autorizado con certificado (Decreto 1076 de 2015). |
| Suelo | RAEE | Equipos de red, fuentes, baterías de sistemas de respaldo y sensores dañados o retirados se gestionan como RAEE (Ley 1672 de 2013) o por programa posconsumo. |
| Suelo | RCD | Gestión según Res. 0472 de 2017 modificada por Res. 1257 de 2021 cuando el tendido genere material sobrante de zanjas. |
| Flora y fauna | Intervención de hábitat | Trabajar solo en áreas liberadas; revisar fauna en cajas de paso, ductos y tableros antes de intervenir; reporte para rescate según PMA. |
| Agua | Escorrentía y cajas inundadas | No bombear agua de cajas de paso hacia cuerpos de agua sin autorización; uso racional del agua. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con el Plan de emergencias NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener la actividad y asegurar la zona: detener el malacate o la tracción, desenergizar el tablero intervenido o apagar la fuente láser.
2. Notificar al responsable SST, al ingeniero de SCADA y al interlocutor de [CLIENTE].
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, lavaojos, extintor en cada frente).
4. Incidente grave: activar ambulancia y traslado al centro asistencial definido; notificar a la ARL.
5. Reportar el evento e investigarlo según la Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Fragmento de fibra en ojos, piel o ingestión

- Ojo: no frotar; lavar con abundante agua limpia o solución del lavaojos durante varios minutos; cubrir con apósito limpio y remitir a valoración oftalmológica.
- Piel: retirar el fragmento visible con cinta adhesiva o pinza, sin presionar; lavar con agua y jabón; si queda incrustado, remitir a valoración.
- Ingestión: no provocar el vómito; remitir a valoración médica inmediata.

## 12.2. Exposición a radiación láser

- Apagar la fuente y retirar a la persona del punto de exposición.
- No frotar los ojos; remitir a valoración oftalmológica aunque no haya síntomas inmediatos, informando la longitud de onda y el equipo involucrado.

## 12.3. Caída en zanja, caja de paso o desde mástil

- No mover a la víctima si hay sospecha de lesión de columna; inmovilizar con camilla rígida.
- En caja de paso o cámara que sea espacio confinado, el rescate lo ejecuta solo personal entrenado con el plan de rescate del permiso (Res. 0491 de 2020).
- Caída suspendida en arnés: activar el plan de rescate en alturas de inmediato para limitar el tiempo en suspensión.

## 12.4. Choque eléctrico en tablero

- No tocar a la víctima mientras siga en contacto; cortar la fuente o separarla con elemento aislante; activar la emergencia y aplicar reanimación si el personal está capacitado.
- Toda persona que sufra un choque eléctrico se remite a valoración médica aunque se sienta bien.

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Ingeniero de SCADA y comunicaciones Neptuno Energy Services | [__________] | [__________] |
| Residente de obra Neptuno Energy Services | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| Centro de control / sala de operación | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Recepción de materiales y equipos de comunicaciones | NES-OPE-F-140 | Supervisor / QA/QC |
| Tendido de cable de fibra óptica | NES-OPE-F-141 | Supervisor |
| Protocolo de empalmes y cierre de caja de empalme u ODF | NES-OPE-F-142 | Técnico empalmador |
| Registro de ensayos OTDR y pérdida de inserción | NES-OPE-F-143 | Técnico empalmador / Ingeniero de SCADA |
| Inspección de montaje de tablero de comunicaciones | NES-OPE-F-144 | Técnico electricista / QA/QC |
| Configuración de red y ciberseguridad | NES-OPE-F-145 | Ingeniero de SCADA |
| Instalación de estación meteorológica y sensores | NES-OPE-F-146 | Técnico de instrumentación / QA/QC |
| Prueba punto a punto de señales | NES-OPE-F-147 | Ingeniero de SCADA |
| Pruebas funcionales en frío de SCADA y PPC | NES-OPE-F-148 | Ingeniero de SCADA |
| Acta de entrega del sistema SCADA y comunicaciones | NES-OPE-F-149 | Residente de obra |
| ATS/ART, permisos de trabajo, alturas, excavación y espacio confinado | Según NES-SST-PR-001 | Responsable SST |
| Certificados de bobinas, calibración y conformidad | — | QA/QC |

\pagebreak

# 14. ANEXOS

## NES-OPE-F-140 — Recepción de materiales y equipos de comunicaciones

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Remisión / orden de compra: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-021 | Proveedor: [__________] |

| Ítem | Material / equipo | Referencia y serie o bobina | Cantidad | Certificado | Estado | Obs. |
|---|---|---|---|---|---|---|
| 1 | Cable de fibra óptica |  |  |  |  |  |
| 2 | Cajas de empalme |  |  |  |  |  |
| 3 | ODF, pigtails y adaptadores |  |  |  |  |  |
| 4 | Switches y transceptores |  |  |  |  |  |
| 5 | PPC / RTU / registrador |  |  |  |  |  |
| 6 | Piranómetros |  |  |  |  |  |
| 7 | Sensores de temperatura y meteorológicos |  |  |  |  |  |
| 8 | Fuentes, UPS y DPS de señal |  |  |  |  |  |

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

## NES-OPE-F-141 — Tendido de cable de fibra óptica

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Enlace / tramo: [__________] desde [____] hasta [____] | Consecutivo: [____] |
| Bobina N.º: [____] | Tipo y número de fibras: [__________] |
| Tensión máxima de instalación (ficha): [____] N | Radio mínimo con carga / sin carga: [____] / [____] mm |
| Marca métrica inicial: [____] m | Marca métrica final: [____] m |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Ducto verificado con mandril y sin obstrucciones |  |  |  |
| 2 | Rodillos y poleas con radio no menor que el mínimo con carga |  |  |  |
| 3 | Tracción por elemento de tracción con destorcedor |  |  |  |
| 4 | Tensión máxima registrada: [____] N, no superior a la de ficha |  |  |  |
| 5 | Sin torsión ni dobleces bajo el radio mínimo |  |  |  |
| 6 | Figura de ocho en puntos intermedios (si aplica) |  |  |  |
| 7 | Reservas dejadas según diseño en cajas y extremos |  |  |  |
| 8 | Profundidad, relleno y cinta de advertencia en zanja (si aplica) |  |  |  |
| 9 | Extremos y bocas de ducto sellados |  |  |  |
| 10 | Rotulación en cajas de paso y extremos |  |  |  |

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

## NES-OPE-F-142 — Protocolo de empalmes y cierre de caja de empalme u ODF

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Caja de empalme / ODF: [__________] | Consecutivo: [____] |
| Cable de entrada: [__________] | Cable de salida: [__________] |
| Empalmadora (serie / último mantenimiento): [__________] | Diagrama de empalmes: [__________] |

| Bandeja / posición | Fibra entrada (tubo / color) | Fibra salida (tubo / color) | Pérdida estimada (dB) | Manguito OK | Obs. |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

{.plain}
| Elemento de tracción anclado: Sí / No | Sello de entradas y tapa: Sí / No |
|---|---|
| Reserva de fibra sin curvas cerradas: Sí / No | Puertos rotulados y con tapa antipolvo: Sí / No |

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

## NES-OPE-F-143 — Registro de ensayos OTDR y pérdida de inserción

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Enlace: [__________] desde [____] hasta [____] | Consecutivo: [____] |
| Longitud del enlace: [____] m | Empalmes / pares de conectores: [____] / [____] |
| OTDR (serie / calibración): [__________] | Fuente y medidor (serie / calibración): [__________] |
| Bobina de lanzamiento / recepción: [____] / [____] m | Método de referencia de pérdida de inserción: [__________] |
| Presupuesto a 1.310 nm: [____] dB | Presupuesto a 1.550 nm: [____] dB |

| Fibra | Longitud OTDR (m) | Máx. empalme bidireccional (dB) | Máx. conector (dB) | Pérdida inserción 1.310 nm (dB) | Pérdida inserción 1.550 nm (dB) | Cumple |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |
| 9 |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |
| 11 |  |  |  |  |  |  |
| 12 |  |  |  |  |  |  |

{.plain}
| Inspección de cara de conectores (IEC 61300-3-35) conforme: Sí / No | Archivos de traza guardados en: [__________] |
|---|---|

{.plain}
| Observaciones (eventos no previstos, macrocurvaturas, fibras rechazadas): |
|---|

| Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |  |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-144 — Inspección de montaje de tablero de comunicaciones

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Tablero: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-021 / NES-SST-PR-001 | Plano de disposición: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Tablero anclado, nivelado y con grado IP de diseño |  |  |  |
| 2 | Puesta a tierra del tablero conectada a la red del bloque |  |  |  |
| 3 | Pantallas de cables aterrizadas según criterio de diseño |  |  |  |
| 4 | DPS de alimentación y de señal instalados |  |  |  |
| 5 | Fuente DC con polaridad y tensión verificadas |  |  |  |
| 6 | Autonomía del respaldo de energía: [____] min |  |  |  |
| 7 | Ventilación o climatización operativa |  |  |  |
| 8 | Switches, convertidores y ODF según plano |  |  |  |
| 9 | Apriete de bornes y orden del cableado |  |  |  |
| 10 | Rotulación de equipos, puertos y cables |  |  |  |
| 11 | Plano de disposición y conexionado dentro del tablero |  |  |  |
| 12 | Energización con permiso de trabajo y LOTO |  |  |  |

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

## NES-OPE-F-145 — Configuración de red y ciberseguridad

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Red / anillo: [__________] | Consecutivo: [____] |
| Plan de direccionamiento IP (versión): [____] | Protocolo de redundancia: [__________] |

| Equipo | Dirección IP | Firmware | Configuración respaldada | Contraseña por defecto cambiada | Puertos no usados deshabilitados | Obs. |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Anillo cerrado con un único enlace bloqueado |  |  |  |
| 2 | Recuperación ante apertura de enlace: [____] ms |  |  |  |
| 3 | VLAN y segmentación según diseño |  |  |  |
| 4 | Sincronización de tiempo en todos los equipos |  |  |  |
| 5 | Cortafuegos en frontera con reglas documentadas |  |  |  |
| 6 | Acceso remoto por el medio aprobado y deshabilitado si no se usa |  |  |  |
| 7 | Cuentas nominales; cuentas de prueba eliminadas |  |  |  |
| 8 | Credenciales entregadas por medio seguro |  |  |  |

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

## NES-OPE-F-146 — Instalación de estación meteorológica y sensores

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Estación / bloque: [__________] | Consecutivo: [____] |
| Clase de monitoreo IEC 61724-1: A / B | Registrador (serie): [__________] |
| Muestreo: [____] s | Intervalo de registro: [____] min |

| Sensor | Serie | Clase / certificado | Posición | Inclinación u orientación verificada | Constante cargada | Contraste OK |
|---|---|---|---|---|---|---|
| Piranómetro POA 1 |  |  |  |  |  |  |
| Piranómetro POA 2 |  |  |  |  |  |  |
| Piranómetro GHI |  |  |  |  |  |  |
| Irradiancia posterior / albedo |  |  |  |  |  |  |
| Temperatura de módulo 1 |  |  |  |  |  |  |
| Temperatura de módulo 2 |  |  |  |  |  |  |
| Temperatura de módulo 3 |  |  |  |  |  |  |
| Temperatura y humedad ambiente |  |  |  |  |  |  |
| Viento (velocidad y dirección) |  |  |  |  |  |  |

{.plain}
| Sin sombras ni reflexiones durante el día: Sí / No | Mástil anclado y aterrizado: Sí / No |
|---|---|
| Señal de viento al sistema de trackers verificada: Sí / No | Programa de limpieza y recalibración acordado: Sí / No |

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

## NES-OPE-F-147 — Prueba punto a punto de señales

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Equipo / sistema: [__________] | Consecutivo: [____] |
| Lista de señales (versión): [____] | Instrumento patrón / calibrador: [__________] |

| N.º señal | Descripción | Tipo (DI / AI / DO / com.) | Valor en origen | Valor en SCADA | Cumple | Obs. |
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
| Señales probadas: [____] | Señales no conformes: [____] |
|---|---|
| Comandos ejecutados con permiso de maniobra N.º: [____] | Pérdida de comunicación alarmada: Sí / No |

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

## NES-OPE-F-148 — Pruebas funcionales en frío de SCADA y PPC

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Sistema: [__________] | Consecutivo: [____] |
| Especificación funcional (versión): [____] | Documento de referencia: NES-OPE-PR-021 |

| Ítem | Prueba | Resultado | Cumple | No cumple | Obs. |
|---|---|---|---|---|---|
| 1 | Comunicación con todos los inversores |  |  |  |  |
| 2 | Comunicación con controladores de trackers |  |  |  |  |
| 3 | Comunicación con medidores, relés y centros de transformación |  |  |  |  |
| 4 | Medida del punto de conexión en el PPC: relación y polaridad |  |  |  |  |
| 5 | Escritura de consignas del PPC en modo de prueba sin inyección |  |  |  |  |
| 6 | Entradas de consigna del operador y del centro de control |  |  |  |  |
| 7 | Comportamiento ante pérdida de comunicación |  |  |  |  |
| 8 | Alarmas, eventos e históricos con marca de tiempo |  |  |  |  |
| 9 | Datos meteorológicos en pantalla e histórico |  |  |  |  |
| 10 | Informes y exportación de datos según especificación |  |  |  |  |
| 11 | Arranque del sistema tras corte de alimentación |  |  |  |  |

{.plain}
| Pendientes para pruebas en caliente (NES-OPE-PR-023): |
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

\pagebreak

## NES-OPE-F-149 — Acta de entrega del sistema SCADA y comunicaciones

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Alcance entregado: [__________] | Consecutivo: [____] |

| Ítem | Entregable | Registro | Conforme | Obs. |
|---|---|---|---|---|
| 1 | Red de fibra ensayada al 100 % | NES-OPE-F-143 |  |  |
| 2 | Diagrama de empalmes y rutas según lo construido | Planos |  |  |
| 3 | Tableros montados y energizados | NES-OPE-F-144 |  |  |
| 4 | Red configurada y medidas de ciberseguridad aplicadas | NES-OPE-F-145 |  |  |
| 5 | Estaciones meteorológicas instaladas y contrastadas | NES-OPE-F-146 |  |  |
| 6 | Lista de señales probada al 100 % | NES-OPE-F-147 |  |  |
| 7 | Pruebas funcionales en frío conformes | NES-OPE-F-148 |  |  |
| 8 | Respaldos de configuración y versiones de firmware | Medio seguro |  |  |
| 9 | Credenciales entregadas | Medio seguro |  |  |
| 10 | Manuales, certificados de calibración y garantías | Dossier |  |  |

{.plain}
| Declaración: el sistema SCADA y de comunicaciones del alcance indicado fue instalado y probado en frío según NES-OPE-PR-021. Las pruebas en caliente del PPC y las exigidas por el operador se ejecutan en NES-OPE-PR-023. |
|---|

{.plain}
| Observaciones y pendientes: |
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
