# Auditoría de ingeniería de procesos — Sistema de columnas a pequeña escala

**Alcance:** `reynolds_and_diameters.py` + diseño del caso (bomba peristáltica 1–40 mL/min, columnas 1 cm ID luer, agua real de regadío, escalamiento objetivo 1 L/s).
**Fecha:** 2026-07-25
**Base de cálculo:** agua a 20 °C (ρ=1000 kg/m³, μ=1.0 mPa·s), material granular 0.3–1 mm, ε≈0.40.

---

## 1. Resumen ejecutivo

El código calcula correctamente el número de Reynolds de tubería y está limpiamente escrito, pero **está resolviendo el problema equivocado**. El criterio Re=2300/4000 no gobierna nada en este sistema, la región graficada está ~1500× fuera de lo que la bomba puede entregar, y el criterio propuesto para seleccionar tubing (igualar Re con el canal de riego) no es un criterio de selección de tubing.

Las variables que sí gobiernan el montaje son otras: **velocidad superficial (v_s), EBCT, volumen muerto del tubing, relación D/dp y colmatación**. Ninguna aparece en el código.

Hay una buena noticia de fondo: **el hardware disponible es adecuado**. La bomba cubre con holgura el rango de velocidades de diseño relevante (5–15 m/h ↔ 6.5–19.6 mL/min, justo en el centro del rango 1–40), y la caída de presión es despreciable (<0.1 bar). El problema no es el equipo, es el criterio de diseño.

| Severidad | Nº | Tema |
|---|---|---|
| 🔴 Crítico | 6 | Criterio de régimen, espacio de diseño irreal, confusión columna/tubing, similitud de escalamiento, volumen muerto, dispersión laminar |
| 🟠 Mayor | 5 | D/dp, colmatación, EBCT alcanzable, fluidización, ausencia de marco de escalamiento |
| 🟡 Menor | 8 | Código muerto, leyenda, encoding, legibilidad |

---

## 2. Hallazgos críticos

### 🔴 C-1. El criterio Re = 2300 / 4000 no aplica a un lecho empacado

`reynolds_and_diameters.py:45-46, 130-141` trazan las fronteras laminar/transición/turbulento de **tubería vacía**. En una columna empacada el régimen se define con el **Reynolds de partícula**:

```
Re_p = ρ · v_s · d_p / μ      (v_s = velocidad superficial = Q/A_vacía)
Darcy/laminar: Re_p < 10  |  transición: 10–300  |  inercial: > 300
```

En este sistema, con d_p = 0.5 mm:

| Q [mL/min] | v_s [m/h] | Re_p |
|---|---|---|
| 5 | 3.8 | 0.53 |
| 10 | 7.6 | 1.06 |
| 20 | 15.3 | 2.12 |
| 40 | 30.6 | 4.24 |

**El lecho está en régimen de Darcy en todo el rango operable.** No hay transición que buscar. Las líneas de 2300 y 4000 son físicamente irrelevantes aquí.

### 🔴 C-2. El espacio de diseño graficado está fuera del alcance del equipo por 3 órdenes de magnitud

`reynolds_and_diameters.py:277-278` barre Q hasta `Q_max = 1.5e-3 m³/s` = **90 000 mL/min**. La bomba entrega **40 mL/min** (6.67e-7 m³/s).

Caudal necesario para alcanzar Re=2300 en cada tubing:

| Tubing ID | Q para Re=2300 | Factor sobre bomba |
|---|---|---|
| 1.6 mm | 173 mL/min | **4.3×** |
| 3.2 mm | 347 mL/min | **8.7×** |
| 4.0 mm | 434 mL/min | **10.8×** |
| 22 mm | 2 385 mL/min | **59.6×** |

**La turbulencia es inalcanzable en cualquier componente del montaje.** El gráfico entero describe una región inoperable. Todo el sistema opera en Re = 2–1061 (tubing) y Re_p = 0.5–4.2 (lecho).

### 🔴 C-3. El código confunde diámetro de columna con diámetro de tubing

