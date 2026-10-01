---
code: NES-OPE-PR-023
header_title: PROCEDIMIENTO DE ENERGIZACIÓN Y PUESTA EN SERVICIO
cover_title: Procedimiento de Energización y Puesta en Servicio
cover_subtitle: Energización por etapas de plantas fotovoltaicas conectadas al SIN
---

# 1. OBJETIVO

Definir la secuencia, los prerrequisitos, la organización de la maniobra, los controles de calidad y las medidas preventivas para la primera energización y la puesta en servicio de la planta FV [PROYECTO]: desde la verificación documental previa y la autorización escrita del [OPERADOR DE RED], pasando por la energización por etapas de la red de media tensión interna, los centros de transformación y los inversores, hasta las pruebas en caliente, las pruebas del controlador de planta (PPC), las pruebas de desempeño y la entrega a operación, conforme al RETIE, a la regulación de la CREG, a los acuerdos del Consejo Nacional de Operación (CNO) y a las instrucciones de los fabricantes de los equipos.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, en especial el contacto eléctrico, el arco eléctrico en media tensión y la energización accidental de circuitos con personal trabajando.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services, a sus subcontratistas y a los representantes de los fabricantes que participen en:

- Verificación de los prerrequisitos documentales, técnicos y regulatorios de la energización.
- Planificación de la energización: plan de maniobras, órdenes de maniobra, cronograma de pruebas de puesta en servicio y reuniones de coordinación.
- Cambio de estado de las áreas de la planta de "en construcción" a "energizado", con su señalización y control de acceso.
- Energización del punto de conexión y de la celda o subestación de llegada, cuando la ejecute Neptuno Energy Services o participe en ella.
- Energización de la red de media tensión interna por circuitos, de los centros de transformación y de los inversores.
- Pruebas en caliente: verificación de fases y secuencia, protecciones y medida con tensión y con carga, supervisión SCADA y funcionamiento del PPC.
- Pruebas de desempeño y de capacidad previstas en el contrato y en la regulación aplicable.
- Desenergización programada y de emergencia durante la etapa de puesta en servicio.
- Entrega de la planta, o de cada etapa, a operación.

No incluye las pruebas en frío del generador fotovoltaico, de los cables y de los equipos, que se rigen por NES-OPE-PR-022 Pruebas y comisionado del generador FV y por los procedimientos de montaje NES-OPE-PR-015 a NES-OPE-PR-021; ni los trámites comerciales y regulatorios que son responsabilidad del [PROPIETARIO] o de su agente generador representante ante el operador del sistema (XM), en los que Neptuno Energy Services solo aporta la información técnica y la ejecución en campo que se le asigne.

> NOTA: El régimen general de permisos de trabajo y de bloqueo y etiquetado está en NES-SST-PR-001. Este procedimiento lo desarrolla para la energización y no lo sustituye: ante discrepancia, manda el criterio más restrictivo.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / ART y PT | Análisis de trabajo seguro / análisis de riesgo del trabajo y permiso de trabajo. |
| Energización | Primera aplicación de tensión a un equipo o circuito nuevo desde una fuente del sistema o desde el propio generador. A partir de ese instante el equipo se trata como energizado de forma permanente. |
| Líder de energización | Ingeniero electricista con matrícula profesional vigente, designado por escrito, que dirige y autoriza cada maniobra de la energización. Es la única voz de mando de la maniobra. |
| Plan de maniobras | Documento aprobado que define la secuencia completa de energización por etapas, los equipos, los estados de cada elemento, las verificaciones y los puntos de espera. |
| Orden de maniobra | Instrucción escrita y numerada, derivada del plan de maniobras, que contiene los pasos de una maniobra concreta, el ejecutante, el verificador y la hora de cada paso. |
| Área energizada | Zona de la planta declarada formalmente con tensión, con señalización, control de acceso y régimen obligatorio de permiso de trabajo eléctrico. |
| Consignación | Procedimiento por el cual se programa, autoriza y coordina con el operador de red o con el operador del sistema la indisponibilidad o la maniobra de un equipo o activo del sistema. |
| Punto de conexión | Punto en que la planta se conecta a la red del [OPERADOR DE RED] o del transportador, definido en el concepto de conexión. |
| PPS | Pruebas de puesta en servicio: periodo anterior a la entrada en operación comercial durante el cual se energiza el proyecto y se verifican el funcionamiento de los equipos y el cumplimiento de los requisitos de conexión. |
| FPO / FDOC | Fecha de puesta en operación y fecha de declaración en operación comercial del proyecto. |
| CND | Centro Nacional de Despacho, a cargo de XM como operador del sistema. |
| Agente generador representante | Agente del mercado designado por el [PROPIETARIO] para tramitar ante XM los requisitos de entrada en operación y declarar la operación comercial. |
| EACP | Estudio de ajuste y coordinación de protecciones del proyecto, aprobado por quien entrega el punto de conexión y, cuando aplica, con visto bueno del CND. |
| PPC | Controlador de planta: sistema que regula en el punto de conexión la potencia activa, la potencia reactiva, la tensión y el factor de potencia mediante consignas a los inversores. |
| Frontera comercial | Punto de medida de energía registrado ante el administrador del mercado, con medidor y transformadores de medida que cumplen el código de medida. |
| Verificación de fases (faseo) | Comprobación de que cada fase de un circuito coincide con la fase correspondiente del circuito o barra al que se conecta, antes de cerrar un punto de unión. |
| Secuencia de fases | Orden de rotación de las tensiones trifásicas (L1-L2-L3). Debe coincidir con la de la red en todo el sistema. |
| Remojo (energización en vacío) | Periodo en que un equipo permanece energizado sin carga, bajo observación, antes de conectar la siguiente etapa. |
| Desenergización de emergencia | Apertura inmediata del interruptor de la etapa afectada, o del interruptor general, ante una condición anormal que pone en riesgo personas o equipos. |
| Cinco reglas de oro | Cortar todas las fuentes, bloquear, verificar ausencia de tensión, poner a tierra y en cortocircuito, y señalizar la zona. |
| LOTO | Bloqueo y etiquetado de dispositivos de maniobra, con candado y tarjeta de quien ejecuta el trabajo. |
| Curva PQ | Curva de capacidad de potencia reactiva en función de la potencia activa de la planta en el punto de conexión. |
| LVRT / HVRT | Capacidad de permanecer conectado ante depresiones de tensión (LVRT) y sobretensiones (HVRT). |
| SOE | Registro secuencial de eventos con estampa de tiempo. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. El punto de conexión, la subestación o celda de llegada, los circuitos de media tensión, los centros de transformación y los inversores se identifican según el plano general de implantación [N° de plano], el diagrama unifilar general [N° de plano] y la nomenclatura operativa aprobada por el [OPERADOR DE RED] [N° de documento].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados. Los requisitos del operador de red y del operador del sistema dependen de la clase de proyecto, del nivel de tensión y de la capacidad: se confirman con el [PROPIETARIO] y el [OPERADOR DE RED] antes de elaborar el plan de maniobras.

## 5.1. Documentales

