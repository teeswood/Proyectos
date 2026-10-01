# NES-OPE-PR-015 — Fuentes consultadas

> Limitación de esta sesión: WebFetch estuvo bloqueado por el proxy de salida para todos los dominios técnicos (southwire.com, okonite.com, site.ieee.org, hvinc.com, netaworldjournal.org, wikipedia, etc.) y el presupuesto de WebSearch se agotó a mitad de la investigación. Las fuentes de abajo se consultaron por los extractos que devolvió el buscador, **no abriendo el documento completo**. Antes de emitir la versión para obra, se recomienda abrir y confirmar las marcadas con (*).

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Power Cable Installation Guide (*) | Fabricante de cable (EE. UU.) | s. f. | https://www.southwire.com/medias/PowerCableInstallGuidepdf.pdf | Tensión máxima con ojo de tiro 0,008 lbf/cmil Cu y 0,006 lbf/cmil Al; ecuaciones de tramo recto y curva; presión lateral = T/R; factor de corrección por peso; relación de atasco |
| Medium Voltage Cable Constructability Overview (*) | IEEE PES/IAS (capítulo) | 2020 | https://site.ieee.org/sas-pesias/files/2020/12/IEEE-Medium-Voltage-Cable-Constructability-Overview-Presentation-Dec-1-2020-Rev-1.pdf | Radios de curvatura 12–15 × D, cálculo por tramos, rodillos y poleas dimensionados para el radio y la presión lateral |
| Recomendaciones para el tendido de cables de media tensión / Libro blanco de la instalación MT (*) | Fabricante de cable (Europa) vía portal técnico | 2018 | https://www.voltimum.es/noticias/prysmian/recomendaciones-tendido-cables ; https://www.prysmianclub.es/wp-content/uploads/2018/05/Guia_TECNICA_Cables_Accesorios_MEDIA_Tension-1.pdf | Esfuerzo máximo 50 N/mm² Cu y 30 N/mm² Al; radio 15 D final y 20 D durante el tendido para unipolar apantallado; manga de tiro |
| Coefficient of friction / Weight correction factor (*) | Fabricante de lubricantes de tendido | s. f. | https://www.polywater.com/en/knowledge-hub/coefficient-of-friction-in-cable-pulling-part-3/ ; https://www.polywater.com/en/knowledge-hub/weight-correction-factor-in-pulling-tension-calculations/ | μ con lubricante 0,15–0,5; w = 1 para un cable; incremento de 20–40% en tiros múltiples |
| A study of tension and jamming when pulling cable around bends (*) | Fabricante de lubricantes (J. M. Fee) | s. f. | https://www.polywater.com/wp-content/uploads/2022/06/A-study-of-tension-and-jamming-when-pulling-cable-around-bends-Fee.pdf | Relación de atasco 2,8–3,2 con tres cables |
| Sidewall pressure limitations (*) | Fabricante de cable (EE. UU.) | s. f. | https://www.okonite.com/media/wysiwyg/Engineering%20Technical%20Center/Tech_05.pdf | 500 lbf/ft (≈7,3 kN/m) para tres unipolares |
| Installation Pulling Tensions & Side Wall Pressures (*) | Fabricante de cable (Reino Unido) | s. f. | https://uk.prysmian.com/sites/uk.prysmian.com/files/media/documents/Installation%20Pulling%20Tensions%20&%20Side%20Wall%20Pressures%20(1).pdf | Concepto de límite de tensión y presión lateral por tipo de cable |
| IEEE 1185 (resúmenes) (*) | IEEE / calculadoras técnicas | 2019 | https://designcalculators.co.in/cablepulling | Temperatura mínima de instalación de PVC del orden de −10 °C; método de cálculo |
| IEC 60229 (muestra) y boletines de ensayos tras instalación (*) | IEC / fabricantes de cable | 2007 / 2020 | https://cdn.standards.iteh.ai/samples/14395/61aa56666bc846c08c4dfbf497a30047/IEC-60229-2007.pdf ; https://omancables.com/wp-content/uploads/2020/06/Tech-Bulletin-3-Electrical-Tests-after-Installation-1.pdf | Ensayo de cubierta 4 kV/mm, máx. 10 kV DC, 1 min, sin perforación |
| On site testing guidelines for MV cables (*) | Fabricante de cable (Reino Unido) | 2019 | https://uk.prysmian.com/sites/uk.prysmian.com/files/media/documents/On%20Site%20Testing%20Guidelines%20%282019%29%20%283%29.pdf | Secuencia de ensayos tras tendido (aislamiento, cubierta) |

Conocimiento normativo de base (no tomado de internet en esta sesión): ocupación de ductos 53/31/40% (NTC 2050, capítulo 9, tabla 1); IR BT ≥ 1 MΩ a 1.000 V para circuitos > 500 V (IEC 60364-6); fórmulas de factor de corrección por peso acunado y triangular (IEEE 1185).

## Ajustes para Colombia

- Fuentes estadounidenses en lbf/cmil, lbf/ft y °F convertidas a SI (N/mm², kN/m, °C), conservando el valor imperial entre paréntesis.
- Requisitos NEC sustituidos por RETIE (Res. 40117 de 2024) y NTC 2050 en lo que el RETIE adopta; profundidades mínimas remitidas a la NTC 2050 y al plano, sin cifras extranjeras.
- Roles: ingeniero COPNIA para el cálculo de tiro, electricistas CONTE, responsable SST con licencia, coordinador de alturas (Res. 4272 de 2021), espacios confinados (Res. 0491 de 2020).
- Manejo manual: 25 kg por persona (Res. 2400 de 1979, art. 392); izaje de carretes remitido a NES-SST-PR-003.
- Clima: tormenta eléctrica, lluvias intensas (estabilidad de zanja), calor y ofidios; la temperatura mínima de instalación casi nunca es limitante salvo alta montaña.
- Ambiente: Res. 2184 de 2019, RESPEL (Decreto 1076 de 2015), RCD (Res. 0472 de 2017 / 1257 de 2021), PMA.
- Emergencias: línea 123, ARL, Res. 1401 de 2007; mordedura de ofidio.
- Se eliminaron nombres de fabricantes; los valores se presentan como "valor típico de fabricante".

## Pendientes de verificar

- Tensión máxima de halado, presión lateral admisible, radios de curvatura y temperatura mínima: ficha del cable del proyecto (las fuentes europea y norteamericana difieren: 50 vs ≈70 N/mm² en Cu; el documento manda usar el menor salvo indicación del fabricante).
- Coeficiente de fricción: ficha del lubricante elegido y compatibilidad con la cubierta.
- Espesores de cama y recubrimiento, altura de la cinta, separación entre circuitos, profundidad: planos de sección tipo del proyecto y NTC 2050 adoptada por el RETIE (no se fijaron cifras).
- Color y leyenda de la cinta de señalización según RETIE vigente.
- Tensión de ensayo de aislamiento MT y valor mínimo: fabricante del cable / especificación del cliente.
- Velocidad de tiro y longitudes de reserva: fabricante y planos.
- Criterios internos marcados (alarma al 80% de la tensión de trabajo; desviación >20% frente a lo calculado): validar con la dirección técnica de Neptuno.
- Confirmar abriendo las fuentes (*) cuando el proxy lo permita.
