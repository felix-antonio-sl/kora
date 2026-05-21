---
_manifest:
  urn: urn:sii:kb:questions-033
  provenance:
    created_by: FS
    created_at: '2026-04-24'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/sii/questions.json
version: 1.0.0
status: borrador
tags:
- sii
- faq
- dataset
- conversion-json
lang: es
extensions:
  kora:
    family: note
---

# SII FAQ Questions 033

Preguntas 1601-1650 de questions.json.

## 001.003.8347.003

**Pregunta:** ¿Cuál es el alcance de la Resolución N°66 de 2022?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_8347.htm
- Created: 16/01/2023
- Updated: 24/04/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Emisión de documentos tributarios electrónicos

### Respuesta

La Resolución fue emitida con el fin de normar la forma en que deben realizarse las transacciones de compra y venta de monedas extranjeras que se efectúan comúnmente, en las cuales se habían detectado diferencias de registro y forma de respaldo documentario en diferentes contribuyentes. Para evitar lo anterior, es que se redefine la Resolución N°98 de 2004 y en esencia esta resolución no cambia el fondo de las operaciones, ni la oportunidad de la emisión de los documentos, así como tampoco establece ni elimina obligaciones de emisión, sino que solo define que cuando se deba emitir documentación tributaria, deben emitirse los tipos de documentos determinados que se indican, así como la forma en como ellos deben completarse.

## 001.003.8352.003

**Pregunta:** ¿Cómo debe emitir un contribuyente de IVA el documento tributario electrónico para que la información quede registrada correctamente en el Registro de Compras y Ventas?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_8352.htm
- Created: 16/01/2023
- Updated: 25/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Emisión de documentos tributarios electrónicos

### Respuesta

Para que el documento emitido quede correctamente registrado en el Registro de Compra y Venta se deberá emitir, como monto facturable solamente la comisión cobrada por el intermediario cuando exista. La operación de compra o venta de moneda extranjera se informará como monto no facturable como informativo, para efectos de control, de modo que tales valores no se computen en el Registro de Compra y Venta.

## 001.003.8353.006

**Pregunta:** En cuanto al esquema del documento tributario electrónico, ¿cómo se debe informar los montos No Facturables en los campos establecidos para ello?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_8353.htm
- Created: 16/01/2023
- Updated: 28/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Emisión de documentos tributarios electrónicos

### Respuesta

Por cada línea de detalle hay un campo denominado , el cual, si no es informado, se asume con valor “cero”, que en ese caso se trataría de un valor afecto a IVA (parte del NETO). Si ése campo es informado con un valor igual a “1”, significa que es un valor exento de IVA (parte del Total Exento), ahora si dicho campo es informado con valor 2 ó 6, se entiende que es un “No Facturable”, el cual es positivo si es valor “2”, y es negativo en caso de ser valor “6”. Al ser solo No Facturable, solo se completa el valor Total No Facturable, y los totalizadores Exento y Neto, deben ir en cero en este caso. Finalmente, el objetivo de la resolución, es que las transacciones no se informen como exentas, sino que solo como flujos de dinero como conceptos “No Facturables”.

## 001.003.8354.002

**Pregunta:** ¿A qué se refiere los conceptos de “Valor a Pagar” y “Valor a Recibir”?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_8354.htm
- Created: 16/01/2023
- Updated: 24/04/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Emisión de documentos tributarios electrónicos

### Respuesta

Estos conceptos, indicados en el ejemplo del Anexo de la Resolución N°66 de 2022, se refieren a lo siguiente: Valor a Pagar: es la cantidad en pesos que “entrega” quién emite el documento cuando compra moneda extranjera. Valor a Recibir: es la cantidad de pesos que “recibe” quién emite el documento en caso de venta de moneda extranjera.

## 001.003.6219.006

**Pregunta:** ¿A qué se refiere -error en firma- que aparece al enviar un DTE?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6219.htm
- Created: 12/03/2012
- Updated: 28/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Errores y rechazos

### Respuesta

Se hace presente que a contar del 01 de agosto de 2017 el Registro de Compras y Ventas (RCV) reemplazó la obligación de llevar el Libro de Compras y Ventas, como también de enviar la Información Electrónica de Compras y Ventas para los contribuyentes que están autorizados como emisores electrónicos. Puede obtener más información relativa a este tema en el sitio Web del SII, sección Servicios online, menú Factura Electrónica y Boleta de Ventas y Servicios Electrónicas.

## 001.003.3664.006

**Pregunta:** ¿Qué es la Factura de Compra Electrónica?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_3664.htm
- Created: 18/11/2005
- Updated: 26/02/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Compra Electrónica

### Respuesta

Es la representación informática de un documento tributario generado y firmado electrónicamente, que reemplaza a la Factura de Compra soportada en papel y tiene la misma validez legal. Este documento es emitido por el comprador y reemplaza a la Factura de Venta, que tendría que haber emitido el vendedor, de no existir la medida de Cambio de Sujeto del impuesto.

## 001.003.3668.009

**Pregunta:** ¿Cuáles son las características de la Factura de Compra Electrónica?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_3668.htm
- Created: 18/11/2005
- Updated: 10/10/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Compra Electrónica

### Respuesta

