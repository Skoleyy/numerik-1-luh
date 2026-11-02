import math

def approximierte_kondition_asin(x, p):
    # Umwandlung in prozentuale Abweichung 
    p = p * 0.01
    
    # Absolute Eingabestörung Delta x
    fehler_x = x * p
    
    # Gestörter Eingangswert
    x_gestoert = x + fehler_x
    
    # Exakter und gestörter Funktionswert
    y = math.asin(x)
    y_gestoert = math.asin(x_gestoert)
    
    # Absoluter Ausgangsfehler Delta y
    fehler_y = abs(y_gestoert - y)
    
    # Absolute Konditionszahl: Delta y / Delta x
    k_abs = fehler_y / fehler_x
    
    # Relativer Eingangsfehler (delta x) und Ausgangsfehler (delta y)
    delta_x = fehler_x / abs(x)
    delta_y = fehler_y / abs(y)
    
    # Relative Konditionszahl: delta y / delta x
    k_rel = delta_y / delta_x
    
    # Rückgabe
    return [x, delta_x, k_abs, k_rel]

# Testaufrufe aus Teil (b)
print(approximierte_kondition_asin(0.99, 1))
print(approximierte_kondition_asin(0.999, 0.1))

def bitfolge_N(z):
    if z == 0:
        return "0"
    bitfolge = ""
    while z > 0:
        bit = z % 2
        bitfolge = str(bit) + bitfolge
        z = z // 2
    
    return bitfolge


print(bitfolge_N(96))
print(bitfolge_N(348))