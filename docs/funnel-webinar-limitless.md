# Funnel Webinar Limitless — estructura relevada

> Relevamiento del funnel público de `webinar.applylimitless.com`, hecho el 20/08/2026
> a partir del link de un anuncio de Instagram y capturas de las tres pantallas del flujo.
> No es un funnel propio: es documentación de referencia para entender la estructura.

---

## 1. Entrada — tráfico pago desde Instagram

URL del anuncio:

```
https://webinar.applylimitless.com/
  ?fbc_id=120249731093380484
  &h_ad_id=120249731094720484
  &utm_medium=paid
  &utm_source=ig
  &utm_id=120249731091940484
  &utm_content=120249731094720484
  &utm_term=120249731093380484
  &utm_campaign=120249731091940484
  &fbclid=PAdGRleAT0M...
```

| Parámetro | Valor | Qué representa |
|---|---|---|
| `utm_id`, `utm_campaign` | `...91940484` | ID de campaña de Meta |
| `utm_term`, `fbc_id` | `...93380484` | ID del ad set |
| `utm_content`, `h_ad_id` | `...94720484` | ID del anuncio |
| `utm_source` / `utm_medium` | `ig` / `paid` | Origen declarado |
| `fbclid` | `PAdGRleAT0M...` | Click ID de Meta (alimenta la cookie `_fbc`) |

Observaciones: los UTMs llevan **IDs numéricos, no nombres** de campaña; `fbc_id` y `h_ad_id`
son parámetros custom que duplican `utm_term` y `utm_content`.

---

## 2. Landing de registro

### Concepto visual

La página entera está montada como un **board de canvas colaborativo** (estilo Miro / FigJam):
fondo oscuro con grilla de puntos, acentos naranja, sticky notes rotadas, polaroids con cinta,
handles de selección alrededor del headline, secciones nombradas `FRAME 01`…`FRAME 04`,
y una toolbar flotante fija abajo (cursor, sticky, lápiz, frame, comentario, zoom 100%).
Es decorativa, no funcional.

### Elementos persistentes

- **Nav superior**: logo `LIMITLESS` · `Board: Sistema +$2,000,000 con Webinars` · pill `● En vivo` ·
  avatares de asistentes (`A` `L` `+9`) · CTA `Reservar lugar`.
- **Barra de countdown sticky**: `La clase empieza en 00D 00H 42M 37S`.

### Hero

- Headline: *"Te voy a dar GRATIS todos mis **SOPs, Software y IA** con los que hice **+$2,000,000** con Webinars"*
- Subheadline: *"Este **20/08** en una clase privada te voy a **REGALAR TODOS** mis sistemas con los que hice **+$220k** en mi último webinar."*
- Sticky note: *"Todos mis SOPs, paso a paso"* · marcador `VOS`
- **VSL** con subtítulos quemados y barra de progreso naranja.
- Tres badges: `Jueves 20 de agosto` · `17:00 hs (ARG) — ESP 22:00 · COL 15:00 · CHI 16:00` · `100% gratis y en vivo`

### Formulario de registro

Título: *"Completá tus datos y reservá tu lugar"*

| Campo | Tipo | Detalle |
|---|---|---|
| Nombre | texto | placeholder "Tu nombre" |
| Email | email | placeholder "tu@email.com" |
| WhatsApp | selector de país + teléfono | default `AR Argentina +54` |
| ¿Cuánto está facturando tu negocio por mes? | dropdown | `Menos de $2,500` / `$2,500 - $10,000` / `Más de $10,000` (sin moneda declarada) |

- CTA: `RESERVÁ TU LUGAR GRATIS`
- Microcopy: *"Sin costo. **Los cupos son limitados.** El acceso te llega por email."*
- Sticky notes decorativas alrededor: `REGALO #2 — Mi software completo`, `REGALO #3 — Mi IA trabajando 24/7`
- Debajo, **countdown en formato flip**: `00 DÍAS · 00 HORAS · 42 MIN · 21 SEG`

### FRAME 01 · Los regalos

Kicker *"todo esto te lo llevás gratis ↓"* → título **"El sistema completo que uso todos los días"**.
Tres sticky cards, cada una con sello `GRATIS`:

1. **Mis SOPs** — los procesos exactos, paso a paso, para lanzar y escalar webinars que venden.
2. **Mi software** — el stack completo: funnel, registro, seguimiento, ventas y métricas. Listo para copiar.
3. **Mi IA** — agentes y prompts que hacen copy, creativos, guiones y seguimiento. "Como sumar un equipo de marketing que trabaja 24/7."

### FRAME 02 · En el entrenamiento

Kicker *"tres cosas ↓"* → título **"Lo que vas a ver en vivo"**. Tres bullets con check:

1. Todas las IAs, sistemas, funnel y softwares usados para hacer **$220,000** en el último webinar.
2. El paso a paso exacto para aplicarlo con tu creador.
3. Cómo replicarlo con múltiples creadores para hacer **+$100,000/mes**.

> El avatar objetivo (growth operators / agencias que trabajan con creadores) recién queda explícito acá.

### FRAME 03 · Tu anfitrión

Polaroid + bio de **Naza**, "Growth Operator":

- +$14,000,000 generados para clientes en 2 años; +$10M de eso en proyectos DWY.
- En LATAM: +$2,000,000 y un negocio llevado a $170,000/mes, solo con orgánico.
- En EEUU: otros +$2,000,000, solo con webinars.
- Argumento central: los mismos $2M, el primero en ~3 años y el segundo en menos de 1 →
  el orgánico depende del creador, el webinar es apalancado y casi no depende de él.
- Tres stat cards: `+$14,000,000 generados para clientes` · `+$2M en EEUU con webinars` · `$170K/mes orgánico en LATAM`

### FRAME 04 · Tu lugar

Kicker *"último paso ↓"* → título **"Reservá tu lugar antes de que se llene"** + sticky `cupos limitados`.

Prueba: **dos capturas de dashboards de gross revenue** en polaroid:

| Captura | Monto | Período |
|---|---|---|
| 1 | `$1,040,487.47` | Sep 1 2024 – Jun 30 2025 |
| 2 | `$1,198,865.06` | Jun 2025 – Jun 2026 |

Suma ≈ **$2.24M**, que es lo que respalda el claim de `+$2,000,000` del hero.
Las capturas no muestran plataforma ni titular de la cuenta.

Cierre: *"Una sesión en vivo. El sistema completo de +$2,000,000 en webinars, y todos mis SOPs,
mi software y mi IA de regalo."* → CTA `QUIERO MI LUGAR GRATIS` + *"Registrate en menos de 30 segundos"*.

---

## 3. Página de gracias (post-registro)

Pill `● REGISTRO CONFIRMADO`.

- Headline: *"Listo. Tu lugar está reservado — Pero tengo **4 REGALOS** para vos"*
- Instrucción: *"**Antes de cerrar esta página**, mirá el video. Hay **4 SOPs de regalo** para vos si completás los 3 pasos de abajo. Te toma 2 minutos."*
- **Segundo VSL**, rodeado de cuatro sticky notes con preview de cada SOP:
  `SOP #1 Sistema de Distribución de Contenido` · `SOP #2 Lazarus` · `SOP #3 B-52` · `SOP #4 Black Hole`
- Se repiten los badges de fecha / hora / gratis. **No se repite el countdown.**

### Los 3 pasos ("Desbloqueá los 4 SOPs")

| Paso | Acción | Copy | CTA |
|---|---|---|---|
| 1 | **Respondé el mail** | "Te acaba de llegar un mail nuestro, el asunto es un regalo (🎁). Abrilo y respondé con la palabra **SOP**. Si no aparece, buscá en promociones o spam." | — (acción en el inbox) |
| 2 | **Unite al grupo** | "Ahí llega el link de acceso el día del evento, más SOPs, entregables y las IAs que usamos en el negocio." | `→ Entrar al grupo de WhatsApp` |
| 3 | **Agendá la clase** | "Sumala a tu calendario para que nada se te cruce ese día. Un click y queda bloqueada con recordatorio." | `+ Agregar a Google Calendar` |

Condición al pie: *"Los 4 SOPs se mandan **solo** a quienes completan los 3 pasos ahora."*

**No hay oferta de venta ni OTO en esta página** — la venta queda reservada para el webinar en vivo.

