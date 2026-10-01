---
code: NES-OPE-PR-024
header_title: PROCEDIMIENTO DE LIMPIEZA DE MÓDULOS FV
cover_title: Procedimiento de Limpieza de Módulos Fotovoltaicos
cover_subtitle: Criterios de decisión, métodos, calidad del agua y control de daños en plantas FV
---

# 1. OBJETIVO

Definir los criterios para decidir cuándo limpiar, los métodos de limpieza admitidos, los límites de agua, presión y temperatura, y las medidas de seguridad, calidad y ambiente para la limpieza de los módulos fotovoltaicos de la planta [PROYECTO], de modo que se recupere la producción perdida por suciedad sin dañar el vidrio, el recubrimiento antirreflejo, el marco ni la garantía del módulo.

Difundir y mantener instruido al personal sobre este procedimiento, en cumplimiento de la política integrada de calidad, ambiente y SST de Neptuno Energy Services, para prevenir, controlar y eliminar condiciones y actos subestándar, en especial el contacto eléctrico con módulos o cables dañados, el atrapamiento por el movimiento del tracker y el uso de agua no autorizada.

# 2. ALCANCE

Aplica al personal directo de Neptuno Energy Services y a sus subcontratistas en las siguientes actividades de operación y mantenimiento (O&M):

- Seguimiento de las pérdidas por suciedad (soiling) y decisión técnico-económica de cada ciclo de limpieza.
- Limpieza manual con agua de baja dureza o desmineralizada y cepillo suave o lanza de baja presión.
- Limpieza mecanizada con vehículo tractor y cepillo rotativo, con o sin agua.
- Limpieza con robots autónomos o semiautónomos, montados sobre la fila o trasladados entre filas.
- Limpieza localizada de manchas persistentes (excrementos de aves, barro, ceniza, resina).
- Inspección visual del módulo durante la limpieza y reporte de daños.
- Abastecimiento, control de calidad, consumo y disposición del agua de limpieza.

No incluye la sustitución de módulos dañados, que se rige por NES-OPE-PR-010; la intervención de conectores o cableado DC, que se rige por NES-OPE-PR-014; el mantenimiento del tracker, que se rige por NES-OPE-PR-025 y NES-OPE-PR-008; ni el control de vegetación, que se rige por NES-OPE-PR-026.

> NOTA: Los límites de presión, temperatura, calidad del agua, tipo de cepillo y fuerza sobre el vidrio dependen del fabricante del módulo y condicionan su garantía. Antes de la primera limpieza se obtienen por escrito del manual del módulo del proyecto y, si se va a usar máquina o robot, la aceptación escrita del fabricante del módulo para ese equipo.

# 3. DEFINICIONES

| Término | Definición |
|---|---|
| ATS / PT | Análisis de trabajo seguro y permiso de trabajo. |
| Soiling (suciedad) | Acumulación de polvo, tierra, ceniza, polen, excrementos de aves, sales u otros materiales sobre el vidrio del módulo, que reduce la irradiancia que llega a las celdas. |
| Ratio de suciedad (SR) | Relación entre la potencia (o la corriente de cortocircuito) de un dispositivo sucio y la del mismo dispositivo limpio, en las mismas condiciones. SR = 1 indica módulo limpio; la pérdida por suciedad es 1 − SR. |
| Estación de suciedad | Conjunto de referencia con un dispositivo que se mantiene limpio y otro que se deja ensuciar al ritmo de la planta, con medición continua, para calcular el SR conforme a la IEC 61724-1. |
| Módulo o celda de referencia | Módulo o celda calibrada del sistema de monitoreo que se usa para comparar estado limpio y sucio. |
| Recubrimiento antirreflejo (ARC) | Capa delgada sobre el vidrio que reduce la reflexión. Es sensible a la abrasión y a productos químicos. |
| Dureza del agua | Contenido de sales de calcio y magnesio, expresado en mg/L (ppm) de CaCO₃. El agua dura deja incrustaciones al secarse. |
| Sólidos disueltos totales (SDT) | Masa total de sales disueltas en el agua, en mg/L. Se estima con conductímetro. |
| Agua desmineralizada | Agua tratada (ósmosis inversa o intercambio iónico) con contenido de sales muy bajo, que no deja residuo al secarse. |
| Choque térmico | Esfuerzo en el vidrio por un cambio brusco de temperatura, por ejemplo agua fría sobre un módulo caliente. |
| Microfisura | Fisura de la celda no visible a simple vista, provocada por carga mecánica, vibración o pisadas, que reduce la potencia con el tiempo. |
| Máquina tractora de limpieza | Vehículo agrícola o portaherramientas con brazo y cepillo rotativo que avanza por la calle entre filas limpiando la superficie del módulo. |
| Robot de limpieza | Equipo autónomo o semiautónomo que recorre la fila sobre los módulos o sobre un riel y limpia con cepillo o microfibra, normalmente en seco. |
| Modo limpieza del tracker | Posición de inclinación fija ordenada desde el controlador o el SCADA para permitir la limpieza, según el manual del fabricante del tracker. |
| Posición de defensa (stow) | Posición de protección del tracker ante viento, granizo o falla, que prevalece sobre cualquier orden de limpieza. |
| Concesión de aguas | Autorización de la autoridad ambiental competente para captar agua de una fuente natural, con caudal, uso y condiciones definidos. |
| Hallazgo | Defecto observado en el módulo, el cableado o la estructura durante la limpieza, que se reporta para su evaluación. |

# 4. LOCALIZACIÓN

[PROYECTO] se ubica en el municipio de [municipio], departamento de [departamento]. Bloques, filas, inversores, estaciones de suciedad, puntos de abastecimiento de agua y zonas de lavado de equipos se identifican según el plano general de implantación [N° de plano] y el plan de O&M del proyecto [__________].

# 5. REFERENCIAS

> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.

## 5.1. Documentales

