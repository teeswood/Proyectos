---
code: NES-OPE-PR-016
header_title: PROCEDIMIENTO DE EMPALMES Y TERMINALES DE MEDIA TENSIÓN
cover_title: Procedimiento de Empalmes y Terminales de Media Tensión
cover_subtitle: Terminales, conectores separables y empalmes en cables hasta 36 kV
---

# 1. OBJETIVO

Definir el método de trabajo, las condiciones de ejecución, los criterios de aceptación y las medidas preventivas para la confección de terminales interiores y exteriores, conectores separables tipo codo y en T, y empalmes contráctiles en frío y termocontráctiles en los cables de media tensión de aislamiento extruido hasta 36 kV (Um) de la planta FV [PROYECTO], incluida la puesta a tierra de pantallas, la marcación y los ensayos posteriores de aceptación en campo, conforme al RETIE, a IEEE 48, IEEE 404, IEEE 386, IEEE 400 e IEEE 400.2, a IEC 60502-4 y a las instrucciones del fabricante del accesorio.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services. La mayoría de las fallas de un sistema de cables MT nuevo ocurren en los accesorios y casi todas tienen su origen en la preparación del cable: un corte en el aislamiento, un residuo de semiconductora, una superficie contaminada o una medida fuera de la instrucción. Este procedimiento existe para que eso no ocurra.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en:

- Confección de terminales de interior y de exterior (premoldeados, contráctiles en frío y termocontráctiles) en cables MT unipolares y tripolares con aislamiento XLPE, TR-XLPE o EPR.
- Montaje de conectores separables apantallados tipo codo (enchufables) y tipo T (atornillables) en celdas MT, transformadores de los centros de transformación y equipos de maniobra.
- Confección de empalmes rectos contráctiles en frío y termocontráctiles, incluida la transición de pantallas de alambres o cintas.
- Compresión de terminales de cable (lugs) y de conectores de empalme, y montaje de conectores de tornillo fusible (shear bolt).
- Puesta a tierra de pantallas metálicas según el esquema de conexión de pantallas del diseño.
- Marcación e identificación de accesorios, fases y circuitos.
- Ensayos posteriores en campo: resistencia de aislamiento, ensayo de tensión soportada VLF, factor de disipación (tan delta) y descargas parciales, según IEEE 400 e IEEE 400.2.

No incluye el tendido de los cables y sus ensayos de recepción (resistencia de aislamiento, continuidad y ensayo de cubierta), que se rigen por NES-OPE-PR-015; la red de puesta a tierra, que se rige por NES-OPE-PR-020; ni las maniobras de energización, que se rigen por NES-OPE-PR-023. Los accesorios de baja tensión y la conectorización DC se rigen por NES-OPE-PR-014.

> NOTA: La instrucción de montaje del fabricante del accesorio es parte de este procedimiento y prevalece sobre él en medidas, secuencia y materiales. Cada kit trae su propia instrucción, que puede cambiar entre lotes: se lee la del kit que se va a instalar, no la del anterior.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / ART y PT | Análisis de trabajo seguro / análisis de riesgo del trabajo y permiso de trabajo. |
| Accesorio | Terminal, empalme o conector separable que completa el sistema de cable. |
| Terminal | Accesorio que termina el cable y controla el campo eléctrico donde se interrumpe la pantalla. IEEE 48 lo clasifica en clase 1 (control de campo, aislamiento externo y sello), clase 2 y clase 3. |
| Terminal de interior / de exterior | Terminal para ambiente protegido de intemperie, o para exposición a radiación UV, lluvia y contaminación, con faldones (campanas) que aumentan la distancia de fuga. |
| Empalme | Accesorio que une dos cables y restituye conductor, aislamiento, pantallas semiconductoras, pantalla metálica y cubierta (IEEE 404). |
| Conector separable | Accesorio apantallado y totalmente aislado que conecta el cable a un equipo mediante un pasatapas (bushing). Tipo codo de 200 A (operable con carga si así está clasificado) o tipo T de 600 A o más (atornillable, sin operación con carga), según IEEE 386 o norma equivalente. |
| Contráctil en frío | Accesorio de caucho expandido en fábrica sobre un núcleo removible; al retirar el núcleo, el caucho se contrae sobre el cable sin calor. |
| Termocontráctil | Accesorio de polímero que se contrae al aplicarle calor con soplete o pistola de calor. |
| Semiconductora externa | Capa extruida sobre el aislamiento que confina el campo eléctrico. Se retira en la zona del accesorio con un corte preciso. |
| Semiconductora interna | Capa extruida sobre el conductor; normalmente no se retira, salvo instrucción del fabricante. |
| Control de campo (de esfuerzo) | Elemento (cono, tubo de alta permitividad o masilla) que distribuye el campo eléctrico donde termina la semiconductora externa. |
| Pantalla metálica | Alambres o cintas de cobre sobre la semiconductora externa, conectados a tierra según el esquema de pantallas. |
| Conexión de pantallas en ambos extremos | Pantallas puestas a tierra en los dos extremos del circuito. Circulan corrientes inducidas por la pantalla. |
| Conexión en un solo punto | Pantallas puestas a tierra en un extremo y abiertas en el otro, con limitador de tensión de pantalla en el extremo abierto cuando el diseño lo exige. |
| Conector de compresión | Terminal de cable (lug) o manguito de empalme que se une al conductor por deformación con herramienta y dado específicos (IEC 61238-1). |
| Conector de tornillo fusible | Conector mecánico cuyos tornillos se rompen por la cabeza al alcanzar el torque de diseño. |
| VLF | Ensayo con tensión alterna de muy baja frecuencia (típicamente 0,1 Hz) para ensayos de tensión soportada y diagnóstico de cables MT (IEEE 400.2). |
| Tan delta (TD) | Factor de disipación del aislamiento. Se mide a varios niveles de tensión; su valor, su estabilidad en el tiempo y su variación con la tensión indican el estado del aislamiento. |
| Descargas parciales (DP) | Descargas localizadas que no puentean el aislamiento, típicas de vacíos, cortes o contaminación en los accesorios. Se miden en pC (IEEE 400.3). |
| U0 | Tensión asignada entre conductor y pantalla (fase a tierra) del cable. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. Los circuitos MT, los centros de transformación, la subestación y la ubicación de cada empalme se identifican en el plano general de implantación [N° de plano], en el diagrama unifilar MT [N° de plano] y en el plano de registro (as-built) de rutas de cables [N° de plano].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

- Diagrama unifilar MT, lista de cables y esquema de conexión de pantallas del proyecto — [N° de plano].
- Instrucciones de montaje de cada referencia de terminal, empalme y conector separable, en la versión que trae el kit.
- Fichas técnicas del cable MT: tensión asignada, sección, material del conductor, tipo de aislamiento, espesor de aislamiento, tipo de pantalla y diámetros sobre aislamiento y sobre semiconductora.
- Fichas técnicas de los conectores de compresión y de tornillo fusible, con la tabla de herramienta, dado y número de compresiones.
- Torques de los pasatapas de los equipos (celdas, transformadores) dados por su fabricante.
- Certificados de ensayos de tipo de los accesorios (IEEE 48, IEEE 404, IEEE 386 o IEC 60502-4) y certificados de conformidad de producto exigidos por el RETIE.
- NES-OPE-PR-015 Tendido de cables de potencia BT y MT; NES-OPE-PR-020 Puesta a tierra y SIPRA; NES-OPE-PR-022 Pruebas y comisionado del generador FV; NES-OPE-PR-023 Energización y puesta en servicio.
- NES-CAL-PLN-002 Plan de calidad; NES-SST-PLN-001 Plan de emergencias; NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado.

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes: requisitos de producto e instalación, competencia del personal, distancias de seguridad, cinco reglas de oro y dictamen de inspección antes de energizar.
- NTC 2050 — Código Eléctrico Colombiano, en los requisitos que el RETIE adopta para instalaciones de más de 1.000 V.
- Ley 1264 de 2008 (técnicos electricistas — CONTE); Ley 51 de 1986 y Ley 842 de 2003 (ingenieros — COPNIA): matrícula profesional vigente del personal.
- IEC 60502-2 — Cables de potencia con aislamiento extruido de 6 kV a 30 kV. IEC 60502-4 — Requisitos de ensayo de accesorios para esos cables.
- IEC 61238-1 — Conectores de compresión y mecánicos para cables de potencia: métodos y requisitos de ensayo.
- IEEE 48 — Terminales de cables de corriente alterna. IEEE 404 — Empalmes de cables de 2,5 kV a 500 kV. IEEE 386 — Conectores separables aislados para sistemas de distribución de más de 600 V. Referencias técnicas de producto.
- IEEE 400 — Guía para ensayos en campo y evaluación del aislamiento de sistemas de cables apantallados. IEEE 400.2 — Ensayos en campo con VLF. IEEE 400.3 — Ensayos de descargas parciales en campo.
- ISO 6789 — Herramientas de apriete: requisitos y calibración de torquímetros.
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST. Resolución 0312 de 2019 — Estándares mínimos.
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en el sector eléctrico; cinco reglas de oro.
- Resolución 0491 de 2020 — Espacios confinados, para empalmes en cámaras que lo sean. Resolución 4272 de 2021 — Trabajo en alturas, para terminales en estructuras elevadas.
- Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo.
- Decreto 1496 de 2018 — SGA, para solventes, masillas, grasas de silicona y gas combustible.
- Decreto 1076 de 2015 y sus modificaciones vigentes (RESPEL); Resolución 2184 de 2019 (código de colores); licencia ambiental y PMA del proyecto — [N° de resolución].
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Residente de obra Neptuno Energy Services