El eje Y está etiquetado `"Diámetro de columna D [m]"` (`línea 235`) y la docstring dice *"diámetro de columna"* (`líneas 94-98`), pero según se confirmó, los 4–22 mm son **tubing comercial**. La columna está **fija en 10 mm**.

Peor, la lógica de recomendación (`líneas 188-229`) selecciona el tubing **cuyo Re se acerca más al Re del canal de riego**. Eso no es un criterio de selección de tubing bajo ningún marco. Los criterios reales son:

1. **Volumen muerto** (dominante — ver C-5)
2. Caída de presión
3. Compatibilidad química y de permeabilidad
4. Compatibilidad mecánica con los barbs luer disponibles

Además, el código trata todo el tubing como una sola variable libre, cuando hay **tres roles distintos**:

| Rol | ID | ¿Variable libre? |
|---|---|---|
| Tubing del cabezal peristáltico | Lo fija el fabricante del cabezal para dar 1–40 mL/min | **No** |
| Líneas de transferencia e interconexión | 0.8–1.6 mm | Sí — minimizar |
| Conexión a luer (barb) | Debe calzar con el OD del tubing elegido | Consecuencia del anterior |

### 🔴 C-4. Igualar Reynolds entre el canal y la columna es un error de similitud

`reynolds_and_diameters.py:162-172, 224-229` calculan `Re_real` del canal (Q=1 L/s, D=0.5 m) y lo usan como objetivo de similitud. Dos problemas:

**(a) El canal no es una tubería llena.** 1 L/s en una sección de 0.5 m llena daría v = 5.1 mm/s (18 m/h) — un canal de riego con ese caudal corre parcialmente lleno. El Re de canal abierto usa el **radio hidráulico** (Re = ρ·v·4R_h/μ), no el diámetro. El `Re_real = 2546` que imprime el código es un artefacto de asumir tubería llena.

**(b) Aunque estuviera bien calculado, es la variable equivocada.** El canal es un problema de *transporte*; la columna es un problema de *adsorción con transferencia de masa*. La similitud correcta para escalar columnas de lecho fijo es:

```
Mantener constantes:  v_s  ·  EBCT  ·  d_p  ·  composición del agua
Escalar por:          área transversal   (A = Q / v_s)
```

Con d_p igual en ambas escalas, esta similitud es exacta y trivial. (Si se cambiara d_p habría que usar RSSCT con las correlaciones de difusividad constante o proporcional de Crittenden — no es el caso aquí.)

### 🔴 C-5. El volumen muerto del tubing puede destruir la curva de ruptura

**Este es el hallazgo con mayor impacto en el entregable solicitado.** Una columna de 10×100 mm tiene sólo **3.14 mL de volumen de poro** (ε=0.40). El tubing compite directamente con esa cifra:

| Tubing ID | Volumen | 1 m vs V_poro de 1 columna |
|---|---|---|
| 0.8 mm | 0.50 mL/m | 16 % |
| 1.6 mm | 2.01 mL/m | 64 % |
| **3.2 mm** | 8.04 mL/m | **256 %** ❌ |
| **4.0 mm** | 12.57 mL/m | **400 %** ❌ |
| **8.0 mm** | 50.27 mL/m | **1600 %** ❌ |

Con tubing de 3.2 mm o más, **la curva de ruptura medida sería mayoritariamente dispersión del tubing, no del lecho.** Los parámetros ajustados (k, q₀, zona de transferencia de masa) serían del montaje, no del material.

Para el tren completo recomendado (~83 cm de lecho, V_poro = 26.2 mL) con 2 m de interconexión:

| Tubing ID | Volumen muerto | % del V_poro | Veredicto |
|---|---|---|---|
| 0.8 mm | 1.01 mL | 3.8 % | ✅ |
| 1.6 mm | 4.02 mL | 15.4 % | ⚠️ aceptable si se corrige |
| 3.2 mm | 16.08 mL | 61.5 % | ❌ |
| 4.0 mm | 25.13 mL | 96.0 % | ❌ |

