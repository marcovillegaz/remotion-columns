# Marco teórico para el diseño y escalamiento de un sistema de columnas de lecho fijo

**Documento base del proyecto**
Fuente primaria: `docs/Fórmulas relevantes.pdf`
Última revisión: 2026-07-25

---

## Propósito y alcance

El presente documento consolida el marco teórico que sustenta el diseño, la caracterización experimental y el escalamiento de un sistema de columnas de lecho fijo destinado a la remoción de un contaminante presente en agua de regadío. Su objeto es servir como referencia normativa única para las etapas sucesivas del proyecto: dimensionamiento del montaje experimental, adquisición de componentes, ejecución de ensayos de ruptura, ajuste de modelos y proyección a escala de operación.

El desarrollo se organiza en siete cuerpos temáticos —balance de materia, balance de energía mecánica, cinética de adsorción, equilibrio termodinámico, análisis dimensional, transferencia de masa y directrices operativas— seguidos de un compendio de ecuaciones y de un conjunto de observaciones técnicas relativas a la aplicación de dichas expresiones al caso particular bajo estudio.

Las ecuaciones se presentan en su forma general. Las particularizaciones numéricas correspondientes al montaje concreto (columnas de 10 mm de diámetro interno, bomba peristáltica de 1–40 mL/min, material granular de 0.3–1 mm) se encuentran documentadas en `AUDITORIA.md` y no se reproducen aquí.

---

## Nomenclatura

| Símbolo | Significado | Unidades |
|---|---|---|
| $A$ | Área transversal de la columna | m² |
| $C$ | Concentración del contaminante en el fluido | mg/L o mol/m³ |
| $C_0$ | Concentración de entrada del contaminante | mg/L |
| $C_t$ | Concentración de salida en el instante $t$ | mg/L |
| $C_e$ | Concentración en equilibrio en el fluido | mg/L |
| $d_p$ | Diámetro de partícula | m |
| $D$ | Diámetro de la columna | m |
| $D_{ax}$ | Coeficiente de dispersión axial | m²/s |
| $D_m$, $D_{AB}$ | Difusividad molecular del contaminante en el fluido | m²/s |
| $h_f$ | Pérdida de carga | m |
| $H_{total}$ | Altura total del lecho | m |
| $k_f$ | Coeficiente de transferencia de masa externo | m/s |
| $k_{Th}$ | Constante cinética de Thomas | L/(min·mg) |
| $K_F$ | Constante de Freundlich | mg/g·(L/mg)^(1/n) |
| $K_L$ | Constante de Langmuir | L/mg |
| $L$ | Longitud del lecho | m |
| $M$ | Masa total de adsorbente en la columna | g |
| $n$ | Factor de heterogeneidad de Freundlich | adimensional |
| $q$ | Concentración de contaminante adsorbido en el sólido | mg/g o mol/kg |
| $q_e$ | Cantidad adsorbida en equilibrio | mg/g |
| $q_{max}$ | Capacidad máxima de adsorción | mg/g |
| $q_0$ | Capacidad de adsorción en equilibrio (modelo de Thomas) | mg/g |
| $Q$ | Caudal volumétrico | L/min o m³/s |
| $t$ | Tiempo | s |
| $t_b$ | Tiempo de ruptura | s |
| $u$ | Velocidad superficial del fluido ($Q/A$) | m/s |
| $V$ | Volumen de fluido tratado en el tiempo $t$ | L |
| $V_{lecho}$ | Volumen del lecho | m³ |
| $z$ | Posición axial en la columna | m |
| $\varepsilon$ | Porosidad del lecho (fracción vacía) | adimensional |
| $\mu$ | Viscosidad dinámica del fluido | Pa·s |
| $\rho$ | Densidad del fluido | kg/m³ |
| $\rho_p$ | Densidad de la partícula adsorbente | kg/m³ |
| $\tau$ | Tiempo de residencia hidráulico | s |
| $\phi_s$ | Factor de esfericidad de las partículas | adimensional |

---