Las características de la Factura de Compra Electrónica son las siguientes: La factura va firmada digitalmente por el emisor. Debe contener el número del RUT del vendedor o prestador de servicios y el número de la guía o guías de despacho emitidas, si así corresponde. La numeración corresponde a los folios electrónicos autorizados por el SII al emisor. Al igual que los demás Documentos Tributarios Electrónicos, la Factura de Compra Electrónica se debe enviar al SII a través de la plataforma electrónica que utilice el emisor, según las exigencias establecidas en la Resolución N°45 de 2003. La impresión del documento es opcional. Así, en el caso de un traslado de bienes corporales muebles, deberá ceñirse a lo establecido en la Resolución N°99 de 2019, que establece la opción de impresión o de portar el documento en formato electrónico en un dispositivo de tratarse de tal caso. El receptor puede consultar la validez del documento en www.sii.cl, sección Factura Electrónica, opción, Verificar Contenido de un Documento. Los contribuyentes autorizados para emitir Facturas de Compra Electrónica podrán verificar la inclusión del documento en su Registro de Compras Electrónico. La Factura de Compra Electrónica, al igual que todos los DTE, deberá cumplir las especificaciones establecidas por el SII en la Resolución N°45 de 2003 y sus modificaciones posteriores publicadas en el sitio web.

## 001.003.3669.007

**Pregunta:** ¿Cómo se debe operar al emitir una Factura de Compra Electrónica?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_3669.htm
- Created: 18/11/2005
- Updated: 25/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Compra Electrónica

### Respuesta

A contar del 03-09-2019, fecha de vigencia de la Resolución N°99 de 2019, cuando exista transporte de bienes corporales muebles con un documento tributario electrónico, deberá generarse en formato digital el DTE, ser enviado por medios electrónicos, y se deberá portar la representación gráfica o impresa de estos documentos tributarios, durante el traslado. Puede obtener más información relativa al tema en el sitio Web del SII, sección Factura Electrónica.

## 001.003.6531.004

**Pregunta:** ¿Cuáles son los requisitos para el llenado de una Factura de compra electrónica?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6531.htm
- Created: 24/06/2014
- Updated: 23/04/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Compra Electrónica

### Respuesta

Contener en forma obligatoria el número del RUT del vendedor o prestador de servicios (receptor del documento) y el número de la Guía o Guías de Despacho emitidas, si corresponde. En caso que el emisor electrónico sea un agente retenedor autorizado, deberá completar el documento de acuerdo con la Guía de Ayuda Emisión Factura de Compra Electrónica, que se encuentra en la página web del SII, sección ayuda, menú "Selecciona un trámite para resolver tus dudas", opción Documentos Tributarios, Facturación gratuito del SII, ayudas, Más información, Guías de ayuda, Guías de ayuda al sistema de Facturación Electrónica SII, emitir documentos tributarios electrónicos, Factura electrónica, ¿Cómo emitir una factura de compra electrónica?. De acuerdo con dicho instructivo, deberá indicar el código para el tipo de producto que corresponde a la transacción, el código de retención, la cantidad de unidades transadas, la(s) unidad(es) de medida, la tasa de retención, el monto de IVA retenido, el monto no retenido y comisiones, si corresponde. En caso que el emisor electrónico efectúe operaciones gravadas, con vendedores o prestadores de servicios que no tengan documentación tributaria y las retenciones se realicen amparadas en la Resolución Exenta N° 1.496, de 1976, se deberá especificar el código de retención establecido en el formato del Documento Tributario Electrónico para retención total e indicar el monto de IVA retenido.

## 001.003.3385.005

**Pregunta:** ¿Cuáles son los requisitos para emitir Facturas de Exportación Electrónicas, Nota de Crédito de Exportación Electrónica y Nota de Débito de Exportación Electrónica?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_3385.htm
- Created: 30/08/2005
- Updated: 15/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Exportación Electrónica

### Respuesta

El exportador que desee emitir una Factura de Exportación Electrónica, Nota de Crédito de Exportación Electrónica y Nota de Débito de Exportación Electrónica, deberá estar autorizado por el SII para ser emisor electrónico. En caso de no estarlo, el contribuyente puede inscribirse en el Sistema de Facturación Gratuito del SII o contratar un software disponible en el mercado. En este último caso, deberá postular al set básico de documentos electrónicos del sistema (Factura Electrónica, Nota de Crédito Electrónica y Nota de Débito Electrónica), en el sitio Web del SII (sii.cl), opción “Menú postulantes", a través de un representante legal del contribuyente interesado, autenticado con certificado digital, en donde, además, podrá seleccionar los documentos Facturas de Exportación Electrónicas, Nota de Crédito de Exportación Electrónica y Nota de Débito de Exportación Electrónica, si así lo requiere. Puede usted consultar más información en el sitio web del SII, sección Servicios online, menú Factura Electrónica.

## 001.003.3433.007

**Pregunta:** ¿Un contribuyente que no ha sido autorizado para ser emisor de Documentos Tributarios Electrónicos (DTE) puede emitir Facturas de Exportación Electrónicas?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_3433.htm
- Created: 21/09/2005
- Updated: 28/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Exportación Electrónica

### Respuesta

Se recuerda que los documentos de exportación electrónicos son obligatorios a contar del 17.01.2020, de acuerdo a lo establecido en Resolución N°113 de 2019, posteriormente modificada por la Resolución N°120 de 2019. Puede obtener más información en el sitio web del SII, sección Servicios online, Menú Factura electrónica.

## 001.003.6293.005

**Pregunta:** ¿Una empresa de servicios exenta de IVA que realizará, en nuestro país, un estudio para un cliente extranjero, debe emitir una Factura de Exportación o simplemente una factura exenta?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6293.htm
- Created: 30/08/2012
- Updated: 25/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Exportación Electrónica

### Respuesta

Corresponde emitir una Factura de Exportación, en caso que el servicio proporcionado al exterior sea calificado como exportación por el Servicio Nacional de Aduanas. Cabe señalar que de acuerdo on lo instruido en la Circular N°50 de 2017, la exención procederá respecto de aquellos servicios que sean prestados total o parcialmente en Chile para ser utilizados en el extranjero, En efecto, con anterioridad a la modificación incorporada en el N°16 Letra E) de este artículo, se eximían del IVA los ingresos percibidos por la prestación de servicios a personas sin domicilio ni residencia en Chile, siempre que éstos fueran prestados totalmente en el país y calificados por el Servicio Nacional de Aduanas como servicios de exportación. Ahora bien, conforme con dicha modificación se precisa que la referida exención también alcanzará a aquellos servicios que se presten en forma parcial en Chile, a personas sin domicilio ni residencia en el país, para ser utilizados en el extranjero.