- Aprobar y divulgar el presente procedimiento y asegurar los recursos para su cumplimiento en calidad, SST y ambiente.
- Asegurar que solo confeccionen accesorios empalmadores cualificados y autorizados por escrito.
- Tramitar ante [CLIENTE] la aprobación de las referencias de accesorios y de cualquier cambio.
- Detener cualquier confección que no cumpla este procedimiento o la instrucción del fabricante.

## 6.2. Responsable eléctrico (ingeniero con matrícula COPNIA vigente)

- Verificar la compatibilidad entre cable, accesorio, conector y pasatapas antes de liberar los kits.
- Emitir el permiso de trabajo eléctrico y verificar que el circuito esté desenergizado, bloqueado y puesto a tierra cuando se trabaje sobre cables conectados o cerca de equipos energizados.
- Definir con el diseñador el esquema de conexión de pantallas y verificar su ejecución.
- Planificar, ejecutar o supervisar los ensayos VLF, tan delta y descargas parciales y firmar sus registros.

## 6.3. Supervisor de empalmes y terminales

- Asignar los trabajos a empalmadores cualificados para la familia de accesorio correspondiente.
- Verificar las condiciones ambientales y del puesto de trabajo antes de iniciar cada accesorio.
- Elaborar con los trabajadores el ATS/ART diario y la charla de inicio de turno.
- Diligenciar los registros el mismo día.

## 6.4. Empalmador (técnico electricista con matrícula CONTE vigente y cualificación del fabricante)

- Leer la instrucción del kit completo antes de cortar el cable y verificar que el kit corresponde al cable.
- Ejecutar la preparación del cable y el montaje según la instrucción, sin omitir ni alterar pasos.
- Medir y registrar las cotas críticas de cada accesorio.
- Rechazar el kit incompleto, vencido, dañado o que no corresponda al cable.

## 6.5. Responsable de calidad (QA/QC)

- Controlar el cumplimiento del Plan de Inspección y Ensayos derivado de NES-CAL-PLN-002, con puntos de espera en la preparación del cable de cada accesorio.
- Mantener la trazabilidad entre accesorio, lote, empalmador, circuito y ensayos.
- Registrar y hacer seguimiento a las no conformidades hasta su cierre.

## 6.6. Responsable SST (con licencia en SST vigente)

- Elaborar y divulgar la matriz de peligros de la actividad: riesgo eléctrico por inducción o por error de circuito, ensayos de alta tensión, trabajo en caliente, cortes, espacios confinados y sustancias químicas.
- Verificar permisos, EPP, extintor y demarcación de la zona de ensayos.
- Aplicar el protocolo de tormenta eléctrica y liderar la atención de emergencias.

## 6.7. Responsable ambiental

- Asegurar el cumplimiento del PMA y la gestión de recortes de cable, residuos de kits, solventes y trapos contaminados con gestores autorizados.

## 6.8. Trabajadores

- Cumplir este procedimiento y participar en el ATS/ART.
- Usar correctamente el EPP y las herramientas asignadas; no improvisar herramientas de preparación ni dados de compresión.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si no se cuenta con la herramienta o el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento/ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Responsable eléctrico, supervisor de empalmes, empalmadores cualificados, ayudantes, QA/QC, responsable SST, operador del equipo de ensayos VLF/TD/DP. |
| Materiales | Accesorios | Kits de terminal, empalme y conector separable de la referencia aprobada para la sección, el diámetro sobre aislamiento y la tensión del cable, dentro de su vida útil de almacenamiento; terminales de cable y manguitos de compresión o de tornillo fusible del fabricante; kits de puesta a tierra de pantallas; trenzas o cables de tierra. |
| Materiales | Consumibles | Solvente de limpieza aprobado por el fabricante del accesorio, paños sin pelusa, tela abrasiva no conductora del grano indicado por el fabricante, grasa o lubricante de silicona del kit, cinta de vinilo, cinta semiconductora y cinta de sellado del kit, rótulos de identificación. |
| Herramientas | Preparación del cable | Herramienta para retirar cubierta, herramienta para retirar semiconductora externa con tope de profundidad, herramienta para retirar aislamiento con tope, herramienta para chaflán, cortacables de trinquete, segueta de dientes finos, flexómetro y calibrador (pie de rey), plantilla de cotas del kit. |
| Herramientas | Compresión y apriete | Prensa hidráulica o manual con los dados indicados por el fabricante del conector; llave para conectores de tornillo fusible; torquímetros calibrados según ISO 6789 en el rango de los pernos de pasatapas y barras; llaves de vaso aisladas. |
| Herramientas | Calor | Pistola de calor industrial o soplete de gas con boquilla de llama suave, para accesorios termocontráctiles; extintor junto al puesto. |
| Equipos | Puesto de trabajo | Carpa o caseta cerrada con piso limpio, iluminación, mesa de trabajo, soportes para mantener el cable recto, bolsas para residuos, higrómetro y termómetro. |
| Equipos | Ensayos | Equipo VLF con medición de tan delta y, cuando el proyecto lo exija, sistema de medición de descargas parciales; megóhmetro de 5.000 V DC; pértigas de descarga y de puesta a tierra; detector de tensión MT; todos con calibración vigente. |
| EPP | Trabajo eléctrico | Guantes dieléctricos de clase acorde con la tensión del sistema con guante de protección, protección facial y ropa con la categoría que indique el análisis de riesgo de arco, calzado dieléctrico, casco dieléctrico. |
| EPP | Básico y químico | Casco con barbuquejo, gafas de seguridad, guantes anticorte para la preparación del cable, guantes de nitrilo para solventes, botas con puntera, ropa manga larga, protector solar, polainas en zonas con ofidios; protección respiratoria si la hoja de seguridad del solvente lo exige. |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

- Cable tendido, ensayado y liberado según NES-OPE-PR-015 (continuidad, resistencia de aislamiento y ensayo de cubierta), con extremos sellados hasta este momento.
- Kit correcto: referencia aprobada, tensión del sistema, sección del conductor, rango de diámetro sobre aislamiento del cable real (medido con calibrador), tipo de pantalla y tipo de conector; kit completo, sin daño y dentro de su vida útil de almacenamiento.
- Instrucción del kit leída por el empalmador y el supervisor, y cotas trasladadas a la plantilla o al formato.
- Empalmador cualificado para esa familia de accesorio, con autorización vigente (formato NES-OPE-F-090).
- Herramientas de preparación con topes ajustados, prensa con el dado correcto y torquímetro calibrado.
- Condiciones ambientales y del puesto verificadas y registradas en el formato NES-OPE-F-091.
- ATS/ART, permiso de trabajo y, si el cable o el equipo tiene conexión a una fuente, permiso de trabajo eléctrico con bloqueo, etiquetado y puesta a tierra según NES-SST-PR-001.
- Permiso de trabajo en caliente según NES-SST-PR-004 si se usa soplete; permiso de espacio confinado si la cámara lo es.