- Concepto de conexión, contrato de conexión y requisitos técnicos del [OPERADOR DE RED] para la puesta en servicio — [N° de documento].
- Diagrama unifilar general con nomenclatura operativa, planos de la subestación o celda de llegada, de la red MT interna y de los centros de transformación — [N° de plano].
- Estudio de ajuste y coordinación de protecciones (EACP) aprobado y tabla de ajustes de cada relé — [N° de documento].
- Protocolos de pruebas en frío aprobados de NES-OPE-PR-022 y de los procedimientos de montaje NES-OPE-PR-015 a NES-OPE-PR-021.
- Dictamen de inspección RETIE de la instalación, o el documento de conformidad que exija el RETIE para la etapa a energizar.
- Manuales de instalación, puesta en marcha y operación de inversores, transformadores, celdas MT, PPC y sistema SCADA, emitidos por sus fabricantes.
- Plan de maniobras y órdenes de maniobra aprobadas por [CLIENTE] y, cuando aplique, por el [OPERADOR DE RED].
- NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-CAL-PLN-003 Plan de inspección y ensayos eléctrico; NES-CAL-PLN-002 Plan de calidad.
- Plan de emergencias del proyecto y análisis de riesgo de arco eléctrico de los tableros y celdas — [N° de documento].

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía): requisitos de instalaciones de generación, distancias de seguridad, trabajo en tensión y sin tensión, y demostración de la conformidad de la instalación antes de su puesta en servicio.
- NTC 2050 — Código Eléctrico Colombiano, en los requisitos que el RETIE adopta.
- Ley 143 de 1994 — Ley eléctrica; funciones del Consejo Nacional de Operación.
- Resolución CREG 025 de 1995 — Código de Redes (código de conexión, código de operación y código de medida), con sus modificaciones.
- Resolución CREG 060 de 2019 — Requisitos técnicos y pruebas de las plantas solares fotovoltaicas y eólicas conectadas al STN y al STR (numeral 7.7 del Código de Operación).
- Resolución CREG 075 de 2021 — Disposiciones y procedimientos para la asignación de capacidad de transporte en el SIN.
- Resolución CREG 148 de 2021 — Integración de plantas solares fotovoltaicas y eólicas en el SDL con capacidad igual o mayor a 5 MW.
- Resolución CREG 101-011 de 2022 — Integración de plantas solares fotovoltaicas y eólicas en el SDL con capacidad igual o mayor a 1 MW y menor a 5 MW.
- Resolución CREG 174 de 2021 — Autogeneración a pequeña escala y generación distribuida, cuando aplique.
- Resolución CREG 038 de 2014 — Código de medida, para la frontera comercial.
- Acuerdo CNO 1937 de 2025 — Procedimiento para la declaración de entrada en operación comercial de proyectos de transmisión y de recursos de generación, o el que lo sustituya.
- Acuerdos CNO 1826, 1830 y 1869 de 2024 — Procedimientos de pruebas de control de potencia activa/frecuencia, de control de tensión y de curva de capacidad de plantas solares fotovoltaicas conectadas al STN y al STR, o los que los sustituyan.
- Ley 1264 de 2008 (técnicos electricistas, CONTE); Ley 51 de 1986 y Ley 842 de 2003 (ingenieros, COPNIA).
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019 — Estándares mínimos.
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en los procesos de generación, transmisión, distribución y comercialización de energía eléctrica.
- Resolución 4272 de 2021 — Trabajo en alturas; Resolución 0491 de 2020 — Espacios confinados, cuando aplique a sótanos de celdas o fosos de cables.
- Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo.
- Decreto 1076 de 2015 (RESPEL); Resolución 2184 de 2019 (código de colores); Resolución 0472 de 2017 modificada por la Resolución 1257 de 2021 (RCD).
- Licencia ambiental y Plan de Manejo Ambiental (PMA) del proyecto — [N° de resolución].
- IEC 62446-1 — Documentación, ensayos de puesta en servicio e inspección de sistemas fotovoltaicos conectados a la red.
- IEC 61724-1 — Monitoreo del desempeño de sistemas fotovoltaicos.
- IEC 62271 (aparamenta MT) e IEC 60076 (transformadores de potencia), como referencia técnica de pruebas.
- NFPA 70E, como referencia técnica para el análisis de riesgo de arco y la selección de EPP.
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

- Aprobar y divulgar el presente procedimiento y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.
- Designar por escrito al líder de energización y a los operadores de maniobra autorizados.
- Presentar a [CLIENTE] el expediente de prerrequisitos de cada etapa y obtener su aprobación antes de solicitar la autorización de energización.
- Coordinar con [CLIENTE], el [PROPIETARIO] y el [OPERADOR DE RED] las fechas, las consignaciones y las ventanas de maniobra.
- Detener cualquier maniobra que no cumpla este procedimiento, el plan de maniobras o la instrucción del fabricante.

## 6.2. Líder de energización (ingeniero electricista con matrícula COPNIA vigente)

- Elaborar el plan de maniobras y las órdenes de maniobra, y someterlos a aprobación.
- Verificar uno a uno los prerrequisitos de la etapa con el formato NES-OPE-F-160 y declarar por escrito que la etapa está lista para energizar.
- Dirigir la reunión previa a la maniobra, impartir cada orden de maniobra y ser la única voz de mando durante la energización.
- Declarar el cambio de estado de las áreas a "energizado" y autorizar su señalización y control de acceso.
- Suspender la maniobra y ordenar la desenergización ante cualquier condición anormal.
- Firmar los registros de energización, de pruebas en caliente y el acta de entrega a operación.

## 6.3. Operador de maniobra (técnico electricista con matrícula CONTE vigente)

- Ejecutar las maniobras solo por orden del líder de energización, repitiendo la orden en voz alta antes de ejecutarla y confirmando su ejecución.
- Verificar la posición de cada equipo (abierto, cerrado, puesto a tierra) en el equipo y en la señalización del tablero o del SCADA.
- Colocar y retirar candados y tarjetas de maniobra según NES-SST-PR-001.

## 6.4. Ingeniero de protecciones y medida

- Verificar que los ajustes implementados en cada relé coinciden con el EACP aprobado y dejar registro firmado de la versión cargada.
- Ejecutar las verificaciones de protecciones con tensión y con carga: magnitudes, ángulos, direccionalidad y estabilidad.
- Verificar la medida de la frontera comercial y de los equipos de medición de calidad de potencia.

## 6.5. Especialista SCADA y PPC

- Verificar la supervisión de cada señal en el SCADA y su coherencia con la medida en campo.
- Ejecutar las pruebas funcionales del PPC y apoyar las pruebas exigidas por el operador del sistema cuando apliquen.
- Coordinar con el [PROPIETARIO] las pruebas de comunicación con el centro de control del [OPERADOR DE RED] y, cuando aplique, con el CND.

## 6.6. Representantes de los fabricantes

- Ejecutar o supervisar la puesta en marcha de su equipo según su protocolo, cuando la garantía lo exija.
- Entregar el informe de puesta en marcha y los parámetros cargados en el equipo.

## 6.7. Responsable de calidad (QA/QC)

- Verificar que todos los protocolos de pruebas en frío de la etapa estén aprobados y que no existan pendientes que impidan energizar.
- Controlar el cumplimiento del Plan de Inspección y Ensayos y los puntos de espera de este procedimiento.
- Registrar y hacer seguimiento a las no conformidades y a la lista de pendientes hasta su cierre.

## 6.8. Responsable SST

- Verificar el análisis de riesgo de arco, el EPP con categoría de arco, las distancias de seguridad y la señalización de las áreas energizadas.
- Verificar que no haya personal dentro de las áreas a energizar antes de cada maniobra.
- Liderar el plan de emergencias de la energización y aplicar el protocolo de tormenta eléctrica.

## 6.9. Responsable ambiental

- Asegurar el cumplimiento del PMA durante la energización y las pruebas.
- Verificar la contención de aceite de los transformadores y la disponibilidad de kits antiderrame.

## 6.10. [CLIENTE] y [PROPIETARIO]

- Aprobar el plan de maniobras y el expediente de prerrequisitos.
- Tramitar por sí o por su agente generador representante la autorización del [OPERADOR DE RED], las consignaciones y los requisitos ante XM que apliquen al proyecto.

## 6.11. Trabajadores

- Cumplir este procedimiento, respetar la señalización de áreas energizadas y participar en el ATS/ART.
- Usar correctamente el EPP asignado y no ingresar a un área energizada sin permiso de trabajo eléctrico.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Líder de energización, operadores de maniobra, ingeniero de protecciones, especialista SCADA/PPC, representantes de fabricantes, QA/QC, responsable SST, brigadistas. Todo el personal que maniobra está calificado, con matrícula vigente y autorizado por escrito. |
| Documentos | Expediente de energización | Plan de maniobras aprobado, órdenes de maniobra, unifilar con nomenclatura operativa, EACP y tablas de ajustes, protocolos en frío aprobados, autorización escrita del [OPERADOR DE RED], dictamen RETIE. |
| Equipos | Medida | Detectores de tensión MT para el nivel de tensión del sistema; multímetro y pinza CAT III o superior; secuencímetro; comparador de fases MT; analizador de redes y calidad de potencia; maleta de inyección secundaria; termógrafo. Todos con certificado de calibración vigente. |
| Equipos | Puesta a tierra temporal | Equipos de puesta a tierra y en cortocircuito para MT, de la sección y corriente de cortocircuito del sistema, con pértiga aislante y certificado vigente. |
| Equipos | LOTO y señalización | Kit LOTO con candados personales y de maniobra, tarjetas de "energizado" y "no operar", cinta y cadena de demarcación, avisos de riesgo eléctrico, conos y barreras. |
| Equipos | Comunicaciones | Radios con canal exclusivo para la maniobra, teléfono satelital o celular de respaldo, línea operativa con el centro de control del [OPERADOR DE RED]. |
| Equipos | Emergencia | Extintores aptos para equipo eléctrico en cada centro de transformación y en la celda de llegada, botiquín, camilla rígida, desfibrilador externo automático, kit antiderrame. |
| EPP | Trabajo eléctrico | Ropa y careta o capucha con la categoría de arco que indique el análisis de riesgo; guantes dieléctricos de la clase del nivel de tensión con guante de cuero de protección; calzado dieléctrico; pértiga aislante; sin elementos metálicos personales. |
| EPP | Básico | Casco dieléctrico con barbuquejo, gafas, protección auditiva, chaleco reflectivo, ropa manga larga ignífuga, protector solar, polainas en zonas con presencia de ofidios. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

