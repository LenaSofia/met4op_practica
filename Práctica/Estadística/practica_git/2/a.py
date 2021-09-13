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


# 2 A. ¿Cuál es la probabilidad de obtener dos dados iguales?

probabilidad_dos_dados_iguales = 0
impares = [1, 3, 5]
pares = [2, 4, 6]

for numero, probabilidad in dado_negro.items():
    if numero in impares:
        probabilidad_dos_dados_iguales += probabilidad * dado_negro_impar_dado_blanco[numero]
    elif numero in pares:
        probabilidad_dos_dados_iguales += probabilidad * dado_negro_par_dado_blanco[numero]

print('La probabilidad de obtener dos dados iguales es de:', probabilidad_dos_dados_iguales)


# Output: La probabilidad de obtener dos dados iguales es de: 0.1325