## 1. Balance de materia en la columna

El balance de materia constituye la ecuación fundamental del sistema. En una columna de lecho fijo describe la variación de la concentración del contaminante en función del tiempo y de la posición axial.

La ecuación general de balance para el adsorbato en un lecho fijo se expresa como:

$$\frac{\partial C}{\partial t} = -u\frac{\partial C}{\partial z} + D_{ax}\frac{\partial^2 C}{\partial z^2} - \frac{(1-\varepsilon)}{\varepsilon}\rho_p\frac{\partial q}{\partial t}$$

Cada término posee un significado físico definido:

- El primer término, $\partial C/\partial t$, representa la **acumulación** de contaminante en la fase fluida.
- El segundo término, $-u\,\partial C/\partial z$, corresponde al **transporte convectivo**, esto es, al arrastre del contaminante por el flujo.
- El tercer término, $D_{ax}\,\partial^2 C/\partial z^2$, describe la **dispersión axial**, entendida como la mezcla difusiva a lo largo del eje de la columna.
- El cuarto término, $-\frac{(1-\varepsilon)}{\varepsilon}\rho_p\,\partial q/\partial t$, cuantifica la **transferencia de masa hacia el sólido**, es decir, la fracción efectivamente adsorbida.

### 1.1 Simplificaciones habituales

La resolución analítica de la ecuación completa resulta impracticable en la mayoría de las aplicaciones, por lo que se recurre a las siguientes hipótesis simplificatorias:

1. **Régimen permanente**: $\partial C/\partial t = 0$, esto es, la concentración no varía con el tiempo.
2. **Dispersión axial despreciable**: $D_{ax} \approx 0$, correspondiente a la idealización de flujo pistón.
3. **Ausencia de reacción química en la fase fluida**: el único fenómeno considerado es la adsorción.

Bajo estas condiciones la ecuación se reduce a:

$$u\frac{\partial C}{\partial z} = -\frac{(1-\varepsilon)}{\varepsilon}\rho_p\frac{\partial q}{\partial t}$$

> **Nota técnica 1.** La segunda hipótesis debe validarse experimentalmente y no asumirse *a priori*. El criterio de validación es el número de Péclet definido en la sección 5: la dispersión axial resulta despreciable únicamente cuando $Pe > 100$. En montajes de escala reducida, la dispersión introducida por el volumen muerto del sistema de conducción puede exceder a la del propio lecho, en cuyo caso la idealización de flujo pistón deja de ser aplicable al conjunto y las curvas experimentales requieren corrección previa mediante un ensayo de trazador en blanco.

---

## 2. Balance de energía mecánica y pérdida de carga

El dimensionamiento de la bomba y de las conducciones exige el cálculo de la caída de presión a través del lecho empacado. La correlación de uso más extendido para este propósito es la **ecuación de Ergun**:

$$\frac{\Delta P}{L} = 150\frac{(1-\varepsilon)^2}{\varepsilon^3}\frac{\mu u}{\phi_s^2 d_p^2} + 1.75\frac{(1-\varepsilon)}{\varepsilon^3}\frac{\rho u^2}{\phi_s d_p}$$

La expresión consta de dos contribuciones de naturaleza distinta:

- El **primer término**, cuyo coeficiente es 150, corresponde a la pérdida por fricción en régimen laminar, dominada por los efectos viscosos.
- El **segundo término**, cuyo coeficiente es 1.75, corresponde a la pérdida asociada a la turbulencia y a los efectos inerciales.

### 2.1 Ecuación de Bernoulli extendida

La carga total del sistema, incluidas las pérdidas por fricción, se determina mediante el balance de energía mecánica:

$$\frac{P_1}{\rho g} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\rho g} + \frac{v_2^2}{2g} + z_2 + h_f$$

donde la pérdida de carga $h_f$ se obtiene directamente de la ecuación de Ergun:

$$h_f = \frac{\Delta P}{\rho g} = \frac{L}{\rho g}\left[150\frac{(1-\varepsilon)^2}{\varepsilon^3}\frac{\mu u}{\phi_s^2 d_p^2} + 1.75\frac{(1-\varepsilon)}{\varepsilon^3}\frac{\rho u^2}{\phi_s d_p}\right]$$

**Aplicación al proyecto.** Este conjunto de ecuaciones permite determinar si la bomba peristáltica seleccionada es capaz de sostener el caudal de diseño sin exceder su capacidad máxima de presión.

> **Nota técnica 2.** La sensibilidad de la ecuación de Ergun a la porosidad es pronunciada: el grupo $(1-\varepsilon)^2/\varepsilon^3$ del término viscoso se incrementa aproximadamente en un factor 3.2 cuando $\varepsilon$ desciende de 0.40 a 0.32. En consecuencia, la caída de presión constituye un indicador temprano de compactación del lecho o de colmatación por sólidos suspendidos, y su registro en el tiempo debe incorporarse al protocolo experimental. Adicionalmente, dado que la bomba peristáltica es un equipo de desplazamiento positivo, ésta no limita la presión de descarga ante una obstrucción progresiva, circunstancia que impone verificar la resistencia mecánica de las conexiones.

---

## 3. Cinética de adsorción y curva de ruptura

El rendimiento de una columna de lecho fijo se describe mediante la **curva de ruptura** (*breakthrough curve*), definida como la concentración de salida en función del tiempo o del volumen tratado. El **tiempo de ruptura** $t_b$ corresponde al instante en que la concentración de salida alcanza un valor límite preestablecido, habitualmente entre el 5 % y el 10 % de la concentración de entrada.

### 3.1 Modelo de Thomas

El modelo de Thomas figura entre los más empleados para la descripción de lechos fijos:

$$\frac{C}{C_0} = \frac{1}{1 + \exp\left(\frac{k_{Th}}{Q}(q_0 M - C_0 V)\right)}$$

Para el ajuste de datos experimentales se recurre a su forma linealizada:

$$\ln\left(\frac{C_0}{C_t} - 1\right) = \frac{k_{Th} q_0 M}{Q} - k_{Th} C_0 t$$

La representación de $\ln(C_0/C_t - 1)$ frente a $t$ produce una recta cuya pendiente permite determinar $k_{Th}$ y cuya ordenada al origen conduce a $q_0$.

**Aplicación al proyecto.** El modelo ajusta satisfactoriamente las curvas de ruptura en columnas de lecho fijo y permite estimar la capacidad de remoción del sistema, así como predecir el instante de saturación de la columna.

> **Nota técnica 3.** Se recomienda expresar la abscisa de las curvas de ruptura en **volúmenes de lecho tratados** (BV) en lugar de tiempo. La variable temporal no es invariante frente al escalamiento, mientras que el número de volúmenes de lecho sí lo es cuando se conservan la velocidad superficial, el EBCT y el diámetro de partícula, lo que convierte a esta representación en la forma directamente transferible a la escala de operación.
>
> Complementariamente, conviene considerar el modelo **BDST** (*Bed Depth Service Time*), que relaciona el tiempo de ruptura con la profundidad del lecho. Dicho modelo entrega de manera directa los parámetros requeridos para el escalamiento y puede alimentarse con datos obtenidos en una única corrida si el montaje contempla puntos de muestreo intermedios a lo largo de un tren de columnas en serie.

---

## 4. Isotermas de adsorción

Las isotermas de adsorción describen la cantidad de contaminante que el adsorbente es capaz de retener en condiciones de equilibrio. Se exponen a continuación los dos modelos de mayor difusión.

### 4.1 Isoterma de Langmuir

El modelo de Langmuir supone adsorción en monocapa sobre sitios energéticamente homogéneos:

$$q_e = \frac{q_{max} K_L C_e}{1 + K_L C_e}$$

Su forma linealizada, empleada para el ajuste de datos, es:

$$\frac{C_e}{q_e} = \frac{1}{q_{max}}C_e + \frac{1}{K_L q_{max}}$$

### 4.2 Isoterma de Freundlich