La energización se ejecuta por etapas y cada etapa tiene su propio expediente de prerrequisitos. Ninguna etapa se energiza si alguno de los prerrequisitos de la tabla siguiente no está cumplido y documentado en el formato NES-OPE-F-160.

| Prerrequisito | Evidencia | Responsable |
|---|---|---|
| Conformidad RETIE de la instalación de la etapa | Dictamen de inspección RETIE o documento de conformidad exigido por el RETIE | [PROPIETARIO] / Neptuno Energy Services |
| Pruebas en frío aprobadas | Protocolos de NES-OPE-PR-015 a NES-OPE-PR-022 firmados y aprobados por [CLIENTE], incluido el certificado de comisionado del generador FV (NES-OPE-F-159) del área | QA/QC |
| Ajustes de protecciones | EACP aprobado y registro de ajustes cargados en cada relé, verificados por inyección secundaria | Ingeniero de protecciones |
| Disparos verificados | Prueba funcional de disparo de cada interruptor desde su protección, sin tensión | Ingeniero de protecciones |
| Autorización del operador de red | Comunicación escrita del [OPERADOR DE RED] que autoriza la energización y fija fecha, hora y condiciones | [PROPIETARIO] |
| Requisitos ante XM, cuando apliquen | Consignación, supervisión, frontera comercial y comunicaciones según el acuerdo CNO vigente | Agente generador representante |
| Plan de maniobras | Plan y órdenes de maniobra aprobados por [CLIENTE] y, cuando aplique, por el [OPERADOR DE RED] | Líder de energización |
| Pendientes de obra | Lista de pendientes sin ítems que impidan energizar (categoría A) en la etapa | QA/QC |
| Puesta a tierra | Mediciones de resistencia de puesta a tierra y continuidad equipotencial conformes (NES-OPE-PR-020) | QA/QC |
| Servicios auxiliares | Alimentación auxiliar, UPS y baterías de la subestación probadas | Líder de energización |
| Señalización y cerramientos | Celdas, centros de transformación e inversores cerrados, rotulados y con señal de riesgo eléctrico | Responsable SST |
| Personal | Divulgación del plan de maniobras y de este procedimiento a todo el personal del proyecto, con registro de asistencia | Residente de obra |
| Emergencias | Brigada, extintores, botiquín, desfibrilador y ruta de evacuación verificados | Responsable SST |

> ALTO: Nada se energiza sin la autorización escrita del [OPERADOR DE RED] y sin la declaración escrita del líder de energización de que la etapa está lista. Una autorización verbal, un correo sin firma del responsable o una instrucción telefónica no reemplazan la autorización escrita.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

La planta se divide en áreas de energización según el unifilar: punto de conexión y celda o subestación de llegada, cada circuito de media tensión, cada centro de transformación con sus inversores, y los campos FV asociados. Cada área tiene uno de tres estados, que se muestran en un tablero de control en la oficina de obra y en la entrada del área:

| Estado | Significado | Régimen de trabajo |
|---|---|---|
| En construcción | Sin tensión y sin conexión posible a ninguna fuente | Permiso de trabajo general |
| Lista para energizar | Prerrequisitos cumplidos, en espera de la maniobra; aislada y bloqueada | Acceso restringido; solo inspección autorizada |
| Energizada | Con tensión o con posibilidad de recibirla en cualquier momento | Permiso de trabajo eléctrico obligatorio, LOTO y cinco reglas de oro |

### 8.2.2. Ingreso de personal

- Evaluar condiciones del área y verificar que no haya trabajos simultáneos en el área a energizar ni en las áreas aguas abajo.
- Diligenciar ATS/ART, permiso de trabajo y permiso de trabajo eléctrico (NES-SST-F-010 y NES-SST-F-011).
- Ubicar equipos de emergencia e inspeccionar el EPP con categoría de arco, guantes dieléctricos y detectores de tensión.
- Registrar el ingreso y la salida de cada persona en el control de acceso del área energizada.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional de equipos y circulación solo por rutas autorizadas.
- Prohibido el paso de maquinaria sobre zanjas, cajas de paso o rutas de cables MT energizados sin la protección mecánica de diseño.
- Ningún equipo de izaje ni vehículo con pluma opera a menos de la distancia de seguridad del RETIE respecto de partes energizadas.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Organización de la energización

- El líder de energización es la única voz de mando. Ninguna maniobra se ejecuta sin su orden, aunque la solicite el fabricante, [CLIENTE] o el centro de control.
- Las comunicaciones de la maniobra usan un canal de radio exclusivo. Toda orden se emite con la nomenclatura operativa del equipo, el operador la repite en voz alta y el líder la confirma antes de ejecutar; al terminar, el operador informa "orden N° [__] ejecutada" con la hora.
- Antes de cada jornada de energización se hace una reunión previa con todo el equipo: alcance de la etapa, plan de maniobras, roles, riesgos, áreas que cambian de estado, puntos de espera, criterios de suspensión y plan de emergencias. Se registra en el formato NES-OPE-F-161.
- Las maniobras de energización se programan en horario diurno, con luz suficiente, sin pronóstico de tormenta eléctrica y con el personal completo descansado. No se energiza una etapa nueva al final de una jornada extensa.
- La coordinación con el centro de control del [OPERADOR DE RED] la hace una sola persona designada en el plan de maniobras, con registro de hora, interlocutor y contenido de cada comunicación.

#### 8.2.4.2. Etapas de la energización

La planta se energiza siempre desde la fuente hacia la carga, una etapa cada vez y desde un circuito ya probado. La secuencia típica es la siguiente; el plan de maniobras del proyecto la ajusta a su unifilar.

| Etapa | Alcance | Condición para pasar a la siguiente |
|---|---|---|
| 0 | Verificación de prerrequisitos, autorización del [OPERADOR DE RED] y, cuando aplique, inicio de las PPS informado a XM | Expediente completo y aprobado |
| 1 | Punto de conexión, línea o acometida y celda o subestación de llegada, transformador de potencia en vacío cuando exista | Tensiones y secuencia correctas, protecciones estables, remojo cumplido |
| 2 | Barras MT de la planta y servicios auxiliares | Medidas correctas en barras y en tableros auxiliares |
| 3 | Circuitos MT internos, uno a la vez, con los centros de transformación abiertos en BT | Circuito estable, sin disparos, inspección visual de terminales y empalmes |
| 4 | Centros de transformación, uno a la vez, en vacío | Tensión y secuencia correctas en BT, sin ruidos ni calentamiento anormal |
| 5 | Inversores, uno a la vez, primero en vacío y luego con generación limitada | Sincronización correcta, sin alarmas, medidas coherentes |
| 6 | Pruebas en caliente de protecciones, medida, SCADA y PPC | Protocolos aprobados |
| 7 | Aumento escalonado de potencia y pruebas de desempeño y capacidad | Resultados conformes al contrato y a la regulación |
| 8 | Entrega a operación | Acta firmada |

#### 8.2.4.3. Plan de maniobras y orden de maniobra

El plan de maniobras se elabora sobre el unifilar con nomenclatura operativa y contiene, como mínimo:

- Alcance de cada etapa y estado inicial requerido de cada interruptor, seccionador y seccionador de puesta a tierra.
- Secuencia numerada de pasos, con el equipo, la acción, el estado esperado, la verificación y el responsable.
- Puntos de espera: verificaciones que deben estar conformes antes de continuar (tensión, secuencia, remojo, inspección).
- Tiempos de remojo de cada equipo, definidos por el líder de energización y el fabricante — [____] minutos para circuitos MT y [____] minutos para transformadores (criterio del proyecto).
- Criterios de suspensión y la maniobra de retorno a estado seguro de cada paso.
- Áreas que cambian de estado y la hora prevista.
- Relación de personas autorizadas y sus roles.

Cada orden de maniobra se diligencia en el formato NES-OPE-F-161, se firma antes de ejecutar y se cierra con la hora de cada paso. Una orden no se modifica en campo: si cambia la condición, se suspende, se emite una nueva orden y se aprueba.

> ALTO: Antes de cada cierre, el líder de energización confirma por radio con cada responsable de área que no hay personas, herramientas ni puestas a tierra temporales en el circuito a energizar, y que todas las puertas de celdas y centros de transformación están cerradas.

#### 8.2.4.4. Cambio de estado de áreas a "energizado"

El cambio de estado de un área es un acto formal que se ejecuta antes de la primera maniobra que pueda aplicarle tensión:

