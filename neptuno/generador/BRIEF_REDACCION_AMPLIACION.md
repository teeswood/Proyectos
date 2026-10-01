# Brief de redacción — ampliación de la biblioteca base Neptuno (fuentes de internet → formato Neptuno → Colombia)

Neptuno Energy Services (NIT 901.744.411-5) ejecuta obra fotovoltaica utility-scale en Colombia (trackers, hincas, módulos, DC, inversores, MT). Esta biblioteca es **base**: documentos sin cliente ni obra que luego se aterrizan en cada proyecto reemplazando marcadores.

El trabajo de cada documento tiene tres pasos: **(1) recopilar** procedimientos, guías y manuales públicos en internet sobre el tema; **(2) volcar** su contenido técnico útil al formato Neptuno; **(3) revisar y aterrizar** a Colombia (normativa, unidades, roles, clima, autoridades).

## 1. Reglas del documento base (obligatorias)

- Ejecutor: **Neptuno Energy Services** (se nombra así). Marcadores para todo lo demás:
  - `[CLIENTE]` quien contrata y aprueba; `[PROPIETARIO]` dueño de la planta; `[PROYECTO]`, `[municipio]`, `[departamento]`.
  - Operador de red: `[OPERADOR DE RED]`. Datos de obra: `[__________]` o `[completar …]`.
- **Cero nombres de empresas, marcas, proyectos o personas reales** en el documento (ni fabricantes de inversores, módulos, cables, equipos de medida, grúas, ni operadores de red, ni clientes). Se escribe "el fabricante del inversor", "el fabricante del módulo", "el fabricante del conector", etc. Las fuentes de internet se citan en el archivo de fuentes, **no** dentro del documento, salvo normas técnicas (IEC, IEEE, NTC, ASTM, NFPA, ISO) y normas legales.
- Excepción ya aprobada: el manual GameChange Solar Genius Tracker™ TF 3.0.1 (rev. 04-16-2026) como tracker de referencia, siempre marcado como tal. En los documentos eléctricos/O&M/SST normalmente no hace falta.
- **No inventes números de norma, artículos ni valores.** Si un valor viene de un manual de fabricante, escríbelo como "valor típico de fabricante; verificar contra el manual del equipo del proyecto". Si no estás seguro de un artículo, cita la norma sin artículo. Si un valor es criterio interno de Neptuno, márcalo "(criterio interno)".
- Dato de campo permanente de Neptuno: la distribución de material a lo largo de filas se hace con máquina; el montaje de tubos de torsión es manual (≥ 10 personas por tubo, ≤ 25 kg por persona, Res. 2400 de 1979, art. 392). Solo menciónalo si viene al caso.
- Español de Colombia; tono técnico, conciso, imperativo. Unidades SI (se admite la imperial entre paréntesis cuando la fuente es imperial).

## 2. Normativa colombiana de referencia (usar la que aplique; no inventar otras)

