# Ejercicio 2:

import pprint

dado_negro = {
    1: 0.4,
    2: 0.3,
    3: 0.15,
    4: 0.075,
    5: 0.05,
    6: 0.025
}

dado_negro_par_dado_blanco = {
    1: 0.4,
    2: 0.3,
    3: 0.15,
    4: 0.075,
    5: 0.05,
    6: 0.025
}

dado_negro_impar_dado_blanco = {
    1: 0.025,
    2: 0.05,
    3: 0.075,
    4: 0.15,
    5: 0.3,
    6: 0.4
}




# 2 C) Probabilidad de obtener un 7


def obtener_probabilidad_par_impar_DB_dependiente_DN(dado_negro, DN_par_DB, DN_impar_DB, numero):
    '''Ingreso como parámetros diccionario dado negro, diccionario dado blanco con dado negro par, diccionario
    dado blanco con dado negro impar y el número cuya probabilidad quiero obtener. Devuelve la probabilidad
    de obtener ese número'''

    probabilidad_obtener_numero = 0

    impares = [1, 3, 5]
    pares = [2, 4, 6]

    for numero_DN, probabilidad_DN in dado_negro.items():

        if numero_DN in impares:
            for numero_DB, probabilidad_DB in DN_impar_DB.items():
                if (numero_DN + numero_DB) == numero:
                    probabilidad_obtener_numero += probabilidad_DN * probabilidad_DB

        elif numero_DN in pares:
            for numero_DB, probabilidad_DB in DN_par_DB.items():
                if (numero_DN + numero_DB) == numero:
                    probabilidad_obtener_numero += probabilidad_DN * probabilidad_DB

    return probabilidad_obtener_numero

probabilidad_obtener_7 = obtener_probabilidad_par_impar_DB_dependiente_DN(dado_negro,dado_negro_par_dado_blanco,dado_negro_impar_dado_blanco,7)

print("La probabilidad de obtener un 7 es de:", probabilidad_obtener_7)