1. El líder de energización comunica por escrito, con al menos [____] horas de anticipación (criterio del proyecto), las áreas que cambian de estado y la fecha, a todos los frentes de Neptuno Energy Services, subcontratistas y [CLIENTE].
2. QA/QC y el supervisor de cada frente confirman que no quedan trabajos abiertos, que los permisos del área están cerrados y que no hay herramientas, materiales ni puestas a tierra temporales.
3. Se retiran los candados de construcción y se instalan los candados y tarjetas de maniobra del líder de energización.
4. Se instala la señalización de "PELIGRO – ÁREA ENERGIZADA" en accesos, puertas de celdas, centros de transformación, inversores y cajas de paso MT, con el nombre del área y la fecha.
5. Se cierran con llave las puertas de las celdas, los centros de transformación y los recintos de inversores; las llaves quedan bajo custodia del líder de energización o del responsable de operación.
6. Se habilita el control de acceso con registro de ingreso y salida, y desde ese momento todo trabajo en el área requiere permiso de trabajo eléctrico y LOTO según NES-SST-PR-001.
7. Se registra el cambio de estado en el formato NES-OPE-F-162, con las firmas del líder de energización, del responsable SST y de [CLIENTE], y se actualiza el tablero de control de estados.

> NOTA: Un área energizada no vuelve a "en construcción" por decisión verbal. Para intervenirla se aplica el régimen de permisos y LOTO; si se requiere devolverla a construcción, se emite un acta inversa con las mismas firmas.

#### 8.2.4.5. Coordinación con el [OPERADOR DE RED] y con XM

Los requisitos dependen del punto de conexión y del tamaño del proyecto. El [PROPIETARIO] o su agente generador representante los gestiona; Neptuno Energy Services aporta la información técnica y ejecuta en campo lo que le corresponda.

| Tipo de proyecto | Coordinación típica |
|---|---|
| Autogeneración a pequeña escala o generación distribuida (Res. CREG 174 de 2021) | Requisitos y visita de verificación del [OPERADOR DE RED] según su procedimiento de conexión |
| Planta solar en el SDL entre 1 MW y menos de 5 MW (Res. CREG 101-011 de 2022) | Protocolo de pruebas e interacción con el centro de control del [OPERADOR DE RED]; requisitos del acuerdo CNO vigente |
| Planta solar en el SDL de 5 MW o más (Res. CREG 148 de 2021) | Requisitos técnicos y pruebas de la resolución y procedimiento de entrada en operación del acuerdo CNO vigente |
| Planta solar conectada al STN o al STR (Res. CREG 060 de 2019) | Procedimiento de entrada en operación comercial del acuerdo CNO vigente ante el CND, consignaciones, supervisión, pruebas de la planta aprobadas por acuerdo CNO |

Para los proyectos que entran al procedimiento del CNO, el [PROPIETARIO] verifica, entre otros, los siguientes requisitos antes de la fecha de inicio de las PPS: registro de las fronteras comerciales, listas de señales SCADA y SOE, unifilar con nomenclatura operativa, pruebas de supervisión con el CND cuando le aplique, certificación del transportador o del [OPERADOR DE RED] sobre la conexión y la capacidad asignada, comunicación de la fecha de inicio de las PPS y cronograma de pruebas. Los plazos de cada requisito son los del acuerdo CNO vigente y no se fijan en este documento.

- La energización de activos existentes del [OPERADOR DE RED] o del transportador se ampara en la consignación correspondiente. No deben quedar activos energizados sin estar en pruebas o declarados en operación comercial.
- Toda maniobra en equipos del [OPERADOR DE RED] la ejecuta o la autoriza su personal; Neptuno Energy Services no opera equipos ajenos.
- El horario, la duración y las condiciones de la ventana de energización que fije el [OPERADOR DE RED] prevalecen sobre el plan interno.

#### 8.2.4.6. Energización del punto de conexión y de la celda de llegada

1. Confirmar con el centro de control del [OPERADOR DE RED] la consignación vigente, la hora y el estado del punto de conexión.
2. Verificar en sitio que todos los interruptores de la planta aguas abajo de la celda de llegada están abiertos y bloqueados, y que los seccionadores de puesta a tierra que deban retirarse están abiertos.
3. Retirar las puestas a tierra temporales, con registro de cada una retirada contra el listado de instaladas.
4. Verificar que los relés de la celda de llegada están en servicio, con los ajustes del EACP y sin señales de disparo activas.
5. Energizar desde la red por orden del [OPERADOR DE RED] o por su personal: la celda de llegada recibe tensión desde un circuito ya probado.
6. Verificar presencia y magnitud de tensión en las tres fases en los secundarios de los transformadores de tensión, en el relé y en el medidor.
7. Verificar la secuencia de fases en el secundario de los transformadores de tensión con secuencímetro.
8. Si existe transformador de potencia de la subestación, energizarlo en vacío, observar la corriente de energización y verificar que las protecciones permanecen estables. Mantener el remojo definido en el plan de maniobras con inspección de ruido, olor, temperatura, nivel de aceite y relé de gas.
9. Registrar los valores en el formato NES-OPE-F-163 y no continuar si cualquier valor está fuera de criterio.

> NOTA: Al energizar un circuito nuevo se prefiere hacerlo desde un circuito ya probado y en servicio, porque ni el interruptor nuevo ni sus protecciones han demostrado aún su funcionamiento con tensión.

#### 8.2.4.7. Energización de la red MT interna por circuitos

- Se energiza un circuito MT a la vez, con todos los centros de transformación del circuito abiertos en su lado MT o con sus interruptores BT abiertos, según el plan.
- Antes del cierre, verificar que el circuito tiene vigentes los ensayos de cable y de terminales de NES-OPE-PR-015 y NES-OPE-PR-016, y que las pantallas están puestas a tierra según el diseño.
- Cerrar el interruptor del circuito por orden del líder; observar la corriente de carga capacitiva del cable y verificar que las protecciones no actúan.
- Verificar tensión y secuencia en el extremo del circuito, en la celda del último centro de transformación, mediante los indicadores de presencia de tensión de la celda o un comparador de fases MT, nunca por contacto directo.
- Mantener el remojo en vacío del circuito definido en el plan; durante el remojo nadie se acerca a terminales, empalmes ni celdas del circuito.
- Terminado el remojo, inspeccionar desde fuera de la distancia de seguridad: ruidos, efluvios, olores, humo o calentamiento en terminales y celdas.
- Si el proyecto lo exige, ejecutar termografía de terminales y conexiones bajo carga una vez el circuito transporte potencia estable.
- Registrar en el formato NES-OPE-F-163 y continuar con el siguiente circuito solo con el primero estable.

#### 8.2.4.8. Energización de los centros de transformación

1. Verificar antes del cierre: protocolos de NES-OPE-PR-019 aprobados, nivel de aceite o estado del transformador seco, posición del cambiador de derivaciones según el estudio, relés del transformador (temperatura, presión, gas) cableados al disparo, puertas cerradas.
2. Verificar que el interruptor o los interruptores BT del transformador hacia los inversores están abiertos.
3. Energizar el transformador en vacío desde su celda MT.
4. Verificar tensiones fase-fase y fase-neutro o fase-tierra en el lado BT y la secuencia de fases en los bornes de llegada de cada inversor, con multímetro CAT III o superior y secuencímetro.
5. Mantener el remojo definido y observar ruido, vibración, temperatura y fugas.
6. Verificar la alimentación de servicios auxiliares del centro (ventilación, iluminación, control, UPS) y la llegada de las señales al SCADA.
7. Registrar en los formatos NES-OPE-F-163 y NES-OPE-F-164.

#### 8.2.4.9. Puesta en marcha de los inversores

La puesta en marcha sigue el protocolo del fabricante del inversor; este procedimiento fija las condiciones mínimas.

- Lado DC: polaridad, tensión de circuito abierto y resistencia de aislamiento de los circuitos de entrada conformes según NES-OPE-PR-014, NES-OPE-PR-017 y NES-OPE-PR-022.
- Parámetros de red cargados en el inversor (tensión y frecuencia nominal, límites de protección de tensión y frecuencia, tiempos de reconexión, rampas y modo de control de reactiva) coherentes con el EACP y con los requisitos del [OPERADOR DE RED], verificados contra el listado aprobado.
- Secuencia típica: cerrar el interruptor AC del inversor, verificar que el inversor reconoce la red; cerrar los seccionadores DC; dar la orden de arranque desde el panel o desde el PPC; verificar la sincronización y la inyección.
- El primer arranque se hace con la potencia limitada desde el PPC o desde el inversor — [____] % de la potencia nominal (criterio del proyecto) — y se aumenta por escalones.
- Verificar en cada inversor: ausencia de alarmas, tensión DC de operación, corrientes DC por entrada, potencias activa y reactiva, factor de potencia, temperatura interna y funcionamiento de la ventilación.
- Comparar la producción del inversor con la de inversores vecinos en las mismas condiciones; una desviación significativa se investiga antes de continuar.
- Registrar en el formato NES-OPE-F-165.

