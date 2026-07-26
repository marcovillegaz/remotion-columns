# Distinción entre el número de Reynolds en el conducto y en el lecho empacado

**Nota conceptual de diseño**
Documento complementario a `docs/marco-teorico.md` y `AUDITORIA.md`
Última revisión: 2026-07-25

---

## Objeto

El montaje experimental contiene dos geometrías de flujo físicamente distintas —el conducto cerrado que conecta los componentes y el medio poroso que constituye el lecho— cada una gobernada por un número de Reynolds construido sobre longitudes características diferentes. La presente nota establece la distinción entre ambos, identifica una tercera formulación carente de significado físico que ha sido empleada erróneamente en el código del proyecto, y define el modo en que ambos conceptos se integran en el diseño del sistema experimental.

---

## 1. El número de Reynolds como plantilla, no como número

La expresión general del número de Reynolds,

$$Re = \frac{\rho\, v\, L_c}{\mu}$$

carece de significado hasta que se especifican la **longitud característica** $L_c$ y la **velocidad** $v$. La elección de ambas no es convencional ni arbitraria: define qué fenómeno físico se está caracterizando y, en consecuencia, qué umbrales de transición resultan aplicables.

En el sistema bajo estudio dicha elección admite tres formulaciones, de las cuales únicamente dos poseen significado físico.

### Tabla comparativa (evaluada a Q = 13 mL/min)

| | Región | $L_c$ | Velocidad $v$ | Valor | Umbrales aplicables | Validez |
|---|---|---|---|---|---|---|
| **A** | Tubing de conexión | $D_{tubo}$ = 1.6 mm | Velocidad media en el conducto, 108 mm/s | **172** | 2300 / 4000 | Válido |
| **B** | Columna tratada como conducto vacío | $D_{col}$ = 10 mm | $u$ = 2.76 mm/s | 27.6 | 2300 / 4000 | **Sin significado físico** |
| **C** | Lecho empacado | $d_p$ = 0.5 mm | $u$ superficial = 2.76 mm/s | **1.38** | 10 / 1000 | Válido |

---

## 2. La formulación B carece de significado físico

La formulación B corresponde a la implementada en `reynolds_and_diameters.py`. Ésta trata la columna como un conducto hueco de 10 mm de diámetro interno. Sin embargo, la columna se encuentra empacada: el fluido no atraviesa en ningún momento una sección circular de 10 mm, sino una red tortuosa de poros cuya dimensión característica es del orden de 0.1 mm.

En consecuencia, el número resultante no describe ninguna geometría existente en el sistema, y los umbrales de transición en conducto cerrado que se le aplican no gobiernan fenómeno alguno. Descartada esta formulación, las formulaciones A y C coexisten sin contradicción, dado que describen regiones distintas del montaje.

---

## 3. Origen de la discrepancia numérica entre A y C

Evaluadas al mismo caudal, las formulaciones A y C difieren en un factor aproximado de 125. Dicha discrepancia no constituye una inconsistencia, sino la consecuencia aritmética de dos factores concurrentes:

- **Razón de áreas.** El tubing de 1.6 mm posee una sección transversal equivalente a 1/39 de la sección de la columna. A caudal constante, la velocidad media en el conducto resulta 39 veces superior a la velocidad superficial en la columna.
- **Razón de longitudes características.** $D_{tubo}/d_p = 1.6/0.5 = 3.2$.

El producto de ambos factores, $39 \times 3.2 \approx 125$, reproduce la razón observada.

---

## 4. Los umbrales de transición proceden de fenómenos distintos

| | Conducto cerrado (2300 / 4000) | Lecho empacado (10 / 1000) |
|---|---|---|
| Cuestión que resuelve | Si el perfil de velocidad es parabólico o se aplana | Si el arrastre sobre cada partícula es de naturaleza viscosa o inercial |
| Mecanismo de inestabilidad | Desestabilización de la capa límite en la pared del conducto | Desprendimiento de estela en la partícula |
| Magnitud que predice | Factor de fricción; distribución de tiempos de residencia del conducto | Término dominante de la ecuación de Ergun; coeficiente $k_f$ mediante la correlación de Sherwood |

La aplicación de los umbrales de conducto cerrado a un lecho empacado, o la operación inversa, constituye un error de categoría. Un mismo valor numérico admite clasificaciones contradictorias según el criterio que se le aplique: $Re = 172$ corresponde a régimen laminar bajo el criterio de conducto y a régimen de transición bajo el criterio de partícula.

---

## 5. La condición laminar posee implicaciones opuestas en cada región

Esta circunstancia constituye la principal fuente de confusión y merece enunciarse de forma explícita.

**En el lecho empacado, el régimen laminar es la condición normal y deseable.** El sistema opera a $Re_p$ comprendido entre 0.5 y 4.2 en todo el rango de la bomba. El empaque proporciona por sí mismo la mezcla radial: la bifurcación sucesiva del fluido en torno a cada partícula homogeneiza el perfil de velocidades sin requerir turbulencia. El lecho aproxima el comportamiento de flujo pistón *pese a* operar en régimen laminar.

**En el conducto de conexión, el régimen laminar constituye una fuente de error.** En ausencia de turbulencia el perfil de velocidad es parabólico, con una velocidad en el eje igual al doble de la velocidad media y una velocidad prácticamente nula en la pared. La verificación del cociente entre el tiempo de difusión radial y el tiempo de residencia arroja:

$$\frac{t_{difusión}}{t_{residencia}} = \frac{R^2/D_m}{L_{tubo}/v} \approx 69 - 212 \gg 1$$