El modelo de Freundlich, de carácter empírico, supone adsorción en multicapa sobre superficies heterogéneas:

$$q_e = K_F C_e^{1/n}$$

cuya forma linealizada corresponde a:

$$\log q_e = \log K_F + \frac{1}{n}\log C_e$$

El parámetro $n$ constituye un factor de heterogeneidad adimensional.

> **Nota técnica 4.** Los parámetros de equilibrio se determinan en ensayos discontinuos (*batch*) independientes de la operación en columna. Su valor reside en que $q_{max}$ o $K_F$ establecen el límite termodinámico superior de la capacidad del material, frente al cual debe contrastarse la capacidad efectivamente alcanzada en columna ($q_0$ del modelo de Thomas). La discrepancia entre ambos cuantifica el grado de aprovechamiento del lecho y guarda relación directa con la longitud de lecho no utilizada definida en la sección 7.

---

## 5. Números adimensionales y criterios de escalamiento

La transposición entre la escala de laboratorio y la escala de operación exige la conservación de determinados grupos adimensionales. El proyecto involucra ambas direcciones: un *scale-down* para el diseño del montaje experimental representativo, y un *scale-up* posterior hacia la unidad de operación.

### 5.1 Número de Reynolds de partícula

Caracteriza el régimen de flujo en el interior del lecho empacado:

$$Re = \frac{\rho u d_p}{\mu}$$

Los intervalos de clasificación son los siguientes:

| Intervalo | Régimen |
|---|---|
| $Re < 10$ | Flujo laminar (predominio de la viscosidad) |
| $10 < Re < 1000$ | Flujo de transición |
| $Re > 1000$ | Flujo turbulento (predominio de la inercia) |

### 5.2 Número de Péclet

Cuantifica el grado de dispersión axial en la columna:

$$Pe = \frac{uL}{D_{ax}}$$

Un valor $Pe \gg 1$ indica predominio de la convección sobre la difusión, condición asociada al flujo pistón ideal; valores bajos de $Pe$ denotan dispersión axial significativa. Como **regla práctica**, la dispersión axial se considera despreciable cuando $Pe > 100$.

### 5.3 Número de Schmidt

Relaciona la difusión de cantidad de movimiento con la difusión molecular:

$$Sc = \frac{\mu}{\rho D_{AB}}$$

donde $D_{AB}$ denota la difusividad molecular del contaminante en el agua.

### 5.4 Tiempo de residencia hidráulico

Corresponde al tiempo medio de permanencia del fluido en el volumen efectivamente disponible:

$$\tau = \frac{V_{lecho}}{Q} = \frac{\varepsilon \cdot A \cdot L}{Q}$$

siendo $A$ el área transversal de la columna. Debe distinguirse del EBCT definido en la sección 7, el cual no incorpora la porosidad.

> **Nota técnica 5.** El documento fuente consigna que en el trabajo de referencia se obtuvo $Re = 497$, valor clasificado allí como flujo laminar. Bajo el criterio de partícula expuesto en esta misma sección ($10 < Re < 1000$), dicho valor corresponde al **régimen de transición**. Se recomienda verificar tanto el valor como su clasificación contra la fuente original antes de emplearlos como base de diseño.
>
> Debe subrayarse asimismo que el número de Reynolds aquí definido es el de **partícula**, construido sobre $d_p$ y sobre la velocidad superficial, y que sus umbrales (10 / 1000) no guardan relación alguna con los umbrales de transición en conducto cerrado (2300 / 4000). La aplicación de estos últimos al interior de un lecho empacado carece de significado físico.
>
> Por último, la conservación del número de Reynolds no constituye por sí sola un criterio suficiente de similitud para el escalamiento de columnas de adsorción. La equivalencia entre escalas se obtiene manteniendo constantes la **velocidad superficial**, el **EBCT** y el **diámetro de partícula**, escalando por área transversal según $A = Q/u$. El número de Reynolds interviene de forma indirecta, a través de su efecto sobre el coeficiente de transferencia de masa (sección 6).

