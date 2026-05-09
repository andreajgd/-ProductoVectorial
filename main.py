import numpy as np

# -----------------------------
# Producto vectorial manual
# -----------------------------
def producto_vectorial(a, b):
    """
    Calcula a x b para vectores 3D.
    a y b deben ser listas, tuplas o arrays de 3 componentes.
    """
    a1, a2, a3 = a
    b1, b2, b3 = b

    return np.array([
        a2*b3 - a3*b2,
        -(a1*b3 - a3*b1),
        a1*b2 - a2*b1
    ], dtype=float)


# -----------------------------
# Fuerza magnética sobre carga
# F = q(v x B)
# -----------------------------
def fuerza_sobre_carga(q, v, B):
    """
    q: carga en coulomb [C]
    v: velocidad en m/s
    B: campo magnético en tesla [T]
    """
    return q * producto_vectorial(v, B)


# -----------------------------
# Fuerza magnética sobre conductor
# F = I(L x B)
# -----------------------------
def fuerza_sobre_conductor(I, P, Q, B):
    """
    I: corriente en amperios [A]
    P: punto inicial del conductor
    Q: punto final del conductor
    B: campo magnético en tesla [T]

    L = Q - P
    """
    P = np.array(P, dtype=float)
    Q = np.array(Q, dtype=float)

    L = Q - P
    F = I * producto_vectorial(L, B)

    return F, L


def mostrar_vector(nombre, vector, unidad="N"):
    magnitud = np.linalg.norm(vector)
    print(f"{nombre} = <{vector[0]:.4g}, {vector[1]:.4g}, {vector[2]:.4g}> {unidad}")
    print(f"|{nombre}| = {magnitud:.4g} {unidad}")


# =====================================================
# ESCENARIO 1
# q = -10 μC
# v = <2, -3, 0.5> x 10^3 m/s
# B = <-1, 0.8, -3> T
# =====================================================

q = -10e-6
v = np.array([2, -3, 0.5]) * 1e3
B = np.array([-1, 0.8, -3])

F1 = fuerza_sobre_carga(q, v, B)

print("ESCENARIO 1")
mostrar_vector("F", F1)


# =====================================================
# ESCENARIO 2
# P = (-7, 4, 5)
# Q = (8, 0, -4)
# I = 20 A
# B = <0.8, 4, -2> T
# =====================================================

P = [-7, 4, 5]
Q = [8, 0, -4]
I = 20
B = [0.8, 4, -2]

F2, L = fuerza_sobre_conductor(I, P, Q, B)

print("\nESCENARIO 2")
mostrar_vector("L", L, "m")
mostrar_vector("F", F2)