- Manual de instalación, operación y mantenimiento del fabricante del módulo del proyecto, capítulo de limpieza: calidad del agua, presión, temperatura, tipo de cepillo, productos admitidos y condiciones de garantía.
- Carta o certificado del fabricante del módulo que acepte el método mecanizado o el robot de limpieza propuesto, cuando aplique.
- Manual del fabricante del tracker: modo limpieza o mantenimiento, ángulos admitidos, límites de viento y procedimiento de bloqueo.
- Manual de operación del fabricante de la máquina tractora o del robot de limpieza.
- Plano general de implantación, plano de vías internas y plan de O&M del proyecto [N° de plano].
- Licencia ambiental o Plan de Manejo Ambiental (PMA) del proyecto, con la fuente de agua autorizada [N° de resolución].
- NES-OPE-PR-010 Montaje y sustitución de módulos FV; NES-OPE-PR-008 Montaje de tracker; NES-OPE-PR-014 Conexionado DC; NES-OPE-PR-025 Mantenimiento preventivo de planta FV; NES-OPE-PR-026 Control de vegetación.
- NES-SST-PR-001 Permisos de trabajo y bloqueo y etiquetado; NES-SST-PR-002 Trabajo en alturas; NES-SST-PLN-001 Plan de emergencias; NES-AMB-PR-001 Gestión integral de residuos.

## 5.2. Normativa aplicable

- RETIE — Resolución 40117 de 2024 (MinEnergía) y sus modificaciones vigentes, en lo relativo a seguridad de las instalaciones fotovoltaicas en operación.
- IEC 61724-1 — Monitoreo del desempeño de sistemas fotovoltaicos; incluye la medición de la relación de suciedad.
- IEC 61730 — Seguridad de módulos fotovoltaicos; IEC TS 62446-3 — Termografía en campo, cuando se use para verificar hallazgos.
- Decreto 1072 de 2015, Libro 2, Parte 2, Título 4, Capítulo 6 — SG-SST; Resolución 0312 de 2019 — Estándares mínimos.
- Resolución 5018 de 2019 (MinTrabajo) — Lineamientos de SST en el sector eléctrico.
- Resolución 2400 de 1979 — Estatuto de seguridad industrial; arts. 388 a 392 (manejo manual de cargas).
- Resolución 4272 de 2021 — Trabajo en alturas, cuando se limpien módulos sobre estructuras con exposición a 2 m o más.
- Decreto 1496 de 2018 — Sistema Globalmente Armonizado (SGA) para productos químicos, si se usa algún producto de limpieza.
- Decreto 1076 de 2015 y sus modificaciones vigentes (Sector Ambiente) — uso del recurso hídrico, concesiones de aguas, vertimientos y gestión de RESPEL.
- Resolución 2184 de 2019 — Código de colores para separación de residuos.
- Ley 1503 de 2011 y Resolución 40595 de 2022 (MinTransporte) — Plan estratégico de seguridad vial, para vehículos y máquinas en vías internas.
- Resolución 1401 de 2007 — Investigación de incidentes y accidentes de trabajo.
- NTC-ISO 9001, NTC-ISO 14001 y NTC-ISO 45001 — Sistemas de gestión.

# 6. RESPONSABILIDADES

## 6.1. Director / Jefe de O&M Neptuno Energy Services

- Aprobar y divulgar este procedimiento y asegurar los recursos para su cumplimiento.
- Aprobar el plan anual de limpieza y cada ciclo con base en el análisis de pérdidas por suciedad.
- Gestionar ante [PROPIETARIO] y [CLIENTE] la aceptación del método de limpieza y la carta del fabricante del módulo.
- Detener cualquier actividad que no cumpla este procedimiento o el manual del fabricante.

## 6.2. Ingeniero de desempeño / analista de monitoreo

- Calcular el SR y las pérdidas por suciedad con los datos de las estaciones de suciedad y del SCADA.
- Elaborar la evaluación técnico-económica de cada ciclo en el formato NES-OPE-F-170 y proponer la secuencia de bloques.
- Verificar después de la limpieza la recuperación de producción y registrar el resultado.

## 6.3. Supervisor de limpieza

- Planificar la jornada, asignar filas y equipos, y coordinar con el centro de control la posición del tracker.
- Elaborar con los trabajadores el ATS diario y la charla de inicio de turno.
- Verificar la calidad del agua al inicio de la jornada y en cada recarga del tanque (NES-OPE-F-172).
- Diligenciar el registro diario de avance y consumo de agua (NES-OPE-F-173) y consolidar los hallazgos (NES-OPE-F-174).

## 6.4. Operador del centro de control

- Llevar las filas del bloque intervenido al modo limpieza, confirmar la posición y bloquear órdenes automáticas no compatibles, salvo la posición de defensa.
- Informar de inmediato al supervisor cualquier alerta de viento, tormenta o falla del tracker.
- Registrar la hora de entrada y salida del modo limpieza por bloque.

## 6.5. Operador de máquina tractora o de robot

- Ejecutar la inspección preoperacional del equipo (NES-OPE-F-175) y operar según su manual y este procedimiento.
- Mantener la distancia, la velocidad y la presión del cepillo ajustadas; suspender ante cualquier contacto anormal con el módulo o la estructura.

## 6.6. Operarios de limpieza

- Limpiar con los métodos, el agua y los utensilios autorizados, sin pisar ni apoyarse sobre los módulos.
- Reportar todo hallazgo (vidrio roto, quemadura, conector suelto, cable colgando) y no tocar el elemento dañado.

## 6.7. Responsable SST (con licencia en SST vigente)

- Elaborar la matriz de peligros de la actividad, verificar EPP, permisos, competencias y condiciones del área.
- Aplicar el protocolo de tormenta eléctrica, estrés térmico y fauna, y liderar la atención de emergencias.

## 6.8. Responsable ambiental

- Verificar que el agua provenga de la fuente autorizada en la licencia o el PMA y que se lleve el registro de volúmenes.
- Controlar el manejo de envases, residuos y aguas de lavado de equipos, y el cumplimiento de las fichas del PMA.

## 6.9. Trabajadores

- Cumplir este procedimiento, participar en el ATS y usar correctamente el EPP.
- Aplicar el derecho a detener la tarea si las condiciones no son seguras, si el tracker se mueve sin aviso, si hay módulos o cables dañados, si no se cuenta con el EPP adecuado, si no se sabe realizar el trabajo o si no existe procedimiento o ATS.

# 7. RECURSOS

