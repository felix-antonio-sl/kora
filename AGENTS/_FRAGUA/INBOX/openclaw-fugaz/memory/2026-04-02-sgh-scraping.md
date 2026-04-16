# Session: 2026-04-02 16:47:06 UTC

- **Session Key**: agent:steipete:telegram:direct:7192195698
- **Session ID**: 365fbf14-b548-4e61-8121-26fefcde3908
- **Source**: telegram

## Conversation Summary

assistant: Voy a reproducir el login SGH con un cliente HTTP mínimo para ver el destino final y entender por qué `index.php` sigue cayendo en el login aun con sesión válida para otros endpoints.
assistant: El login no redirige a un home clásico; devuelve una página mínima autenticada, así que voy a leer ese HTML y extraer scripts/forms ocultos por donde quizás se entra al resto del sistema.
assistant: Encontré una anomalía importante: el `login` SGH con las credenciales del CLI está devolviendo modal de **“Usuario o Contraseña Incorrectos”** en el root, aunque algunos endpoints específicos siguen respondiendo. No me frena para seguir mapeando lecturas concretas, pero sí explica por qué el menú global está raro. Mientras tanto voy a exprimir los JS del módulo paciente por cualquier ruta oculta relacionada al índice compartido.
assistant: El primer extractor reventó por una regex de Go demasiado grande. Lo corrijo y sigo.
assistant: Ya confirmé algo útil para seguir construyendo el CLI aunque no sea todavía la Historia Clínica Compartida:

- la ficha SGH clásica sí tiene una capa JS rica para **ambulatorias**, **urgencias** y **documentos OSIRIS**
- `detalleAtencionHistorica(modalidad, codCita, codInst, codPacie)` llama:
  - `osiris/listadoDocumentos.php`
  - con `cc`, `ci`, `cp`, `m=2`, `g=1`
- y de ahí abre:
  - `ipdPdf.php`
  - `excepcionPdf.php`
  - `cierreCasoPdf.php`
  - `sospechaPdf.php`
  - `alta_pdf.php`
  - `atencion_pdf.php`
  - `noAlta_pdf.php`

Eso valida que el siguiente frente útil por SGH es **profundizar ambulatorio/OSIRIS documental**, que sí está vivo y accesible desde esta superficie.

La Historia Clínica Compartida de tu screenshot sigue sin aparecer en esta ficha clásica, así que probablemente vive en otra ruta/módulo. Mientras la ubico, puedo avanzar por esta veta que ya está confirmada y nos da valor inmediato para el CLI.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1304",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Thu 2026-04-02 15:41 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

sgh ambulatorias corresponde al cae (centro de atención especializada) , es decir el consultorio de especialidades adosado al hospital, pero de atención ambulatoria. Eso es diferente a los registros de aps
assistant: [[reply_to_current]] Sí, correcto. Buena corrección.

## Distinción correcta
### **SGH Ambulatorias**
No es APS.  
Corresponde al **CAE / policlínico de especialidades** adosado al hospital:
- cardiología
- oftalmo
- neurocirugía
- dermatología
- kinesiología
- etc.

O sea:
> **atención ambulatoria especializada hospitalaria**

### **APS**
Es otra capa:
- CESFAM
- consultorios
- controles crónicos
- morbilidad general
- red primaria / Rayen

O sea:
> **atención primaria de salud en la red comunal**

## Implicancia para el CLI
Entonces el modelo correcto queda así:

- `h amb` = **CAE / especialidades hospitalarias ambulatorias**
- `h aps` = **APS / CESFAM / consultorios**

Y eso refuerza algo importante:
- lo que sí tengo bien abierto hoy por SGH es **CAE ambulatorio**
- lo que sigue trabado o escondido es la **superficie APS real**

## Lectura estratégica
Eso hace todavía más valioso perseguir la vista de tu screenshot, porque probablemente esa **Historia Clínica Compartida** sí mezcla:
- APS
- ambulatorio hospitalario
- formularios
- prescripciones
- otras capas de la red