**Recomendación: 1/16" (1.6 mm ID) como máximo en líneas de transferencia, con longitudes minimizadas.** Descartar del listado de compra todo lo ≥3.2 mm para esta función.

### 🔴 C-6. El flujo laminar en el tubing genera una RTD parabólica, no de pistón

En todo el tubing el flujo es laminar (Re = 106–1061), lo que implica perfil parabólico. La pregunta es si la difusión radial alcanza a homogeneizarlo (régimen de Taylor-Aris) o no:

```
t_difusión_radial / t_residencia = 212     (constante para todos los ID a Q fijo)
```

Como este cociente es ≫1, **no hay tiempo para homogeneización radial**: el fluido viaja con perfil parabólico puro. La distribución de tiempos de residencia resultante tiene el frente adelantado (t_mín = t_medio/2) y una cola larga — exactamente la firma que se confundiría con transferencia de masa lenta en el lecho.

**Mitigación obligatoria: ensayo de trazador en blanco (sin columna, sólo bomba + tubing + colector) antes de cualquier ensayo de adsorción**, para caracterizar y restar la dispersión del sistema.

---

## 3. Hallazgos mayores

### 🟠 M-1. La relación D/dp exige tamizar el material

Criterio estándar para evitar canalización por pared: **D_columna / d_p ≥ 20** (idealmente ≥ 30).

| d_p | D/d_p | Veredicto |
|---|---|---|
| 0.3 mm | 33.3 | ✅ |
| 0.5 mm | 20.0 | ✅ límite |
| **1.0 mm** | **10.0** | ❌ **bypass de pared** |

El material es 0.3–1 mm. **Con columna de 10 mm hay que tamizar y usar la fracción 0.3–0.5 mm, descartando lo >0.5 mm.** No es opcional: con la fracción gruesa el agua canaliza por la pared y la curva de ruptura sale prematura y con cola, sin que eso refleje el material.

Nota de escalamiento: el material tamizado debe ser **el mismo d_p** que se use a escala real, o la similitud de C-4 se rompe.

### 🟠 M-2. El EBCT alcanzable con una sola columna es demasiado corto

Con D fijo en 10 mm, EBCT y v_s sólo se desacoplan variando el **largo de lecho** (EBCT = L/v_s). Una columna de 10 cm da:

| Q [mL/min] | 5 | 10 | 20 | 40 |
|---|---|---|---|---|
| **EBCT [min]** | 1.57 | 0.79 | 0.39 | 0.20 |

Son EBCT muy bajos para caracterizar adsorción. Largo de lecho necesario para EBCT representativo:

| v_s | EBCT=2 min | EBCT=5 min | EBCT=10 min |
|---|---|---|---|
| 5 m/h (6.5 mL/min) | 16.7 cm | 41.7 cm | 83.3 cm |
| **10 m/h (13.1 mL/min)** | 33.3 cm | **83.3 cm (≈8 columnas)** | 166.7 cm |
| 15 m/h (19.6 mL/min) | 50.0 cm | 125.0 cm | 250.0 cm |

**Consecuencia de diseño: el sistema no es "una columna", es un tren de columnas en serie.** Esto es una ventaja, no un problema — las conexiones luer lo hacen trivial, y muestreando entre columnas se obtiene:
- el perfil de la **zona de transferencia de masa** en un solo ensayo,
- datos de **BDST** (tiempo de ruptura vs. largo de lecho) para escalar, sin repetir corridas.

**Este es el diseño que recomiendo y que el código debería estar dimensionando.**

### 🟠 M-3. Riesgo de fluidización si se opera en flujo ascendente

Si se elige flujo ascendente (habitual para evitar burbujas), hay que verificar que no se fluidice el lecho. Estimación en régimen laminar:

| ρ_s [kg/m³] | v_mf (d_p=0.3 mm) | v_mf (d_p=0.5 mm) |
|---|---|---|
| 1300 | 0.68 m/h (0.9 mL/min) | 1.88 m/h (2.5 mL/min) |
| 1500 | 1.13 m/h (1.5 mL/min) | 3.14 m/h (4.1 mL/min) |
| 1800 | 1.81 m/h (2.4 mL/min) | 5.02 m/h (6.6 mL/min) |
| 2200 | 2.71 m/h (3.6 mL/min) | 7.53 m/h (9.9 mL/min) |
| 2650 | 3.73 m/h (4.9 mL/min) | 10.36 m/h (13.6 mL/min) |

**Si el material tiene ρ_s ≲ 1800 kg/m³, el caudal de trabajo recomendado (13 mL/min) fluidiza el lecho en ascendente** y se pierde el frente de adsorción. Falta el dato de densidad de partícula — ver §7.

Alternativas: operar en **descendente** (con retención superior para evitar levantamiento y purga de burbujas), o limitar v_s por debajo de v_mf.

### 🟠 M-4. Agua real de regadío → colmatación no considerada

El caso especifica **agua real**, que trae sólidos suspendidos, algas y biopelícula. Sin control:
- el lecho se colmata y se mide **filtración, no adsorción**;
- ΔP sube y la peristáltica (desplazamiento positivo) **no lo limita** — sigue empujando hasta que algo cede.

Requerido:
- **Prefiltro** aguas arriba (rango 10–25 µm) y registro de SST/turbidez entrada-salida.
- **Manómetro o registro de ΔP en el tiempo** como indicador temprano de colmatación (una curva de ruptura tomada sobre un lecho colmatándose no es interpretable).
- Ensayo con **columna de control sin material** (sólo soporte inerte) para separar retención física de adsorción.

### 🟠 M-5. Falta por completo el marco de escalamiento — que es el entregable pedido

El encargo pide "curvas características para caracterizar y escalar". El código no toca ninguna de las variables que producen esas curvas. Falta:

- **EBCT** y **volúmenes de lecho (BV)** como abscisa de la curva de ruptura (C/C₀ vs BV es la forma escalable; vs tiempo no lo es).
- **Zona de transferencia de masa (MTZ)** y grado de utilización del lecho.
- **Modelos de ajuste**: Thomas, Bohart-Adams, Yoon-Nelson, y sobre todo **BDST** (`t_ruptura = f(L)`), que es el que entrega directamente los parámetros de escalamiento.
- **Cierre de balance de masa** (masa retenida por integración de la curva vs. masa en el sólido) como criterio de validez del ensayo.
- **Réplicas y blancos**.

Duración esperada de los ensayos (dato de planificación que hoy no existe):

| Condición | BV/día | Ruptura a 500 BV | a 5000 BV |
|---|---|---|---|
| v_s=10 m/h, EBCT=5 min | 288 | 41.7 h | 17.4 días |
| v_s=10 m/h, EBCT=2 min | 720 | 16.7 h | 6.9 días |

---

## 4. Realidad del escalamiento a 1 L/s — advertencia para conversar con el mandante

Aplicando la similitud correcta (§C-4) al objetivo confirmado de **1 L/s = 86.4 m³/día**:

| v_s | D columna real | EBCT=5 min | EBCT=15 min |
|---|---|---|---|
| 5 m/h | **0.96 m** | L=0.42 m, 300 L de material | L=1.25 m, **900 L** |
| 10 m/h | **0.68 m** | L=0.83 m, 300 L | L=2.50 m, **900 L** |
| 15 m/h | **0.55 m** | L=1.25 m, 300 L | L=3.75 m, **900 L** |

**El sistema a escala real es una columna de 0.5–1 m de diámetro con 300–900 litros de material.** Conviene confirmar con el investigador que el material es producible en ese orden de magnitud (cientos de kg) *antes* de comprar el montaje. Si el material se produce en gramos o cientos de gramos, el objetivo de 1 L/s continuo no es alcanzable y habría que redefinirlo (tratar una fracción del caudal, operación intermitente, o punto de uso).

Nota favorable: como v_s, L y d_p se mantienen constantes, **la caída de presión a escala real es la misma que en el laboratorio** — el escalamiento no introduce un problema hidráulico nuevo.

---

## 5. Lo que sí está correcto

