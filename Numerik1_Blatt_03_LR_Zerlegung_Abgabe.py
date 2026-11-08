import numpy as np
 
# Aufgabe b) LR-Zerlegung für tridiagonale Matrizen
# Annahme: alle Pivotelemente r[i] sind ungleich null (keine Pivotisierung)
def factorize_lr_tridiagonal(a, b, c):
    n = len(b)
    l = np.zeros(n - 1)
    r = np.zeros(n, dtype=float)
    
    r[0] = b[0]
    for i in range(n - 1):
        l[i] = a[i] / r[i]
        r[i+1] = b[i+1] - l[i] * c[i]
    
    # die obere Nebendiagonale von R ist einfach c
    return l, r, c
 
# Aufgabe c) Lösen des linearen Gleichungssystems Ax = f
def solve_tridiagonal_system(a, b, c, f):
    n = len(f)
    l, r, c = factorize_lr_tridiagonal(a, b, c)
    
    # Vorwärtseinsetzen: L * z = f
    z = np.zeros(n)
    z[0] = f[0]
    for i in range(1, n):
        z[i] = f[i] - l[i-1] * z[i-1]
        
    # Rückwärtseinsetzen: R * x = z
    x = np.zeros(n)
    x[-1] = z[-1] / r[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (z[i] - c[i] * x[i+1]) / r[i]
        
    return x
 
# Aufgabe d) Testen für n = 1000
n = 1000
 
# Hauptdiagonale b
b = np.full(n, 2.0)
b[0] = 1.0
b[-1] = 1.0
 
# Nebendiagonalen a und c
a = np.full(n - 1, -1.0)
a[-1] = 0.0
 
c = np.full(n - 1, -1.0)
c[0] = 0.0
 
# Rechte Seite f wie auf dem Blatt
f = np.full(n, -9.81)
f[0] = 0.0
f[-1] = 0.0
 
# System lösen
x = solve_tridiagonal_system(a, b, c, f)
 
# Residuum Ax - f, ohne die volle Matrix
Ax = b * x
Ax[1:] += a * x[:-1]
Ax[:-1] += c * x[1:]
residuum = np.linalg.norm(Ax - f, ord=np.inf)
 
print(f"Residuum ||Ax - f||_inf: {residuum}")
print(f"Randwerte: x[0] = {x[0]}, x[-1] = {x[-1]}")
 
""" 
Aufgabe e), Aufwand
In jedem Eliminationsschritt i steht unter dem Pivot r_i nur ein Eintrag (a_i),
und in der Pivotzeile rechts vom Pivot auch nur einer (c_i). Deshalb ändert sich
pro Schritt nur ein einziger Eintrag, nämlich r_{i+1}.
Dafür braucht man 1 Division (l_i), 1 Multiplikation und 1 Subtraktion (r_{i+1}).
Bei n-1 Schritten sind das 3(n-1) Operationen, also O(n).
Bei einer vollen Matrix wären es dagegen O(n^3).
"""