"""
SCRIPT PARA DISEÑO DE COLUMNAS DE ADSORCIÓN
Muestra todos los cálculos en formato de tabla con la fórmula utilizada.
"""
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PARÁMETROS DEL SISTEMA (MODIFICAR SEGÚN PROYECTO)
# ============================================================
rho = 1000.0          # densidad [kg/m³]
mu = 0.001            # viscosidad dinámica [Pa·s]
epsilon = 0.4         # porosidad
phi_s = 0.8           # esfericidad
dp = 0.001            # diámetro de partícula [m]
L = 0.3               # altura de columna [m]
D_col = 0.02          # diámetro de columna [m]
A = np.pi * (D_col/2)**2
Q = 0.01           # caudal [m³/s]
u = Q / A             # velocidad superficial [m/s]
C0 = 10.0             # concentración entrada [mg/L]
q0 = 50.0             # capacidad de adsorción [mg/g]
M = 50.0              # masa adsorbente [g]
k_Th = 0.001          # constante Thomas [L/(min·mg)]
D_AB = 1e-9           # difusividad molecular [m²/s]
q_max = 100.0         # Langmuir
K_L = 0.05
K_F = 10.0
n = 2.0

# ============================================================
# FUNCIONES DE CÁLCULO
# ============================================================
def ergun(u, dp, epsilon, phi_s, rho, mu, L):
    term1 = 150 * (1 - epsilon)**2 / (epsilon**3) * (mu * u) / (phi_s**2 * dp**2)
    term2 = 1.75 * (1 - epsilon) / (epsilon**3) * (rho * u**2) / (phi_s * dp)
    return (term1 + term2) * L

def thomas(t, C0, Q, q0, M, k_Th):
    V = Q * t
    exponente = (k_Th / Q) * (q0 * M - C0 * V)
    return C0 / (1 + np.exp(exponente))

def langmuir(Ce, q_max, K_L):
    return (q_max * K_L * Ce) / (1 + K_L * Ce)

def freundlich(Ce, K_F, n):
    return K_F * Ce ** (1/n)

def reynolds(u, dp, rho, mu):
    return rho * u * dp / mu

def schmidt(mu, rho, D_AB):
    return mu / (rho * D_AB)

def peclet(u, L, D_ax):
    return u * L / D_ax

def sherwood_wakao(Re, Sc):
    return 2.0 + 1.1 * Re**(1/3) * Sc**(1/3)

def tiempo_residencia(epsilon, A, L, Q):
    return epsilon * A * L / Q

def ebct(D_col, L, Q):
    V_lecho = np.pi * (D_col/2)**2 * L
    return V_lecho / Q

# ============================================================
# FUNCIONES PARA MOSTRAR TABLAS CON FÓRMULAS Y RESULTADOS
# ============================================================
def mostrar_tabla(titulo, encabezados, filas, formula=""):
    """Imprime una tabla formateada con los datos."""
    print("\n" + "="*80)
    print(f" {titulo}")
    print("="*80)
    if formula:
        print(f"Fórmula: {formula}")
        print("-"*80)
    # Calcular anchos de columna
    col_widths = [max(len(str(item)) for item in col) for col in zip(*([encabezados] + filas))]
    # Imprimir encabezados
    header_line = " | ".join(f"{encabezados[i]:<{col_widths[i]}}" for i in range(len(encabezados)))
    print(header_line)
    print("-"*len(header_line))
    # Imprimir filas
    for fila in filas:
        line = " | ".join(f"{str(fila[i]):<{col_widths[i]}}" for i in range(len(fila)))
        print(line)
    print("="*80)
    input("Presiona Enter para continuar...")

def mostrar_balance():
    titulo = "1. BALANCE DE MATERIA EN LA COLUMNA"
    formula = "∂C/∂t = -u·∂C/∂z + D_ax·∂²C/∂z² - (1-ε)/ε · ρ_p · ∂q/∂t"
    encabezados = ["Parámetro", "Valor", "Unidades"]
    filas = [
        ["Velocidad superficial u", f"{u:.6f}", "m/s"],
        ["Porosidad ε", f"{epsilon:.2f}", "-"],
        ["Concentración entrada C₀", f"{C0:.2f}", "mg/L"],
        ["Nota", "Se requiere ∂q/∂t (cinética)", "-"]
    ]
    mostrar_tabla(titulo, encabezados, filas, formula)