## 001.003.3429.011

**Pregunta:** ¿Cuál es la normativa legal relacionada con Facturas de Exportación Electrónicas, Notas de Crédito de Exportación Electrónicas y Notas de Débito de Exportación Electrónicas?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_3429.htm
- Created: 21/09/2005
- Updated: 25/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Factura de Exportación Electrónica

### Respuesta

Principalmente, la que se indica a continuación: • Resolución N°93 de 2005 , que establece normas referentes a la autorización para emitir Facturas de Exportación Electrónicas, Notas de Crédito de Exportación Electrónicas y Notas de Débito de Exportación. • Resolución N°45 de 2003, que establece normas y procedimientos de operación respecto de los Documentos Tributarios Electrónicos. • Resolución N°18 de 2003, que establece que los contribuyentes que sean autorizados para emitir Documentos Tributarios Electrónicos, deberán otorgarlos impresos en soporte papel a los receptores no electrónicos y a los receptores electrónicos en los casos que indica. • Resolución N°11 de 2003, que establece el procedimiento para que contribuyentes autorizados para emitir Documentos Tributarios Electrónicos que se indican puedan también enviarlos por estos medios a “Receptores Manuales”. • Resolución N°84 de 2005, modificatoria de la Resolución N°18 de 2003, permitiendo la emisión de representaciones impresas de Documentos Tributarios Electrónicos en un tamaño mínimo de un tercio de oficio. • Resolución N°76 de 2005, complementaria de la Resolución N°18 de 2003, que autoriza la emisión de representaciones impresas de Documentos Tributarios Electrónicos, por medio de tecnologías alternativas de impresión. • Resolución N°105 de 2014, que autoriza emisión en papel de documentos tributarios que deban ser emitidos en formato electrónico a los contribuyentes que indica. • Resolución N°22 de 2016, modifica Resolución N°18 del 2003, en la forma de la emisión de representaciones impresas de documentos tributarios electrónicos en un ancho de 5,7 centímetros. • Resolución N°99 de 2019, modifica Resolución N°18 del 2003 y Resolución N°45 del 2003, eliminando la obligación de entregar un ejemplar impreso del DTE y deja sin efecto Resolución N°11 del 2003. • Resolución N°113 de 2019, que revoca autorización de emisión en papel de documentos tributarios, que deben ser emitidos en formato electrónico, a los contribuyentes que indica • Resolución N°120 de 2019, que fija nueva vigencia de Resolución N°113 de 2019, que revoca autorización de emisión en papel de documentos tributarios, que deben ser emitidos en formato electrónico, a los contribuyentes que indica. Puede obtener más información en la Oficina Virtual del Servicio de Impuestos Internos en Internet (www.sii.cl), Menú Factura electrónica, sección Información sobre Factura Electrónica , opción Descripción Formato de Documentos Electrónicos.

### Links
- {'url': 'http://www.sii.cl/documentos/resoluciones/2005/reso93.htm', 'text': ''}

## 001.003.3348.006

**Pregunta:** ¿Cómo puedo modificar una Guía de Despacho Electrónica cuando sólo se recibe una parte de la mercadería que menciona dicha guía?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_3348.htm
- Created: 12/08/2005
- Updated: 25/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Guía de Despacho Electrónica

### Respuesta

La Guía de Despacho Electrónica no puede ser modificada (está firmada digitalmente). Al momento de registrarse en el Libro de Guías Electrónico, es necesario dejar constancia de esta situación a nivel de detalle, en el campo 2. Frente a esta eventualidad, el emisor debe facturar la Guía de Despacho por el total y, posteriormente, emitir una Nota de Crédito por la diferencia no recibida por el comprador. Tenga presente que la Ley N°21.131 de Pago a Treinta Días estableció cambios en la Ley del IVA, incorporando la Guía Electrónica a los documentos que deben ser emitidos electrónicamente, sumándose a las: Facturas Facturas de compra Liquidaciones facturas Notas de débito y crédito que emitan los contribuyentes.

## 001.003.4090.009

**Pregunta:** ¿Puedo emitir una Guía de Despacho Electrónica para un traslado que no constituye venta?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_4090.htm
- Created: 21/04/2006
- Updated: 29/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Guía de Despacho Electrónica

### Respuesta

A contar del 03/09/2019, cuando exista transporte de bienes corporales muebles con un documento tributario electrónico, deberá generarse en formato digital el DTE, ser enviado por medios electrónicos, y se deberá portar la representación gráfica o impresa de estos documentos tributarios, durante el traslado.

## 001.003.7473.004

**Pregunta:** ¿Qué contribuyentes se eximen de la obligación de emitir guías de despacho electrónicas?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_7473.htm
- Created: 20/01/2020
- Updated: 25/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Guía de Despacho Electrónica

### Respuesta

Se eximen de la obligación de emitir guías de despacho electrónicas, pudiendo emitirlas en formato papel, cumpliendo con todas las obligaciones y formalidades instruidas por este Servicio, los contribuyentes que pertenezcan a los siguientes grupos o realicen las siguientes actividades: Sector pesca artesanal. Sector silvoagropecuario. Sector pequeña minería y pirquineros. Sin embargo, los contribuyentes de los rubros señalados podrán emitir Guías de Despacho Electrónicas, si así lo decidieren. Toda modificación y/o actualización de los grupos de contribuyentes exceptuados de emitir electrónicamente dichos documentos tributarios, deberá efectuarse mediante la dictación de la respectiva Resolución.