> ALTO: No se corta un cable MT hasta tener el kit correcto en la mano, verificado contra el cable real. Un cable cortado a la cota de otro kit no se recupera: hay que cortar de nuevo y la reserva de longitud puede no alcanzar.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

Se delimitan y señalizan: el puesto de confección (carpa o caseta), la zona del equipo de ensayos y ambos extremos del circuito durante los ensayos, las celdas y transformadores intervenidos, las cámaras de empalme abiertas y el punto de acopio de residuos. En celdas y centros de transformación con partes energizadas cercanas se aplican las distancias de seguridad del RETIE y se demarca el límite de aproximación.

### 8.2.2. Ingreso de personal

- Verificar que no haya trabajos simultáneos incompatibles en el mismo circuito o en el mismo centro de transformación.
- Diligenciar ATS/ART, permiso de trabajo y, cuando aplique, permiso de trabajo eléctrico, en caliente o de espacio confinado.
- Ubicar equipos de emergencia e inspeccionar el EPP.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional de vehículos y del generador eléctrico del puesto; circulación por rutas autorizadas.
- El vehículo del equipo de ensayos se ubica fuera de la zona demarcada de alta tensión y con su tierra conectada según el manual del equipo.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Cualificación del empalmador

- Solo confecciona accesorios MT el técnico electricista con matrícula CONTE vigente que además cumpla las tres condiciones siguientes:
  - Capacitación del fabricante del accesorio (o de su representante) en la familia correspondiente: terminal, empalme, conector separable; contráctil en frío o termocontráctil.
  - Probeta de calificación en obra: confección de un accesorio de cada familia sobre un tramo de cable del proyecto, en presencia de QA/QC, y disección posterior para verificar cotas, cortes, limpieza y posición del control de campo.
  - Autorización escrita del responsable eléctrico, registrada en el formato NES-OPE-F-090, con las familias y referencias autorizadas.
- La autorización se suspende si un accesorio confeccionado por el empalmador falla en ensayo por causa atribuible a la confección, hasta nueva probeta.
- Cada accesorio queda marcado con la identificación del empalmador y la fecha, para trazabilidad.

#### 8.2.4.2. Condiciones ambientales y puesto de trabajo

| Condición | Requisito |
|---|---|
| Recinto | Carpa o caseta cerrada por los cuatro costados, con piso limpio, que proteja de polvo, lluvia, viento y radiación solar directa. No se confecciona a la intemperie. |
| Humedad | Sin condensación sobre el cable ni sobre las piezas; humedad relativa dentro del límite del fabricante del accesorio — [____] % —; temperatura de las piezas por encima del punto de rocío. Registro con higrómetro al inicio y cada dos horas. |
| Temperatura | Dentro del rango de instalación del fabricante — [____] °C a [____] °C —. Con calor extremo, el caucho contráctil en frío se ablanda y los adhesivos curan distinto; con frío, los termocontráctiles requieren más calor. |
| Polvo | Sin polvo en suspensión; se suspenden los trabajos de movimiento de tierra cercanos durante la preparación final y el montaje. |
| Continuidad | Una vez iniciada la preparación final del aislamiento, el accesorio se completa sin interrupción. Si se debe interrumpir, se protege la zona preparada con película limpia y se repite la limpieza antes de continuar. |
| Iluminación | Suficiente para inspeccionar cortes y superficies; lámpara portátil para el interior de las celdas. |
| Cable | Recto y sin tensión en la zona del accesorio, soportado para que no gire ni se doble durante el montaje; enderezado con radio no menor que el mínimo del fabricante. |

> NOTA: En la costa Caribe y en los llanos de Colombia la humedad relativa en la madrugada y después de la lluvia es alta. Se programa la preparación final y el montaje en las horas de menor humedad del día y se registra la condición real; no se trabaja con la superficie del aislamiento húmeda.

#### 8.2.4.3. Verificación del kit y del cable

1. Medir con calibrador el diámetro sobre aislamiento y el diámetro sobre cubierta del cable real y verificar que están dentro del rango del kit.
2. Verificar en el rótulo del cable la sección, el material del conductor y la tensión; verificar que el conector (lug o manguito) corresponde a la sección y al material.
3. Revisar el contenido del kit contra la lista de la instrucción: piezas, masillas, cintas, grasa, solvente, paños, conectores.
4. Verificar la fecha de fabricación y la vida útil de almacenamiento del kit, en especial de los accesorios contráctiles en frío y de las masillas.
5. Verificar en conectores separables que la interfaz del pasatapas del equipo (tipo y corriente asignada) corresponde a la del conector.
6. Cortar el extremo sellado del cable y, si al cortarlo aparece humedad en el conductor o bajo la pantalla, detenerse y consultar al responsable eléctrico: se corta hasta encontrar cable seco o se reemplaza el tramo.

#### 8.2.4.4. Preparación del cable

La preparación se hace con las cotas de la instrucción del kit, medidas desde el extremo del cable, y se registra en el formato del accesorio. La secuencia general es:

1. Enderezar el cable y fijar la cota de corte final según la posición del pasatapas, del terminal o del empalme; cortar perpendicular con cortacables de trinquete.
2. Retirar la cubierta exterior a la cota de la instrucción, con un corte circular y uno longitudinal sin dañar la pantalla metálica. Limpiar la grasa o el material bloqueador de agua si lo hay.
3. Pantalla de alambres: doblar los alambres hacia atrás sobre la cubierta, ordenados y sin cruzarlos, o reunirlos según la instrucción. Pantalla de cintas: fijar el borde de la cinta con un amarre de alambre o con muelle de fuerza constante en la cota y cortar la cinta sin rasgar ni dejar puntas levantadas.
4. Retirar la semiconductora externa a la cota de la instrucción con la herramienta de profundidad ajustada, sin cortar ni rayar el aislamiento. El borde de la semiconductora debe quedar recto, continuo, sin dientes ni desprendimientos, y con el chaflán o el bisel que indique la instrucción.
5. Inspeccionar el aislamiento con luz rasante: sin cortes, ranuras, rayas profundas, residuos de semiconductora ni marcas de herramienta. Las marcas leves se eliminan con la tela abrasiva no conductora del grano del fabricante, sin reducir el diámetro por debajo del rango del kit y sin llevar partículas de semiconductora hacia el aislamiento.
6. Retirar el aislamiento en la zona del conector a la cota de la instrucción (largo del barril más la tolerancia que indique el fabricante), sin dañar los hilos del conductor; hacer el chaflán del borde del aislamiento si la instrucción lo exige.
7. Retirar la semiconductora interna del conductor solo si la instrucción lo indica.
8. Verificar las cotas con flexómetro y registrarlas antes de continuar. QA/QC verifica la preparación como punto de espera en los primeros accesorios de cada empalmador y por muestreo después — [____] % (criterio interno) —.

> ALTO: Un corte o una raya en el aislamiento bajo el control de campo, o un residuo de semiconductora sobre el aislamiento, concentra el campo eléctrico y produce descargas parciales que terminan en perforación. Un aislamiento cortado no se repara con cinta: se corta el cable y se prepara de nuevo.

#### 8.2.4.5. Limpieza del aislamiento

1. Limpiar el aislamiento con el solvente y los paños sin pelusa del kit o aprobados por el fabricante, en una sola dirección: desde el aislamiento hacia la semiconductora, nunca al revés, para no arrastrar partículas conductoras al aislamiento.
2. Usar cada paño una sola vez por pasada; no volver a pasar un paño usado.
3. Dejar evaporar el solvente por completo antes de aplicar grasa o montar piezas, según el tiempo del fabricante.
4. No tocar con las manos la superficie limpia; si se contamina, limpiar de nuevo.
5. No usar solventes distintos de los aprobados: algunos dejan residuo o atacan el caucho del accesorio.

#### 8.2.4.6. Conectores de compresión y de tornillo fusible

Compresión:

1. Verificar que el conector corresponde a la sección y al material del conductor (cobre o aluminio); para aluminio, usar conector apto y compuesto inhibidor si el fabricante lo indica.
2. Limpiar el conductor; en aluminio, cepillar la capa de óxido y aplicar el compuesto según el fabricante del conector.
3. Insertar el conductor hasta el fondo del barril; en manguitos de empalme, hasta el tope central o la marca de inserción en ambos lados.
4. Comprimir con la prensa y el dado indicados por el fabricante del conector, con el número y la secuencia de compresiones de su tabla: en terminales, desde el lado de la pala hacia el extremo del barril; en manguitos, desde el centro hacia los extremos, salvo que el fabricante indique otra secuencia.
5. Completar cada ciclo de la prensa hasta que el dado cierre por completo.
6. Retirar las rebabas y aristas vivas con lima fina y dejar la superficie lisa; limpiar las limaduras.
7. Verificar visualmente: compresiones completas, alineadas, sin fisuras en el barril y con la marca del dado legible si el sistema la imprime.

Tornillo fusible:

1. Verificar que el rango de sección del conector cubre el conductor.
2. Apretar los tornillos de forma alternada y en la secuencia del fabricante hasta que se rompa la cabeza de cada uno.
3. Limar los restos de cabeza que sobresalgan y limpiar las limaduras.

> NOTA: La resistencia de una unión mal comprimida aumenta con los ciclos térmicos hasta fallar. El dado y la prensa no se sustituyen por otros que «también cierran»: el sistema de compresión está ensayado como conjunto según IEC 61238-1.

#### 8.2.4.7. Terminales interiores y exteriores

Secuencia general, que se adapta a la instrucción del kit:

1. Preparar y limpiar el cable según los numerales 8.2.4.4 y 8.2.4.5.
2. Aplicar la masilla de control de campo o de relleno de vacíos en el borde de la semiconductora y, en terminales termocontráctiles, el tubo de control de campo, en la posición exacta de la instrucción respecto del borde de la semiconductora.
3. Instalar el terminal de cable (lug) por compresión y sellar la zona entre el lug y el aislamiento con la masilla o cinta de sellado del kit.
4. Contráctil en frío: posicionar el cuerpo del terminal según la marca de referencia (normalmente el borde de la semiconductora o una cota sobre la cubierta) y retirar el núcleo desenrollándolo en el sentido que indique la flecha, sujetando el cuerpo para que no se desplace mientras contrae.
5. Termocontráctil: contraer el tubo aislante y los faldones con llama suave y en movimiento continuo, empezando por el punto que indique la instrucción (generalmente desde el extremo del control de campo hacia el lug), hasta que el tubo quede liso, sin arrugas, sin burbujas y con el adhesivo asomando en los bordes. No se sobrecalienta ni se carboniza.
6. Terminal de exterior: verificar que los faldones quedan en número, separación y orientación (abertura hacia abajo) según la instrucción, y que la distancia de fuga corresponde al nivel de contaminación del sitio.
7. Conectar la pantalla metálica a tierra con el kit y la conexión del esquema de pantallas (numeral 8.2.4.10).
8. Instalar el terminal en el equipo o en la estructura, sin esfuerzo mecánico sobre el accesorio: el cable se soporta con abrazaderas para que su peso no cuelgue del lug.
9. Apretar la conexión del lug con el torque del fabricante del equipo o del conector — [____] N·m — con torquímetro calibrado, y marcar el perno con pintura de control de torque.
10. Verificar las distancias en aire entre fases y a tierra que exija el equipo y el RETIE.

#### 8.2.4.8. Conectores separables tipo codo y tipo T

1. Verificar la correspondencia entre la interfaz del conector y la del pasatapas del equipo, y la corriente asignada (por ejemplo, 200 A tipo codo o 600 A tipo T, según IEEE 386 o norma equivalente del producto).
2. Preparar y limpiar el cable según los numerales 8.2.4.4 y 8.2.4.5, con las cotas del conector.
3. Instalar el adaptador de cable (si el sistema lo usa) y el conector de compresión con la orientación de la pala que exija el pasatapas.
4. Aplicar la grasa de silicona del kit en la interfaz del cable y del adaptador según la instrucción; no usar grasas no aprobadas.
5. Introducir el cuerpo del conector sobre el cable hasta la posición final y verificar que el ojo del conector queda alineado con el pasatapas.
6. Limpiar el pasatapas del equipo con paño sin pelusa y aplicar la grasa en la interfaz según la instrucción.
7. Tipo T: montar sobre el pasatapas, colocar el perno o el espárrago, la arandela y la tuerca, y apretar al torque del fabricante del conector — [____] N·m — con torquímetro; instalar el tapón aislante y apretarlo a su torque; instalar la tapa conductora. Si hay conectores apilados o descargadores, montarlos en la secuencia de la instrucción.
8. Tipo codo: acoplar al pasatapas con la pértiga o a mano según el estado del equipo, hasta el enclavamiento completo; verificar que el anillo indicador (si lo tiene) no queda visible.
9. Conectar a tierra el punto de prueba o el drenaje del cuerpo semiconductor del conector y la pantalla del cable, según la instrucción.
10. Soportar los cables en la celda para que no ejerzan esfuerzo lateral sobre los pasatapas.
11. Los pasatapas no usados se cubren con tapón aislante apantallado aterrizado; nunca quedan expuestos.

> ALTO: Un conector tipo T no se opera con carga. Un codo de 200 A solo se opera con carga si está clasificado para ello y con pértiga, siguiendo el procedimiento de maniobra del proyecto. La operación de conectores separables durante la energización se rige por NES-OPE-PR-023.

#### 8.2.4.9. Empalmes rectos

1. Verificar la longitud de reserva de ambos cables y el espacio en la cámara o la zanja para el empalme más su zona de trabajo. Los empalmes de fases de un mismo circuito se desplazan entre sí cuando el diseño lo indica.
2. Antes de unir los conductores, colocar sobre uno de los cables, en el orden de la instrucción, todas las piezas que se deslizan: cuerpo del empalme, tubos, malla de pantalla y cubierta exterior. Una pieza olvidada obliga a cortar el conector y rehacer.
3. Preparar y limpiar ambos extremos según los numerales 8.2.4.4 y 8.2.4.5.
4. Instalar el manguito de compresión o de tornillo fusible según el numeral 8.2.4.6; retirar rebabas y limpiar.
5. Rellenar con la masilla o la cinta semiconductora el espacio entre el manguito y el aislamiento, si la instrucción lo indica.
6. Contráctil en frío: centrar el cuerpo del empalme con las marcas de la instrucción respecto del centro del manguito, retirar el núcleo en el sentido de la flecha y verificar que el cuerpo cubre la semiconductora de ambos lados en la longitud indicada.
7. Termocontráctil: contraer los tubos de control de campo, de aislamiento y de semiconductora en el orden de la instrucción, desde el centro hacia los extremos, con llama suave y en movimiento, sin arrugas ni burbujas.
8. Restituir la continuidad de la pantalla metálica con la malla de cobre o el conector de pantalla del kit, unida a los alambres o cintas de ambos lados con la sección exigida por el diseño.
9. Instalar la cubierta exterior (tubo termocontráctil con adhesivo o manga contráctil en frío y masilla de sellado), con el traslape sobre la cubierta original que indique la instrucción, para impedir el ingreso de agua.
10. Dejar el empalme recto, apoyado sobre la cama de arena o soportado en la cámara, sin curvas en los primeros tramos a cada lado y sin esfuerzo mecánico.
11. Identificar el empalme con circuito, fase, número de empalme, empalmador y fecha, y registrar su ubicación georreferenciada en el plano de registro.

#### 8.2.4.10. Puesta a tierra de pantallas

- El esquema de conexión de pantallas (ambos extremos, un solo punto o transposición) lo define el diseñador y se ejecuta exactamente como está en el plano. No se modifica en campo.
- En conexión en ambos extremos, las pantallas de las tres fases se conectan a la barra de tierra del equipo en cada extremo, con conductor de la sección del diseño y conexión de compresión o atornillada.
- En conexión en un solo punto, el extremo abierto se aísla con el accesorio previsto y, si el diseño lo exige, se instala el limitador de tensión de pantalla; se señaliza que la pantalla puede tener tensión inducida.
- En los empalmes, la pantalla se da continuidad salvo que el diseño prevea seccionamiento o transposición; en ese caso se instalan los accesorios de aislamiento de pantalla y las cajas de conexión del diseño.
- Las conexiones de pantalla a tierra se aprietan al torque del fabricante del conector o del equipo y se verifican con continuidad.
- La red de tierra a la que se conectan se rige por NES-OPE-PR-020.