---

## 6. Transferencia de masa

La velocidad a la que el contaminante se transfiere desde la fase fluida hacia el adsorbente se describe mediante el **coeficiente de transferencia de masa externo** $k_f$.

### 6.1 Número de Sherwood

Constituye el grupo adimensional característico de la transferencia de masa:

$$Sh = \frac{k_f d_p}{D_m}$$

donde $D_m$ es la difusividad molecular del contaminante en el fluido.

### 6.2 Correlaciones aplicables

**Correlación de Wakao-Funazkri**, recomendada para lechos empacados:

$$Sh = 2.0 + 1.1\,Re^{1/3} Sc^{1/3}$$

**Correlación de Wilson-Geankoplis**, propuesta como alternativa:

$$Sh = \frac{1.09}{\varepsilon}Re^{1/3}Sc^{1/3}$$

**Aplicación al proyecto.** Ambas correlaciones permiten estimar el coeficiente de transferencia de masa y, por consiguiente, predecir la velocidad del proceso de adsorción.

> **Nota técnica 6.** La correlación de Wakao-Funazkri incorpora el término asintótico $Sh = 2.0$, correspondiente al límite de difusión pura en un medio estancado, por lo que conserva validez a números de Reynolds muy bajos. La correlación de Wilson-Geankoplis carece de dicho término y su validez se restringe al intervalo $0.0015 < Re < 55$. En sistemas operados a $Re$ de partícula del orden de la unidad, ambas expresiones convergen razonablemente, si bien la primera resulta preferible como estimación conservadora.
>
> El valor de $k_f$ así obtenido adquiere sentido al contrastarse con la resistencia difusiva intrapartícula mediante el número de Biot de materia. Dicho contraste determina si el proceso se encuentra controlado por la película externa —en cuyo caso el caudal es la variable de operación dominante— o por la difusión interna, situación en que la variable determinante pasa a ser el diámetro de partícula.

---

## 7. Directrices operativas de diseño

### 7.1 Tiempo de contacto en lecho vacío (EBCT)

Se define como el cociente entre el volumen del lecho y el caudal tratado, sin considerar la porosidad:

$$EBCT = \frac{V_{lecho}}{Q} = \frac{\pi D^2 L}{4Q}$$

### 7.2 Longitud de lecho no utilizado (LUB)

Corresponde a la porción de la columna que aún no ha alcanzado la saturación en el momento de la ruptura:

$$LUB = \frac{Q \cdot t_b}{A}\left(1 - \frac{C_t}{C_0}\right)$$

La altura total de la columna se relaciona con esta magnitud según:

$$H_{total} = H_{utilizada} + LUB$$

### 7.3 Relación entre diámetro de columna y diámetro de partícula

El criterio geométrico establece que debe mantenerse:

$$\frac{D}{d_p} > 10$$

La razón de este requisito es evitar la **canalización** (*channeling*) del fluido en las paredes de la columna, fenómeno que provoca una ruptura prematura no atribuible a las propiedades del material.

> **Nota técnica 7.** El valor $D/d_p > 10$ constituye el umbral mínimo absoluto. La práctica habitual en el diseño de columnas de laboratorio destinadas a la obtención de parámetros transferibles a escala mayor recomienda $D/d_p \geq 20$, y preferentemente $\geq 30$, con objeto de reducir el efecto de pared a un nivel que no comprometa la interpretación de la curva de ruptura. En montajes de diámetro reducido este criterio suele imponer el tamizado previo del material y la selección de la fracción granulométrica fina.
>
> Análogamente, se recomienda verificar la relación $L/d_p \geq 50$, la cual asegura que la dispersión axial en el lecho permanezca acotada.
>
> Respecto de la expresión de LUB consignada en 7.2, conviene contrastarla con la formulación alternativa $LUB = L\,(1 - t_b/t_s)$, donde $t_s$ es el tiempo estequiométrico obtenido por integración de la curva de ruptura completa. Esta segunda forma se apoya en un balance de masa cerrado y resulta preferible cuando se dispone de la curva íntegra hasta saturación.