Dado que este cociente es muy superior a la unidad, la difusión radial no dispone de tiempo suficiente para promediar el perfil. La distribución de tiempos de residencia resultante presenta un frente adelantado y una cola prolongada, cuya firma es indistinguible de una transferencia de masa lenta en el material adsorbente, esto es, precisamente la magnitud que el ensayo pretende determinar.

---

## 6. El número de Péclet como magnitud de integración

El número de Péclet permite unificar el tratamiento de ambas regiones, por cuanto cuantifica en las dos el mismo fenómeno: el ensanchamiento que experimenta un pulso al atravesarlas.

### 6.1 En el lecho empacado

Adoptando la estimación de dispersión mecánica $D_{ax} \approx u\,d_p/2$, válida para $Re_p > 1$:

$$Pe = \frac{uL}{D_{ax}} = \frac{2L}{d_p}$$

La velocidad se cancela. Se concluye que **la aproximación a flujo pistón en el lecho es una propiedad geométrica, independiente del caudal de operación**. De esta expresión se desprende asimismo la equivalencia:

$$Pe > 100 \iff \frac{L}{d_p} > 50$$

El criterio $L/d_p \geq 50$ enunciado en `docs/marco-teorico.md` y el criterio $Pe > 100$ constituyen, por tanto, una misma condición expresada de dos formas.

Valores para el montaje ($d_p$ = 0.5 mm):

| Configuración | $L$ | $L/d_p$ | $Pe$ | Condición |
|---|---|---|---|---|
| Columna individual | 10 cm | 200 | 400 | Cumple |
| Tren de 8 columnas | 83 cm | 1660 | 3320 | Cumple |

### 6.2 En el conducto de conexión

La expresión anterior no resulta aplicable, por cuanto el conducto no se encuentra en régimen dispersivo de Taylor-Aris (véase sección 5). El control del aporte del conducto se ejerce, en consecuencia, mediante el criterio directo de volumen muerto.

---

## 7. Integración en el diseño del sistema experimental

El montaje constituye una cadena de elementos en serie. La señal registrada a la salida corresponde a la convolución de las respuestas individuales:

```
bomba ⊛ conducto de entrada ⊛ COLUMNA ⊛ conducto de salida ⊛ sistema de muestreo
                                  ↑
                    única contribución de interés experimental
```

El objetivo del diseño consiste en lograr que la contribución de la columna domine dicha convolución. Ambos números de Reynolds concurren a este objetivo, si bien desempeñando funciones distintas:

| Magnitud | Variable de diseño que determina | Criterio | Estado del montaje |
|---|---|---|---|
| $Re$ en el conducto (A) | Diámetro interno y longitud del tubing | $V_{muerto}/V_{poro} < 10\%$ | 1.6 mm → 15 %; 3.2 mm → 62 % (no cumple) |
| $Re_p$ en el lecho (C) | Diámetro de partícula y caudal | $Re_p < 10$ (régimen de Darcy); alimenta la correlación de Sherwood para $k_f$ | 0.5 – 4.2 (cumple) |
| $Pe = 2L/d_p$ | Longitud del lecho | $Pe > 100$ | 400 – 3320 (cumple) |

**Enunciado sintético:** el número de Reynolds del conducto se emplea para volver despreciable la contribución del conducto; el número de Reynolds de partícula se emplea para caracterizar el lecho. Ambos no compiten entre sí, no se promedian y no deben igualarse.

### Volumen muerto admisible

Volumen de poro del tren de columnas (83 cm de lecho, $\varepsilon$ = 0.40): **26.2 mL**.

| Diámetro interno | Volumen en 2 m | Fracción del volumen de poro | Veredicto |
|---|---|---|---|
| 0.8 mm | 1.01 mL | 3.8 % | Adecuado |
| 1.6 mm | 4.02 mL | 15.4 % | Aceptable con corrección |
| 3.2 mm | 16.08 mL | 61.5 % | Inadmisible |
| 4.0 mm | 25.13 mL | 96.0 % | Inadmisible |

---

## 8. Convención relativa a la velocidad en $Re_p$

El número de Reynolds de partícula se calcula **por convención con la velocidad superficial** $u = Q/A$, definida como la que presentaría el fluido si la columna se encontrase vacía, y no con la velocidad intersticial $u_i = u/\varepsilon$, pese a que esta última corresponde a la velocidad real del fluido entre las partículas.

A 13 mL/min, $u$ = 9.9 m/h mientras que $u_i$ = 24.8 m/h. El empleo de la velocidad intersticial incrementa $Re_p$ en un factor 2.5 e invalida tanto el resultado de la ecuación de Ergun como el de las correlaciones de Sherwood, por cuanto ambas fueron establecidas sobre la base de la velocidad superficial. Se recomienda consignar esta convención de forma explícita en el protocolo experimental.

---

## 9. Verificación experimental

La totalidad de las consideraciones precedentes admite verificación empírica mediante ensayos de trazador, cuya ejecución se recomienda con anterioridad a cualquier corrida de adsorción:

1. **Ensayo de trazador en ausencia de columna.** Se conecta la bomba directamente al colector a través del tubing definitivo y se inyecta un pulso de trazador conservativo. La curva de salida corresponde a la contribución del sistema de conducción.
2. **Ensayo de trazador con lecho inerte.** Se repite el procedimiento con la columna empacada con material inerte del mismo diámetro de partícula. Permite determinar la dispersión propia del lecho.
3. **Comparación de varianzas.** Si $\sigma^2_{conducto}$ excede aproximadamente el 10 % de $\sigma^2_{total}$, procede reducir la longitud de las líneas o su diámetro interno con anterioridad al inicio de los ensayos.

Este procedimiento convierte el criterio de volumen muerto de estimación en medición, y proporciona adicionalmente el valor experimental de $D_{ax}$ del lecho, magnitud requerida para el escalamiento.