| Categoría | Recurso | Descripción |
|---|---|---|
| Humanos | Personal | Jefe de O&M, analista de desempeño, supervisor de limpieza, operador del centro de control, operadores de máquina o robot con licencia de conducción y certificación de operación cuando aplique, operarios de limpieza, responsable SST y responsable ambiental. |
| Materiales | Agua | Agua de la fuente autorizada en el PMA, tratada cuando sea necesario (ósmosis inversa, intercambio iónico o filtración) hasta cumplir los límites del numeral 8.2.4.4. |
| Materiales | Productos | Solo agua. Detergente únicamente si el fabricante del módulo lo admite por escrito: neutro, no abrasivo, biodegradable, con ficha de datos de seguridad (FDS) y rotulado SGA. |
| Herramientas | Limpieza manual | Cepillos de cerdas suaves no conductoras (nailon u otro material admitido por el fabricante), pértigas telescópicas no conductoras, esponjas o microfibra, rasquetas de goma para secado, lanzas de agua de baja presión con regulador y manómetro. |
| Equipos | Mecanizados | Máquina tractora con brazo y cepillo rotativo con sensor de distancia o control de altura; tanque de agua con filtro; robots de limpieza con su estación de carga y vehículo de traslado. Todos con certificado de aceptación del fabricante del módulo cuando se exija. |
| Equipos | Medición | Conductímetro o medidor de SDT, kit o medidor de dureza, medidor de pH, termómetro infrarrojo para la temperatura del vidrio y del agua, manómetro en boquilla, anemómetro portátil. Instrumentos con verificación vigente. |
| Equipos | Apoyo | Carrotanque o tanque remolcable con contador de volumen, radios, señalización, kit antiderrame, hidratación y sombra. |
| EPP | Básico | Casco con barbuquejo, gafas con filtro UV, botas de caucho o calzado dieléctrico con suela antideslizante, ropa manga larga, cubrenuca, protector solar, guantes de nitrilo o caucho, chaleco reflectivo, polainas en zonas con presencia de ofidios. |
| EPP | Específico | Protección auditiva para operadores de máquina; guantes dieléctricos y careta cuando se deba aislar un módulo o un cable dañado, solo por personal eléctrico calificado (NES-OPE-PR-014). |

# 8. DESARROLLO DE LA ACTIVIDAD

## 8.1. Verificaciones previas

- Evaluación de suciedad y decisión de limpieza aprobadas (NES-OPE-F-170).
- Manual del módulo vigente en campo y límites de agua, presión y temperatura transcritos en el permiso de la jornada.
- Fuente de agua autorizada y volumen disponible; análisis de calidad del agua conforme (NES-OPE-F-172).
- Coordinación con el centro de control: bloque, filas, hora de inicio y modo limpieza del tracker.
- Pronóstico meteorológico del día: sin tormenta eléctrica prevista, viento por debajo del límite del tracker y del equipo.
- Inspección preoperacional de máquina, robot, carrotanque y bomba (NES-OPE-F-175).
- Personal con inducción en riesgo eléctrico básico en plantas FV, movimiento del tracker y este procedimiento.
- ATS y permiso de trabajo diligenciados (NES-OPE-F-171).

> ALTO: Ningún módulo se limpia si presenta vidrio roto, marco desprendido, caja de conexión abierta o quemada, o cable o conector caído. Se marca, se aísla la zona y se reporta al responsable eléctrico. Con agua sobre un módulo dañado hay riesgo de choque eléctrico y de falla de aislamiento del string.

## 8.2. Metodología general

### 8.2.1. Identificación de las zonas de trabajo

La limpieza se organiza por bloque de inversor y por fila. Se señalizan: el bloque intervenido, el punto de abastecimiento de agua, la zona de estacionamiento del carrotanque y de la máquina, el área de lavado de equipos y el punto de acopio de residuos. Las filas en modo limpieza se informan por radio al centro de control y a todo el personal del bloque.

### 8.2.2. Ingreso de personal

- Verificar con el centro de control que las filas estén en modo limpieza y que no haya trabajos simultáneos incompatibles (por ejemplo, desbroce con proyección de piedras en la fila contigua).
- Diligenciar ATS y permiso de trabajo; inspeccionar el EPP.
- Ubicar botiquín, extintor, camilla y punto de encuentro del bloque.

### 8.2.3. Ingreso de vehículos y equipos

- Preoperacional de vehículos y máquinas; circulación solo por vías internas y calles autorizadas, a la velocidad del PESV del proyecto.
- Ningún vehículo pasa sobre cajas de paso, cables expuestos, canalizaciones ni zanjas.
- La máquina tractora mantiene la distancia lateral mínima a la fila que fije su manual; en terreno húmedo o con huellas profundas se suspende el paso para no desestabilizar la máquina ni los hincados.

### 8.2.4. Descripción de las actividades

#### 8.2.4.1. Seguimiento de la suciedad

La suciedad reduce la irradiancia efectiva y la producción. Su ritmo depende del sitio: polvo de vías destapadas y de cultivos, quemas agrícolas, ceniza, polen, excrementos de aves, salinidad costera y época del año. En Colombia el ritmo suele aumentar en las temporadas secas, cuando no hay lavado natural por lluvia, y disminuir en las temporadas lluviosas.

Se mide de forma continua con las estaciones de suciedad del proyecto y se complementa así:

- Ratio de suciedad (SR) diario de cada estación, calculado conforme a la IEC 61724-1, con datos de mediodía solar y cielo despejado para reducir la incertidumbre.
- Comparación de la corriente o la producción específica entre strings o inversores equivalentes, antes y después de lluvias.
- Inspección visual semanal de filas representativas por zona (cerca de vías, zonas de cultivo, perímetro con árboles con aves).
- Registro de eventos que aceleran la suciedad: quemas en la región, obras, temporada de cosecha, paso de maquinaria.

> NOTA: Las estaciones de suciedad se instalan en zonas representativas y, cuando la planta es extensa o heterogénea, en más de un punto. El dispositivo de referencia limpio se limpia con la frecuencia que exija su fabricante; una referencia sucia invalida el cálculo.

#### 8.2.4.2. Decisión de limpieza

No existe un umbral único de suciedad válido para todas las plantas. La decisión es técnico-económica y se documenta en NES-OPE-F-170:

1. Estimar la energía perdida por suciedad desde la última limpieza y su proyección: energía esperada × (1 − SR) para el periodo hasta la siguiente lluvia significativa prevista.
2. Valorar la energía perdida con el precio de venta del contrato de [PROPIETARIO] [__________].
3. Calcular el costo del ciclo de limpieza: mano de obra, agua y su transporte o tratamiento, equipos, combustible y riesgo de rotura.
4. Limpiar cuando el ingreso recuperable hasta la siguiente lluvia supere el costo del ciclo, o cuando el SR baje del umbral contractual o del umbral definido en el plan de O&M [__________].
5. Priorizar los bloques con menor SR y los de mayor producción específica.
6. Si el pronóstico indica lluvias significativas en pocos días, evaluar aplazar el ciclo.

Además de los ciclos generales, se programan limpiezas localizadas cuando haya manchas que generen sombra parcial sobre celdas (excrementos de aves, barro, hojas), porque pueden originar puntos calientes aunque el SR general sea alto. La termografía del NES-OPE-PR-025 ayuda a ubicarlas.

#### 8.2.4.3. Selección del método

| Método | Uso típico | Condiciones |
|---|---|---|
| Lavado manual con agua de baja dureza y cepillo suave | Plantas pequeñas, suciedad adherida, manchas localizadas, zonas no accesibles a máquina | Rendimiento bajo; mayor exposición del personal. Agua y cepillo dentro de los límites del fabricante. |
| Enjuague manual con lanza de baja presión, sin contacto | Polvo suelto, retiro previo de partículas abrasivas | Presión medida en boquilla dentro del límite del fabricante; boquilla en abanico, sin chorro concentrado. |
| Máquina tractora con cepillo rotativo, con agua | Plantas utility-scale con calles transitables | Requiere aceptación escrita del fabricante del módulo; control de altura y presión del cepillo; terreno firme. |
| Máquina tractora con cepillo rotativo, en seco | Polvo seco no adherido, zonas con restricción de agua | Igual que el anterior; algunos fabricantes de módulos no admiten limpieza en seco con cepillo rotativo. |
| Robot autónomo | Plantas con alta tasa de suciedad y limpieza frecuente | Requiere aceptación del fabricante del módulo y compatibilidad con el tracker; inspección del cepillo y de las ruedas. |
| Limpieza localizada | Excrementos de aves, resina, barro seco | Humedecer, dejar ablandar y retirar con esponja o cepillo suave; nunca raspar con objetos metálicos. |

> NOTA: Algunos fabricantes de módulos advierten que los cepillos rotativos pueden generar microfisuras o desgastar el recubrimiento antirreflejo. El uso de máquina o robot solo se aprueba con el certificado o la carta del fabricante del módulo del proyecto y con los parámetros que este fije (velocidad, presión de contacto, material de cerdas).

#### 8.2.4.4. Calidad y suministro del agua

El agua se toma únicamente de la fuente autorizada en la licencia ambiental o el PMA del proyecto: concesión de aguas otorgada por la autoridad ambiental competente, compra a un proveedor que acredite su propia autorización, o red de acueducto con disponibilidad del prestador. Prohibido captar de ríos, quebradas, jagüeyes, reservorios o pozos sin autorización.

Se verifica la calidad al inicio de la jornada y en cada recarga del tanque, y se registra en NES-OPE-F-172:

| Parámetro | Valor de referencia | Fuente |
|---|---|---|
| Dureza total | Menor a 75 mg/L como CaCO₃ para lavado sin secado; entre 75 y 200 mg/L solo con secado con rasqueta de goma; mayor a 200 mg/L no se usa | Valor típico de fabricante; verificar contra el manual del módulo del proyecto |
| pH | Entre 6,5 y 8,5 | Valor típico de fabricante; verificar contra el manual del módulo del proyecto |
| Cloruros | No mayor a 250 mg/L | Valor típico de fabricante; verificar contra el manual del módulo del proyecto |
| Sólidos disueltos totales | Según el manual del módulo; un fabricante admite agua dulce con SDT menor a 1.500 mg/L, otros exigen agua desmineralizada | Valor típico de fabricante; verificar contra el manual del módulo del proyecto |
| Sólidos en suspensión | Agua sin arena ni partículas visibles; filtrada antes de la bomba | Este procedimiento |
| Temperatura del agua | Diferencia con la temperatura del vidrio no mayor al límite del fabricante (ver 8.2.4.5) | Manual del módulo |

Si el agua no cumple, se trata (ósmosis inversa, intercambio iónico o filtración) o se cambia de fuente. El rechazo de la planta de tratamiento se gestiona como lo indique el PMA.

#### 8.2.4.5. Horario y condiciones de limpieza

- Limpiar en las primeras horas de la mañana, al final de la tarde o con cielo cubierto, cuando el vidrio está frío. Así se evita el choque térmico, se reduce la evaporación que deja manchas y se reduce la corriente disponible en los strings.
- Medir con termómetro infrarrojo la temperatura del vidrio y la del agua antes de iniciar cada fila en horas de calor. La diferencia no supera el límite del fabricante: los manuales consultados fijan entre 10 °C y 20 °C — valor típico de fabricante; verificar contra el manual del módulo del proyecto.
- No limpiar con temperatura ambiente cercana al punto de congelación; en Colombia aplica en plantas de altiplano a primera hora — el límite lo fija el manual del módulo.
- La limpieza nocturna solo se hace con robots diseñados para ello o con iluminación, permiso específico y análisis de riesgo aprobado.
- Suspender con viento por encima del límite del modo limpieza del tracker o de la máquina, con lluvia intensa, con tormenta eléctrica o con niebla densa que impida la visibilidad del operador.

#### 8.2.4.6. Posición del tracker

1. El supervisor solicita al centro de control el modo limpieza para las filas del bloque, indicando el ángulo que exige el método: el que defina el manual del fabricante de la máquina o del robot, o el que facilite el alcance seguro del operario sin apoyarse sobre los módulos.
2. El operador del centro de control ordena la posición, verifica en el SCADA que todas las filas la alcanzaron y lo confirma por radio. Las filas que no alcanzan la posición no se limpian hasta revisar el controlador.
3. Ningún operario ni máquina entra en la calle mientras el tracker se está moviendo.
4. La posición de defensa por viento o granizo prevalece siempre: si el tracker se mueve a defensa durante la limpieza, todo el personal y las máquinas salen de las calles y no regresan hasta nueva confirmación.
5. Si el trabajo exige permanecer bajo la mesa o junto a puntos de pellizco (motor, transmisión, amortiguadores), el accionamiento se bloquea y etiqueta según NES-SST-PR-001.
6. Al terminar, el centro de control devuelve las filas a seguimiento normal y registra la hora en NES-OPE-F-173.