---

## 8. Compendio de ecuaciones

| Aplicación | Ecuación | Variable clave |
|---|---|---|
| Balance de materia | $\frac{\partial C}{\partial t} = -u\frac{\partial C}{\partial z} + D_{ax}\frac{\partial^2 C}{\partial z^2} - \frac{(1-\varepsilon)}{\varepsilon}\rho_p\frac{\partial q}{\partial t}$ | $C(z,t)$ |
| Pérdida de carga | $\frac{\Delta P}{L} = 150\frac{(1-\varepsilon)^2}{\varepsilon^3}\frac{\mu u}{\phi_s^2 d_p^2} + 1.75\frac{(1-\varepsilon)}{\varepsilon^3}\frac{\rho u^2}{\phi_s d_p}$ | $\Delta P$ |
| Curva de ruptura | $\frac{C}{C_0} = \frac{1}{1+\exp\left(\frac{k_{Th}}{Q}(q_0 M - C_0 V)\right)}$ | Tiempo de saturación |
| Isoterma de Langmuir | $q_e = \frac{q_{max}K_L C_e}{1+K_L C_e}$ | Capacidad de adsorción |
| Isoterma de Freundlich | $q_e = K_F C_e^{1/n}$ | Capacidad de adsorción |
| Reynolds de partícula | $Re = \frac{\rho u d_p}{\mu}$ | Régimen de flujo |
| Péclet | $Pe = \frac{uL}{D_{ax}}$ | Dispersión axial |
| Tiempo de residencia | $\tau = \frac{\varepsilon A L}{Q}$ | Escala temporal |
| Sherwood (Wakao) | $Sh = 2.0 + 1.1\,Re^{1/3}Sc^{1/3}$ | Transferencia de masa |
| EBCT | $EBCT = \frac{\pi D^2 L}{4Q}$ | Tiempo de contacto |
| LUB | $H_{total} = H_{utilizada} + LUB$ | Altura de columna |

---

## 9. Consideraciones para el desarrollo posterior del proyecto

El marco expuesto cubre la descripción fenomenológica del lecho empacado. Su aplicación al montaje experimental concreto requiere incorporar tres elementos adicionales que no forman parte del documento fuente y que condicionan la validez de los parámetros obtenidos:

**a) Caracterización hidrodinámica del sistema de conducción.** En montajes de escala reducida el volumen muerto asociado a tuberías, conectores y accesorios puede resultar comparable al volumen de poro del lecho. Dado que dicho volumen introduce una dispersión ajena al material, la determinación experimental de la respuesta del sistema mediante ensayo de trazador en ausencia de columna constituye un requisito previo a la interpretación de cualquier curva de ruptura.

**b) Estabilidad mecánica del lecho.** La operación en flujo ascendente exige verificar que la velocidad superficial permanezca por debajo de la velocidad mínima de fluidización, magnitud que depende de la densidad de partícula, del diámetro de partícula y de la porosidad. La fluidización del lecho suprime el frente de adsorción y anula la representatividad del ensayo.

**c) Control de la calidad del afluente.** El empleo de agua real de regadío introduce sólidos suspendidos y actividad biológica susceptibles de colmatar el lecho. En ausencia de pretratamiento y de un control mediante columna testigo, la retención observada no puede atribuirse inequívocamente al mecanismo de adsorción.

El análisis cuantitativo de estos tres aspectos, particularizado al montaje disponible, se encuentra desarrollado en `AUDITORIA.md`.

---

## Trazabilidad documental

Este documento constituye una transposición del material contenido en `docs/Fórmulas relevantes.pdf` a un formato de referencia formal. Se han conservado íntegramente las ecuaciones, definiciones, unidades y criterios del documento original. Las adiciones se limitan a las secciones marcadas como **Nota técnica** y a la sección 9, las cuales recogen precisiones metodológicas derivadas de la revisión de ingeniería de procesos y quedan explícitamente diferenciadas del cuerpo principal.
