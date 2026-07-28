# Protocolo experimental para la caracterización de columnas de lecho fijo y su escalamiento

**Documento operativo del proyecto**
Complementa `docs/marco-teorico.md`, `docs/reynolds-tubing-vs-lecho.md` y `AUDITORIA.md`
Última revisión: 2026-07-25

---

## Propósito

El presente documento define la campaña experimental destinada a caracterizar el material adsorbente y el sistema de columnas de lecho fijo, con el objeto de obtener los parámetros requeridos para proyectar la operación a escala real (caudal objetivo: 1 L/s).

La campaña se organiza en **seis fases secuenciales separadas por puntos de decisión**. Cada fase produce una magnitud que dimensiona la fase siguiente. Esta estructura responde a una consideración de ingeniería: la duración y el consumo de agua de los ensayos de ruptura dependen de la capacidad del material, magnitud desconocida al inicio, y que puede hacer variar la campaña entre horas y meses. Iniciar los ensayos de columna sin haber determinado previamente dicha capacidad expone el proyecto a comprometer recursos sobre una configuración inviable.

---

## Configuración base del montaje

La totalidad de la campaña se ejecuta sobre una única configuración:

| Elemento | Especificación | Fundamento |
|---|---|---|
| Columnas | 4 unidades de 10 mm ID × 10 cm, en serie mediante conexión luer lock | Permite obtener 4 profundidades de lecho en una sola corrida |
| Puertos de muestreo | Uno tras cada columna (L = 10, 20, 30, 40 cm) | Genera los datos de BDST sin repetir corridas |
| Lecho total | 40 cm; V = 31.4 mL; M ≈ 25 g (con ρ_bulk = 0.80 g/mL) | — |
| Fracción granulométrica | 0.3 – 0.5 mm (tamizada) | Asegura D/d_p ≥ 20 |
| Tubing de interconexión | 1.6 mm ID máximo, longitud minimizada | Limita el volumen muerto |
| Caudal de referencia | 6.54 mL/min (v_s = 5 m/h) | EBCT de 4.8 min en el puerto terminal |

### Tiempo de contacto obtenido en cada puerto

| v_s [m/h] | Q [mL/min] | EBCT a 10 cm | 20 cm | 30 cm | 40 cm |
|---|---|---|---|---|---|
| 3.0 | 3.93 | 2.00 min | 4.00 | 6.00 | 8.00 |
| **5.0** | **6.54** | **1.20 min** | **2.40** | **3.60** | **4.80** |
| 7.5 | 9.82 | 0.80 min | 1.60 | 2.40 | 3.20 |
| 10.0 | 13.09 | 0.60 min | 1.20 | 1.80 | 2.40 |

Esta disposición constituye el elemento de mayor eficiencia de la campaña: **cada corrida entrega simultáneamente cuatro curvas de ruptura a cuatro EBCT distintos y cuatro puntos del modelo BDST**, magnitudes que de otro modo requerirían cuatro corridas independientes.

---

## FASE 0 — Caracterización y acondicionamiento del material

**Objeto:** determinar las propiedades físicas que cierran el cálculo hidráulico y decidir la dirección de flujo.

### Determinaciones

| # | Determinación | Método | Magnitud obtenida |
|---|---|---|---|
| 0.1 | Distribución granulométrica | Tamizado en serie | $d_{50}$, amplitud de la distribución |
| 0.2 | Separación de la fracción de trabajo | Tamizado a 0.3 – 0.5 mm | Material de ensayo |
| 0.3 | Densidad de partícula | Picnometría | $\rho_s$ |
| 0.4 | Densidad aparente del lecho | Probeta, con y sin compactación | $\rho_{bulk}$ |
| 0.5 | Porosidad | $\varepsilon = 1 - \rho_{bulk}/\rho_s$ | $\varepsilon$ (valor preliminar) |
| 0.6 | Resistencia a la atrición | Agitación controlada y retamizado | Generación de finos |

### Cálculos derivados

- Verificación de la relación $D/d_p \geq 20$.
- Verificación de la relación $L/d_p \geq 50$, equivalente a $Pe > 100$.
- **Velocidad mínima de fluidización**, según:

$$u_{mf} = \frac{(\rho_s - \rho)\,g\,d_p^2\,\varepsilon_{mf}^3}{150\,\mu\,(1-\varepsilon_{mf})}$$

### ▸ Punto de decisión A — Dirección de flujo