> ALTO: La pantalla de un cable con un extremo abierto puede tener tensión inducida o transferida peligrosa durante una falla o con el circuito en servicio. Se trata como parte activa: no se toca sin verificar y poner a tierra.

#### 8.2.4.11. Marcación e identificación

- Identificar cada terminal y cada conector separable con circuito, fase (L1, L2, L3) y destino, con rótulo indeleble y resistente a UV.
- Identificar cada empalme con circuito, fase, número de empalme, empalmador, fecha y lote del kit.
- Mantener la correspondencia de fases de extremo a extremo; se verifica con el ensayo de continuidad y correspondencia antes del ensayo VLF.
- Registrar en el plano de registro la posición de cada empalme y el tipo de accesorio de cada extremo.

#### 8.2.4.12. Ensayos posteriores a la confección

Con todos los accesorios del circuito confeccionados, y antes de la energización, se ejecutan los ensayos siguientes, en este orden, y se registran en el formato NES-OPE-F-095. Los ensayos de alta tensión los ejecuta personal calificado con permiso de trabajo eléctrico, zona demarcada en ambos extremos y comunicación por radio.

Preparación del circuito:

1. Aislar el circuito: conectores separables retirados de los pasatapas o equipos desconectados, transformadores de tensión y descargadores desconectados, salvo que el fabricante permita ensayarlos.
2. Si los conectores separables no se pueden retirar, verificar con el fabricante del equipo que el pasatapas y la celda admiten la tensión de ensayo; si no la admiten, ensayar el cable con adaptadores de ensayo.
3. Conectar a tierra las pantallas de todas las fases y las fases no ensayadas.
4. Verificar la ausencia de tensión y poner a tierra el circuito antes de conectar el equipo.

Secuencia de ensayos:

| N.º | Ensayo | Método | Criterio |
|---|---|---|---|
| 1 | Continuidad y correspondencia de fases | Óhmetro o equipo de identificación de fases entre extremos. | Correspondencia L1-L1, L2-L2, L3-L3. |
| 2 | Resistencia de aislamiento antes del VLF | Megóhmetro a 5.000 V DC (o la tensión del fabricante), 1 min, conductor contra pantalla aterrizada. | Valor del fabricante o de la especificación — [____] MΩ —; fases coherentes. Sirve para descartar una falla franca antes de aplicar VLF. |
| 3 | Tan delta (si el proyecto lo exige) | VLF 0,1 Hz sinusoidal; escalones a 0,5 U0, 1,0 U0 y 1,5 U0, varias mediciones por escalón (IEEE 400.2). | Ver tabla de tan delta. En cable nuevo los valores sirven de línea base. |
| 4 | Tensión soportada VLF | 0,1 Hz sinusoidal o coseno-rectangular, tensión de instalación o de aceptación de la tabla de IEEE 400.2, durante el tiempo que fije el proyecto (IEEE 400.2 recomienda 30 min; el proyecto puede fijar hasta 60 min). | Sin ruptura durante todo el tiempo de ensayo. |
| 5 | Descargas parciales (si el proyecto lo exige) | Medición en línea o fuera de línea según IEEE 400.3, con localización de las fuentes. | Sin descargas parciales en los accesorios por encima de la sensibilidad declarada a la tensión de ensayo, o el criterio de la especificación — [____] pC —. |
| 6 | Resistencia de aislamiento después del VLF | Igual que el ensayo 2. | Sin disminución significativa respecto del valor previo. |
| 7 | Continuidad de pantallas y conexiones a tierra | Óhmetro. | Conexiones según el esquema de pantallas. |

Tensiones de ensayo VLF de referencia, sinusoidal de 0,1 Hz, fase a tierra, según IEEE 400.2 (edición 2013):

| Clase de tensión del cable (fase a fase) | Instalación (kV rms / kV pico) | Aceptación (kV rms / kV pico) | Uso típico en Colombia |
|---|---|---|---|
| 15 kV | 19 / 27 | 21 / 30 | Colectores de 13,2 kV y 13,8 kV |
| 25 kV | 29 / 41 | 32 / 45 | Colectores de 22 kV a 25 kV |
| 35 kV | 39 / 55 | 44 / 62 | Colectores de 34,5 kV |

La prueba de instalación se aplica al cable tendido antes de los accesorios; la de aceptación, al sistema completo con accesorios antes de la energización. Las de mantenimiento son del orden del 75% de la de aceptación. Antes de ensayar se confirma la tabla de la edición vigente de IEEE 400.2 y la que exija la especificación de [CLIENTE]. Cuando el cable sea de tensión asignada IEC (U0/U), el responsable eléctrico define la tensión de ensayo con base en U0 y lo deja escrito en el formato.

Criterios de referencia de tan delta para aislamiento tipo PE (PE, XLPE, TR-XLPE) envejecido en servicio, a 0,1 Hz, según IEEE 400.2 (edición 2013), en unidades de 10⁻³:

| Condición | Estabilidad a U0 (desviación estándar) | Diferencia de TD (1,5 U0 − 0,5 U0) | TD medio a U0 |
|---|---|---|---|
| No requiere acción | < 0,1 | < 5 | < 4 |
| Requiere estudio adicional | 0,1 a 0,5 | 5 a 80 | 4 a 50 |
| Requiere acción | > 0,5 | > 80 | > 50 |

> NOTA: La tabla de tan delta de IEEE 400.2 se construyó con cables envejecidos y tiene criterios distintos para aislamientos rellenos (EPR). En cable nuevo, un valor alto, inestable o que crece con la tensión indica humedad, contaminación o un accesorio defectuoso: se investiga antes de aceptar. El criterio definitivo lo fija la especificación del proyecto y se confirma contra la edición vigente de la norma.

> ALTO: No se usa ensayo de tensión DC de alto valor en cables de aislamiento extruido envejecidos: IEEE 400 advierte que puede dañar el aislamiento. En cable nuevo, la tensión DC se limita al ensayo de aislamiento con megóhmetro y al ensayo de cubierta; la tensión soportada se hace con VLF, salvo especificación distinta de [CLIENTE] acordada con el fabricante del cable.

Al terminar cada ensayo de alta tensión, descargar el circuito con la pértiga de descarga y dejarlo puesto a tierra el tiempo que indique el fabricante del equipo de ensayo; el cable aislado puede recuperar carga después de una descarga breve.

#### 8.2.4.13. Resultados fuera de criterio

- Ruptura en VLF: se localiza la falla, se corta el tramo o el accesorio fallado, se analiza la causa (disección del accesorio en presencia de QA/QC) y se repite el ensayo completo del circuito tras la reparación.
- Tan delta o descargas parciales fuera de criterio: se segmenta el circuito o se localizan las descargas para identificar el accesorio responsable, se rehace y se repite el ensayo.
- Toda falla atribuible a la confección suspende la autorización del empalmador hasta nueva probeta (numeral 8.2.4.1) y se registra como no conformidad grado 3.

#### 8.2.4.14. Trabajo en caliente con accesorios termocontráctiles

- Preferir pistola de calor industrial; si se usa soplete de gas, aplicar el permiso de trabajo en caliente, extintor a la distancia que fije NES-SST-PR-004 Trabajos en caliente, cilindro en posición vertical y fuera de la carpa, mangueras y reguladores inspeccionados.
- Retirar de la zona solventes, paños con solvente y materiales combustibles; no calentar mientras haya vapores de solvente.
- Ventilar la carpa o la cámara; en cámaras que sean espacio confinado, monitorear la atmósfera y no introducir el cilindro de gas.

#### 8.2.4.15. No conformidades