> ALTO: Ningún inversor se arranca con personal dentro de su recinto ni con las puertas de sus compartimentos de potencia abiertas. Abrir un seccionador DC bajo carga puede producir un arco sostenido.

#### 8.2.4.10. Verificación de fases y secuencia

- Antes de cerrar cualquier punto que una dos fuentes o dos tramos que se energizaron por separado, se ejecuta la verificación de fases con un comparador de fases MT de la clase del sistema, o en los secundarios de los transformadores de tensión: la diferencia entre fases homólogas debe ser prácticamente nula y entre fases distintas igual a la tensión de línea.
- La secuencia de fases se verifica en la celda de llegada, en cada barra, en el lado BT de cada transformador y en los bornes AC de cada inversor. Debe coincidir con la de la red en todo el sistema.
- La identificación de fases en celdas, terminales y bornes se compara con la marcación de diseño y se corrige cualquier discrepancia antes de seguir.
- Los resultados se registran en el formato NES-OPE-F-164.

#### 8.2.4.11. Pruebas en caliente de protecciones, medida y supervisión

Con tensión y, cuando sea posible, con carga, se verifica que el sistema de protección y medida funciona como se probó en frío:

- Magnitudes en relés: tensiones y corrientes de cada fase, potencia y sentido del flujo leídos en el relé, comparados con el medidor y con el analizador de redes.
- Polaridad y relación de transformadores de corriente: verificación con carga de que las corrientes de las tres fases son equilibradas y con el ángulo correcto respecto a la tensión.
- Direccionalidad: las funciones direccionales y de potencia inversa ven el flujo en el sentido esperado.
- Estabilidad de diferenciales: la corriente diferencial con carga es despreciable frente al ajuste.
- Medida de la frontera comercial: verificación del medidor, de las relaciones de transformación y de la coherencia de energía con el SCADA, en coordinación con el [PROPIETARIO] y su representante de frontera.
- Supervisión SCADA: cada señal de estado, alarma y medida del listado aprobado se compara con su valor en campo; las órdenes de mando remoto se prueban una a una con la autorización del líder de energización.
- Registro de eventos: verificación de la estampa de tiempo y de la sincronización horaria de relés, SCADA y registradores.

Los resultados se registran en el formato NES-OPE-F-166. Una protección que no se comporta según el EACP se deja fuera de servicio solo con autorización escrita del ingeniero de protecciones y del [OPERADOR DE RED], y la etapa no continúa hasta corregirla.

#### 8.2.4.12. Pruebas de funcionamiento del PPC

Las pruebas funcionales verifican que el PPC controla la planta en el punto de conexión según su especificación y según los requisitos regulatorios aplicables. Como mínimo:

| Prueba | Verificación |
|---|---|
| Comunicación PPC–inversores | Todos los inversores reciben y ejecutan consignas; pérdida de comunicación de un inversor detectada y alarmada |
| Limitación de potencia activa | La potencia en el punto de conexión sigue la consigna con el error y el tiempo especificados |
| Rampas de potencia activa | Rampas de subida y bajada dentro del valor declarado |
| Control de potencia activa/frecuencia | Banda muerta y estatismo configurados según lo que defina el CND, cuando aplique |
| Control de reactiva | Modos de tensión, potencia reactiva y factor de potencia; cambio de modo sin perturbación |
| Respuesta a escalón de consigna | Tiempos de respuesta y de establecimiento dentro de los requisitos aplicables |
| Consignas remotas | Recepción de consignas desde el centro de control del [OPERADOR DE RED] o del CND, cuando aplique |
| Límites | Operación dentro de la curva PQ declarada en el punto de conexión |

Para plantas conectadas al STN o al STR, la Resolución CREG 060 de 2019 exige, entre otros, que el control de reactiva/tensión tenga modos de tensión, potencia reactiva y factor de potencia, con tiempo de respuesta inicial menor a 2 segundos y tiempo de establecimiento menor a 10 segundos ante un escalón de consigna; y que el control de potencia activa/frecuencia tenga estatismo configurable entre 2 % y 6 %, banda muerta configurable entre 0 y 120 mHz, tiempo de respuesta inicial máximo de 2 segundos y tiempo de establecimiento máximo de 15 segundos. Antes de declararse en operación comercial, estas plantas deben realizar y remitir al CND las pruebas de curva de capacidad, control de potencia activa/frecuencia, rampa operativa, control de potencia reactiva/tensión, operación ante depresiones de tensión y sobretensiones, e inyección rápida de corriente reactiva, en los términos de los acuerdos CNO vigentes. Los valores se confirman contra la versión vigente de la regulación antes de cada prueba.

Las pruebas regulatorias las dirige el [PROPIETARIO] o su agente con el organismo o la firma que corresponda; Neptuno Energy Services aporta la planta lista, las maniobras y el personal de apoyo. Los resultados de las pruebas funcionales se registran en el formato NES-OPE-F-167.

#### 8.2.4.13. Pruebas de desempeño y de capacidad

- Aumento escalonado de potencia: la planta se lleva por escalones de potencia definidos en el plan — [____] % (criterio del proyecto) — con verificación en cada escalón de temperaturas, protecciones, calidad de potencia y alarmas antes del siguiente.
- Prueba de capacidad: demostración de la potencia en el punto de conexión frente a la capacidad contratada o asignada, con las condiciones de irradiancia, temperatura y duración del contrato y, cuando aplique, del acuerdo CNO vigente.
- Prueba de desempeño: cálculo del índice de desempeño (PR) o del indicador del contrato con el sistema de monitoreo, sensores de irradiancia y temperatura calibrados y la metodología de la IEC 61724-1 o la que fije el contrato.
- Prueba de funcionamiento continuo: operación sin fallas durante el periodo y con la disponibilidad que fije el contrato — [____] días.
- Termografía de celdas, transformadores, tableros BT e inversores con la planta a carga estable, cuando el proyecto la exija.
- Los resultados se registran en el formato NES-OPE-F-168 y se adjuntan los datos crudos del sistema de monitoreo.

#### 8.2.4.14. Desenergización programada y de emergencia

Desenergización programada: se ejecuta con orden de maniobra, en sentido inverso a la energización (desde la carga hacia la fuente): reducir la potencia desde el PPC, detener los inversores, abrir los interruptores BT, abrir los circuitos MT y, si se requiere, solicitar al [OPERADOR DE RED] la apertura del punto de conexión. Para intervenir un equipo se aplican las cinco reglas de oro y el LOTO de NES-SST-PR-001.

Desenergización de emergencia: cualquier integrante del equipo puede pedir por radio "ALTO – EMERGENCIA" ante humo, fuego, arco, ruido anormal, persona en riesgo o disparo no explicado. El líder de energización ordena de inmediato:

1. Apertura del interruptor de la etapa afectada desde el punto de mando más alejado del equipo con falla (SCADA, mando remoto o tablero de control).
2. Si la condición persiste o no se identifica, apertura del interruptor general de la planta.
3. Parada de los inversores desde el PPC o el SCADA.
4. Aviso al centro de control del [OPERADOR DE RED] y, si la falla afecta su red, solicitud de apertura del punto de conexión.
5. Activación del plan de emergencias del numeral 12.

Ningún equipo que haya disparado por protección se vuelve a energizar sin la revisión del ingeniero de protecciones, la lectura de los registros de falla y la autorización del líder de energización.

> ALTO: Mientras el campo FV reciba luz, el lado DC de los inversores y de las cajas combinadoras sigue energizado aunque la red esté abierta. Desenergizar la planta no desenergiza el generador fotovoltaico.

#### 8.2.4.15. Entrega a operación

La planta, o cada etapa, se entrega a operación con el acta NES-OPE-F-169 cuando:

- Todos los protocolos de pruebas en caliente y de desempeño están aprobados por [CLIENTE].
- La lista de pendientes no tiene ítems que impidan operar; los demás tienen responsable y fecha.
- Se entregaron las llaves de celdas y recintos, el control de los candados de maniobra, el registro de estados de áreas y los parámetros cargados en relés, inversores y PPC.
- Se entregaron los manuales de operación, el plan de maniobras de operación normal, los ajustes de protecciones definitivos y los documentos conforme a obra disponibles.
- El personal de operación del [PROPIETARIO] recibió la capacitación prevista en el contrato.
- Se definió por escrito quién es, desde la firma del acta, el responsable de autorizar maniobras y permisos de trabajo en las áreas entregadas.