| Condición | Decisión |
|---|---|
| $u_{mf} > u_{operación}$ con margen ≥ 50 % | Se admite operación en flujo ascendente |
| $u_{mf} \leq u_{operación}$ | **Operación en flujo descendente obligatoria**, con retención superior del lecho |

Conforme al análisis preliminar consignado en `AUDITORIA.md`, si $\rho_s \lesssim 1800$ kg/m³ la operación ascendente resulta inviable al caudal de referencia.

### Procedimiento de empaque

El empaque condiciona la reproducibilidad de la totalidad de la campaña y debe protocolizarse:

1. Empaque **en húmedo**: la columna se llena parcialmente con agua desmineralizada y el material se incorpora en suspensión, en fracciones sucesivas.
2. Golpeteo lateral uniforme entre fracciones, con número de golpes registrado y constante entre columnas.
3. Registro de la masa efectivamente cargada en cada columna y de la altura final del lecho.
4. **Acondicionamiento en flujo ascendente** a caudal bajo durante un mínimo de 10 volúmenes de lecho, con objeto de desplazar el aire ocluido, con independencia de la dirección de operación posterior.
5. Verificación visual de ausencia de estratificación, canales preferenciales y burbujas retenidas.

> El aire ocluido constituye la causa más frecuente de irreproducibilidad en columnas de diámetro reducido. Una burbuja retenida altera la porosidad local y genera una canalización estable que persiste durante toda la corrida.

---

## FASE 1 — Caracterización hidrodinámica del sistema

**Objeto:** cuantificar la contribución del montaje a la dispersión, de modo que ésta pueda separarse de la contribución del material. Esta fase es previa e indispensable a cualquier ensayo de adsorción.

### Ensayos

**1.1 — Trazador en ausencia de columna (blanco de sistema).** Se conecta la bomba directamente al colector empleando el tubing definitivo. Se inyecta un pulso de trazador conservativo. La curva de salida corresponde íntegramente a la contribución del sistema de conducción. Duración estimada: 2 h.

**1.2 — Trazador sobre lecho inerte.** Se repite el ensayo con las columnas empacadas con material inerte de igual granulometría. Duración estimada: 4 h.

**1.3 — Trazador sobre material virgen.** Idéntico al anterior, empleando el material de estudio sin cargar. Entrega la porosidad efectiva y el tiempo de residencia reales. Duración estimada: 4 h.

**1.4 — Curva de pérdida de carga.** Registro de $\Delta P$ en cinco caudales entre 3 y 30 mL/min, en orden ascendente y descendente. Duración estimada: 3 h.

### Magnitudes obtenidas

| Magnitud | Procedencia |
|---|---|
| $\varepsilon$ efectiva | Primer momento de la curva de trazador (1.3) |
| $\tau$ real | Primer momento |
| $D_{ax}$, $Pe$ | Segundo momento (varianza) |
| $\sigma^2_{conducto}$ | Ensayo 1.1 |
| $\phi_s \cdot d_p$ efectivo | Ajuste de la ecuación de Ergun sobre 1.4 |

La histéresis entre las ramas ascendente y descendente del ensayo 1.4 revela compactación o reordenamiento del lecho.

### ▸ Punto de decisión B — Validez del montaje

| Criterio | Umbral | Acción si no se cumple |
|---|---|---|
| $\sigma^2_{conducto} / \sigma^2_{total}$ | < 10 % | Reducir longitud o diámetro interno del tubing |
| $Pe$ del lecho | > 100 | Incrementar longitud de lecho o reducir $d_p$ |
| Cierre del balance de trazador | 95 – 105 % | Revisar fugas y volúmenes muertos no contabilizados |

**No se procede a la Fase 3 sin haber superado este punto de decisión.** Una curva de ruptura obtenida sobre un montaje cuya dispersión propia es comparable a la del lecho no admite interpretación.

---

## FASE 2 — Equilibrio de adsorción en discontinuo

**Objeto:** determinar la capacidad del material, magnitud que dimensiona la totalidad de la campaña de columnas.

### Ensayos

**2.1 — Isotermas.** Serie de ensayos discontinuos a temperatura controlada, con masa de adsorbente variable y concentración inicial constante, hasta alcanzar el equilibrio. Ajuste a los modelos de Langmuir y Freundlich según `docs/marco-teorico.md`, sección 4.

**2.2 — Cinética en discontinuo.** Seguimiento de la concentración en función del tiempo a masa fija. Permite estimar el orden de magnitud de la difusividad intrapartícula y contrastarla con el coeficiente de película $k_f$ obtenido por correlación.