- RETIE — Resolución 40117 de 2024 (MinEnergía), con NTC 2050 en lo que el RETIE adopta. Para personal: competencia/matrícula profesional vigente (Ley 1264 de 2008 técnicos electricistas — CONTE; Ley 51 de 1986 y Ley 842 de 2003 ingenieros — COPNIA). Dictamen de inspección RETIE de la instalación antes de energizar.
- Resolución 5018 de 2019 (MinTrabajo) — lineamientos SST en procesos de generación, transmisión, distribución y comercialización de energía eléctrica.
- Decreto 1072 de 2015 (Libro 2, Parte 2, Título 4, Capítulo 6, SG-SST); Resolución 0312 de 2019 (estándares mínimos).
- Resolución 2400 de 1979 (estatuto de seguridad industrial; manejo de cargas arts. 388 a 392; manejo y transporte mecánico de materiales arts. 398 a 447).
- Resolución 4272 de 2021 (trabajo en alturas). Resolución 0491 de 2020 (espacios confinados).
- Resolución 1401 de 2007 (investigación de incidentes y accidentes). Resolución 2844 de 2007 (GATI ruido).
- Decreto 1496 de 2018 (SGA, sustancias químicas). Ley 1503 de 2011 y Resolución 40595 de 2022 MinTransporte (PESV).
- Ambiente: Decreto 1076 de 2015 (compila RESPEL, antes Decreto 4741 de 2005); Resolución 2184 de 2019 (código de colores blanco/negro/verde); Resolución 0472 de 2017 modificada por la 1257 de 2021 (RCD); Ley 1672 de 2013 (RAEE); licencia ambiental / PMA del proyecto `[N° de resolución]`.
- Sector: Ley 1715 de 2014; CREG 174 de 2021 (AGPE/GD); CREG 075 de 2021 (conexión al SIN); procedimientos del operador de red `[OPERADOR DE RED]` y del operador del sistema (XM) para la puesta en servicio cuando aplique.
- Normas técnicas internacionales usuales: IEC 62446-1, IEC TS 62446-3, IEC 62548, IEC 60364-7-712, IEC 61730, IEC 62852 (conectores DC), IEC 60502 (cables MT), IEEE 400/400.2 (ensayos de cables), IEEE 48 y IEEE 404 (terminales y empalmes), IEEE 81 (medición de puesta a tierra), IEC 62305 / NTC 4552 (rayos), IEC 61724-1 (monitoreo), IEC 60076 (transformadores), IEC 62271 (aparamenta MT), NFPA 70E, NTC-ISO 9001/14001/45001, ISO 6789 (torquímetros). Cítalas solo si aplican al tema.

## 3. Estructura

Procedimientos (`-PR-`), los 15 H1 exactos y en este orden (el validador lo exige):

`# 1. OBJETIVO` / `# 2. ALCANCE` / `# 3. DEFINICIONES` / `# 4. LOCALIZACIÓN` / `# 5. REFERENCIAS` / `# 6. RESPONSABILIDADES` / `# 7. RECURSOS` / `# 8. DESARROLLO DE LA ACTIVIDAD` / `# 9. ASPECTOS SST (HSE)` / `# 10. ANÁLISIS DE TRABAJO SEGURO (ATS)` / `# 11. ASPECTOS AMBIENTALES` / `# 12. ATENCIÓN DE EMERGENCIAS` / `# 13. REGISTROS` / `# 14. ANEXOS` / `# 15. CONTROL DE CAMBIOS`

Patrón interno (calcar del documento de referencia): 5 con `## 5.1. Documentales` y `## 5.2. Normativa aplicable`; 6 por roles (`## 6.1. Director / Residente de obra Neptuno Energy Services`, …, `## 6.n. Trabajadores` con el derecho a detener la tarea); 7 tabla `| Categoría | Recurso | Descripción |`; 8 con `## 8.1. Verificaciones previas`, `## 8.2. Metodología general` (`### 8.2.1. Identificación de las zonas de trabajo`, `### 8.2.2. Ingreso de personal`, `### 8.2.3. Ingreso de vehículos y equipos`, `### 8.2.4. Descripción de las actividades` con `#### 8.2.4.x.` por actividad), `## 8.3. Criterios de aceptación` (tabla), `## 8.4. Documentación para mantener y registrar`, `## 8.5. Control de calidad`; 9 con `## 9.1. Reglas de oro` (SIEMPRE / NUNCA en negrita); 10 tabla `| Secuencia de trabajo | Riesgos potenciales | Medidas de control |`; 11 tabla `| Variable | Impacto | Medidas de control |`; 12 secuencia numerada + tabla de contactos (línea de emergencias 123) + subnumerales de emergencias específicas del tema; 13 tabla `| Registro | Código | Responsable |`; 14 formatos como `## NES-XXX-F-NNN — Título` (bloque `{.plain}` de cabecera, tabla de ítems, `{.plain}` Observaciones, tabla de firmas con filas Empresa/Nombre/Cargo/Firma), separados por `\pagebreak`; 15 tabla:

```
| Versión | N.º de cambios | Fecha | Tipo (I/E/A/N) | Sumario de modificaciones |
|---|---|---|---|---|
| 01 | 0 | 25-09-2026 | N | Creación inicial del documento base. |
```

