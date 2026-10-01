# Neptuno Energy Services — ampliación de la biblioteca base (V01, 25-09-2026)

Procedimientos fotovoltaicos recopilados de fuentes públicas en internet, volcados al formato Neptuno (`build_neptuno.py`) y revisados para Colombia. Son documentos **base**: sin cliente ni obra, con marcadores `[CLIENTE]`, `[PROPIETARIO]`, `[PROYECTO]`, `[municipio]`, `[departamento]` y `[OPERADOR DE RED]`.

## Contenido

| Carpeta | Qué hay |
|---|---|
| `generador/content/` | 18 documentos nuevos en .md (fuente única) |
| `generador/build_neptuno.py` | Generador original. Único cambio: lee `nombres_archivo.json` para los nombres de archivo de los documentos nuevos |
| `generador/validar.py` | Comprueba las reglas del brief (YAML, 15 H1, tablas, sin marcas ni empresas, códigos de formato únicos) y compila |
| `generador/mapa_codigos.json` | Mapa de códigos fusionado (los 13 originales + 18 nuevos), para `listado_maestro.py` |
| `generador/BRIEF_REDACCION_AMPLIACION.md` | Brief de redacción y checklist de revisión para Colombia |
| `investigacion/catalogo_fuentes_internet.md` | Catálogo de unos 70 documentos públicos por tema, valores técnicos extraídos y normativa colombiana verificada |
| `investigacion/fuentes/` | Fuentes, ajustes Colombia y pendientes de cada documento |

## Documentos nuevos

| Código | Documento | Formatos |
|---|---|---|
| NES-OPE-PR-015 | Tendido de cables de potencia BT y MT | F-080 a F-085 |
| NES-OPE-PR-016 | Empalmes y terminales de media tensión | F-090 a F-096 |
| NES-OPE-PR-017 | Montaje de cajas combinadoras y tableros DC | F-100 a F-109 |
| NES-OPE-PR-018 | Montaje y conexionado de inversores | F-110 a F-119 |
| NES-OPE-PR-019 | Montaje de centros de transformación | F-120 a F-129 |
| NES-OPE-PR-020 | Puesta a tierra y protección contra rayos | F-130 a F-139 |
| NES-OPE-PR-021 | SCADA, comunicaciones y fibra óptica | F-140 a F-149 |
| NES-OPE-PR-022 | Pruebas y comisionado del generador FV (IEC 62446-1/-3) | F-150 a F-159 |
| NES-OPE-PR-023 | Energización y puesta en servicio | F-160 a F-169 |
| NES-OPE-PR-024 | Limpieza de módulos FV | F-170 a F-175 |
| NES-OPE-PR-025 | Mantenimiento preventivo de planta FV | F-180 a F-188 |
| NES-OPE-PR-026 | Control de vegetación | F-190 a F-195 |
| NES-CAL-PLN-003 | Plan de inspección y ensayos eléctrico | NES-CAL-F-010 a F-019 |
| NES-SST-PR-001 | Permisos de trabajo y bloqueo y etiquetado | NES-SST-F-010 a F-019 |
| NES-SST-PR-002 | Trabajo seguro en alturas | NES-SST-F-020 a F-029 |
| NES-SST-PR-003 | Izaje de cargas con grúa | NES-SST-F-030 a F-036 |
| NES-SST-PR-004 | Trabajos en caliente | NES-SST-F-040 a F-046 |
| NES-AMB-PR-001 | Gestión integral de residuos en obra | NES-AMB-F-001 a F-007 |

Los bloques de formatos siguen la convención existente (una decena por documento: PR-012 → F-040, PR-013 → F-050, PR-014 → F-060, INS-001 → F-070).

## Cómo generar los .docx con la marca real

1. Copiar `generador/content/*.md`, `nombres_archivo.json` y `mapa_codigos.json` a `_HERRAMIENTAS_NEPTUNO\generador_NEPTUNO_BASE\` (o reemplazar `build_neptuno.py` por esta versión).
2. `python build_neptuno.py` → `out\`. Luego `finalize_meta.py` y `listado_maestro.py` como siempre.

Los logos de `brand/` de este repositorio son provisionales y no se versionan.

## Antes de aprobar la V01: pendientes de verificar

En el entorno de trabajo el proxy bloqueó la apertura de casi todas las páginas, así que el contenido sale de extractos de buscador y de conocimiento técnico. La excepción son los acuerdos del CNO, que sí se leyeron completos. Todo valor no confirmado quedó marcado en el texto como `[____]`, "valor típico de fabricante; verificar contra el manual…" o "(criterio interno)".

1. **RETIE**: la Res. 40117 de 2024 fue modificada por la Res. 40284 de 2026 (libros 1 a 4). Se cita "y sus modificaciones vigentes". Hay que cotejar la tabla de resistencias de puesta a tierra y la de distancias de seguridad, que quedaron en `[____]`.
2. **RESPEL**: Decreto 1076 de 2015, título modificado por el Decreto 0766 de 2026. Cotejar los artículos citados en AMB-PR-001 y la Res. 1362 de 2007.
3. **IEC 62446-1**: tensión de ensayo y mínimo de aislamiento para sistemas de 1.500 V y arreglos grandes (en `[____]`). Definir la tolerancia de corriente entre strings: el documento usa 5 % y algunas fuentes dan 10 %.
4. **IEEE 400.2**: tabla de criterios de tan δ y filas VLF de 5 y 8 kV (PR-016).
5. **Res. 4272 de 2021 y Res. 2400 de 1979**: los artículos se citan sin número o se confirmaron solo por fragmentos. Verificar también las horas de formación en alturas.
6. **Fibra óptica (PR-021)**: los valores de pérdida (0,3 dB por empalme, 0,75 dB por par de conectores) son de TIA-568 por conocimiento general. Verificar contra la especificación.
7. **NFPA 51B**: el vigía posterior queda en 60 min según la edición 2024. Confirmar la edición que pide el cliente.
8. **Criterios internos** para que los confirme el área técnica y SST: muestreos, ±5 % de Voc, 0,5 Ω punto a punto, umbral de excavación de 1,2 m, vigencia del permiso de 12 h, viento de 40 km/h para alturas y 9,8 m/s para la grúa, frecuencias del plan de mantenimiento.
9. Pares, holguras, límites de impacto, presiones de gas y calidad del agua de limpieza dependen del equipo del proyecto. Mandan siempre los manuales del fabricante.