**2.3 — Isoterma sobre agua real.** Repetición de 2.1 empleando la matriz real de regadío, con objeto de cuantificar la competencia de la matriz frente al ensayo en agua sintética.

### ▸ Punto de decisión C — Viabilidad de la campaña de columnas

La capacidad obtenida permite estimar la duración de los ensayos de ruptura mediante:

$$t_{estequiométrico} = \frac{q_0 M}{C_0 Q} \qquad t_{ruptura} \approx 0.6 - 0.8 \; t_{estequiométrico}$$

**Duración y consumo de agua previstos** (Q = 6.54 mL/min, M = 25 g):

| $C_0$ [mg/L] | $q_0$ = 1 mg/g | 5 mg/g | 20 mg/g | 50 mg/g |
|---|---|---|---|---|
| **1** | 2.7 d / 25 L | 13.3 d / 126 L | 53.4 d / 503 L | 133 d / 1257 L |
| **5** | 12.8 h / 5 L | 2.7 d / 25 L | 10.7 d / 100 L | 26.7 d / 251 L |
| **20** | 3.2 h / 1.3 L | 16.0 h / 6 L | 2.7 d / 25 L | 6.7 d / 63 L |

*(valores de tiempo estequiométrico; el volumen indicado corresponde al agua consumida en ese lapso)*

Criterios de decisión:

| Duración prevista | Decisión |
|---|---|
| < 7 días y < 60 L | Proceder a Fase 3 en configuración directa |
| 7 – 20 días | Proceder, evaluando incremento de $C_0$ o de $v_s$ |
| > 20 días o > 150 L | **Recurrir a ensayo acelerado (RSSCT)** |

> El consumo de agua constituye una restricción frecuentemente subestimada. El agua real de regadío no admite almacenamiento prolongado sin alteración de su composición por sedimentación y actividad biológica. Superados los ~100 L, la logística de abastecimiento pasa a condicionar el diseño experimental.

### Opción acelerada: ensayo en columna reducida (RSSCT)

Procede únicamente si el punto de decisión C lo determina. Consiste en moler el material a una granulometría inferior, conservando la similitud mediante las relaciones de Crittenden. Con $d_p$ de escala real de 0.5 mm, $v_s$ = 10 m/h y EBCT = 5 min:

| $d_p$ molido | Razón | **PD**: EBCT / $v_s$ / Q / t_ensayo | **CD**: EBCT / $v_s$ / Q / t_ensayo |
|---|---|---|---|
| 0.30 mm | 0.60 | 3.00 min / 16.7 m/h / 21.8 mL/min / 0.60× | 1.80 min / 16.7 m/h / 21.8 mL/min / 0.36× |
| 0.20 mm | 0.40 | 2.00 min / 25.0 m/h / 32.7 mL/min / 0.40× | 0.80 min / 25.0 m/h / 32.7 mL/min / **0.16×** |
| 0.15 mm | 0.30 | 1.50 min / 33.3 m/h / 43.6 mL/min ⚠ / 0.30× | 0.45 min / 33.3 m/h / 43.6 mL/min ⚠ / 0.09× |

⚠ Excede la capacidad de la bomba (40 mL/min).

- **PD** (difusividad proporcional): aplicable a adsorbentes de poro amplio.
- **CD** (difusividad constante): aplicable cuando domina la difusión en microporo. Reduce el tiempo de forma más pronunciada.
- La relación $D/d_p$ se mantiene conforme en todos los casos (50 – 67 con $D$ = 10 mm).

**Advertencia:** el RSSCT modifica el diámetro de partícula, por lo que el ensayo deja de ejecutarse en las condiciones de la escala real. La validez del resultado queda condicionada a la hipótesis de difusividad adoptada, la cual debe verificarse mediante al menos una corrida de contraste a $d_p$ real.

---

## FASE 3 — Curvas de ruptura

**Objeto:** obtener las curvas características que constituyen el entregable del encargo.

### Matriz de corridas

| ID | Ensayo | Q [mL/min] | Muestreo | Objeto |
|---|---|---|---|---|
| R5 | Ruptura base, $v_s$ = 5 m/h | 6.54 | 4 puertos | Condición de referencia; BDST |
| R6 | Ruptura, $v_s$ = 10 m/h | 13.09 | 4 puertos | Efecto de la velocidad sobre la MTZ |
| R7 | Réplica de R5 | 6.54 | 4 puertos | Reproducibilidad |
| R8 | $C_0$ alterno | 6.54 | 4 puertos | Dependencia respecto de la concentración |
| R9 | Columna testigo sin material | 6.54 | 1 puerto | Discrimina retención física de adsorción |