- Kit incompleto, vencido, dañado o que no corresponde al cable: cuarentena y consulta a QA/QC.
- Cota fuera de tolerancia, corte o raya en el aislamiento, residuo de semiconductora, compresión incompleta, pieza olvidada en un empalme: se corta y se rehace.
- Torque no verificado o sin marca: se verifica con torquímetro calibrado antes de liberar.
- Esquema de pantallas distinto del plano: se corrige antes de los ensayos.
- Cambio de referencia de accesorio: requiere aprobación escrita del diseñador y de [CLIENTE] y queda en el registro de RFI.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Empalmador | Matrícula CONTE vigente, capacitación del fabricante en la familia, probeta aprobada y autorización escrita | Ley 1264 de 2008 / RETIE / Este procedimiento |
| Accesorio | Referencia aprobada, rango de diámetro compatible con el cable real, dentro de su vida útil, con ensayos de tipo y certificado de producto | Fabricante / IEEE 48, 404, 386 / IEC 60502-4 / RETIE |
| Condiciones ambientales | Recinto cerrado, sin condensación, humedad y temperatura dentro de los límites del fabricante | Instrucción del fabricante |
| Cotas de preparación | Las de la instrucción del kit, medidas y registradas | Instrucción del fabricante |
| Superficie del aislamiento | Sin cortes, ranuras, residuos de semiconductora ni contaminación; limpieza en un solo sentido | Instrucción del fabricante |
| Borde de semiconductora | Recto, continuo, sin dientes; chaflán según instrucción | Instrucción del fabricante |
| Compresión | Herramienta, dado, número y secuencia de compresiones del fabricante; sin rebabas | Fabricante del conector / IEC 61238-1 |
| Tornillo fusible | Cabezas rotas en la secuencia del fabricante; restos limados | Fabricante del conector |
| Torques | Los del fabricante del conector o del equipo, aplicados con torquímetro calibrado (ISO 6789) y marcados | Fabricante / ISO 6789 |
| Terminal de exterior | Faldones y distancia de fuga según instrucción y nivel de contaminación del sitio | Instrucción del fabricante |
| Pantallas | Según el esquema del diseño; continuidad verificada | Diseño / NES-OPE-PR-020 |
| Identificación | Circuito, fase, empalmador, fecha y lote en cada accesorio | Este procedimiento |
| Tensión soportada VLF | Sin ruptura a la tensión de IEEE 400.2 (o de la especificación) durante el tiempo fijado | IEEE 400.2 |
| Tan delta | Según criterio de la especificación; referencia IEEE 400.2 | IEEE 400.2 / Especificación |
| Descargas parciales | Sin DP en accesorios sobre la sensibilidad declarada o el valor de la especificación | IEEE 400.3 / Especificación |
| Resistencia de aislamiento | Valor del fabricante o de la especificación, coherente entre fases y antes y después del VLF | Fabricante / Especificación |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-090 a NES-OPE-F-096 de este procedimiento.
- Instrucciones de montaje de los kits instalados, certificados de ensayos de tipo y de conformidad de producto por lote.
- Certificados de calibración de torquímetros, prensas (cuando aplique), megóhmetro y equipos VLF, TD y DP.
- Informes completos de los ensayos VLF, tan delta y descargas parciales generados por el equipo.
- Registro fotográfico de cada accesorio en sus etapas de preparación del cable, conector instalado y accesorio terminado.
- Plano de registro (as-built) con la posición de empalmes y el esquema de pantallas ejecutado.

## 8.5. Control de calidad

QA/QC verifica como punto de espera (H) la preparación del cable de los tres primeros accesorios de cada empalmador y de cada familia, y después por muestreo — [____] % (criterio interno) —; verifica el 100% de los accesorios terminados (identificación, torques marcados, pantallas) y asiste como punto de espera a los ensayos de aceptación de todos los circuitos MT. Si un accesorio falla en ensayo por causa de confección, se revisan los demás accesorios del mismo empalmador y del mismo lote. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Desviación que no afecta calidad, prestación ni seguridad, por ejemplo rótulo incompleto o registro tardío. | Registro y cierre. |
| 2 | Requiere corregir sin rehacer el accesorio: torque no marcado, soporte del cable insuficiente, conexión de pantalla floja. | Corrección por la cuadrilla y reinspección. |
| 3 | Afecta la confiabilidad o la seguridad del circuito: accesorio mal preparado o con pieza faltante, kit incorrecto, ruptura en VLF, tan delta o DP fuera de criterio, esquema de pantallas erróneo. | Suspensión del circuito, rehacer el accesorio, análisis de causa y aprobación escrita antes de energizar. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS/ART y la charla diaria, verifica que las zonas de confección y de ensayos estén señalizadas y demarcadas y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre características del proyecto, riesgo eléctrico en MT, tensiones inducidas, ensayos de alta tensión, trabajo en caliente, sustancias químicas, puntos de encuentro y uso correcto del EPP.

## 9.1. Reglas de oro

- **SIEMPRE** aplicaré las cinco reglas de oro del RETIE antes de intervenir un cable o un equipo MT: cortar, bloquear, verificar ausencia de tensión, poner a tierra y señalizar (Res. 5018 de 2019).
- **NUNCA** confiaré en que un cable está desenergizado porque «no está conectado»: verifico y pongo a tierra.
- **SIEMPRE** trataré como activa la pantalla con un extremo abierto y el cable recién ensayado hasta descargarlo y ponerlo a tierra.
- **NUNCA** entraré en la zona demarcada de ensayo de alta tensión mientras el equipo esté conectado.
- **SIEMPRE** custodiaré el extremo remoto del cable durante un ensayo, con radio y señalización.
- **NUNCA** operaré un conector tipo T con carga ni un codo que no esté clasificado para ello.
- **SIEMPRE** usaré guantes anticorte al preparar el cable y cortaré alejando la herramienta del cuerpo.
- **NUNCA** calentaré con llama cerca de solventes o en espacio confinado sin permiso y monitoreo.
- **SIEMPRE** suspenderé la actividad ante tormenta eléctrica y me dirigiré al refugio o punto de encuentro.
- **SIEMPRE** ejecutaré el trabajo con ATS/ART y permiso de trabajo diligenciados.

## 9.2. Riesgos específicos

- Riesgo eléctrico: error de circuito, retorno de tensión desde otra fuente, tensión inducida por circuitos paralelos energizados, carga capacitiva residual tras los ensayos. Control con NES-SST-PR-001, detector de tensión MT, puesta a tierra temporal y distancias de seguridad del RETIE.
- Ensayos de alta tensión: zona demarcada con cinta y señal en ambos extremos, vigía en cada extremo, comunicación permanente, descarga a tierra al terminar.
- Cortes: herramientas de preparación con hoja expuesta; guantes anticorte, corte hacia afuera, herramientas guardadas con protector.
- Trabajo en caliente: quemaduras, incendio de la carpa; pistola de calor preferida, extintor, permiso.
- Sustancias químicas: solventes inflamables e irritantes; hoja de seguridad, guantes de nitrilo, ventilación y almacenamiento rotulado según el SGA (Decreto 1496 de 2018).
- Espacio confinado y trabajo en alturas: Resoluciones 0491 de 2020 y 4272 de 2021 cuando apliquen.

## 9.3. Condiciones climáticas de [departamento]