> NOTA: Hasta la firma del acta de entrega, Neptuno Energy Services es responsable del control de las maniobras y de los permisos en las áreas energizadas que tiene a su cargo. Después de la firma, cualquier trabajo de Neptuno Energy Services en esas áreas requiere el permiso del operador de la planta.

#### 8.2.4.16. No conformidades durante la energización

- Valor de tensión, secuencia o fase fuera de criterio: suspender, desenergizar la etapa, investigar y corregir antes de reintentar.
- Disparo de una protección: no reenergizar; leer los registros, analizar la causa con el ingeniero de protecciones y documentar.
- Ruido, olor, humo, efluvio o calentamiento anormal: desenergizar de inmediato y tratar como emergencia potencial.
- Alarma persistente de un inversor o del PPC: dejar el equipo fuera de servicio y escalar al fabricante.
- Todas se registran como no conformidad y, cuando hubo riesgo para personas, como incidente según la Resolución 1401 de 2007.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Autorización para energizar | Escrita, del [OPERADOR DE RED], vigente para la fecha y la etapa | RETIE / procedimiento del [OPERADOR DE RED] |
| Conformidad de la instalación | Dictamen de inspección RETIE o documento exigido por el RETIE para la etapa | RETIE Res. 40117 de 2024 |
| Prerrequisitos | 100 % de los ítems del formato NES-OPE-F-160 conformes | Este procedimiento |
| Ajustes de protecciones | Iguales al EACP aprobado, verificados por inyección y con registro de la versión cargada | EACP / acuerdo CNO vigente |
| Tensión en barras y en BT | Dentro del rango del diseño y de la tolerancia del [OPERADOR DE RED] — [____] % | Diseño / [OPERADOR DE RED] |
| Secuencia de fases | Igual a la de la red en todos los puntos verificados | Diseño |
| Verificación de fases | Diferencia entre fases homólogas prácticamente nula antes de cerrar puntos de unión | Este procedimiento |
| Energización de circuitos y transformadores | Sin disparo, sin ruido, olor ni calentamiento anormal durante el remojo | Plan de maniobras / fabricante |
| Inversores | Sincronización sin alarmas; parámetros de red iguales al listado aprobado | Fabricante / EACP |
| Medida y protecciones con carga | Magnitudes coherentes entre relé, medidor y analizador; direccionalidad y estabilidad correctas | EACP / código de medida |
| Supervisión SCADA | 100 % de las señales del listado verificadas contra campo | Listado aprobado |
| Control de reactiva/tensión (STN/STR) | Respuesta inicial menor a 2 s y establecimiento menor a 10 s ante escalón | Res. CREG 060 de 2019 |
| Control de potencia activa/frecuencia (STN/STR) | Estatismo 2 % a 6 %, banda muerta 0 a 120 mHz, Tr máximo 2 s, Te máximo 15 s | Res. CREG 060 de 2019 |
| Capacidad y desempeño | Según el contrato y, cuando aplique, el acuerdo CNO vigente | Contrato / CNO |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-160 a NES-OPE-F-169 de este procedimiento.
- Autorización escrita del [OPERADOR DE RED], consignaciones y comunicaciones con su centro de control.
- Dictamen de inspección RETIE y protocolos de pruebas en frío aprobados.
- EACP aprobado y registros de ajustes cargados en cada relé.
- Informes de puesta en marcha de los fabricantes y parámetros cargados en inversores y PPC.
- Certificados de calibración de los instrumentos usados.
- Datos crudos del sistema de monitoreo durante las pruebas de desempeño.

## 8.5. Control de calidad

QA/QC verifica el 100 % de los prerrequisitos de cada etapa, presencia cada maniobra de energización como punto de espera y revisa el 100 % de los registros antes de la entrega a operación. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación que no afecta la seguridad ni el funcionamiento, por ejemplo señalización o rotulación incompleta. | Registro y cierre antes de la entrega. |
| 2 | Requiere corregir un ajuste, una señal SCADA o un parámetro de inversor, o repetir una prueba. | Corrección, nueva prueba y registro. |
| 3 | Afecta la seguridad o la conexión: disparo no explicado, secuencia errada, protección no conforme, falla de equipo. | Desenergización de la etapa, análisis de causa, aprobación escrita de [CLIENTE] y, si aplica, del [OPERADOR DE RED] antes de reenergizar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al líder de energización en el ATS/ART y la reunión previa, verifica que las áreas energizadas estén señalizadas y con control de acceso y que se cumplan las medidas de este procedimiento. Todo el personal del proyecto, no solo el eléctrico, recibe antes de la primera energización una charla sobre las áreas que cambian de estado, la señalización y la prohibición de ingreso.

## 9.1. Reglas de oro

- **SIEMPRE** trataré como energizado todo equipo de un área declarada energizada, aunque no se haya cerrado aún ningún interruptor.
- **SIEMPRE** aplicaré las cinco reglas de oro antes de intervenir un equipo en un área energizada (Res. 5018 de 2019).
- **NUNCA** ejecutaré una maniobra sin orden escrita y sin la orden verbal del líder de energización.
- **NUNCA** energizaré una etapa sin la autorización escrita del [OPERADOR DE RED] y sin los prerrequisitos cumplidos.
- **SIEMPRE** repetiré la orden en voz alta antes de ejecutarla y confirmaré su ejecución.
- **SIEMPRE** usaré el EPP con la categoría de arco que indique el análisis de riesgo al maniobrar celdas y tableros.
- **NUNCA** traspasaré la distancia de seguridad del RETIE respecto de partes energizadas sin permiso de trabajo eléctrico.
- **NUNCA** reenergizaré un equipo que disparó por protección sin análisis y autorización.
- **SIEMPRE** recordaré que el lado DC sigue energizado mientras haya luz, aunque la red esté abierta.
- **SIEMPRE** suspenderé la maniobra ante tormenta eléctrica y me dirigiré al refugio.

## 9.2. Distancias de seguridad y riesgo de arco

- Las distancias mínimas de aproximación a partes energizadas son las del RETIE para cada nivel de tensión; se señalizan en el piso o con barreras en la celda de llegada y en los centros de transformación.
- Las maniobras de celdas MT se hacen con las puertas cerradas, desde el mando eléctrico o desde la posición más alejada que permita el equipo, y con el EPP de la categoría que fije el análisis de riesgo de arco.
- Solo permanece frente a una celda durante la maniobra el operador que la ejecuta; el resto del equipo se ubica fuera de la zona de proyección.

## 9.3. Condiciones climáticas de [departamento]