R9 se ejecuta **en paralelo** a R5, alimentada desde el mismo estanque.

### Programa de muestreo

El muestreo debe concentrarse en torno a la ruptura, no distribuirse uniformemente:

| Intervalo | Frecuencia |
|---|---|
| 0 – 0.3 $t_b$ estimado | Baja (verificación de línea base) |
| 0.3 – 0.6 $t_b$ | Media |
| **0.6 – 1.5 $t_b$** | **Alta — 60 % de los puntos** |
| 1.5 $t_b$ – saturación | Decreciente hasta $C/C_0 > 0.95$ |

Se requieren de 20 a 25 puntos por puerto para el ajuste de los modelos. Con cuatro puertos y seis corridas, la carga analítica asciende a 480 – 600 determinaciones.

> **Mitigación de la carga analítica.** Se recomienda implementar una señal continua en línea (conductividad, absorbancia u otro proxy adecuado al contaminante), calibrada contra un subconjunto de determinaciones discretas de laboratorio. Este esquema entrega resolución temporal elevada a costo reducido y permite además detectar la ruptura en tiempo real, evitando su omisión durante períodos no atendidos.

### Registro continuo obligatorio

Con independencia del muestreo de concentración, deben registrarse a lo largo de toda la corrida:

| Variable | Frecuencia | Fundamento |
|---|---|---|
| **Caudal por gravimetría** | 2 – 3 veces al día | El tubing peristáltico se deforma con el uso y el caudal deriva. La lectura del dial no es evidencia de caudal. |
| $\Delta P$ | Continua o diaria | Indicador temprano de colmatación |
| Temperatura | Continua | $\mu$ varía en un factor 1.9 entre 5 y 30 °C |
| $C_0$ del afluente | En cada punto de muestreo | La matriz real deriva durante el almacenamiento |
| Turbidez / SST, entrada y salida | Diaria | Discrimina filtración de adsorción |

La verificación gravimétrica del caudal constituye el control de mayor rendimiento de la campaña: una deriva no detectada del 15 % invalida el eje de volúmenes de lecho de la totalidad de la curva.

### ▸ Punto de decisión D — Validez de la corrida

Cierre del balance de masa:

$$m_{adsorbida} = Q \int_0^{t_{sat}} (C_0 - C)\,dt \qquad \text{contrastada con} \qquad q_0 \cdot M$$

| Criterio | Umbral |
|---|---|
| Cierre del balance de masa | 90 – 110 % |
| Diferencia entre R5 y su réplica R7 en $t_b$ | < 15 % |
| Retención en columna testigo R9 | < 5 % de la retención en R5 |
| $\Delta P$ final / $\Delta P$ inicial | < 2 |

Una corrida que no satisfaga el cierre de balance no se incorpora al ajuste de modelos.

---

## FASE 4 — Ajuste de modelos y obtención de parámetros

### Modelos aplicados

| Modelo | Datos requeridos | Parámetros obtenidos |
|---|---|---|
| **Thomas** | Curva completa por puerto | $k_{Th}$, $q_0$ |
| **Yoon-Nelson** | Curva completa | $k_{YN}$, $\tau_{50}$ |
| **BDST** | $t_b$ frente a $L$ (4 puertos) | $N_0$, $K_a$ |
| **LUB / MTZ** | Curva completa | Longitud de lecho no utilizada |

El **modelo BDST constituye el instrumento central del escalamiento**, por cuanto relaciona directamente el tiempo de servicio con la profundidad del lecho:

$$t_b = \frac{N_0}{C_0 u}L - \frac{1}{K_a C_0}\ln\left(\frac{C_0}{C_b}-1\right)$$

La pendiente de la recta $t_b$ frente a $L$ entrega $N_0/(C_0 u)$, esto es, la capacidad volumétrica del lecho; la ordenada al origen entrega la constante cinética y define la **profundidad crítica de lecho**, valor por debajo del cual la ruptura es inmediata.

### Curvas características (entregable del encargo)