> ALTO: El tracker puede moverse en cualquier momento por una orden automática de defensa. Nadie se ubica entre la mesa y el terreno ni entre la mesa y el poste en la zona de giro sin bloqueo del accionamiento.

#### 8.2.4.7. Limpieza manual

1. Recorrer la fila e inspeccionar visualmente módulos, conectores y cables antes de mojar.
2. Retirar con agua a baja presión o cepillo seco suave el polvo suelto y las partículas de arena, empezando por la parte alta del módulo, para no arrastrar partículas abrasivas con el cepillo.
3. Humedecer la superficie y cepillar con movimientos suaves, sin presionar el vidrio y sin golpear el marco con la pértiga.
4. Enjuagar de arriba hacia abajo con agua de la calidad autorizada.
5. Si la dureza del agua está entre 75 y 200 mg/L, secar con rasqueta de goma para evitar incrustaciones.
6. Dirigir el agua solo al vidrio: no apuntar a la caja de conexión, los conectores, las cajas combinadoras, los inversores ni los motores y controladores del tracker.
7. Trabajar desde el suelo con pértiga. Si la altura de la mesa obliga a usar escalera o plataforma, se aplica NES-SST-PR-002.

#### 8.2.4.8. Limpieza con máquina tractora

1. Verificar que la máquina y el cepillo cuentan con la aceptación del fabricante del módulo y que el cepillo no tiene cerdas endurecidas, contaminadas con arena ni desgastadas.
2. Ajustar el ángulo del brazo al ángulo del tracker en modo limpieza y la altura del cepillo con su sensor o guía, según el manual de la máquina.
3. Ajustar la velocidad de avance, la velocidad de giro del cepillo y el caudal de agua a los valores aprobados para el módulo del proyecto [__________].
4. Iniciar con una fila de prueba y revisar al final que no haya marcas, rayas, módulos desplazados ni conectores enganchados.
5. Operar sin que el cepillo toque el marco de forma continua, los soportes, los cables ni la estructura. Ante un golpe o un ruido anormal, detener, levantar el brazo y revisar.
6. Ningún peatón se ubica en la calle de trabajo de la máquina ni en su radio de giro.
7. Lavar el cepillo y el tanque al final de la jornada en el área de lavado autorizada.

#### 8.2.4.9. Limpieza con robot

- Operar el robot según su manual y con la aceptación del fabricante del módulo; verificar que el peso por rueda o por apoyo y el material de contacto estén aprobados.
- Verificar la alineación entre mesas, las rampas o puentes de transferencia y que el tracker esté en la posición que exige el robot.
- Inspeccionar diariamente cepillos o microfibras, ruedas, sensores de borde y estado de carga; retirar el robot de servicio ante cualquier falla de sensor de borde.
- Registrar en el SCADA o en NES-OPE-F-173 las filas limpiadas y las alarmas del robot.

#### 8.2.4.10. Prohibiciones

- Prohibido pisar, sentarse, arrodillarse o apoyarse sobre los módulos, y apoyar escaleras, herramientas o pértigas sobre ellos.
- Prohibido usar hidrolavadoras de alta presión, vapor o chorro concentrado.
- Prohibido usar productos ácidos o alcalinos, solventes, amoníaco, hipoclorito, abrasivos, polvos limpiadores, gasolina o ACPM. Los manuales consultados excluyen expresamente, entre otros, el ácido clorhídrico, el amoníaco, el hidróxido de sodio y el d-limoneno.
- Prohibido usar estropajos, lana de acero, cuchillas, espátulas metálicas o cepillos de cerdas duras.
- Prohibido limpiar módulos con vidrio roto o con cables o conectores dañados.
- Prohibido mojar inversores, cajas combinadoras, transformadores, motores o controladores del tracker.
- Prohibido usar agua de fuente no autorizada.
- Prohibido limpiar con el tracker en movimiento o sin confirmación del modo limpieza.

#### 8.2.4.11. Inspección visual y reporte de daños

Durante la limpieza se inspecciona cada módulo y se reportan en NES-OPE-F-174, con fila, mesa, posición y fotografía:

- Vidrio roto, astillado o con impacto; delaminación, burbujas, decoloración o caracol (snail trail).
- Marco doblado o desprendido; abrazaderas sueltas o faltantes.
- Caja de conexión abierta, deformada o con marcas de calentamiento.
- Cable colgando, en contacto con el suelo, con aislamiento dañado o roído por fauna; conector suelto o con evidencia de arco.
- Nidos, panales o animales en la estructura.
- Manchas persistentes que no salen con el método autorizado.

Los hallazgos eléctricos se tratan por NES-OPE-PR-014 y la sustitución de módulos por NES-OPE-PR-010. Ningún operario de limpieza manipula el elemento dañado.

#### 8.2.4.12. Verificación de resultados

- Inspección visual de muestra al final de cada fila: superficie uniforme, sin vetas, sin manchas de agua ni residuos.
- Comparación del SR o de la producción específica de los bloques limpiados contra los no limpiados, en los días siguientes.
- Registro de la recuperación obtenida en NES-OPE-F-170 para ajustar el umbral del siguiente ciclo.

#### 8.2.4.13. No conformidades

- Rayas, marcas o pérdida de recubrimiento antirreflejo: suspensión del método, informe al fabricante del módulo y a [PROPIETARIO].
- Rotura de vidrio durante la limpieza: se registra como incidente, se aísla el módulo, se investiga la causa y se repone según NES-OPE-PR-010.
- Uso de agua fuera de especificación o de fuente no autorizada: suspensión, reporte al responsable ambiental y análisis de causa.

## 8.3. Criterios de aceptación