def mostrar_ergun():
    deltaP = ergun(u, dp, epsilon, phi_s, rho, mu, L)
    titulo = "2. ECUACIÓN DE ERGUN (PÉRDIDA DE CARGA)"
    formula = "ΔP/L = 150·(1-ε)²/ε³ · μ·u/(φₛ²·dₚ²) + 1.75·(1-ε)/ε³ · ρ·u²/(φₛ·dₚ)"
    encabezados = ["Parámetro", "Valor", "Unidades"]
    filas = [
        ["Porosidad ε", f"{epsilon:.2f}", "-"],
        ["Esfericidad φₛ", f"{phi_s:.2f}", "-"],
        ["Diámetro partícula dₚ", f"{dp*1000:.2f}", "mm"],
        ["Velocidad u", f"{u:.6f}", "m/s"],
        ["Longitud L", f"{L*100:.1f}", "cm"],
        ["Densidad ρ", f"{rho:.1f}", "kg/m³"],
        ["Viscosidad μ", f"{mu:.4f}", "Pa·s"],
        ["Caída de presión ΔP", f"{deltaP:.4f}", "Pa"],
        ["ΔP/L", f"{deltaP/L:.4f}", "Pa/m"]
    ]
    mostrar_tabla(titulo, encabezados, filas, formula)

def mostrar_thomas():
    t = 60  # minutos
    Q_Lmin = Q * 60 * 1000  # L/min
    Ct = thomas(t, C0, Q_Lmin, q0, M, k_Th)
    titulo = "3. MODELO DE THOMAS (CURVA DE RUPTURA)"
    formula = "C_t/C₀ = 1 / [1 + exp((k_Th/Q)·(q₀·M - C₀·V))]"
    encabezados = ["Parámetro", "Valor", "Unidades"]
    filas = [
        ["Concentración entrada C₀", f"{C0:.2f}", "mg/L"],
        ["Caudal Q", f"{Q_Lmin:.4f}", "L/min"],
        ["Constante Thomas k_Th", f"{k_Th:.4f}", "L/(min·mg)"],
        ["Capacidad q₀", f"{q0:.2f}", "mg/g"],
        ["Masa adsorbente M", f"{M:.2f}", "g"],
        ["Tiempo t (ejemplo)", f"{t}", "min"],
        ["Volumen tratado V", f"{Q_Lmin*t:.2f}", "L"],
        ["Concentración salida C_t", f"{Ct:.4f}", "mg/L"],
        ["Relación C_t/C₀", f"{Ct/C0:.4f}", "-"]
    ]
    mostrar_tabla(titulo, encabezados, filas, formula)

def mostrar_isotermas():
    Ce = 5.0  # ejemplo
    q_L = langmuir(Ce, q_max, K_L)
    q_F = freundlich(Ce, K_F, n)
    titulo = "4. ISOTERMAS DE ADSORCIÓN"
    formula = "Langmuir: q_e = (q_max·K_L·C_e)/(1+K_L·C_e)  |  Freundlich: q_e = K_F·C_e^(1/n)"
    encabezados = ["Modelo", "Parámetro", "Valor", "Unidades"]
    filas = [
        ["Langmuir", "q_max", f"{q_max:.2f}", "mg/g"],
        ["Langmuir", "K_L", f"{K_L:.3f}", "L/mg"],
        ["Langmuir", f"q_e (Ce={Ce})", f"{q_L:.2f}", "mg/g"],
        ["Freundlich", "K_F", f"{K_F:.2f}", "mg/g·(L/mg)^(1/n)"],
        ["Freundlich", "n", f"{n:.2f}", "-"],
        ["Freundlich", f"q_e (Ce={Ce})", f"{q_F:.2f}", "mg/g"]
    ]
    mostrar_tabla(titulo, encabezados, filas, formula)

def mostrar_adimensionales():
    Re = reynolds(u, dp, rho, mu)
    Sc = schmidt(mu, rho, D_AB)
    Pe = peclet(u, L, D_AB)
    Sh_wakao = sherwood_wakao(Re, Sc)
    titulo = "5. NÚMEROS ADIMENSIONALES"
    formula = "Re=ρ·u·dₚ/μ, Sc=μ/(ρ·D_AB), Pe=u·L/D_ax, Sh=2.0+1.1·Re^(1/3)·Sc^(1/3)"
    encabezados = ["Número", "Valor", "Interpretación"]
    filas = [
        ["Reynolds (Re)", f"{Re:.2f}", "LAMINAR" if Re<10 else "TRANSICIÓN" if Re<1000 else "TURBULENTO"],
        ["Schmidt (Sc)", f"{Sc:.2f}", "-"],
        ["Péclet (Pe)", f"{Pe:.2e}", "Dispersión axial despreciable" if Pe>100 else "Dispersión significativa"],
        ["Sherwood (Wakao)", f"{Sh_wakao:.2f}", "-"]
    ]
    mostrar_tabla(titulo, encabezados, filas, formula)