---

## 4. Lógica del funnel

```
Anuncio IG (tráfico pago)
        ↓
Landing "board"  →  VSL + 4 frames de argumentación  →  form de 4 campos
        ↓                                                 (califica por facturación)
Página de gracias  →  VSL #2  →  3 pasos que en realidad son mecánicas de show-up:
        ↓                          · responder el mail  → deliverability de toda la secuencia
        ↓                          · grupo de WhatsApp  → canal de recordatorio (mejor show-up en LATAM)
        ↓                          · Google Calendar    → recordatorio nativo
Webinar en vivo (jue 20/08, 17:00 ARG)  →  acá ocurre la venta
```

Piezas clave de la estructura:

- **Un solo objetivo por página.** La landing solo pide el registro; la thank-you solo pide asistencia.
- **Los "regalos" hacen doble trabajo**: son el incentivo del registro (SOPs / software / IA en el FRAME 01)
  y el incentivo del show-up (los 4 SOPs desbloqueables en la thank-you).
- **La escasez está en tres capas**: countdown, "cupos limitados" y "antes de que se llene".
- **La prueba es first-party**: dashboards de revenue propios, sin testimonios de terceros.
- **La calificación se hace en el registro**, no después: el dropdown de facturación segmenta el lead
  antes de que entre al webinar.

## 5. Datos que captura

Del usuario: nombre, email, teléfono con código de país, rango de facturación mensual.
De la sesión: `fbclid` + UTMs en la URL (queda por verificar si el form los persiste en campos ocultos).

---

## 6. Puntos observados

Hallazgos del relevamiento, por si sirven como referencia de qué mirar en una estructura así:

**Riesgo alto**
- Anuncios activos a 42 minutos del inicio, sin fallback evergreen visible: cuando el countdown
  llega a cero, el tráfico pago cae en una página vencida.
- Claims de ingresos específicos (`+$100,000/mes`, `+$220,000`, `$170K/mes`) sin disclaimer de
  resultados ni política de privacidad visible, recolectando email y teléfono → expuesto a
  las políticas de Meta sobre income claims y lead collection.

**Conversión**
- El formulario queda por debajo del VSL (crítico en mobile, que es casi todo el tráfico de IG).
- Cuatro campos para un registro gratuito, incluido un dropdown de calificación.
- El dropdown de facturación **no declara moneda** y su techo (`Más de $10,000`) agrupa al lead
  de $11k con el de $150k, que es justamente el que compra ticket alto.
- Se pide WhatsApp pero el microcopy solo promete entrega por email.
- La prueba más fuerte (los dashboards de revenue) está en el FRAME 04, al final del scroll.
- El hero no declara para quién es; el avatar aparece recién en el FRAME 02.

**Thank-you page**
- Perdió el countdown: con el evento a 40 minutos, la página comunica como si faltaran días.
- La jerarquía visual destaca el Paso 1 (responder el mail) por sobre el Paso 2 (WhatsApp),
  que es el que realmente predice la asistencia.
- "Te toma 2 minutos" subestima los tres pasos.
- El Paso 1 exige que el remitente acepte respuestas y que alguien (o algo) procese la keyword `SOP`.
- Condicionar la entrega a los 3 pasos deja sin nada a quien completa 2.

**Tracking**
- `utm_source=ig` + `utm_medium=paid` no cae en Paid Social en GA4 (queda en *Unassigned* / *Paid Other*).
  Convención esperada: `utm_source=instagram`, `utm_medium=paid_social`.
- UTMs con IDs en vez de nombres → los reportes muestran `120249731091940484` en lugar del nombre de campaña.
- Sin verificar: persistencia de `fbclid`/`_fbc`/`_fbp` en campos ocultos del form,
  evento `Lead` por pixel + CAPI con `event_id` compartido, UTMs conservados en la URL de gracias,
  y evento custom en el click de "Entrar al grupo de WhatsApp" (el mejor predictor de show-up).

### Plantilla de UTMs de referencia

```
?utm_source=instagram
&utm_medium=paid_social
&utm_campaign={{campaign.name}}
&utm_term={{adset.name}}
&utm_content={{ad.name}}
&utm_id={{campaign.id}}
&utm_source_platform=meta
```