1. **Curva de ruptura**: $C/C_0$ frente a volúmenes de lecho (BV), parametrizada por EBCT.
2. **Curva BDST**: $t_b$ frente a $L$.
3. **Isoterma de equilibrio**: $q_e$ frente a $C_e$, en agua sintética y en agua real.
4. **Curva de pérdida de carga**: $\Delta P$ frente a $Q$, y $\Delta P$ frente al tiempo.
5. **Distribución de tiempos de residencia**: respuesta al trazador, del sistema y del lecho.
6. **Longitud de la zona de transferencia de masa** frente a $v_s$.

> La abscisa de la curva de ruptura debe expresarse en **volúmenes de lecho**, no en tiempo. El tiempo no es invariante frente al escalamiento; el número de volúmenes de lecho sí lo es cuando se conservan $v_s$, EBCT y $d_p$.

---

## FASE 5 — Proyección a escala de operación

### Relaciones de escalamiento

Conservando $v_s$, EBCT y $d_p$, la proyección se reduce a un escalamiento por área:

$$A_{real} = \frac{Q_{real}}{v_s} \qquad L_{real} = v_s \cdot EBCT \qquad V_{lecho} = A_{real} \cdot L_{real}$$

En estas condiciones, el número de volúmenes de lecho hasta la ruptura, la pérdida de carga y el perfil de la curva se conservan entre ambas escalas.

### Dimensionamiento resultante para 1 L/s (86.4 m³/día)

| $v_s$ | Diámetro | EBCT = 5 min | EBCT = 15 min |
|---|---|---|---|
| 5 m/h | 0.96 m | L = 0.42 m; 300 L de material | L = 1.25 m; 900 L |
| 10 m/h | 0.68 m | L = 0.83 m; 300 L | L = 2.50 m; 900 L |
| 15 m/h | 0.55 m | L = 1.25 m; 300 L | L = 3.75 m; 900 L |

### Magnitudes derivadas para el diseño de la unidad

- **Frecuencia de reposición del material**: BV hasta ruptura, obtenido en Fase 3, dividido por los BV/día de la unidad real.
- **Consumo másico anual** de material.
- **Profundidad crítica de lecho** (de BDST): fija el mínimo dimensional.
- **Configuración de la unidad**: la comparación entre la longitud de la MTZ y la longitud del lecho determina si procede una disposición en serie con reemplazo alternado, que incrementa el aprovechamiento del material.

### Validación

Se recomienda una corrida final de confirmación en una configuración distinta de las empleadas en el ajuste —por ejemplo, EBCT intermedio no ensayado— con objeto de contrastar la predicción de los modelos frente a un dato no utilizado en su calibración. La discrepancia observada constituye la estimación honesta de la incertidumbre asociada al escalamiento.

---

## Secuencia y dependencias

```
FASE 0  Material            →  ▸A  dirección de flujo
   ↓
FASE 1  Hidrodinámica       →  ▸B  validez del montaje   ── no se avanza sin superarlo
   ↓
FASE 2  Equilibrio batch    →  ▸C  ¿directo o RSSCT?     ── dimensiona toda la campaña
   ↓
FASE 3  Curvas de ruptura   →  ▸D  cierre de balance
   ↓
FASE 4  Ajuste de modelos
   ↓
FASE 5  Proyección y validación
```

**Duración estimada:** Fases 0 a 2, de dos a tres semanas. Fase 3, determinada por el punto de decisión C. Fases 4 y 5, una semana.

---

## Riesgos identificados y medidas de control

| Riesgo | Manifestación | Control |
|---|---|---|
| Deriva del caudal por desgaste del tubing | Eje de BV incorrecto en toda la curva | Verificación gravimétrica; reemplazo programado del tubing |
| Colmatación por sólidos suspendidos | Incremento de $\Delta P$; retención no atribuible a adsorción | Prefiltro 10 – 25 µm; columna testigo R9; registro de $\Delta P$ |
| Aire ocluido en el lecho | Canalización estable; irreproducibilidad | Acondicionamiento ascendente; alimentación desgasificada |
| Sorción del contaminante en el tubing | Ruptura aparente retardada; cola falsa | Blanco de tubing (Fase 1.1) con el contaminante, no solo con trazador |
| Alteración del agua almacenada | $C_0$ derivante durante la corrida | Muestreo del afluente en cada punto; volúmenes de acopio reducidos |
| Fluidización en flujo ascendente | Pérdida del frente de adsorción | Punto de decisión A |
| Omisión de la ruptura fuera de horario | Pérdida de la región de mayor información | Señal en línea con registro continuo |