| Parámetro | Criterio | Fuente |
|---|---|---|
| Decisión de limpieza | Ingreso recuperable mayor que el costo del ciclo, o SR por debajo del umbral del plan de O&M | IEC 61724-1 / Plan de O&M |
| Fuente de agua | Autorizada en licencia ambiental o PMA, con registro de volumen | Decreto 1076 de 2015 / PMA |
| Dureza del agua | Según 8.2.4.4 | Manual del módulo |
| pH y cloruros | Según 8.2.4.4 | Manual del módulo |
| Presión en boquilla | No mayor al límite del fabricante; los manuales consultados fijan límites del orden de 35 a 40 bar, y algunos menores — verificar contra el manual del módulo del proyecto | Manual del módulo |
| Diferencia de temperatura agua–vidrio | No mayor al límite del fabricante (10 °C a 20 °C en los manuales consultados) | Manual del módulo |
| Utensilios | Cerdas suaves no conductoras; sin elementos metálicos ni abrasivos | Manual del módulo |
| Máquina o robot | Aceptación escrita del fabricante del módulo y parámetros aprobados | Fabricante del módulo |
| Posición del tracker | Modo limpieza confirmado en SCADA para todas las filas del bloque | Manual del tracker |
| Resultado visual | Superficie uniforme, sin vetas, manchas ni residuos | Este procedimiento |
| Daños | Cero daños atribuibles a la limpieza; hallazgos reportados el mismo día | Este procedimiento |

## 8.4. Documentación para mantener y registrar

- Anexos NES-OPE-F-170 a NES-OPE-F-175 de este procedimiento.
- Manual de limpieza del fabricante del módulo y carta de aceptación del método mecanizado o del robot.
- Soporte de la fuente de agua autorizada y registro de volúmenes captados o comprados.
- Verificaciones de los instrumentos de medición de calidad del agua.

## 8.5. Control de calidad

El supervisor verifica cada fila al terminarla y QA/QC de O&M audita por muestreo al menos un bloque por ciclo (criterio interno). Si se encuentra una marca o un daño atribuible al método, se suspende el método en toda la planta hasta su análisis. Las no conformidades se clasifican así:

| Grado | Descripción | Tratamiento |
|---|---|---|
| 1 | Limpieza incompleta o con vetas en filas aisladas. | Repaso y registro. |
| 2 | Agua fuera de parámetros, registro incompleto, utensilio no autorizado. | Corrección inmediata, reentrenamiento y verificación. |
| 3 | Daño de módulo, pérdida de recubrimiento, uso de fuente de agua no autorizada o incidente con el tracker. | Suspensión del frente, análisis de causa, informe a [PROPIETARIO] y, si aplica, al fabricante del módulo. |

# 9. ASPECTOS SST (HSE)

El responsable SST asesora al supervisor en el ATS y la charla diaria, verifica la señalización del bloque y que se cumplan las medidas de este procedimiento. Todo el personal recibe inducción sobre el riesgo eléctrico en plantas FV (un módulo genera tensión siempre que recibe luz), el movimiento automático del tracker, el uso de agua cerca de equipos energizados, la fauna del sitio y el uso del EPP.

## 9.1. Reglas de oro

- **SIEMPRE** trataré los módulos, cables y conectores como energizados mientras reciban luz.
- **SIEMPRE** confirmaré con el centro de control el modo limpieza antes de entrar a la calle.
- **NUNCA** me ubicaré bajo la mesa ni en la zona de giro del tracker sin bloqueo del accionamiento.
- **NUNCA** pisaré ni me apoyaré sobre un módulo.
- **NUNCA** usaré hidrolavadora de alta presión, químicos ni utensilios abrasivos.
- **NUNCA** mojaré inversores, cajas combinadoras, motores ni controladores.
- **NUNCA** limpiaré ni tocaré un módulo con vidrio roto o un cable dañado: lo reporto.
- **SIEMPRE** usaré agua de la fuente autorizada y verificada.
- **SIEMPRE** suspenderé la actividad ante tormenta eléctrica y me dirigiré al refugio.
- **SIEMPRE** trabajaré con ATS y permiso de trabajo diligenciados.

## 9.2. Condiciones climáticas de [departamento]

- Tormenta eléctrica: ante aviso o primer trueno, suspender, alejarse de estructuras metálicas y agua, retirar máquinas de las calles y dirigirse al refugio. Se reanuda con autorización del responsable SST.
- Calor y radiación: en temporada seca, programar la limpieza en las primeras horas; hidratación, sombra, pausas y rotación según el programa de prevención del estrés térmico del SG-SST.
- Lluvias intensas: suspender el tránsito de máquinas en terreno saturado para evitar atascamiento, volcamiento y daño a la estructura.
- Viento: suspender por encima del límite del modo limpieza del tracker o de la máquina.
- Fauna: revisar la base de los postes y la sombra bajo las mesas antes de ubicarse; uso de polainas; no introducir las manos en cavidades.

# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)

Se cumple la normativa de la sección 5. Los riesgos siguientes corresponden a las actividades de este procedimiento y se ajustan en campo en el ATS diario.

| Secuencia de trabajo | Riesgos potenciales | Medidas de control |
|---|---|---|
| 1. Traslado al bloque y abastecimiento de agua | Colisión, volcamiento del carrotanque, atropellamiento. | Conductores autorizados; PESV; velocidades del proyecto; carga del tanque asegurada; señalero en maniobras. |
| 2. Coordinación con centro de control y modo limpieza | Movimiento inesperado del tracker, atrapamiento. | Confirmación por radio y SCADA; nadie en la calle durante el movimiento; bloqueo del accionamiento cuando aplique. |
| 3. Inspección previa de la fila | Contacto con módulo o cable dañado. | Inspección visual antes de mojar; no tocar elementos dañados; reporte. |
| 4. Limpieza manual con pértiga | Choque eléctrico, sobreesfuerzo, posturas forzadas, caídas al mismo nivel. | Pértiga no conductora; guantes; rotación; pausas activas; terreno inspeccionado. |
| 5. Uso de agua cerca de equipos | Choque eléctrico, cortocircuito, daño de equipos. | Agua solo sobre el vidrio; prohibido mojar equipos eléctricos; distancia a cajas e inversores. |
| 6. Operación de máquina tractora | Atropellamiento, golpe a la estructura, rotura de módulos, volcamiento. | Operador calificado; preoperacional; zona de exclusión; terreno firme; fila de prueba; velocidad controlada. |
| 7. Operación y traslado de robots | Sobreesfuerzo, caída del robot, atrapamiento. | Izaje mecánico o entre dos personas, respetando 25 kg por persona (Res. 2400 de 1979, art. 392); manual del robot. |
| 8. Trabajo sobre mesas altas | Caída a distinto nivel. | Plataforma o escalera certificada; Res. 4272 de 2021 cuando haya exposición a 2 m o más (NES-SST-PR-002). |
| 9. Exposición ambiental | Radiación UV, estrés térmico, deshidratación, ofidios, insectos. | Horario temprano; ropa manga larga, cubrenuca, protector solar, hidratación; polainas; revisión del área. |
| 10. Tormenta eléctrica, viento y lluvia | Descarga atmosférica, golpe por estructura en movimiento, volcamiento. | Suspensión; refugio; seguimiento meteorológico; defensa del tracker. |
| 11. Lavado de equipos y orden | Resbalones, contaminación del suelo. | Área de lavado autorizada; kit antiderrame; separación de residuos. |

