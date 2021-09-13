# Ejercicio 2:

import pprint


# G. ¿Cuál es la esperanza de X?


def sacar_esperanza(distribución):
    '''Introducis la distribución cuya esperanza querés obtener, se iteran las claves y valores (multiplicandolos) y se suman a la esperanza'''
    esperanza = 0
    for numero, probabilidad in distribución.items():
        esperanza += numero * probabilidad
    return esperanza

distribucion_probabilidad_X = {
    0: 0.28125,
    1: 0.3624999999999998,
    4: 0.18374999999999997,
    9: 0.0975,
    16: 0.05500000000000001,
    25: 0.020000000000000004
}

esperanza_X = sacar_esperanza(distribucion_probabilidad_X)
print('La esperanza de X es:', esperanza_X)