## 001.003.7454.005

**Pregunta:** ¿Las guías de despacho especiales, por ejemplo, la “Guía de Despacho Especial para el Movimiento o Traslado de Animales”; o la -Guía de Despacho de Combustibles de las FF.AA. y de Orden”; pueden seguir emitiéndose en forma manual, a pesar de la obligación de hacerlo electrónicamente?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_7454.htm
- Created: 08/01/2020
- Updated: 21/04/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Guía de Despacho Electrónica

### Respuesta

No, esas guías de despacho deberán ajustarse al formato electrónico; así, deben cumplir con la obligatoriedad incorporando sus características especiales al formato XML para las guías de despacho. Esto es posible para los usuarios de Sistemas Propios o de Mercado; en el caso de usuarios del Sistema Gratuito del SII este ajuste aún no es posible. Cabe señalar que solo podrá emitir en papel si cuenta con la prórroga o exención que señala la Ley sobre esta materia.

## 001.003.6222.009

**Pregunta:** ¿Cómo se registra la recuperación del impuesto al combustible cuando en la factura aparece Impuesto fijo y variable (este último en negativo)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6222.htm
- Created: 12/03/2012
- Updated: 25/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Libros de Compra y Venta Electrónicos

### Respuesta

Es importante recordar que de acuerdo a las Resoluciones N°61 y N°68 ambas de 2017, a contar del período de agosto de 2017, la IECV ha sido reemplazada por el Registro de Compras y Ventas (RCV).

## 001.003.6590.006

**Pregunta:** ¿Cómo puedo recuperar los correos de validación de envío de libros electrónicos, ya que estos fueron enviados y la casilla informada en el SII se encuentra expirada?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6590.htm
- Created: 09/09/2014
- Updated: 16/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Libros de Compra y Venta Electrónicos

### Respuesta

Es importante recordar que a contar del período de agosto de 2017, la Información Electrónica de Compras y Ventas (IECV) ha sido reemplazada por el Registro de Compras y Ventas (RCV).

## 001.003.6914.004

**Pregunta:** ¿Desde cuándo se contabilizan los 8 días que tiene el comprador o beneficiario del servicio para reclamar contra una factura electrónica?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6914.htm
- Created: 12/01/2017
- Updated: 19/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 19.983 modificada por Ley N°20.956, plazo para reclamar una Factura

### Respuesta

El plazo de los 8 días corridos se considera desde que el documento tributario electrónico ha sido recibido por el Servicio de Impuestos Internos. Por ejemplo, si el documento es recibido en el SII el día 01 de Enero a las 20:00 hrs., el plazo de los 8 días finaliza el día 09 de Enero a las 23:59 hrs.

## 001.003.6915.004

**Pregunta:** ¿Qué pasa si dentro del plazo de 8 días que tiene el comprador para reclamar, la Factura Electrónica posee un reclamo contra el contenido de la factura, o un reclamo por la falta total o parcial de las mercaderías entregadas o servicios prestados?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6915.htm
- Created: 12/01/2017
- Updated: 19/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 19.983 modificada por Ley N°20.956, plazo para reclamar una Factura

### Respuesta

En estos casos, se entiende que la factura está reclamada y por lo tanto, el receptor no podrá hacer uso del crédito fiscal contenido en la factura electrónica. Además, el Registro Público Electrónico de Transferencia de Créditos rechazará las anotaciones de cesión electrónica que se efectúen con posterioridad al reclamo.

## 001.003.6916.003

**Pregunta:** ¿Qué pasa si dentro del plazo de 8 días que tiene el comprador para reclamar, la Factura Electrónica es aceptada, posteriormente se puede reclamar?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6916.htm
- Created: 12/01/2017
- Updated: 29/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 19.983 modificada por Ley N°20.956, plazo para reclamar una Factura

### Respuesta

Cuando una Factura Electrónica ha sido aceptada dentro del período que el comprador tiene para reclamar, posteriormente dicha factura no puede ser reclamada, porque en tal caso dicha reclamación no tiene efectos, por lo que posteriormente podrá ser cedida cuando tenga el recibo de mercaderías entregadas o servicio prestado, o se presuma que la mercadería fue entregada o que el servicio fue prestado. Puede obtener más información en el sitio web del SII, menú Normativa y legislación, Circulares, opciones.

## 001.003.6917.003

**Pregunta:** ¿Qué pasa si dentro del plazo de 8 días que tiene el comprador para reclamar, la Factura Electrónica es aceptada, y dentro del mismo período de los 8 días se emite una Nota de Crédito Electrónica de Anulación?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6917.htm
- Created: 12/01/2017
- Updated: 19/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 19.983 modificada por Ley N°20.956, plazo para reclamar una Factura

### Respuesta

En caso que se emita una Nota de Crédito Electrónica de Anulación, que referencia una Factura Electrónica dentro del plazo o fuera del plazo de reclamación que posee el comprador, dicha Factura Electrónica no estará apta para ceder posterior a la emisión de la Nota de Crédito, por lo que será rechazada por el Registro Público Electrónico de Transferencia de Créditos.

## 001.003.6918.004

**Pregunta:** ¿Se puede ceder una factura electrónica que no ha sido aceptada ni reclamada dentro del plazo de 8 días?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6918.htm
- Created: 12/01/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 19.983 modificada por Ley N°20.956, plazo para reclamar una Factura

### Respuesta

Sí, en caso que una factura electrónica no haya sido reclamada dentro del plazo que estipula la ley N°19.983, se presumirá que las mercaderías fueron entregadas o que los servicios fueron prestados, por lo que la factura electrónica quedará apta para cederse electrónicamente con posterioridad a dicho plazo.

## 001.003.6501.001

**Pregunta:** ¿Qué implica la Ley de Factura Electrónica para los contribuyentes?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6501.htm
- Created: 20/05/2014
- Updated: 28/02/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