- Tormenta eléctrica: no se inicia ninguna maniobra con pronóstico o aviso de tormenta; ante el primer trueno se suspende, se deja la planta en estado estable y seguro y el personal se dirige al refugio. Se reanuda solo con autorización del responsable SST.
- Lluvia: no se abren celdas, centros de transformación ni inversores bajo lluvia; las maniobras que lo requieran se aplazan.
- Calor y radiación: hidratación, sombra, pausas y rotación; la ropa ignífuga se escoge con la menor carga térmica compatible con la categoría de arco.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado a la subestación y a los centros de transformación | Colisión, volcamiento, caídas al mismo nivel. | Conductores autorizados; vías y velocidades del proyecto; cinturón obligatorio. |
| 2. Reunión previa y verificación de prerrequisitos | Energización de una etapa incompleta; desconocimiento del plan. | Formato NES-OPE-F-160 completo; divulgación del plan de maniobras; asistencia registrada. |
| 3. Cambio de estado de áreas | Personal o herramientas dentro del área; ingreso posterior de terceros. | Barrido del área; cierre de permisos; señalización; candados y control de acceso. |
| 4. Retiro de puestas a tierra temporales | Olvido de una puesta a tierra que provoca cortocircuito al energizar. | Listado de puestas a tierra instaladas y retiradas; verificación del líder antes del cierre. |
| 5. Maniobra de celdas MT | Arco eléctrico, explosión de celda, quemaduras. | Puertas cerradas; mando remoto; EPP con categoría de arco; solo el operador frente a la celda. |
| 6. Energización de circuitos y transformadores | Falla de aislamiento, disparo, incendio de transformador. | Pruebas en frío aprobadas; remojo; observación a distancia; extintores; plan de desenergización. |
| 7. Verificación de tensión, fases y secuencia | Contacto eléctrico, lectura errónea. | Comparador de fases y detectores MT de la clase del sistema; instrumentos CAT III o superior; puntas aisladas. |
| 8. Puesta en marcha de inversores | Arco en DC, contacto eléctrico, daño al equipo. | Protocolo del fabricante; puertas cerradas; potencia limitada; nadie dentro del recinto. |
| 9. Pruebas en caliente de protecciones y SCADA | Disparo no deseado, mando remoto sobre equipo con personal. | Autorización del líder para cada mando; verificación de área despejada; comunicación por radio. |
| 10. Pruebas del PPC y de desempeño | Sobretensiones o perturbaciones en la red; disparo de la planta. | Pruebas coordinadas con el [OPERADOR DE RED]; escalones de consigna limitados; vigilancia de alarmas. |
| 11. Desenergización de emergencia | Demora en la respuesta, maniobra en el equipo con falla. | Plan de emergencia divulgado; apertura desde el punto más alejado; simulacro previo. |
| 12. Trabajo en altura en estructuras de la subestación | Caída a distinto nivel. | Res. 4272 de 2021; coordinador de alturas; equipos certificados. |
| 13. Exposición ambiental | Radiación UV, estrés térmico, ofidios. | Hidratación, sombra, pausas; polainas; revisión de celdas y fosos antes de ingresar. |
| 14. Tormenta eléctrica y lluvia | Descarga atmosférica, contacto eléctrico. | Suspensión; planta en estado seguro; refugio. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Aire | Emisiones y ruido | Vehículos y equipos con revisión técnico-mecánica al día; motores apagados en reposo; humectación de vías en época seca. |
| Aire | Gases aislantes de aparamenta MT | Si las celdas usan gas aislante, no se abre ni se ventea ningún compartimiento; cualquier fuga o pérdida de presión se reporta y la recuperación la hace personal certificado del fabricante. |
| Suelo | Aceite dieléctrico | Verificar antes de energizar la contención o el foso de aceite de cada transformador; kit antiderrame en cada centro de transformación; un derrame se contiene y el material contaminado se gestiona como RESPEL. |
| Suelo | Residuos sólidos | Separación en la fuente con el código de colores de la Res. 2184 de 2019; embalajes, precintos y tarjetas usadas a su corriente; entrega a gestores autorizados. |
| Suelo | Residuos peligrosos (RESPEL) | Trapos y absorbentes contaminados, baterías y elementos con residuo de quemado, en recipientes rotulados; almacenamiento temporal y entrega a gestor autorizado con certificado (Decreto 1076 de 2015). |
| Suelo | RCD | Gestión según Res. 0472 de 2017 modificada por Res. 1257 de 2021; disposición con gestor autorizado. |
| Flora y fauna | Fauna en celdas y recintos | Revisar presencia de fauna dentro de celdas, centros de transformación y recintos de inversores antes de cerrar y energizar; sellar pasos de cables; reporte de fauna para rescate según PMA. |
| Agua | Aguas residuales y consumo | Baños portátiles con gestor autorizado; uso racional del agua; prohibido intervenir cuerpos de agua. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente. Los datos de contacto se completan al inicio del proyecto y se publican en la subestación, en cada centro de transformación y en la oficina de obra.

1. Ordenar "ALTO – EMERGENCIA" por radio y ejecutar la desenergización de emergencia del numeral 8.2.4.14 desde un punto seguro.
2. Alejar al personal de la zona y no manipular equipos afectados.
3. Notificar al líder de energización, al responsable SST, al centro de control del [OPERADOR DE RED] y al interlocutor de [CLIENTE].
4. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, desfibrilador, extintor).
5. Incidente grave: activar ambulancia por la línea 123 y traslado al centro asistencial definido; notificar a la ARL.
6. Reportar el evento y realizar la investigación según Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Arco eléctrico o falla en celda MT

- No acercarse a la celda: abrir el interruptor aguas arriba desde el SCADA o el tablero de control, o pedir la apertura al [OPERADOR DE RED].
- Delimitar la zona; humo y gases de una falla en celda son tóxicos: no ingresar al recinto hasta su ventilación y autorización del responsable SST.
- No reenergizar hasta la inspección del equipo y el análisis de la falla.

## 12.2. Incendio en transformador o inversor

- Desenergizar el equipo por ambos lados: MT y BT, y detener los inversores; recordar que el lado DC permanece energizado con luz.
- Usar extintor apto para equipo eléctrico energizado solo en conato y desde la distancia segura; nunca agua sobre un equipo energizado.
- Si el fuego avanza, evacuar, aislar la zona y activar los bomberos por la línea 123, informándoles que es una instalación eléctrica con generación fotovoltaica.

## 12.3. Contacto eléctrico

- No tocar a la víctima mientras siga en contacto con el circuito; cortar la fuente o separarla con elemento aislante de la clase adecuada.
- Activar la emergencia y aplicar reanimación y desfibrilador si el personal está capacitado.
- Toda persona que sufra un contacto eléctrico se remite a valoración médica aunque se sienta bien.

## 12.4. Quemaduras y flash de arco

- Enfriar la quemadura con agua limpia a temperatura ambiente; no aplicar hielo, cremas ni remedios caseros; no retirar ropa adherida.
- Cubrir con apósito estéril o paño limpio y seco; remitir a valoración médica toda quemadura por arco y toda exposición ocular al destello.

| Contacto | Nombre | Teléfono |
|---|---|---|
| Líder de energización Neptuno Energy Services | [__________] | [__________] |
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Residente de obra Neptuno Energy Services | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| Centro de control del [OPERADOR DE RED] | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Bomberos / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Lista de verificación de prerrequisitos para energización | NES-OPE-F-160 | Líder de energización / QA/QC |
| Reunión previa y orden de maniobra de energización | NES-OPE-F-161 | Líder de energización |
| Acta de cambio de estado de área a energizado | NES-OPE-F-162 | Líder de energización / Responsable SST |
| Registro de energización de circuitos MT y centros de transformación | NES-OPE-F-163 | Líder de energización |
| Registro de verificación de fases y secuencia | NES-OPE-F-164 | Operador de maniobra |
| Registro de puesta en marcha de inversores | NES-OPE-F-165 | Responsable eléctrico / fabricante |
| Protocolo de pruebas en caliente de protecciones, medida y SCADA | NES-OPE-F-166 | Ingeniero de protecciones |
| Protocolo de pruebas funcionales del PPC | NES-OPE-F-167 | Especialista SCADA y PPC |
| Registro de prueba de desempeño y capacidad | NES-OPE-F-168 | Líder de energización / QA/QC |
| Acta de entrega a operación | NES-OPE-F-169 | Director / Residente de obra |
| Permisos de trabajo, ATS/ART y registros de LOTO | NES-SST-PR-001 | Responsable SST |
| Autorizaciones, consignaciones y comunicaciones del [OPERADOR DE RED] | — | Residente de obra |

\pagebreak

# 14. ANEXOS

## NES-OPE-F-160 — Lista de verificación de prerrequisitos para energización

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Etapa / área a energizar: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-023 | Plano unifilar: [__________] |

| Ítem | Prerrequisito | Evidencia (N.º de documento) | Cumple | No cumple |
|---|---|---|---|---|
| 1 | Dictamen de inspección RETIE o documento de conformidad de la etapa |  |  |  |
| 2 | Protocolos de pruebas en frío de cables, terminales y empalmes MT aprobados |  |  |  |
| 3 | Protocolos de celdas, transformadores e inversores aprobados |  |  |  |
| 4 | Protocolos de puesta a tierra y equipotencialidad conformes; certificado NES-OPE-F-159 del generador FV del área |  |  |  |
| 5 | EACP aprobado y ajustes cargados y verificados por inyección |  |  |  |
| 6 | Prueba funcional de disparo de interruptores |  |  |  |
| 7 | Autorización escrita del [OPERADOR DE RED] vigente |  |  |  |
| 8 | Requisitos ante XM cumplidos, cuando apliquen (consignación, supervisión, frontera, PPS) |  |  |  |
| 9 | Plan de maniobras y órdenes de maniobra aprobados |  |  |  |
| 10 | Lista de pendientes sin ítems categoría A en la etapa |  |  |  |
| 11 | Servicios auxiliares, UPS y baterías probados |  |  |  |
| 12 | Celdas, centros e inversores cerrados, rotulados y señalizados |  |  |  |
| 13 | Divulgación del plan a todo el personal del proyecto |  |  |  |
| 14 | Brigada, extintores, botiquín y desfibrilador verificados |  |  |  |
| 15 | Pronóstico del tiempo sin tormenta eléctrica para la ventana de maniobra |  |  |  |

{.plain}
| Declaración del líder de energización: la etapa está lista para energizar. Sí / No |
|---|

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-161 — Reunión previa y orden de maniobra de energización

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Etapa: [__________] | Orden de maniobra N.º: [____] |
| Líder de energización: [__________] | Canal de radio: [____] |

