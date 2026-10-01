# Fuentes — NES-OPE-PR-021 Procedimiento de Instalación de SCADA, Comunicaciones y Fibra Óptica

> Limitación de la investigación (01-10-2026): en esta sesión el proxy de salida bloqueó WebFetch para todos los dominios que se probaron (incluidos thefoa.org y wikipedia.org), y el presupuesto de WebSearch de la sesión se agotó al iniciar la búsqueda específica de fibra óptica y redes. Lo de IEC 61724-1 viene de resúmenes del buscador de las URL que siguen. Los valores de fibra óptica (tracción, radios, pérdidas por empalme y conector, atenuación) y de red se redactaron con normas técnicas de conocimiento general (ANSI/TIA-568.3, ANSI/TIA-598, IEC 61280-4-2, IEC 61300-3-35, IEC 60825-2, ITU-T G.652/G.657), sin URL abierta que los respalde. En el documento quedan como "valor de referencia de la norma de cableado / verificar contra la ficha y la especificación del proyecto". Se deben verificar antes de publicar.

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| IEC 61724-1:2021 Sensor Requirements for PV Plant Performance Monitoring | Fabricante de sensores (guía técnica) | s. f. | https://www.sevensensor.com/iec-61724-12021-sensor-requirements-for-pv-plant-performance-monitoring | Clase A: sensores de temperatura de módulo por tamaño de planta (6/12/18/24); resolución de temperatura de 0,1 °C. |
| How to Select Sensors and Quantities for PV Plant According to IEC 61724-1:2021 | Fabricante de sensores (guía técnica) | s. f. | https://www.sevensensor.com/how-to-select-sensors-and-quantities-for-pv-plant-according-to-iec-61724-12021 | Cantidad de estaciones y sensores por potencia de planta. |
| How many monitoring stations for utility-scale PV power plants? | Fabricante de piranómetros (nota de aplicación) | s. f. | https://www.hukx.com/us/applications/how-many-monitoring-systems-on-a-pv-solar-power-plant | Estaciones Clase A: 2 por debajo de 40 MW, 3 de 40 a 100 MW, 4 a partir de 100 MW. |
| The IEC 61724-1:2021 standard for PV monitoring systems: a quick explanation | Fabricante de piranómetros | s. f. | https://www.hukx.com/us/applications/the-iec-61724-12021-standard-for-pv-monitoring-systems-a-quick-explanation | Ed. 2021 con dos clases (A y B); requisitos de clase del piranómetro, mitigación de rocío, alineación, limpieza y calibración. |
| IEC 61724-1:2021 Class A Meteorological Monitoring Station (folleto) | Fabricante de registradores | s. f. | https://s.campbellsci.com/documents/us/product-brochures/b_solar-op-meteorological-monitoring-station.pdf | Composición típica de una estación Clase A (POA, GHI, temperatura de módulo, ambiente, viento). |
| Weather Solutions for IEC 61724-1 Class A Solar Monitoring Systems | Fabricante de registradores (blog) | s. f. | https://www.campbellsci.com/blog/weather-solutions-solar-monitoring-systems | Clase A: muestreo de 3 s o menos, registro de 1 min o menos. |
| Meeting IEC 61724-1 Solar Monitoring Requirements | Fabricante de equipos meteorológicos (blog) | s. f. | https://www.nrgsystems.com/blog/meeting-iec-61724-1-solar-monitoring-requirements-with-nrg-equipment | Contexto de requisitos de sensores. |
| IEC 61724-1 Ed. 2.0 2021 (vista previa) | IEC | 2021 | https://webstore.ansi.org/preview-pages/iec/preview_iec61724-1%7Bed2.0%7Db.pdf | Alcance y estructura de la norma. |
| IEC 61724-1: Sensor Maintenance Guide | Fabricante de sensores | s. f. | https://www.sevensensor.com/iec-61724-1-sensor-maintenance-guide | Limpieza y recalibración de sensores (se dejó como programa a acordar con el cliente). |
| PV module temperature sensor selection according to IEC 61724-1 | Fabricante de sensores | s. f. | https://www.sevensensor.com/pv-module-temperature-sensor-selection-according-to-iec-61724-1 | Montaje del sensor de temperatura en la cara posterior del módulo. |

## Ajustes para Colombia

- Se aplicó el RETIE (Res. 40117 de 2024) y la NTC 2050 a tableros, puesta a tierra y DPS. Personal con matrícula CONTE/COPNIA.
- La supervisión del operador se remite a la CREG 075 de 2021 y a los procedimientos del [OPERADOR DE RED] y de XM. Las pruebas en caliente del PPC pasan a NES-OPE-PR-023.
- SST: cinco reglas de oro (Res. 5018 de 2019); alturas en mástiles (Res. 4272 de 2021); cajas de paso como espacio confinado (Res. 0491 de 2020); manejo de bobinas (Res. 2400 de 1979, arts. 392 y 398 a 447); alcohol isopropílico con SGA (Decreto 1496 de 2018).
- Ciberseguridad: IEC 62443 solo como referencia técnica, sin normativa extranjera como requisito. Se escribe "IEC 62443" y no "ISA/IEC 62443" para no nombrar organizaciones.
- Ambiente: fragmentos de fibra como residuo cortopunzante con gestor autorizado; RESPEL; RAEE (Ley 1672 de 2013); Res. 2184 de 2019; RCD.
- Clima: tormenta eléctrica (el mástil meteorológico atrae descargas), lluvia (suspende empalmes y apertura de cajas) y calor (empalme bajo carpa).
- Emergencias: línea 123, ARL, Res. 1401 de 2007; atención de fragmentos de fibra en ojos y de exposición láser.
- No se nombra ningún fabricante. El tracker se cita como "el fabricante del tracker del proyecto".

## Pendientes de verificar

- Valores de fibra tomados de memoria técnica, sin URL abierta: empalme de 0,3 dB máx., par de conectores de 0,75 dB máx., atenuación de planta externa monomodo de 0,5 dB/km (ANSI/TIA-568.3); radios de curvatura típicos de 20 y 10 veces el diámetro; canal de cobre de 100 m. Se deben confirmar contra la edición vigente de ANSI/TIA-568.3 y contra la ficha del cable.
- Tensión máxima de tracción, radio mínimo y reservas: dependen del cable y del diseño ([____] en el documento).
- Tabla de IEC 61724-1: falta confirmar las estaciones para menos de 5 MW (se puso 2, porque la fuente da 2 para menos de 40 MW) y el criterio a partir de 200 MW. También faltan la incertidumbre exigida al sensor de temperatura de módulo, la exactitud de alineación del piranómetro y el intervalo de recalibración.
- Requisito de irradiancia posterior para módulos bifaciales en la clase de monitoreo del proyecto.
- Tiempo de recuperación del anillo, tolerancia de sincronización y latencia del PPC: dependen de la especificación del integrador y del PPC.
- Requisitos de supervisión e intercambio de información de XM y del [OPERADOR DE RED] aplicables al proyecto.