Y por eso parecía más rica que la pestaña APS legacy.

## Ajuste mental correcto
No debo seguir diciendo “APS/ambulatorio” como si fueran una sola cosa.  
Desde ahora los separo así:

- **CAE ambulatorio SGH**
- **APS red primaria**
- **Historia Clínica Compartida** como capa transversal que probablemente cruza ambos

Sigo con esa separación.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1306",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Thu 2026-04-02 17:46 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

pero historia clinica compartida es aps de base con añadidos de otras fuentes, q no todas las veces está presente
assistant: [[reply_to_current]] Sí. Eso calza mucho mejor.

## Entonces el modelo correcto queda así

### 1. **SGH Ambulatorias**
- CAE / especialidades del hospital
- policlínico adosado
- ambulatorio hospitalario

### 2. **APS**
- CESFAM / consultorios / red primaria
- Rayen / atención primaria base

### 3. **Historia Clínica Compartida**
No es “otra fuente” aparte, sino más bien una **capa agregadora** donde:
- la **base fuerte suele ser APS**
- y a veces se le suman otras cosas:
  - ambulatorio hospitalario
  - formularios
  - prescripciones
  - diagnósticos
  - procedimientos
  - otras piezas longitudinales

Y como dices, **no siempre está presente**.

## Eso cambia la estrategia
Entonces no debo perseguir Historia Clínica Compartida como si fuera:
- una pantalla universal
- siempre disponible
- o equivalente a APS puro

Más bien hay que tratarla como:

> **superficie oportunista de alto valor**  
> cuando existe para ese paciente y esa trayectoria documental

## Implicancia para el CLI
El CLI debería modelarlo así:

- **fuentes base estables**
  - `amb` = CAE
  - `aps` = APS
- **fuente agregada condicional**
  - `hcc` / historia clínica compartida, si aparece

O sea:
- no reemplaza APS
- no reemplaza CAE
- los complementa cuando está disponible

## Lectura práctica
Tu screenshot entonces no refuta que APS legacy esté fallando.  
Lo que muestra es que **a veces SGH logra exponer una capa longitudinal compartida basada en APS**, pero eso es:
- **parcial**
- **no garantizado**
- **dependiente del caso**

Y eso, de hecho, es más interesante para diseñar bien el CLI.

## Siguiente paso correcto
Yo seguiría con esta taxonomía explícita:

- **APS base**
- **CAE ambulatorio**
- **HCC condicional**

y desde ahí mapear:
1. cuándo aparece HCC
2. qué endpoint la alimenta
3. qué mezcla de fuentes trae en cada caso

Ese ya es el modelo correcto.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1308",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Thu 2026-04-02 18:23 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

así, continúa con el desarrollo
assistant: Voy a cristalizar esta taxonomía en el CLI y, si el HTML lo permite, dar el siguiente salto útil: sacar de **ambulatorias/CAE** los identificadores para listar sus documentos OSIRIS desde SGH.
assistant: Encontré valor inmediato: el parser actual de `amb` está leyendo columnas en orden incorrecto y está ignorando los IDs/acciones que sí vienen en el HTML. Voy a corregir eso y agregar la siguiente capa: **listar documentos OSIRIS de una atención ambulatoria/CAE**.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1313",
  "sender_id": "7192195698",
  "sender": "Ominono",
  "timestamp": "Thu 2026-04-02 18:41 GMT+2"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Ominono (7192195698)",
  "id": "7192195698",
  "name": "Ominono"
}
```

documenta y memoriza tu trabajo en cli-hsc y commit. vamos a empezar una nueva sesión . fdame el prompt handoff
assistant: Voy a dejar un handoff canónico dentro de `hsc-cli`, actualizar la matriz con la taxonomía correcta **APS vs CAE vs HCC**, memorizarlo y hacer un commit de documentación solamente.
assistant: Ahora hago commit limpio solo con documentación/handoff.