- Tormenta eléctrica: ante el aviso o el primer trueno, suspender la confección y los ensayos, proteger la zona preparada, poner a tierra el circuito, alejarse de cables, celdas y estructuras metálicas y dirigirse al refugio. Se reanuda solo con autorización del responsable SST.
- Lluvia y humedad: no se confecciona si la carpa no garantiza ausencia de agua y de condensación; no se ensaya con terminales de exterior mojados o contaminados.
- Calor y radiación: hidratación, sombra, pausas y rotación; la carpa se ventila para no superar la temperatura de instalación del fabricante.
- Fauna: revisar cámaras, celdas y zanjas antes de intervenir; presencia de ofidios e insectos en cámaras; polainas.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado al frente | Colisión, volcamiento, caídas al mismo nivel. | Conductores autorizados; vías y velocidades del proyecto; PESV. |
| 2. Montaje de carpa y puesto de trabajo | Caída de la estructura por viento, golpes, sobreesfuerzo. | Carpa anclada; dos personas; no montar con viento fuerte. |
| 3. Verificación de ausencia de tensión y puesta a tierra | Choque eléctrico, arco, error de circuito. | Permiso de trabajo eléctrico; NES-SST-PR-001; detector de tensión MT probado; puesta a tierra temporal; EPP con categoría de arco. |
| 4. Corte y preparación del cable | Cortes en manos y antebrazos, proyección de partículas. | Herramientas con tope; guantes anticorte; gafas; corte hacia afuera. |
| 5. Limpieza con solventes | Inhalación, irritación, incendio. | Hoja de seguridad; guantes de nitrilo; ventilación; sin llama cercana. |
| 6. Compresión de conectores | Atrapamiento de dedos en la prensa, proyección por falla hidráulica. | Prensa inspeccionada; manos fuera del dado; mangueras sin daño. |
| 7. Contracción con calor | Quemaduras, incendio. | Pistola de calor preferida; permiso en caliente con soplete; extintor; cilindro fuera de la carpa. |
| 8. Montaje en celdas y transformadores | Contacto con partes energizadas cercanas, golpes. | Distancias de seguridad del RETIE; equipos desenergizados y aterrizados; iluminación. |
| 9. Apriete con torquímetro | Golpes, sobreesfuerzo, herramienta inadecuada. | Torquímetro calibrado; postura estable; llaves aisladas cerca de partes energizadas. |
| 10. Empalmes en cámaras o zanjas | Derrumbe, atmósfera peligrosa, caídas. | NES-OPE-PR-002; permiso de espacio confinado y medición de gases cuando aplique; escaleras. |
| 11. Ensayos VLF, TD y DP | Choque eléctrico por tensión de ensayo o carga residual. | Zona demarcada en ambos extremos; vigías con radio; equipo aterrizado; pértiga de descarga; personal calificado. |
| 12. Exposición ambiental | Radiación UV, estrés térmico, ofidios, tormenta eléctrica. | Ropa manga larga, cubrenuca, protector solar, hidratación, pausas; polainas; protocolo de tormenta. |
| 13. Orden, aseo y residuos | Cortes con recortes de cable, contaminación. | Recortes y residuos de kits en recipiente; trapos con solvente como RESPEL. |

# 11. ASPECTOS AMBIENTALES

El personal debe haber recibido la inducción ambiental de ingreso y la charla sobre flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Aire | Emisiones, vapores de solvente y humo de calentamiento | Cantidad mínima de solvente; recipientes cerrados; no sobrecalentar polímeros; ventilación. |
| Suelo | Residuos sólidos | Separación en la fuente con el código de colores de la Res. 2184 de 2019; cajas y embalajes de kits a aprovechamiento. |
| Suelo | Recortes de cable y de conductor | Recogidos el mismo día y almacenados como aprovechables; entrega a gestor autorizado con certificado. |
| Suelo | Residuos peligrosos (RESPEL) | Paños con solvente, envases de solvente y de masillas, núcleos y piezas contaminadas en recipientes rotulados; almacenamiento temporal en zona RESPEL y entrega a gestor autorizado según Decreto 1076 de 2015. |
| Suelo | Derrames | Kit antiderrame para solventes y para el aceite hidráulico de la prensa; bandeja bajo el generador. |
| Flora y fauna | Intervención de hábitat | Trabajar solo en áreas liberadas; revisar cámaras antes de intervenir; reporte de fauna para rescate según PMA. |
| Agua | Contaminación | Prohibido verter solventes o lavar herramientas en drenajes o cuerpos de agua. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener la actividad, desenergizar el equipo de ensayo y asegurar la zona.
2. Notificar al responsable SST y al responsable eléctrico de Neptuno Energy Services y al interlocutor de [CLIENTE].
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, extintor en cada frente).
4. Incidente grave: activar ambulancia por la línea 123 y traslado al centro asistencial definido; notificar a la ARL.
5. Reportar el evento y realizar la investigación según Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Choque eléctrico o arco

- No tocar a la víctima mientras siga en contacto con el circuito; cortar la fuente o separarla con elemento aislante; descargar el cable con pértiga si estaba en ensayo.
- Activar la emergencia y aplicar reanimación si el personal está capacitado. Toda persona que sufra un choque eléctrico se remite a valoración médica aunque se sienta bien.
- Quemaduras por arco: enfriar con agua limpia a temperatura ambiente, no retirar ropa adherida, cubrir con apósito estéril y remitir; exposición ocular al destello: cubrir y remitir a valoración oftalmológica.

## 12.2. Cortes

- Controlar la hemorragia con presión directa y apósito estéril; elevar la extremidad; remitir si el corte es profundo o compromete tendones.

## 12.3. Incendio en el puesto de trabajo

- Cerrar la válvula del cilindro de gas si es seguro; usar el extintor apto; si el fuego avanza, evacuar y activar la emergencia.

## 12.4. Exposición a solventes

- Inhalación: llevar a la persona al aire libre. Contacto con piel u ojos: lavar con abundante agua durante el tiempo que indique la hoja de seguridad. Remitir con la hoja de seguridad del producto.

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Responsable eléctrico Neptuno Energy Services | [__________] | [__________] |
| Residente de obra Neptuno Energy Services | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| Centro de control / sala de operación | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Cualificación y autorización de empalmadores MT | NES-OPE-F-090 | Responsable eléctrico |
| Condiciones ambientales y liberación del puesto de trabajo | NES-OPE-F-091 | Supervisor de empalmes |
| Protocolo de confección de terminal MT | NES-OPE-F-092 | QA/QC |
| Protocolo de confección de empalme MT | NES-OPE-F-093 | QA/QC |
| Protocolo de montaje de conector separable | NES-OPE-F-094 | QA/QC |
| Registro de ensayos VLF, tan delta y descargas parciales | NES-OPE-F-095 | Responsable eléctrico |
| Registro de conexión de pantallas y torques | NES-OPE-F-096 | QA/QC |
| ATS/ART y permisos de trabajo (eléctrico, en caliente, espacio confinado) | Según SG-SST | Supervisor / Responsable SST |
| Certificados de calibración y de producto | Según NES-CAL-PLN-002 | QA/QC |

\pagebreak

# 14. ANEXOS

## NES-OPE-F-090 — Cualificación y autorización de empalmadores MT

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Nombre del empalmador: [__________] | Documento de identidad: [__________] |
| Matrícula CONTE N.º: [__________] | Vigencia: [____] |
| Documento de referencia: NES-OPE-PR-016 | Consecutivo: [____] |

| Familia de accesorio | Referencia / fabricante | Certificado de capacitación del fabricante | Probeta (fecha) | Resultado de disección | Autorizado (Sí / No) |
|---|---|---|---|---|---|
| Terminal interior |  |  |  |  |  |
| Terminal exterior |  |  |  |  |  |
| Conector separable tipo T |  |  |  |  |  |
| Conector separable tipo codo |  |  |  |  |  |
| Empalme contráctil en frío |  |  |  |  |  |
| Empalme termocontráctil |  |  |  |  |  |

| Ítem | Verificación de la probeta | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Cotas de preparación según instrucción |  |  |  |
| 2 | Aislamiento sin cortes ni rayas bajo el accesorio |  |  |  |
| 3 | Borde de semiconductora recto y continuo |  |  |  |
| 4 | Limpieza sin residuos de semiconductora |  |  |  |
| 5 | Compresión con dado y número de compresiones correctos |  |  |  |
| 6 | Control de campo en la posición de la instrucción |  |  |  |
| 7 | Sin vacíos ni burbujas en la interfaz |  |  |  |

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

## NES-OPE-F-091 — Condiciones ambientales y liberación del puesto de trabajo

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito / ubicación: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-016 | Límites del fabricante: HR [____] % / T [____] °C |

| Hora | Temperatura (°C) | Humedad relativa (%) | Punto de rocío (°C) | Condensación (Sí / No) | Polvo / viento | Apto (Sí / No) |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

| Ítem | Verificación | Cumple | No cumple | N/A |
|---|---|---|---|---|
| 1 | Carpa o caseta cerrada, piso limpio, iluminación suficiente |  |  |  |
| 2 | Cable recto, soportado y sin tensión en la zona del accesorio |  |  |  |
| 3 | Circuito desenergizado, bloqueado y puesto a tierra (si aplica) |  |  |  |
| 4 | Permiso de trabajo eléctrico vigente (si aplica) |  |  |  |
| 5 | Permiso de trabajo en caliente y extintor (si se usa soplete) |  |  |  |
| 6 | Permiso de espacio confinado y medición de gases (si aplica) |  |  |  |
| 7 | Sin trabajos de movimiento de tierra cercanos durante el montaje |  |  |  |
| 8 | Kit verificado contra el cable real y dentro de su vida útil |  |  |  |

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