{.plain}
| Temas de la reunión previa: alcance, plan de maniobras, roles, riesgos, áreas que cambian de estado, puntos de espera, criterios de suspensión, plan de emergencias. Asistentes en lista anexa. |
|---|

| Paso | Equipo (nomenclatura operativa) | Acción | Estado esperado | Hora | Ejecutó | Verificó |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |

{.plain}
| Puestas a tierra temporales retiradas: [____] de [____] | Área despejada confirmada por radio: Sí / No |
|---|---|
| Comunicación con el [OPERADOR DE RED]: hora [____] | Interlocutor: [__________] |

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-162 — Acta de cambio de estado de área a energizado

{.plain}
| Proyecto: [__________] | Fecha y hora efectiva: [____] |
|---|---|
| Área / equipos que cambian de estado: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-023 / NES-SST-PR-001 | Plano unifilar: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Comunicación previa a todos los frentes, subcontratistas y [CLIENTE] | | | |
| 2 | Permisos de trabajo del área cerrados | | | |
| 3 | Área barrida: sin personas, herramientas, materiales ni puestas a tierra temporales | | | |
| 4 | Candados de construcción retirados y candados de maniobra instalados | | | |
| 5 | Señalización "PELIGRO – ÁREA ENERGIZADA" instalada en accesos y equipos | | | |
| 6 | Celdas, centros y recintos cerrados con llave; llaves en custodia | | | |
| 7 | Control de acceso habilitado con registro de ingreso y salida | | | |
| 8 | Tablero de control de estados actualizado | | | |

{.plain}
| Custodio de llaves: [__________] | Responsable de autorizar permisos en el área: [__________] |
|---|---|

{.plain}
| Observaciones: |
|---|

{.plain}
| | Líder de energización | Responsable SST | Residente de obra | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-163 — Registro de energización de circuitos MT y centros de transformación

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito / centro de transformación: [__________] | Orden de maniobra N.º: [____] |
| Tensión nominal: [____] kV | Instrumentos (serie / calibración): [__________] |

| Equipo | Hora de cierre | Tensión L1-L2 / L2-L3 / L3-L1 | Secuencia OK | Remojo (min) | Disparo / alarma | Cumple |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

| Ítem | Inspección durante y después del remojo | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Sin ruido, vibración ni efluvios anormales | | | |
| 2 | Sin olor a quemado ni humo | | | |
| 3 | Nivel de aceite, temperatura y relés del transformador normales | | | |
| 4 | Terminales y celdas sin calentamiento visible | | | |
| 5 | Protecciones estables, sin disparos ni arranques | | | |
| 6 | Señales recibidas correctamente en el SCADA | | | |

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-164 — Registro de verificación de fases y secuencia

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Punto verificado: [__________] | Consecutivo: [____] |
| Instrumento (comparador / secuencímetro, serie): [__________] | Calibración vigente hasta: [____] |

| Punto de medida | Fase A–A' | Fase B–B' | Fase C–C' | Secuencia | Marcación coincide | Cumple |
|---|---|---|---|---|---|---|
| Celda de llegada | | | | | | |
| Barra MT | | | | | | |
| Circuito MT [__] extremo | | | | | | |
| CT [__] lado BT | | | | | | |
| Inversor [__] bornes AC | | | | | | |
| | | | | | | |

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-165 — Registro de puesta en marcha de inversores

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Centro de transformación: [__________] | Consecutivo: [____] |
| Irradiancia: [____] W/m² | Temperatura ambiente: [____] °C |

| Inversor | Parámetros de red verificados | Udc (V) | P (kW) | Q (kvar) | Alarmas | Cumple |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Pruebas DC de entradas conformes (NES-OPE-PR-022) | | | |
| 2 | Parámetros de protección de red iguales al listado aprobado | | | |
| 3 | Secuencia de arranque del fabricante cumplida | | | |
| 4 | Primer arranque con potencia limitada al [____] % | | | |
| 5 | Ventilación y temperatura interna normales | | | |
| 6 | Comunicación con el PPC y el SCADA verificada | | | |
| 7 | Producción coherente con inversores vecinos | | | |

{.plain}
| Representante del fabricante: [__________] | Informe del fabricante N.º: [__________] |
|---|---|

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-166 — Protocolo de pruebas en caliente de protecciones, medida y SCADA

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Equipo / bahía: [__________] | Relé (referencia y versión de ajustes): [__________] |
| Documento de referencia: EACP [__________] | Potencia durante la prueba: [____] MW |

| Magnitud | Relé | Medidor | Analizador | Diferencia | Cumple |
|---|---|---|---|---|---|
| Tensión L1 / L2 / L3 | | | | | |
| Corriente L1 / L2 / L3 | | | | | |
| Potencia activa y sentido | | | | | |
| Potencia reactiva y sentido | | | | | |
| Ángulo corriente–tensión | | | | | |
| Corriente diferencial | | | | | |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Polaridad y relación de transformadores de corriente con carga | | | |
| 2 | Direccionalidad de funciones direccionales y de potencia inversa | | | |
| 3 | Estabilidad de la protección diferencial | | | |
| 4 | Medida de la frontera comercial coherente con el SCADA | | | |
| 5 | Señales de estado, alarmas y medidas SCADA verificadas contra campo | | | |
| 6 | Mandos remotos probados con autorización | | | |
| 7 | Estampa de tiempo y sincronización horaria verificadas | | | |

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-167 — Protocolo de pruebas funcionales del PPC

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Versión de software y parámetros del PPC: [__________] | Consecutivo: [____] |
| Punto de medida: [__________] | Irradiancia durante la prueba: [____] W/m² |

| Prueba | Consigna | Valor alcanzado | Tiempo de respuesta | Tiempo de establecimiento | Criterio | Cumple |
|---|---|---|---|---|---|---|
| Comunicación PPC–inversores | | | | | | |
| Limitación de potencia activa | | | | | | |
| Rampa de subida | | | | | | |
| Rampa de bajada | | | | | | |
| Control de tensión | | | | | | |
| Control de potencia reactiva | | | | | | |
| Control de factor de potencia | | | | | | |
| Potencia activa/frecuencia | | | | | | |
| Consigna remota | | | | | | |

{.plain}
| Coordinación con el [OPERADOR DE RED] / CND: Sí / No / No aplica | Interlocutor: [__________] |
|---|---|

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-168 — Registro de prueba de desempeño y capacidad

{.plain}
| Proyecto: [__________] | Periodo de prueba: [____] a [____] |
|---|---|
| Metodología: contrato [__________] / IEC 61724-1 | Consecutivo: [____] |
| Sensores de irradiancia y temperatura (serie / calibración): [__________] | Medidor de referencia: [__________] |

| Escalón / prueba | Potencia objetivo | Potencia medida | Irradiancia (W/m²) | Temperatura de módulo (°C) | Resultado | Cumple |
|---|---|---|---|---|---|---|
| Escalón 1 | | | | | | |
| Escalón 2 | | | | | | |
| Escalón 3 | | | | | | |
| Capacidad | | | | | | |
| Desempeño (PR o indicador del contrato) | | | | | | |
| Funcionamiento continuo | | | | | | |

{.plain}
| Datos crudos adjuntos: Sí / No | Termografía ejecutada: Sí / No |
|---|---|

{.plain}
| Observaciones: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

\pagebreak

## NES-OPE-F-169 — Acta de entrega a operación

{.plain}
| Proyecto: [__________] | Fecha y hora de entrega: [____] |
|---|---|
| Etapa / alcance entregado: [__________] | Consecutivo: [____] |
| Recibe por [PROPIETARIO]: [__________] | Contrato N.º: [__________] |

| Ítem | Documento o condición | Entregado | No aplica | Obs. |
|---|---|---|---|---|
| 1 | Protocolos de pruebas en caliente y de desempeño aprobados | | | |
| 2 | Lista de pendientes con responsable y fecha | | | |
| 3 | Llaves de celdas, centros y recintos | | | |
| 4 | Control de candados de maniobra y registro de estados de áreas | | | |
| 5 | Ajustes definitivos de protecciones y parámetros de inversores y PPC | | | |
| 6 | Manuales de operación y plan de maniobras de operación normal | | | |
| 7 | Documentos conforme a obra disponibles | | | |
| 8 | Capacitación del personal de operación | | | |
| 9 | Designación del responsable de maniobras y permisos desde la entrega | | | |

{.plain}
| Observaciones y condiciones de la entrega: |
|---|

{.plain}
| | Entrega | Entrega | Recibe | Recibe |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] | [PROPIETARIO] |
| Nombre | | | | |
| Cargo | | | | |
| Firma | | | | |

# 15. CONTROL DE CAMBIOS

| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
