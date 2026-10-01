# Fuentes — NES-SST-PR-001 Procedimiento de Permisos de Trabajo y Bloqueo y Etiquetado

> Nota de método: en esta sesión el proxy de salida bloqueó la apertura directa de casi todos los dominios (.gov.co, osha.gov, nfpa.org, portales de ARL y normogramas). El contenido se tomó de los fragmentos y resúmenes que devolvió el buscador web para cada URL listada, más conocimiento técnico del redactor. Por eso todo artículo no confirmado se cita sin número, y los valores numéricos dudosos quedan marcados en el documento como "referencia técnica", "criterio interno" o "[____]".

| Fuente | Emisor | Año | URL | Qué se tomó |
|---|---|---|---|---|
| Resolución 5018 de 2019 (texto en gestor normativo) | MinTrabajo | 2019 | https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_mtra_5018_2019.htm | Objeto, campo de aplicación (generación convencional y no convencional), deroga la Res. 1348 de 2009. |
| Resolución 5018 de 2019 (Bogotá jurídica) | Alcaldía de Bogotá (compilación) | 2019 | https://www.bogotajuridica.gov.co/sisjur/normas/Norma1.jsp?dt=S&i=88299 | Confirmación de fecha (20-11-2019) y alcance. |
| Guías de implementación de la Res. 5018 de 2019 (varias) | Consultoras SST colombianas | 2021–2024 | https://safetya.co/normatividad/resolucion-5018-de-2019/ ; https://www.fltingenieriasas.com/resolucion-5018-de-2019/ ; https://smanova.co/resolucion-5018-de-2019/ | Enunciado de las cinco reglas de oro del anexo técnico: corte visible, condenación/bloqueo y etiquetado con candado y tarjeta "NO OPERAR", verificación de ausencia de tensión en cada fase, puesta a tierra y en cortocircuito, señalización y delimitación; estructura del anexo (generalidades, distancias de seguridad). |
| Guía de gestión del riesgo eléctrico | Consejo Colombiano de Seguridad | 2022 | https://wp.ccs.org.co/wp-content/uploads/2022/10/GUI%CC%81A-GESTIO%CC%81N-RIESGO-ELE%CC%81CTRICO_FINAL_compressed-1.pdf | Enfoque de jerarquía de controles y permiso de trabajo eléctrico (referencia general). |
| RETIE — Resolución 40117 de 2024 | MinEnergía | 2024 | https://gestornormativo.creg.gov.co/gestor/entorno/docs/resolucion_minminas_40117_2024.htm | Vigencia (02-04-2024), definición de trabajos con tensión y exigencia de procedimiento previo, obligatoriedad del SPT. No se pudo abrir la tabla de distancias: se dejan los valores como "[____] m" a completar con el RETIE. |
| Resolución 4272 de 2021 | MinTrabajo | 2021 | https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=120880 | Exigencia de permiso de alturas con lista de chequeo (usado en la tabla de tipos de permiso). |
| NFPA 70E (tablas de límites de aproximación) | NFPA | 2024 | (no accesible; conocimiento técnico) | Valores de referencia técnica de límites de aproximación seguro y restringido (1,0/0,3 m; 1,5/0,66 m; 1,8/0,78 m; 3,0 m conductores móviles) y concepto de EPP por energía incidente. Marcados como referencia, no requisito. |
| OSHA 29 CFR 1910.147 (control de energía peligrosa) | OSHA | vigente | https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147 (bloqueado; conocimiento técnico) | Buena práctica: secuencia de bloqueo en 8 pasos, bloqueo grupal con caja, retiro de candado en ausencia del trabajador (verificación de ausencia, intento de contacto, notificación antes de reanudar), cambio de turno sin perder continuidad del bloqueo. Sin citarla en el documento. |

## Ajustes para Colombia

- Las cinco reglas de oro se citan desde el RETIE y la Res. 5018 de 2019 (no desde normativa española ni OSHA). Se adoptó el término colombiano "condenación" como sinónimo de bloqueo y "consignación/desconsignación" para la entrega de instalaciones.
- Los requisitos LOTO de OSHA 1910.147 (retiro en ausencia, bloqueo grupal, cambio de turno) se volcaron como método interno sin citar OSHA.
- Límites de aproximación: tabla con espacio para el valor del RETIE vigente y la cifra NFPA 70E solo como referencia técnica; regla "si hay diferencia, se aplica el mayor".
- Roles: emisor/autorizante/ejecutor adaptados a la figura colombiana del responsable eléctrico con matrícula CONTE (Ley 1264 de 2008) o COPNIA (Ley 842 de 2003), responsable SST con licencia, coordinador de alturas (Res. 4272 de 2021), supervisor de entrada y vigía (Res. 0491 de 2020).
- Particularidad DC fotovoltaica integrada con NES-OPE-PR-014 / NES-OPE-F-060 (el PR-001 es el sistema general).
- Emergencias: línea 123, ARL, Res. 1401 de 2007, enlace con NES-SST-PLN-001.
- Ambiente: Res. 2184 de 2019, RESPEL con gestor autorizado, RAEE (Ley 1672 de 2013).

## Pendientes de verificar

- Tabla de distancias mínimas / límites de aproximación del RETIE (Res. 40117 de 2024) para 13,2 kV, 34,5 kV y BT/DC del proyecto; reemplazar los "[____] m".
- Número de artículo / numeral del RETIE y del anexo de la Res. 5018 de 2019 donde están las reglas de oro (se citan sin artículo).
- Límites de atmósfera de la Res. 0491 de 2020 para el permiso NES-SST-F-017 (se dejaron como "[__________]").
- Energía incidente y categorías de EPP por punto: dependen del estudio de arco del proyecto; los 8 y 25 cal/cm² son criterio interno a confirmar.
- Corriente de cortocircuito y tiempo de despeje para dimensionar las puestas a tierra temporales de MT.
- Tiempo de descarga de condensadores del inversor del proyecto (manual del fabricante).
- Profundidad umbral del permiso de excavación (1,2 m criterio interno de referencia).