En general, la Ley hace universal y obligatorio el uso de la factura electrónica para todos los contribuyentes con actividad económica de primera categoría, en reemplazo de los documentos físicos o de papel, según los plazos que señala la Ley.

## 001.003.6502.013

**Pregunta:** ¿Qué documentos tributarios serán obligatorios en formato electrónico?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6502.htm
- Created: 22/05/2014
- Updated: 30/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

Los documentos tributarios que obliga la ley a emitir en formato electrónico son los siguientes: Facturas, Facturas No Afectas o Exentas, Facturas de Compra, Liquidaciones Factura, Notas de Débito, Notas de Crédito, Guías de Despacho, Facturas de Exportación, Notas de Crédito de Exportación y Notas de Débito de Exportación. Los documentos de exportación electrónicos son obligatorios a contar del 17.01.2020, que revoca autorización a emitir en papel a los contribuyentes obligados a emitir documentos tributarios electrónicos, que correspondan a las operaciones determinadas. La guía de despacho electrónica es obligatoria a contar del 17.01.2020, acorde a lo establecido en el artículo 3° de la Ley N° 21.131 que establece el pago a treinta días.

## 001.003.6503.004

**Pregunta:** ¿Cómo se clasifican las empresas según sus ingresos por ventas, de acuerdo a la ley?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6503.htm
- Created: 22/05/2014
- Updated: 28/02/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

Según la Ley N° 20.416 de 2010, las empresas se clasifican, según sus ingresos anuales por ventas y servicios y otras actividades del giro del año calendario anterior, en: Clasificación de Empresas según Ley N° 20.416 (en UF) Clasificación General Tipo de Empresa Desde Hasta Microempresas 0 2.400 Empresa de Menor Tamaño (EMT) Pequeña Empresa 2.400 25.000 Mediana Empresa 25.000 100.000 Gran Empresa 100.000 y más Gran Empresa Valor UF al 31 de diciembre de 2020: $ 29.070,33

## 001.003.6504.005

**Pregunta:** ¿Según la Ley, en qué formato el Contribuyente deberá emitir las guías de despacho?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6504.htm
- Created: 28/05/2014
- Updated: 30/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

A partir del 17 de enero de 2020, entra en vigencia la obligatoriedad de emitir el documento guía de despacho en formato electrónico, de acuerdo a lo indicado en la Ley N°21.131, del 16 de enero de 2019, “Ley de pago a treinta días". Esto significa que las guías de despacho emitidas en forma manual y timbradas en el SII ya no serán válidas.

## 001.003.6505.004

**Pregunta:** ¿Cuándo el Contribuyente estará obligado a facturar electrónicamente?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6505.htm
- Created: 28/05/2014
- Updated: 30/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

La obligación de emitir facturas y los otros documentos electrónicos señalados, entrará en vigencia dependiendo de los Ingresos anuales por ventas y servicios de las Empresas en el último año calendario y si su ubicación es urbana o rural. El Servicio ha calificado el ingreso gradual de los contribuyentes, como Etapa 1, 2 y 3, según el siguiente cuadro: Calendario de Ingreso de los Contribuyentes a Facturación Electrónica Etapas Tamaño Ingresos anuales por ventas y servicios (1) Ubicación Geográfica Plazo Fecha Etapa 1 Empresas calificadas Etapa 1 Grandes Empresas (2) 100.000 UF y más Urbana o Rural (sin distinción) 9 meses 1 de noviembre de 2014 Etapa 2 Empresas calificadas para Etapas 2 y 3. Empresa de Menor Tamaño (EMT)(3) 2.400 UF a 100.000 UF Urbana 30 meses 1 de agosto de 2016 Rural 36 meses 1 de febrero de 2017 Etapa 3 2.400 UF y menos Urbana 36 meses 1 de febrero de 2017 Rural 48 meses 1 de febrero de 2018 (1) Ingresos anuales por ventas y servicios en el último año calendario, Ley 20.416 de 2010. (2) Mayoritariamente Grandes Empresas. Hay empresas de otros segmentos. (3) Ley N° 20.780 del 29.09.14, modifica los plazos de EMT. Valor UF al 31 de enero de 2014: $ 23.435.

## 001.003.6514.007

**Pregunta:** ¿A qué se refiere el -acuse de recibo- que se debe enviar y que relación tiene con el derecho a crédito fiscal?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6514.htm
- Created: 03/06/2014
- Updated: 30/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

Se denomina “acuse de recibo” a lo expresado en el inciso primero del artículo 9° de la Ley N° 19.983, que regula la transferencia y otorga mérito ejecutivo a la copia de la factura, y su otorgamiento, da derecho a crédito fiscal al comprador o beneficiario cuando el impuesto ha sido recargado en facturas electrónicas. Dicho acuse de recibo, se refiere al recibo de mercaderías o servicios prestados que se otorga en el ejemplar impreso (identificado con la expresión “cedible”) de una factura electrónica, guía de despacho, o bien, a través de un archivo electrónico, de acuerdo al formato establecido por SII. La Ley indica que el impuesto recargado en las facturas electrónicas dará derecho a “crédito fiscal” para el comprador o beneficiario, en el período en que efectúe el “acuse de recibo” o se entiendan recibidas las mercaderías entregadas o el servicio prestado. El acuse de recibo de mercaderías o servicios prestados, debe ser informado dentro del plazo de 8 días a través de la plataforma dispuesta por el SII en su sitio web. Transcurridos los 8 días corridos desde su recepción, el acuse de recibo se hará automáticamente.

## 001.003.6581.001

**Pregunta:** Una vez que todos estemos obligados a emitir documentos tributarios electrónicos ¿Cómo sabré si un documento tradicional recibido es válido?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6581.htm
- Created: 08/09/2014
- Updated: 30/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

