# Ejercicio 2:

import pprint

distribucion_probabilidad_X = {
    0: 0.28125,
    1: 0.3624999999999998,
    4: 0.18374999999999997,
    9: 0.0975,
    16: 0.05500000000000001,
    25: 0.020000000000000004
}

esperanza_X = 3.3549999999999995


# H. ¿Cuál es la Varianza de X?

def sacar_varianza(distribución, esperanza):
    '''Introducis la distribución cuya varianza querés obtener, se iteran las claves y valores '''
    varianza = 0
    for numero, probabilidad in distribución.items():
        varianza += (((numero - esperanza)**2) * probabilidad)
    return varianza

varianza_X = sacar_varianza(distribucion_probabilidad_X, esperanza_X)
print('La varianza de X es:', varianza_X)