- ✅ La fórmula `Re = 4ρQ/(πDμ)` (`línea 29`) es correcta y está bien derivada en la docstring.
- ✅ `calcular_reynolds` es una función pura, vectorizada y bien separada de la graficación.
- ✅ Uso de `LogNorm` + `np.logspace` para los niveles del `contourf` (`líneas 111-114`) — apropiado dado el rango de Re de 4 órdenes de magnitud.
- ✅ Filtrado de niveles de contorno al rango real de datos (`líneas 118, 134`) — evita el error de matplotlib con niveles fuera de rango.
- ✅ Docstrings claras, consistentes y en español.
- ✅ La *intención* de mapear un espacio de diseño (Q, D) es metodológicamente buena. El problema son las variables y los criterios elegidos, no el enfoque.
- ✅ **La bomba es adecuada.** El rango de diseño (5–15 m/h) cae en 6.5–19.6 mL/min, cómodamente dentro de 1–40. Ventana de trabajo recomendada: **5–25 mL/min** (el extremo 1–3 mL/min tiene pulsación relativa alta y es el menos estable).
- ✅ **La presión no es un problema.** Ergun para L=10 cm: 0.008–0.084 bar (ε=0.40), y hasta 0.21 bar en el peor caso (d_p=0.3 mm, ε=0.32 por compactación). Muy por debajo de cualquier límite de luer.

---

## 6. Hallazgos menores (código)

| # | Ubicación | Hallazgo |
|---|---|---|
| 🟡 1 | `líneas 32-79` | `graficar_reynolds` es **código muerto** — nunca se invoca. |
| 🟡 2 | `línea 232` | `plt.legend()` está **dentro de** `if Q_real is not None`. Si `Q_real=None`, los handles de régimen acumulados en `leyenda_handles` se descartan silenciosamente y el gráfico sale sin leyenda. |
| 🟡 3 | `líneas 223-229` | Los `print` de resultados están anidados dos niveles dentro de la lógica de graficado. Mezcla I/O con presentación; los resultados numéricos deberían retornarse, no imprimirse desde dentro del plot. |
| 🟡 4 | `líneas 258-260` | `diametros_mercado` está desordenado (`4, 22, 21, 20, 18, 16, 12, 14, 11, 10, 8, 7, 6, 5`) y sin deduplicar. |
| 🟡 5 | `líneas 149-157` | Las 14 etiquetas de diámetro se dibujan todas en `Q.max()` con `ha="right"` → se apilan ilegibles en el borde derecho. |
| 🟡 6 | `línea 204` | `markeredgecolor=None` **no** significa "sin borde": hereda el rcParam. Para sin borde va `"none"` (string). |
| 🟡 7 | `requirements.txt` | Está codificado en **UTF-16 con BOM**. `pip install -r requirements.txt` puede fallar. Debe ser UTF-8. |
| 🟡 8 | `líneas 247-293` | Todos los parámetros del caso están hardcodeados en `__main__`. Sin archivo de configuración, sin tests, `README.md` vacío (4 bytes). |
| 🟡 9 | `líneas 254-255` | ρ y μ fijas a 20 °C. En campo el agua va de 5 a 30 °C → μ varía de 1.52 a 0.80 mPa·s (**factor 1.9**), lo que afecta Re_p y ΔP directamente. Hay que registrar la temperatura en cada ensayo. |

---

## 7. Qué debería calcular el código (reemplazo propuesto)

Sustituir el mapa Re(Q,D) por un **mapa de diseño operable**, con Q limitado al rango real de la bomba (1–40 mL/min) y D fijo en 10 mm:

1. **Ventana operativa**: v_s [m/h], EBCT [min] y Re_p vs. Q, con el rango de la bomba como límite duro del eje.
2. **Selección del tren**: nº de columnas en serie necesarias para cada par (v_s, EBCT) objetivo.
3. **Balance de volumen muerto**: V_tubing / V_poro para cada opción de tubing y longitud → criterio de compra.
4. **Ergun**: ΔP acumulada del tren vs. Q, con sensibilidad a ε (compactación) y d_p.
5. **Fluidización**: v_mf vs. v_s operativa (requiere ρ_s) → decide ascendente vs. descendente.
6. **Transferencia de masa en película** (Wilson-Geankoplis, válida para Re_p 0.0015–55, que es exactamente el rango aquí):

   | Q [mL/min] | Re_p | Sh | k_f [m/s] |
   |---|---|---|---|
   | 5 | 0.53 | 22.1 | 4.41e-05 |
   | 10 | 1.06 | 27.8 | 5.56e-05 |
   | 20 | 2.12 | 35.0 | 7.00e-05 |
   | 40 | 4.24 | 44.1 | 8.82e-05 |

   Este es el **uso legítimo del Reynolds en este problema**: no para clasificar régimen, sino para estimar k_f y con ello el número de Biot, que dice si el control es por película o por difusión intrapartícula. Esa es la información que efectivamente sirve para escalar.

7. **Escalamiento**: A = Q_real/v_s, L = v_s·EBCT, masa de material requerida.

---

## 8. Lista de compra — criterios corregidos

| Ítem | Recomendación | Razón |
|---|---|---|
| Tubing cabezal peristáltico | El ID que especifique el fabricante del cabezal para 1–40 mL/min. **No es variable libre.** | Lo fija el cabezal, no el proceso |
| Tubing de transferencia/interconexión | **1/16" (1.6 mm ID) máximo**; 0.8 mm si el fitting lo permite | C-5: volumen muerto |
| Tubing ≥3.2 mm | **Descartar** para esta función | C-5: 61–96 % del V_poro |
| Longitud de líneas | Minimizar; presupuestar ≤2 m totales de interconexión | C-5 |
| Tipo de conector | **Luer LOCK, no luer slip** | Peristáltica = desplazamiento positivo; ante colmatación la presión sube sin límite y el slip se desconecta |
| Material del tubing | Considerar PTFE/FEP en líneas de transferencia | Ver nota abajo |
| Prefiltro | 10–25 µm aguas arriba | M-4 |
| Manómetro / registro ΔP | Sí | M-4 |
| Tamiz | Para fracción 0.3–0.5 mm | M-1 |

**Nota sobre la silicona** (esto es compatibilidad de proceso, no química del material — cae en nuestro alcance): la silicona es **permeable a gases** (entra O₂ → se forman burbujas en el lecho → canalización) y **sorbe compuestos orgánicos hidrofóbicos**. Se mencionó que el contaminante es "algo con cloro"; si se trata de un organoclorado, la silicona lo va a sorber y liberar, sesgando la curva de ruptura. **Esto se resuelve empíricamente sin entrar en la química: correr un blanco de tubing** (C₀ conocido, bombeado por el montaje completo sin columna, midiendo salida). Si hay pérdida, cambiar líneas de transferencia a PTFE/FEP y dejar la silicona sólo en el cabezal.

---

## 9. Preguntas abiertas (bloquean cerrar el diseño)

1. **ρ_s (densidad de partícula) del material** — sin este dato no se puede decidir ascendente vs. descendente (M-3), y es el único parámetro que falta para cerrar la hidráulica.
2. **Largo real de las columnas de 1 cm disponibles** (5, 10, 15 cm) — determina cuántas hacen falta en serie.
3. **¿Cuánto material hay disponible?** El tren recomendado consume 30–65 mL de lecho por corrida. El escalamiento a 1 L/s pide 300–900 L (§4). Es la pregunta que más puede cambiar el alcance del proyecto.
4. **C₀ del contaminante y límite de descarga/norma objetivo** — define el criterio de ruptura (típico 5 % o 10 % de C₀) y con ello la duración de los ensayos.
5. **Modelo/marca del cabezal peristáltico** — para fijar el ID del tubing del cabezal, que no es negociable.
6. **¿El agua real estará disponible en continuo, o hay que almacenarla?** Almacenar agua de riego cambia su composición (sedimentación, actividad biológica) en horas-días, y los ensayos duran 1–17 días (M-5).