Los contribuyentes que estando obligados por ley, se encuentren exceptuados por resolución del SII de la obligación de emitir documentos tributarios en formato electrónico, podrán utilizar documentos en formato papel, los que deben estar vigentes y timbrados por el SII. No obstante, deberán estampar, en un lugar visible de la copia cliente, el número y fecha de la resolución del SII que los exceptúa a dicha obligación. Esta información se podrá efectuar mediante impresión a través de medios computacionales, aposición de un timbre de goma o mediante cualquier otro medio manual o mecánico. Asimismo, el SII publicará en su sitio web (www.sii.cl) la nómina de contribuyentes exceptuados o prorrogados de la obligación de emitir documentos tributarios en formato electrónico, pudiendo verificar dicha información.

## 001.003.6584.008

**Pregunta:** Si estoy obligado a emitir documentos en formato electrónico, y a su vez, continúo emitiendo documentos tributarios en papel. ¿Existe alguna sanción?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6584.htm
- Created: 09/09/2014
- Updated: 30/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

Sí, el incumplimiento de la obligación de los contribuyentes de emitir exclusivamente documentos tributarios electrónicos, establecida en el artículo 54° de la LIVS, será sancionado de acuerdo al Código Tributario. El contribuyente podrá auto denunciarse en la Dirección Regional o Unidad correspondiente a su domicilio, adjuntar los documentos emitidos, indicar el documento que emitió manualmente y el monto total de éstos. Adicionalmente, el documento emitido no ajustado a la obligación considerada en el artículo 54° de la LIVS, no será válido para respaldar las operaciones y el crédito fiscal del receptor del documento. Dichos documentos deberán seguir el procedimiento de anulación respectivo. Así, en caso de detectarse la emisión de documentos manuales por algún contribuyente que se encuentre obligado a emitirlos en formato electrónico se cursará una infracción establecida en el Código Tributario. Cabe señalar que la Resolución establece el procedimiento de anulación de documentos tributarios manuales para los contribuyentes obligados a emitir documentos tributarios electrónicos, el cual debe llevarse a cabo respecto de los documentos tributarios en papel que posean, cuando no se hayan emitido.

## 001.003.6624.005

**Pregunta:** ¿Qué puedo hacer si por alguna contingencia temporal, no puedo emitir un documento electrónico?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6624.htm
- Created: 01/12/2014
- Updated: 30/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Ley N° 20.727, obligatoriedad de Factura Electrónica

### Respuesta

Actualmente la mayoría de los documentos tributarios se deben emitir en formato electrónico. Sólo en las situaciones excepcionales que contempla la Ley N° 20.727, el contribuyente podrá optar por emitir los documentos tributarios autorizados en papel.

## 001.003.6971.006

**Pregunta:** ¿Qué es el Registro de Compras y Ventas (RCV)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6971.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

El Registro de Compras y Ventas, es un nuevo sistema disponible en sii.cl, el cual está compuesto por 2 registros, un Registro de Compras (RC) y otro Registro de Ventas (RV). Este sistema tiene como finalidad de respaldar las operaciones afectas, exentas y no afectas a IVA efectuadas por el contribuyente, permitiendo controlar el Impuesto al Valor Agregado. Este registro es abastecido por los documentos tributarios electrónicos (DTE’s) que han sido recibidos por el Servicio de Impuestos Internos. En el caso de los documentos tributarios recibidos y emitidos en soporte distinto al electrónico, deberán deben ser informados por el contribuyente incorporándolos al registro correspondiente ya sea de compra, o de venta, ya sea de forma individual o en forma de resumen, según corresponde el caso.

## 001.003.6972.006

**Pregunta:** ¿Qué es el Registro de Compras (RC)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6972.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

El Registro de Compras, es una de las partes que compone el Registro de Compras y Ventas. Este Registro, es el que da cuenta de todas las operaciones de compras realizadas por un contribuyente de acuerdo con los documentos tributarios electrónicos recepcionados por el Servicio de Impuestos Internos, complementado con los documentos tributarios de compras, en soporte distinto al electrónico, en el cual deberá indicarse la naturaleza de las operaciones en cuanto a la procedencia e identificación del crédito fiscal. Este registro, determina el uso del crédito fiscal del Impuesto al Valor Agregado y está compuesto de 4 secciones: 1. Registro: En esta sección, están todas las compras del giro a las que el contribuyente deberá indicar la naturaleza de la operación por documento, las cuales, por defecto, serán clasificadas como del Giro, y podrán ser modificadas a: Supermercado, Bienes Raíces, Activo Fijo, IVA Uso Común, IVA No Recuperable, o No Incluir. 2. Pendiente: En esta sección, se encuentran todos aquellos documentos que requieren como requisito que el comprador otorgue recibo de mercaderías entregadas o servicios prestados, y que al momento de consultar esta sección, tienen pendiente dicho requisito. 3. Reclamados: En esta sección, se almacenarán todos aquellos documentos que el comprador ha reclamado dentro del plazo de 8 días. 4. No incluir: En esta sección, se encuentran los documentos que el contribuyente ha decidido no considerar para el desarrollo de su actividad comercial, y que por lo tanto, no es considerado como IVA crédito fiscal, ni como gasto para efectos del Impuesto a la Renta.

## 001.003.6973.007

**Pregunta:** ¿Qué es el Registro de Ventas (RV)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6973.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

