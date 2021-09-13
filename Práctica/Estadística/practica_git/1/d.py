# Ejercicio 1

dado_negro = {
    1 : 0.4,
    2 : 0.3,
    3 : 0.15,
    4 : 0.075,
    5 : 0.05,
    6 : 0.025
}

dado_blanco = {
    1 : 0.025,
    2 : 0.05,
    3 : 0.075,
    4 : 0.15,
    5 : 0.3,
    6 : 0.4
}

# D. ¿Cual es la esperanza del dado Blanco y del dado Negro?


def sacar_esperanza(distribución):
    '''Introducis la distribución cuya esperanza querés obtener, se iteran las claves y valores (multiplicandolos) y se suman a la esperanza'''
    esperanza = 0
    for numero, probabilidad in distribución.items():
        esperanza += numero * probabilidad
    return esperanza


# Esperanza dado negro

esperanza_dado_negro = sacar_esperanza(dado_negro)

print("La esperanza del dado negro es:", esperanza_dado_negro)




# Esperanza dado blanco

esperanza_dado_blanco = sacar_esperanza(dado_blanco)

print("La esperanza del dado blanco es:", esperanza_dado_blanco)