Planes (`-PLN-`) llevan la estructura propia del plan (objetivo, alcance, referencias, organización, matriz de inspección y ensayos con puntos H/W/R, criterios, registros, anexos, control de cambios).

Al inicio de 5 va el recuadro: `> NOTA: Documento base de Neptuno Energy Services. Al aterrizarlo en una obra se reemplazan [CLIENTE], [PROPIETARIO], [PROYECTO], [municipio] y [departamento], y se verifican los valores contra los manuales de los fabricantes de los equipos del proyecto y los planos aprobados.`

## 4. Formato (lo parsea `build_neptuno.py`)

Archivo `content/<CÓDIGO>.md`, UTF-8, encabezado YAML:

```
---
code: NES-OPE-PR-015
header_title: PROCEDIMIENTO DE TENDIDO DE CABLES DE POTENCIA
cover_title: Procedimiento de Tendido de Cables de Potencia BT y MT
cover_subtitle: Zanja, ducto y bandeja en plantas fotovoltaicas
---
```

`header_title` en mayúsculas, máximo 55 caracteres. Luego, solo:

- `# 1. TÍTULO` (H1), `## 1.1. Título` (H2), `### 1.1.1. Título` (H3), `#### 1.1.1.1. Título` (H4).
- Párrafos de una línea, separados por línea en blanco.
- Viñetas `- texto`; segundo nivel con dos espacios. Pasos numerados `1. texto`.
- Tablas pipe con línea `|---|` obligatoria justo después de la primera fila, máximo 7 columnas, `<br>` para saltos dentro de celda. Antes de una tabla sin fila de encabezado, la línea `{.plain}` (y aun así lleva `|---|` tras la primera fila).
- Recuadros: `> NOTA: …` y `> ALTO: …` (una sola línea).
- Negrita `**texto**`. Sin cursiva, enlaces, imágenes ni HTML (salvo `<br>`). No uses guion bajo ni asteriscos sueltos.
- Salto de página: línea con `\pagebreak`.
- No escribas portada, tabla de revisiones ni índice: los genera el script.

Codificación de formatos (anexos): cada documento usa su bloque propio, indicado en la tarea. No repitas códigos de otros documentos.

## 5. Revisión para Colombia (checklist que debe quedar aplicado)

1. Normativa: legal colombiana en 5.2; ninguna referencia a OSHA, NEC, normativa española/chilena/mexicana como requisito (puede quedar una norma técnica internacional como referencia técnica).
2. Roles colombianos: responsable SST con licencia en SST vigente; electricistas con matrícula CONTE; ingeniero con matrícula COPNIA; coordinador de alturas (Res. 4272 de 2021); ARL; COPASST/vigía.
3. Trabajo eléctrico: cinco reglas de oro del RETIE, distancias de seguridad del RETIE, EPP con categoría de arco, permiso de trabajo, bloqueo y etiquetado.
4. Energización: dictamen RETIE, coordinación con `[OPERADOR DE RED]` y, si aplica, XM; nada se energiza sin autorización escrita.
5. Clima: tormenta eléctrica (suspensión y refugio), estrés térmico, lluvias intensas, fauna (ofidios), según `[departamento]`.
6. Ambiente: PMA, RESPEL con gestor autorizado, Res. 2184 de 2019, RCD, RAEE si aplica.
7. Emergencias: línea 123, ARL, centro asistencial `[__________]`, Res. 1401 de 2007.
8. Unidades SI; fechas dd-mm-aaaa; decimales con coma.

## 6. Entregables por documento

1. `generador/content/<CÓDIGO>.md`.
2. `investigacion/fuentes/<CÓDIGO>_fuentes.md`: tabla `| Fuente | Emisor | Año | URL | Qué se tomó |` con las fuentes de internet realmente consultadas (URL abiertas), y una sección "Ajustes para Colombia" con lo que cambiaste respecto a la fuente (norma extranjera → norma colombiana, rol, unidad, etc.) y "Pendientes de verificar" (valores que dependen del equipo o del proyecto).
3. Validación limpia: `cd /home/user/Proyectos/neptuno/generador && python3 validar.py content/<CÓDIGO>.md` debe terminar en `OK` y generar el .docx en `out/`.