## NES-OPE-F-092 — Protocolo de confección de terminal MT

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito / fase / equipo: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-016 / IEEE 48 | Tipo: interior / exterior; frío / calor |

{.plain}
| Cable (referencia, sección, U0/U): [__________] | Diámetro sobre aislamiento medido: [____] mm |
|---|---|
| Kit (referencia, lote, fecha): [__________] | Rango de diámetro del kit: [____] mm |
| Terminal de cable (referencia, dado): [__________] | Empalmador: [__________] |

| Ítem | Verificación | Cota instrucción (mm) | Cota medida (mm) | Cumple |
|---|---|---|---|---|
| 1 | Retiro de cubierta |  |  |  |
| 2 | Corte de pantalla metálica |  |  |  |
| 3 | Retiro de semiconductora externa |  |  |  |
| 4 | Retiro de aislamiento (zona del lug) |  |  |  |
| 5 | Posición del control de campo respecto del borde de semiconductora |  |  |  |
| 6 | Aislamiento sin cortes, rayas ni residuos | — | — |  |
| 7 | Limpieza en un solo sentido con solvente aprobado | — | — |  |
| 8 | Compresión del lug: N.º de compresiones [____], sin rebabas | — | — |  |
| 9 | Contracción completa, sin arrugas, burbujas ni carbonización | — | — |  |
| 10 | Faldones en número y orientación de la instrucción (exterior) | — | — |  |
| 11 | Pantalla conectada a tierra según esquema | — | — |  |
| 12 | Torque de la conexión del lug: [____] N·m, marcado | — | — |  |
| 13 | Distancias en aire fase-fase y fase-tierra verificadas | — | — |  |
| 14 | Cable soportado sin esfuerzo sobre el terminal | — | — |  |
| 15 | Identificación de circuito, fase, empalmador y fecha | — | — |  |

{.plain}
| Observaciones y registro fotográfico: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-093 — Protocolo de confección de empalme MT

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito / fase / N.º de empalme: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-016 / IEEE 404 | Tipo: contráctil en frío / termocontráctil |
| Ubicación (cámara / abscisa / coordenadas): [__________] | Empalmador: [__________] |

{.plain}
| Cable lado A (referencia, carrete): [__________] | Cable lado B (referencia, carrete): [__________] |
|---|---|
| Diámetro sobre aislamiento A / B: [____] / [____] mm | Kit (referencia, lote, fecha): [__________] |
| Manguito (referencia, dado o tornillo fusible): [__________] | Rango de diámetro del kit: [____] mm |

| Ítem | Verificación | Cota instrucción (mm) | Cota medida A / B (mm) | Cumple |
|---|---|---|---|---|
| 1 | Piezas deslizantes colocadas en orden antes de unir conductores | — | — |  |
| 2 | Retiro de cubierta |  |  |  |
| 3 | Corte de pantalla metálica |  |  |  |
| 4 | Retiro de semiconductora externa |  |  |  |
| 5 | Retiro de aislamiento (zona del manguito) |  |  |  |
| 6 | Aislamiento sin cortes, rayas ni residuos; limpieza en un sentido | — | — |  |
| 7 | Manguito comprimido desde el centro, N.º de compresiones [____], sin rebabas | — | — |  |
| 8 | Cuerpo del empalme centrado según marcas | — | — |  |
| 9 | Traslape sobre semiconductora en ambos lados |  |  |  |
| 10 | Continuidad de pantalla restituida con la sección del diseño | — | — |  |
| 11 | Cubierta exterior sellada con traslape sobre la cubierta original |  |  |  |
| 12 | Empalme recto y apoyado, sin esfuerzo mecánico | — | — |  |
| 13 | Identificación y posición registrada en as-built | — | — |  |

{.plain}
| Observaciones y registro fotográfico: |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-094 — Protocolo de montaje de conector separable

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Equipo (celda / transformador) y posición: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-016 / IEEE 386 | Tipo: T (atornillable) / codo (enchufable) |

{.plain}
| Cable (referencia, sección, U0/U): [__________] | Diámetro sobre aislamiento medido: [____] mm |
|---|---|
| Conector (referencia, lote, corriente asignada): [__________] | Interfaz del pasatapas: [__________] |
| Torque del perno o espárrago (fabricante): [____] N·m | Empalmador: [__________] |

| Ítem | Verificación | L1 | L2 | L3 |
|---|---|---|---|---|
| 1 | Interfaz y corriente del conector compatibles con el pasatapas |  |  |  |
| 2 | Cotas de preparación según instrucción |  |  |  |
| 3 | Aislamiento sin cortes ni residuos; limpieza en un sentido |  |  |  |
| 4 | Conector de compresión con orientación correcta de la pala |  |  |  |
| 5 | Grasa del kit aplicada en interfaces; pasatapas limpio |  |  |  |
| 6 | Conector en posición final, alineado con el pasatapas |  |  |  |
| 7 | Torque del perno aplicado con torquímetro y marcado |  |  |  |
| 8 | Tapón aislante apretado a su torque y tapa conductora instalada |  |  |  |
| 9 | Punto de prueba / drenaje y pantalla conectados a tierra |  |  |  |
| 10 | Cable soportado sin esfuerzo lateral sobre el pasatapas |  |  |  |
| 11 | Pasatapas libres cubiertos con tapón apantallado aterrizado |  |  |  |
| 12 | Identificación de circuito y fase |  |  |  |

{.plain}
| Torquímetro (serie / calibración): [__________] | Accesorios apilados o descargadores: [__________] |
|---|---|

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

## NES-OPE-F-095 — Registro de ensayos VLF, tan delta y descargas parciales

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito (origen / destino): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-016 / IEEE 400 / IEEE 400.2 / IEEE 400.3 | Longitud del circuito: [____] m |
| Cable (referencia, U0/U, aislamiento): [__________] | N.º de empalmes en el circuito: [____] |
| Equipo VLF / TD / DP (serie, calibración): [__________] | Temperatura / HR: [____] °C / [____] % |

{.plain}
| U0 del cable: [____] kV | Forma de onda y frecuencia: [____] |
|---|---|
| Tensión de ensayo VLF aplicada: [____] kV rms | Duración del ensayo: [____] min |
| Criterio aplicado (norma / especificación): [__________] | Elementos desconectados para el ensayo: [__________] |

| Fase | Aislamiento antes (MΩ a [____] V) | TD medio a U0 (10⁻³) | Estabilidad a U0 (10⁻³) | TD 1,5U0 − 0,5U0 (10⁻³) | VLF soportado (Sí / No) | Aislamiento después (MΩ) |
|---|---|---|---|---|---|---|
| L1 |  |  |  |  |  |  |
| L2 |  |  |  |  |  |  |
| L3 |  |  |  |  |  |  |

| Fase | Descargas parciales: tensión de inicio (kV) | Nivel máximo (pC) | Ubicación de la fuente | Cumple |
|---|---|---|---|---|
| L1 |  |  |  |  |
| L2 |  |  |  |  |
| L3 |  |  |  |  |

{.plain}
| Circuito descargado y puesto a tierra al terminar: Sí / No | Informe del equipo adjunto: Sí / No |
|---|---|

{.plain}
| Observaciones y decisión (liberado / no liberado): |
|---|

{.plain}
| | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-096 — Registro de conexión de pantallas y torques

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Circuito: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-016 / NES-OPE-PR-020 | Esquema de pantallas del diseño: ambos extremos / un punto / transposición |

| Punto (extremo / empalme) | Fase | Conexión de pantalla (tierra / aislada / limitador) | Sección del conductor de tierra (mm²) | Torque especificado (N·m) | Torque aplicado y marcado | Continuidad OK |
|---|---|---|---|---|---|---|
|  | L1 |  |  |  |  |  |
|  | L2 |  |  |  |  |  |
|  | L3 |  |  |  |  |  |
|  | L1 |  |  |  |  |  |
|  | L2 |  |  |  |  |  |
|  | L3 |  |  |  |  |  |

{.plain}
| Torquímetro (serie / calibración ISO 6789): [__________] | Esquema ejecutado igual al del plano: Sí / No |
|---|---|

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

# 15. CONTROL DE CAMBIOS

| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