El Registro de Ventas (RV), es parte del Registro de Compras y Ventas (RCV), y da cuenta de todas las operaciones de ventas realizadas por un contribuyente, de acuerdo a los documentos tributarios electrónicos recibidos en el Servicio de Impuestos Internos, complementado con los documentos tributarios de ventas, exportación o prestaciones de servicios en soporte distinto al electrónico, informando además, las ventas que se deben indicar al nivel de resumen, como por ejemplo las ventas con boleta, ventas respaldadas con vales en reemplazo de boletas, comprobante de pagos electrónicos, boletas electrónicas, etc. Este registro, podrá determinar el débito fiscal del Impuesto al Valor Agregado. Es importante señalar, que en la emisión de las facturas electrónicas se deberá informar el tipo de transacción de ventas (del giro, bienes raíces o activo fijo), dicha información no es editable desde el registro de ventas, por lo que en caso de algún error en dicha información, deberá anular el documento mediante una nota de crédito electrónica y emitir uno nuevo, con el tipo de venta correspondiente.

## 001.003.6974.005

**Pregunta:** ¿A contar de qué mes es válido el Registro de Compras y Ventas (RCV)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6974.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

El Registro de Compras y Ventas (RCV) es válido a contar del 01 de Agosto de 2017, y permitirá que a contar del 01 de Septiembre de 2017 el contribuyente pueda acceder a la propuesta de IVA. Es importante señalar que hasta el mes de Julio se deberá informar la Información Electrónica de Compras y Ventas (IECV), obligación que corresponde cumplir todos los meses a los contribuyentes autorizados a emitir documentos tributarios electrónicos, y que para este último periodo tienen plazo para enviar al SII hasta el 31 de Agosto. Lo anterior con excepción de los contribuyentes clasificados como microempresas rurales que aún no se encuentran inscritos como facturadores electrónicos, quienes aún deberán llevar el libro de compras y ventas en formato físico. Podrán hacer uso del Registro de Compras y Ventas a contar del periodo en que se inscriban como facturadores electrónicos, o en su defecto, a contar del 01.02.2018.

## 001.003.6975.006

**Pregunta:** ¿Se debe firmar electrónicamente el Registro de Compras y Ventas?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6975.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

No, no se debe firmar el Registro de Compras y Ventas, puesto que la información se encuentra dispuesta en las bases de datos del SII, y cualquier modificación de la información es posible realizarla sólo utilizando la autenticación de RUT y Clave.

## 001.003.6976.003

**Pregunta:** ¿Se considera el acuse de recibo para registrar una factura en el Registro de Compras (RC)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6976.htm
- Created: 28/07/2017
- Updated: 29/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

Si, el Registro de Compras considerará las facturas del período en que se otorga o se entienda otorgado el recibo de mercaderías entregadas o servicios prestados, según lo informado por el comprador en el Registro de Aceptación o Reclamos, de nuestro sitio web. Si no es otorgado dicho acuse de recibo y no ha sido reclamado, transcurrido el plazo de 8 días corridos desde la recepción de la factura electrónica en el SII, se asignará automáticamente al período en que se entienda otorgado dicho acuse de recibo. Cabe señalar que si la factura fue reclamada dentro del plazo de 8 días este se asignará automáticamente a la sección Reclamadas, sin que pueda ser asignada a otra sección del RC.

## 001.003.6977.004

**Pregunta:** ¿Hasta qué fecha puedo esperar que un documento electrónico emitido por un proveedor sea incorporado a mi Registro de Compras y de Ventas?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6977.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

La fecha límite que un documento electrónico debiera estar consignado en un Registro de Compras y Ventas de un periodo determinado, para el emisor es hasta el día 10 del período tributario siguiente, esto considerando la posibilidad que se emitan Facturas Electrónicas sobre Guías de Despacho, respecto de las cuáles fue otorgado el acuse de recibo de mercaderías. En el caso del comprador a la fecha indicada anteriormente (día 10 del período tributario siguiente) se debe contemplar además el plazo que tiene para reclamar o aceptar dicho documento.

## 001.003.6978.005

**Pregunta:** ¿Cuándo se realiza alguna acción en el Registro de Compras o de Ventas, el SII informa de esto enviando algún mail o notificación?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6978.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

No, a diferencia de la Información Electrónica de Compras y Ventas, al complementar o agregar información a los Registros de Compras y Ventas no se envía notificación o mail alguno al contribuyente, toda vez que la modificación queda ingresada y vigente en forma inmediata. Para confirmar que los cambios se hayan grabado, es posible descargar la información que el SII posee en sus bases de datos.

## 001.003.6979.004

**Pregunta:** ¿El RCV reemplaza los Libros de Compras y Ventas?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6979.htm
- Created: 28/07/2017
- Updated: 29/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

Sí, este nuevo Registro reemplaza la obligación de llevar el Libro de Compras y Ventas, como también de enviar la Información Electrónica de Compras y Ventas para los contribuyentes que están autorizados como emisores electrónicos. Así mismo, estarán eximidos de llevar el Libro de Compras y Ventas los contribuyentes no sujetos al sistema de facturación electrónica, o que emitan otro tipo de documentos tributarios electrónicos que no requieren ser enviados al Servicio de Impuestos Internos, tales como boletas, vouchers u otros, siempre que la información relativa a sus ventas y prestaciones de servicios, la complementen en el Registro de Ventas informando los Resúmenes correspondientes.

## 001.003.6980.006

**Pregunta:** ¿A partir de qué período tributario, se suspende el envío de la Información Electrónica de Compras y Ventas (IECV) al SII?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6980.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

El contribuyente podrá enviar la IECV hasta el periodo de julio 2017. Por lo tanto, a partir del periodo siguiente, deberá registrar los antecedentes en el Registro de Compras y Ventas (RCV).

## 001.003.6983.005

**Pregunta:** ¿Qué sucede si mi Información Electrónica de Compras y Ventas (IECV) difiere de la Información registrada en el Registro de Compras y Ventas (RCV)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6983.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

La información válida es la registrada e informada en el RCV de acuerdo a los documentos emitidos y efectivamente recibidos en el SII, considerando que la IECV ya no debe enviarse al SII, sólo existe tal obligación hasta el periodo de julio 2017. Si existiese diferencia de documentos emitidos por el contribuyente o por terceros y no recepcionados, se debe gestionar su reenvío.

