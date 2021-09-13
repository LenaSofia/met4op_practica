# Ejercicio 1

dado_negro = {
    1 : 0.4,
    2 : 0.3,
    3 : 0.15,
    4 : 0.075,
    5 : 0.05,
    6 : 0.025
}

esperanza_dado_negro = 2.15


dado_blanco = {
    6 : 0.4,
    5 : 0.3,
    4 : 0.15,
    3 : 0.075,
    2 : 0.05,
    1 : 0.025
}

esperanza_dado_blanco = 4.85


# E. ¿Cuál es la varianza del dado Blanco y del dado Negro?

def sacar_varianza(distribución, esperanza):
    '''Introducis la distribución cuya varianza querés obtener, se iteran las claves y valores aplicando la fórmula ((x - esperanza)**2) * p(x) para obtener la varianza'''
    varianza = 0
    for numero, probabilidad in distribución.items():
        varianza += (((numero - esperanza)**2) * probabilidad)
    return varianza


# Varianza dado negro:

varianza_dado_negro = sacar_varianza(dado_negro, esperanza_dado_negro)

print("La varianza del dado negro es:", varianza_dado_negro)


# Varianza dado blanco:

varianza_dado_blanco = sacar_varianza(dado_blanco, esperanza_dado_blanco)

print("La varianza del dado blanco es:", varianza_dado_blanco)