def mostrar_directrices():
    tau = tiempo_residencia(epsilon, A, L, Q)
    EBCT_val = ebct(D_col, L, Q)
    t_b = 120
    Ct = thomas(t_b, C0, Q*60*1000, q0, M, k_Th)
    LUB_val = (Q*60*1000 * t_b) / A * (1 - Ct/C0)
    relacion = D_col / dp
    titulo = "6. DIRECTRICES OPERATIVAS DE DISEÑO"
    formula = "τ=ε·A·L/Q, EBCT=V_lecho/Q, LUB=(Q·t_b)/A·(1-C_t/C₀), D_col/dₚ>10"
    encabezados = ["Parámetro", "Valor", "Unidades", "Observación"]
    filas = [
        ["Tiempo residencia τ", f"{tau:.2f}", "s", "-"],
        ["EBCT", f"{EBCT_val:.2f}", "s", "-"],
        ["LUB", f"{LUB_val:.4f}", "m", f"({LUB_val*100:.2f} cm)"],
        ["Relación D_col/dₚ", f"{relacion:.1f}", "-", "Válido" if relacion>10 else "Precaución: canalización"]
    ]
    mostrar_tabla(titulo, encabezados, filas, formula)

# ============================================================
# GRÁFICOS
# ============================================================
def graficar_reynolds():
    u_range = np.linspace(0.001, 0.1, 50)
    dp_range = np.linspace(0.0001, 0.01, 50)
    U, DP = np.meshgrid(u_range, dp_range)
    Re = rho * U * DP / mu
    plt.figure(figsize=(10,6))
    contourf = plt.contourf(U, DP, Re, levels=50, cmap='viridis')
    plt.colorbar(contourf, label='Re')
    levels = [10, 100, 1000, 10000]
    contour = plt.contour(U, DP, Re, levels=levels, colors='black')
    plt.clabel(contour, inline=True, fmt='%d')
    plt.plot(u, dp, 'ro', label=f'Operación Re={reynolds(u,dp,rho,mu):.1f}')
    plt.legend()
    plt.xlabel('u [m/s]')
    plt.ylabel('dₚ [m]')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Curvas de nivel de Reynolds')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_ruptura():
    t = np.linspace(0, 600, 100)
    Ct = thomas(t, C0, Q*60*1000, q0, M, k_Th)
    plt.figure(figsize=(10,6))
    plt.plot(t/60, Ct/C0, 'b-', label='Thomas')
    plt.axhline(0.05, color='r', linestyle='--', label='Ruptura 5%')
    plt.axhline(0.10, color='orange', linestyle='--', label='Ruptura 10%')
    plt.xlabel('Tiempo [h]')
    plt.ylabel('C_t/C₀')
    plt.title('Curva de Ruptura')
    plt.grid(True)
    plt.legend()
    plt.show()

def graficar_isotermas():
    Ce = np.linspace(0, 1000, 10000, 100000)
    q_L = langmuir(Ce, q_max, K_L)
    q_F = freundlich(Ce, K_F, n)
    plt.figure(figsize=(10,6))
    plt.plot(Ce, q_L, 'b-', label='Langmuir')
    plt.plot(Ce, q_F, 'r--', label='Freundlich')
    plt.xlabel('C_e [mg/L]')
    plt.ylabel('q_e [mg/g]')
    plt.title('Isotermas de Adsorción')
    plt.grid(True)
    plt.legend()
    plt.show()

# ============================================================
# MENÚ PRINCIPAL
# ============================================================
def menu():
    while True:
        print("\n" + "="*50)
        print("     CÁLCULOS PARA COLUMNA DE ADSORCIÓN")
        print("="*50)
        print("1.  Balance de materia")
        print("2.  Ecuación de Ergun (pérdida de carga)")
        print("3.  Modelo de Thomas (curva de ruptura)")
        print("4.  Isotermas de adsorción")
        print("5.  Números adimensionales")
        print("6.  Directrices operativas de diseño")
        print("7.  Gráfico: Curvas de nivel de Reynolds")
        print("8.  Gráfico: Curva de ruptura")
        print("9.  Gráfico: Isotermas de adsorción")
        print("10. Mostrar TODO el resumen completo")
        print("11. Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción (1-11): ")
        
        if opcion == '1':
            mostrar_balance()
        elif opcion == '2':
            mostrar_ergun()
        elif opcion == '3':
            mostrar_thomas()
        elif opcion == '4':
            mostrar_isotermas()
        elif opcion == '5':
            mostrar_adimensionales()
        elif opcion == '6':
            mostrar_directrices()
        elif opcion == '7':
            graficar_reynolds()
        elif opcion == '8':
            graficar_ruptura()
        elif opcion == '9':
            graficar_isotermas()
        elif opcion == '10':
            mostrar_balance()
            mostrar_ergun()
            mostrar_thomas()
            mostrar_isotermas()
            mostrar_adimensionales()
            mostrar_directrices()
        elif opcion == '11':
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()