# 11. ASPECTOS AMBIENTALES

El personal recibe la inducción ambiental de ingreso y la charla sobre uso del agua, flora y fauna del sitio. Se cumplen las fichas del PMA del proyecto y las siguientes medidas:

| Variable | Impacto | Medidas de control |
|---|---|---|
| Agua | Captación del recurso | Solo de la fuente autorizada (concesión de aguas, proveedor autorizado o acueducto); contador de volumen; registro diario en NES-OPE-F-173 y consolidado mensual para la autoridad ambiental cuando la concesión lo exija; no superar el caudal ni el volumen autorizado. |
| Agua | Uso eficiente | Limpiar solo cuando la decisión técnico-económica lo justifique; preferir métodos de bajo consumo o en seco aprobados por el fabricante; reparar fugas; aprovechar la temporada de lluvias. La literatura del sector reporta consumos de 3 a 5 L por módulo en lavado manual y mayores en zonas áridas (referencia; se verifica en la prueba piloto del proyecto). |
| Agua | Escorrentía del lavado | Con agua sola, la escorrentía se infiltra en el terreno de la planta. Si el fabricante y el PMA admiten detergente, se usa solo el autorizado y se verifica que el PMA permita su descarga al suelo; prohibido descargar a cuerpos de agua o drenajes. |
| Agua | Rechazo de tratamiento | El rechazo de ósmosis o el regenerante del intercambio iónico se gestiona como indique el PMA; no se vierte sin autorización. |
| Suelo | Erosión y huellas | Calles transitables; suspender máquinas con suelo saturado; reparar huellas y cárcavas. |
| Suelo | Derrames de combustible y aceite | Kit antiderrame en máquinas y carrotanques; tanqueo solo en zonas autorizadas con contención. |
| Suelo | Residuos | Microfibras, cepillos gastados, envases y filtros separados en la fuente (Res. 2184 de 2019); envases de productos químicos y filtros contaminados como RESPEL con gestor autorizado, según NES-AMB-PR-001. |
| Aire | Polvo y emisiones | Velocidad baja en vías; humectación de vías en temporada seca con agua autorizada; motores apagados en reposo. |
| Fauna | Perturbación y nidos | No retirar nidos ni panales sin el responsable ambiental; rescate y reubicación según PMA; prohibido cazar o alimentar fauna. |

# 12. ATENCIÓN DE EMERGENCIAS

Ante cualquier incidente se sigue la secuencia siguiente, en concordancia con NES-SST-PLN-001. Los datos de contacto se completan al inicio del proyecto y se publican en cada frente.

1. Detener la actividad, retirar a las personas del peligro y asegurar la zona; pedir al centro de control que detenga el tracker del bloque.
2. Notificar al responsable SST y al jefe de O&M de Neptuno Energy Services y al interlocutor de [CLIENTE].
3. Brindar primeros auxilios con personal capacitado (botiquín, camilla rígida, extintor en cada frente).
4. Incidente grave: activar la línea 123, traslado al centro asistencial definido y notificación a la ARL.
5. Reportar el evento e investigarlo según la Res. 1401 de 2007 y el SG-SST; divulgar la lección aprendida.

## 12.1. Choque eléctrico

- No tocar a la víctima mientras siga en contacto con el módulo o el cable; separarla con elemento aislante seco y solo si es seguro.
- Pedir al responsable eléctrico la apertura del circuito desde la caja combinadora o el inversor.
- Activar la emergencia y aplicar reanimación si el personal está capacitado. Toda persona que sufra un choque se remite a valoración médica aunque se sienta bien.

## 12.2. Atrapamiento por el tracker

- Ordenar al centro de control la parada del bloque y bloquear el accionamiento antes de liberar a la víctima.
- No mover la mesa a mano ni con la máquina; seguir las instrucciones del responsable de la planta.
- Inmovilizar y trasladar según la lesión.

## 12.3. Rotura de módulo con agua

- Detener el agua, alejar al personal y no tocar el módulo.
- El responsable eléctrico evalúa la necesidad de aislar el string (NES-OPE-PR-014) y el reemplazo (NES-OPE-PR-010).

## 12.4. Mordedura de serpiente (accidente ofídico)

- Alejarse del animal, mantener a la víctima en calma y quieta, retirar anillos y elementos que compriman.
- Lavar la herida con agua y jabón; anotar la hora y, si es posible sin riesgo, una descripción o foto del animal.
- No hacer torniquete, no cortar, no succionar, no aplicar remedios caseros ni dar alcohol.
- Trasladar de inmediato al centro asistencial con disponibilidad de suero antiofídico [__________].

| Contacto | Nombre | Teléfono |
|---|---|---|
| Responsable SST Neptuno Energy Services | [__________] | [__________] |
| Jefe de O&M Neptuno Energy Services | [__________] | [__________] |
| Centro de control / sala de operación | [__________] | [__________] |
| Interlocutor de [CLIENTE] | [__________] | [__________] |
| ARL | [__________] | [__________] |
| Ambulancia / Línea de emergencias | — | 123 |
| Centro asistencial más cercano (con suero antiofídico) | [__________] | [__________] |

# 13. REGISTROS

| Registro | Código | Responsable |
|---|---|---|
| Evaluación de suciedad y decisión de limpieza | NES-OPE-F-170 | Analista de desempeño |
| Permiso de jornada de limpieza y verificación previa | NES-OPE-F-171 | Supervisor de limpieza |
| Control de calidad del agua de limpieza | NES-OPE-F-172 | Supervisor de limpieza |
| Registro diario de avance, consumo de agua y modo limpieza | NES-OPE-F-173 | Supervisor de limpieza |
| Reporte de hallazgos y daños en módulos | NES-OPE-F-174 | Supervisor de limpieza |
| Inspección preoperacional de máquina de limpieza o robot | NES-OPE-F-175 | Operador de máquina o robot |
| ATS y permisos de trabajo | Según NES-SST-PR-001 | Supervisor / Responsable SST |
| Soportes de fuente y volumen de agua | Según PMA | Responsable ambiental |

