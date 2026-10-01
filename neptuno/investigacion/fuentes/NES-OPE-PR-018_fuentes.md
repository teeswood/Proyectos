# NES-OPE-PR-018 — Fuentes consultadas

Nota de método: en esta sesión el proxy de salida bloqueó la apertura directa (WebFetch) de todos los dominios intentados. El contenido se tomó de los extractos que devolvió el motor de búsqueda (WebSearch) para cada URL listada. Las URL no se abrieron completas; los valores marcados como "valor típico de fabricante" deben contrastarse contra el manual del inversor del proyecto.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Medium Voltage Power Station – System manual / installation | Fabricante de inversores centrales (SMA) | varios | https://files.sma.de/downloads/MVPS21MOW-TA-en-25.pdf | Apoyos estándar compensan desnivel de ±20 mm; equipo horizontal con peso repartido en todos los apoyos; altura libre mínima al terreno definida por el fabricante. |
| Medium Voltage Power Station 630SC-JP – transport and installation requirements | Fabricante de inversores centrales (vía manualslib) | s. f. | https://www.manualslib.com/manual/1574588/Sma-Medium-Voltage-Power-Station-630sc-Jp.html | Requisitos de transporte, izaje y asentamiento de estaciones de potencia. |
| Central inverter PVS980-58 Commissioning manual | Fabricante de inversores centrales (FIMER) | s. f. | https://www.fimer.com/sites/default/files/PVS980-58_5MVA_CM_EN_RevA.pdf | Condiciones ambientales de arranque dentro de límites; prerrequisitos de comisionado (solo extracto). |
| PV Inverter User Manual CSI-40/60K | Fabricante de inversores string (CSI Solar) | 2023 | https://www.csisolar.com/emea/wp-content/uploads/sites/6/2023/08/91000207-PV-Inverter-User-Manual_CSI-40-60K-T40001-E_EN_20230525.pdf | Separación ≥ 500 mm entre inversores y arriba/abajo; aumento con ambiente > 45 °C; inclinación hacia atrás no menor a 15° de la horizontal, nunca hacia adelante; lateral reducible a 200 mm. |
| Installation and Operation Manual CPS SCA36KTL | Fabricante de inversores string (CPS) | 2020 | https://www.chintpowersystems.com/wp-content/uploads/2020/05/CPS_36kW_usermanual.pdf | Comunicación Modbus RS-485; secuencia de instalación y verificaciones (extracto). |
| Installation and Commissioning Checklist | Fabricante de inversores (CSI) | 2019 | https://static.csisolar.com/wp-content/uploads/2019/12/Commissioning-Checklist.pdf | Estructura de lista de verificación: montaje, DC, AC, tensiones, tierra. |
| SG110CX user manual / Hopewind user manual / Solis manual | Fabricantes de inversores string | 2022-2025 | https://device.report/manual/4567826 | Terminal OT de tierra adicional a 2 N·m; la tierra de chasis no reemplaza al PE del cable AC; puertos RS-485. |
| Installation and Operation Manual On-Grid PV Inverter T06061-03 | Fabricante de inversores string (Afore) | 2025 | https://www.aforenergy.com/wp-content/uploads/2025/04/three-phase-pv-string-inverter-36-60kw-Belgium-users-manual.pdf | Humedad ≤ 90% sin condensación; almacenamiento −40 a +65 °C, 5–90% HR; aislamiento string-tierra > 10 kΩ (umbral interno del equipo). |
| Complete Solar Inverter Commissioning Checklist / Ultimate guide | Guías técnicas (Aforenergy) | 2025 | https://www.aforenergy.com/complete-solar-inverter-commissioning-checklist-for-safe-startup/ | Secuencia de arranque: Voc por string, polaridad, secuencia de fases, configuración de red y MPPT, cierre DC gradual y luego AC. |
| 2.55 MW PV Inverter Commissioning Procedure Rev3 | Fabricante de inversores centrales (vía Scribd) | s. f. | https://www.scribd.com/document/470505641/PVH-L2550E-Commissioning-Procedure-Rev3-EN-pdf | Ocho pasos de comisionado: seguridad, inspección visual, conexiones, aislamiento, tensiones y rotación de fases, ajustes de protección, interfaz, operación. |
| Solar Commissioning Checklist 2026 | Guía técnica (SurgePV) | 2026 | https://www.surgepv.com/blog/solar-commissioning-checklist | Aislamiento DC antes de conectar el inversor, ensayo L+/E, L−/E. |
| Sling angle / rigging guides | Guías de izaje | varios | https://www.sciencedirect.com/topics/engineering/sling-angle | Ángulo de eslinga ≥ 45°, preferible 60°. |
| Desiccant guidelines | Guía técnica | s. f. | https://www.multisorb.com/blog/desiccant-packet-expiration-and-storage-guidelines/ | Reemplazo de desecante cada 6 a 12 meses como referencia. |

## Ajustes para Colombia

- Perfiles de red de EE. UU./Europa (UL 1741, IEEE 1547, EN 50549) no se citan como requisito: los parámetros se toman del estudio de conexión aprobado por [OPERADOR DE RED], en el marco de CREG 075 de 2021 o CREG 174 de 2021 y, cuando aplique, de XM. Frecuencia nominal 60 Hz. Se prohíbe usar el perfil de otro país sin verificar valor por valor.
- Certificación de producto según RETIE (Res. 40117 de 2024) con ensayos IEC 62109-1/-2 e IEC 62116 como respaldo técnico.
- Primer arranque condicionado a dictamen RETIE, autorización escrita del responsable eléctrico y de [CLIENTE] y autorización de [OPERADOR DE RED]; secuencia según NES-OPE-PR-023.
- Izaje según NES-SST-PR-003 y Res. 2400 de 1979; distancias a líneas según RETIE; alturas Res. 4272 de 2021; espacios confinados Res. 0491 de 2020 para fosos.
- Derrateo por altitud (zonas altas andinas) y por temperatura (Caribe, Llanos); corrosividad del sitio (ISO 9223) en zonas costeras.
- Roles: COPNIA, CONTE, licencia SST, ARL, COPASST/vigía; técnico del fabricante como rol de garantía.
- Ambiente: Res. 2184 de 2019, RESPEL (aceite del transformador), RAEE, RCD.
- Unidades SI; pulgadas convertidas a mm.

## Pendientes de verificar

- Distancias de ventilación, inclinación, rangos de almacenamiento y operación, tiempo máximo de almacenamiento, tiempo de descarga de condensadores y torques DC/AC/tierra: dependen del manual del inversor del proyecto.
- Tolerancia de nivelación de ±20 mm y altura libre de la estación: valor de un fabricante; confirmar.
- Tabla de parámetros de red: debe venir del estudio de conexión aprobado.
- Horas de observación tras el primer arranque y muestreo de torque (10% string, 100% central): criterios internos por confirmar con [CLIENTE] y el fabricante.
- Confirmar en la edición vigente de IEC 62446-1 la tabla de aislamiento para sistemas de 1.500 V.