## 001.003.6984.004

**Pregunta:** ¿Puedo agregar al RCV un documento electrónico que no ha sido recibido por el SII?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6984.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

No, los documentos tributarios electrónicos válidos son solo aquellos que han sido recibidos correctamente por el SII, y que están disponibles para ser consultados en su sitio web sii.cl, además de ser registrado en el Registro de Ventas del Vendedor como en el Registro de Compras del Comprador o Beneficiario del servicio.

## 001.003.6985.005

**Pregunta:** ¿Qué acciones se deben efectuar si un documento emitido por un proveedor no ha sido recibido en el SII?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6985.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

Contactarse con el proveedor para verificar la situación y solicitar el reenvío, de lo contrario este documento no se considera válido.

## 001.003.6986.003

**Pregunta:** ¿El Registro de Compras y Ventas (RCV) cuenta con funcionalidades que faciliten la consulta y administración de la información caracterizada y/o complementada?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6986.htm
- Created: 28/07/2017
- Updated: 03/03/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

Sí, el RCV cuenta con varias funcionalidades que permiten facilitar su administración, tales como filtros por tipo de documentos, por número de folio, por fechas, por montos, también es posible ordenarlos utilizando los criterios antes indicados y además se puede descargar la información en un archivo para su administración.

## 001.003.6987.005

**Pregunta:** ¿Qué significa caracterizar o indicar la naturaleza de una operación en el Registro de Compras (RC)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6987.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

Las compras se caracterizan por cada uno de los documentos recibidos, y este no podrá contener más de una clasificación de tipo de compra, a excepción del IVA Uso Común, que podrá informarse junto con Activo Fijo, Bienes Raíces o Supermercados. Las opciones de caracterización son las siguientes: 1. Del Giro: Esta es la clasificación que se considerará por defecto en el Registro de Compras (RC), en el caso que en la factura electrónica no se indique una clasificación distinta en el tipo de compra sugerido. Esta clasificación significa que la factura respalda compras relacionadas con la actividad declarada por el contribuyente al Servicio de Impuestos Internos. 2. Supermercado: Esta clasificación corresponde a compras que no son parte de la actividad que desarrolla la empresa, pero que corresponden a gastos que la ley permite realizar. 3. Bienes Raíces: Esta clasificación como su nombre lo indica es para identificar las compras de Bienes Raíces. 4. Activo Fijo: Esta clasificación es para identificar aquellas compras de bienes que han sido adquiridos o construidos con el ánimo de usarlos en forma permanente en la explotación del giro del contribuyente y que corresponden principalmente a parte de la infraestructura física del negocio. 5. IVA Uso Común: Esta clasificación es para identificar aquellas compras que al momento de realizarse no es posible identificar si se destinarán a ventas afectas o exentas de IVA, a las que se les deberán aplicar un factor de proporcionalidad, el cual se calcula de acuerdo a la relación de las ventas afectas sobre el total. Al informar este tipo de compra podrá adicionalmente informar para el mismo documento los tipos de compra Activo Fijo, Bienes Raíces o Supermercados. 6. IVA No Recuperable: Esta clasificación aplica para aquellas compras en que el comprador no tiene derecho a utilizar, por ejemplo por encontrarse fuera de plazo. 7. No Incluir: Esta clasificación se encuentra en los documentos que el contribuyente ha decidido no considerar para el desarrollo de su actividad comercial, y que por lo tanto no son considerados como crédito de IVA, ni como gasto para efectos del Impuesto a la Renta. Al seleccionar esta opción, el documento se moverá de sección, desde la sección Registro, a la sección No Incluir.

## 001.003.6988.005

**Pregunta:** ¿Cómo se caracteriza el tipo de compra de los documentos en el Registro de Compras (RC)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6988.htm
- Created: 28/07/2017
- Updated: 29/05/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

En el Registro de Compras, tanto los documentos tributarios electrónicos como los no electrónicos se pueden caracterizar uno a uno, ingresando al detalle del documento, vía formulario en pantalla, a través de la Web en un campo dispuesto para seleccionar la clasificación de tipo de compra que se requiera. Otra forma para realizar la caracterización del tipo de compra es por carga masiva, subiendo un archivo plano (extensión .csv), en donde la información de tipo de compra se puede modificar a más de un documento tributario electrónico. Si requiere modificar el tipo de compra de los documentos no electrónicos, deberá volver a subir los documentos con el tipo de transacción de compra que corresponda, reemplazando la información subida anteriormente. La caracterización de cada documento se encuentra definida en la siguiente tabla: Caracterización de compras Valores Tipo de Transacción de Compra Código Compras del Giro 1 Compras en Supermercados o comercios similares 2 Adquisición de bienes raíces 3 Compra de Activo Fijo 4 Compras con IVA Uso Común 5 Compras sin Derecho a Crédito (IVA no recuperable) 6 Compras que no corresponde incluir 7

## 001.003.6989.005

**Pregunta:** ¿Cómo se caracteriza el tipo de venta de los documentos en el Registro de Ventas (RV)?

- URL: https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6989.htm
- Created: 28/07/2017
- Updated: 27/06/2025
- Breadcrumbs: Menú Principal > Factura Electrónica > Registro de Compras y Ventas

### Respuesta

En el Registro de Ventas, no es posible caracterizar los documentos tributarios electrónicos, ya que el tipo de venta debe informarse al momento de la emisión del Documento. En caso de no indicar el tipo de venta al momento de generar el documento, este es considerado por defecto, como del giro. En el caso que usted esté autorizado a emitir documentos no electrónicos (papel), podrá informar el tipo de transacción de venta, al momento de ingresar el documento en el Registro de Ventas.