# 14. ANEXOS

## NES-OPE-F-170 — Evaluación de suciedad y decisión de limpieza

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque(s) evaluado(s): [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-024 / IEC 61724-1 | Última limpieza: [____] |

| Ítem | Dato | Valor | Unidad | Observación |
|---|---|---|---|---|
| 1 | SR medio de la estación de suciedad (últimos 7 días) |  | — |  |
| 2 | Pérdida por suciedad (1 − SR) |  | % |  |
| 3 | Energía esperada hasta la próxima lluvia significativa |  | MWh |  |
| 4 | Energía recuperable estimada (3 × 2) |  | MWh |  |
| 5 | Precio de venta de referencia |  | COP/MWh |  |
| 6 | Ingreso recuperable (4 × 5) |  | COP |  |
| 7 | Costo estimado del ciclo (personal, agua, equipos, combustible) |  | COP |  |
| 8 | Pronóstico de lluvia en los próximos días |  | — |  |
| 9 | Decisión: limpiar / aplazar / limpieza localizada |  | — |  |
| 10 | Recuperación verificada después de limpiar |  | % |  |

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

## NES-OPE-F-171 — Permiso de jornada de limpieza y verificación previa

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque / filas: [__________] | Consecutivo: [____] |
| Método: manual / máquina tractora / robot | Fuente de agua: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Decisión de limpieza aprobada (NES-OPE-F-170) |  |  |  |
| 2 | Límites del fabricante del módulo transcritos: presión, ΔT, dureza, utensilios |  |  |  |
| 3 | Aceptación escrita del fabricante del módulo para máquina o robot (si aplica) |  |  |  |
| 4 | Calidad del agua conforme (NES-OPE-F-172) |  |  |  |
| 5 | Pronóstico sin tormenta; viento bajo el límite del tracker y del equipo |  |  |  |
| 6 | Modo limpieza confirmado por el centro de control (hora) |  |  |  |
| 7 | Preoperacional de máquina, robot, carrotanque y bomba conforme |  |  |  |
| 8 | ATS y charla de inicio de turno realizados |  |  |  |
| 9 | EPP completo e inspeccionado; polainas en zona de ofidios |  |  |  |
| 10 | Botiquín, extintor, camilla, radio e hidratación en el frente |  |  |  |
| 11 | Personal con inducción en este procedimiento |  |  |  |

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

## NES-OPE-F-172 — Control de calidad del agua de limpieza

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Fuente autorizada: [__________] | Acto administrativo o soporte: [__________] |
| Documento de referencia: NES-OPE-PR-024 / manual del módulo | Instrumentos (serie): [__________] |

| Hora / tanque | Dureza (mg/L CaCO₃) | pH | SDT o conductividad | Cloruros (mg/L) | T agua / T vidrio (°C) | Conforme |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Límites del manual del módulo del proyecto: dureza [____]; pH [____]; cloruros [____]; SDT [____]; ΔT máx. [____] °C |
|---|

{.plain}
| Observaciones y acciones (tratamiento, cambio de fuente): |
|---|

|  | Elaboró | Revisó | Aprobó | Vo.Bo. [CLIENTE] |
|---|---|---|---|---|
| Empresa | Neptuno Energy Services | Neptuno Energy Services | Neptuno Energy Services | [CLIENTE] |
| Nombre |  |  |  |  |
| Cargo |  |  |  |  |
| Firma |  |  |  |  |

\pagebreak

## NES-OPE-F-173 — Registro diario de avance, consumo de agua y modo limpieza

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Supervisor: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-024 | Método: [__________] |

| Bloque / filas | Entrada modo limpieza (hora) | Salida (hora) | Módulos limpiados | Agua usada (m³) | Equipo / cuadrilla | Obs. |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

{.plain}
| Total módulos del día: [____] | Total agua del día: [____] m³ |
|---|---|
| Lectura inicial del contador: [____] | Lectura final del contador: [____] |

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

## NES-OPE-F-174 — Reporte de hallazgos y daños en módulos

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Bloque: [__________] | Consecutivo: [____] |
| Documento de referencia: NES-OPE-PR-024 / NES-OPE-PR-010 / NES-OPE-PR-014 | Reportó: [__________] |

| N.º | Fila / mesa / posición | Tipo de hallazgo | Descripción | Foto N.º | Causa probable | Acción y responsable |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |

{.plain}
| Tipos: vidrio roto; delaminación; marco o abrazadera; caja de conexión; cable o conector; nido o fauna; mancha persistente; otro. |
|---|

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

## NES-OPE-F-175 — Inspección preoperacional de máquina de limpieza o robot

{.plain}
| Proyecto: [__________] | Fecha: [____] |
|---|---|
| Equipo (tipo / N.º interno): [__________] | Horómetro: [____] |
| Documento de referencia: NES-OPE-PR-024 / manual del equipo | Operador: [__________] |

| Ítem | Verificación | Cumple | No cumple | Obs. |
|---|---|---|---|---|
| 1 | Documentos del equipo y aceptación del fabricante del módulo disponibles |  |  |  |
| 2 | Cepillo o microfibra limpio, sin arena, sin cerdas endurecidas ni desgaste excesivo |  |  |  |
| 3 | Sensor de altura o de borde y paradas de emergencia funcionando |  |  |  |
| 4 | Brazo, articulaciones y mangueras hidráulicas sin fugas ni daños |  |  |  |
| 5 | Bomba, filtro y manómetro en buen estado; presión ajustada al límite aprobado |  |  |  |
| 6 | Llantas u orugas, frenos, luces, pito y alarma de reversa (máquina tractora) |  |  |  |
| 7 | Ruedas, batería y estado de carga (robot) |  |  |  |
| 8 | Niveles de combustible, aceite y refrigerante; sin goteos |  |  |  |
| 9 | Kit antiderrame y extintor a bordo |  |  |  |
| 10 | Operador con licencia y entrenamiento vigentes |  |  |  |

{.plain}
| Resultado: apto / no apto | Observaciones: |
|---|---|

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
