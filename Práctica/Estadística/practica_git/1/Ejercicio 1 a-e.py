import pprint

# Defino funciones que me pueden servir:

# Esperanza:

def sacar_esperanza(distribución):
    '''Introducis la distribución cuya esperanza querés obtener, se iteran las claves y valores (multiplicandolos) y se suman a la esperanza'''
    esperanza = 0
    for numero, probabilidad in distribución.items():
        esperanza += numero * probabilidad
    return esperanza



# Ejercicio 1 a-e:

dado_negro = {
    1 : 0.4,
    2 : 0.3,
    3 : 0.15,
    4 : 0.075,
    5 : 0.05,
    6 : 0.025
}

dado_blanco = {
    6 : 0.4,
    5 : 0.3,
    4 : 0.15,
    3 : 0.075,
    2 : 0.05,
    1 : 0.025
}




# B. ¿Cuál es la probabilidad de obtener dos dados cuyos números sean consecutivos?

probabilidad_consecutivos = ((dado_negro[1] * dado_blanco[2])
                         + (dado_negro[2] * dado_blanco[1])
                         + (dado_negro[2] * dado_blanco[3])
                         + (dado_negro[3] * dado_blanco[2])
                         + (dado_negro[3] * dado_blanco[4])
                         + (dado_negro[4] * dado_blanco[3])
                         + (dado_negro[4] * dado_blanco[5])
                         + (dado_negro[5] * dado_blanco[4])
                         + (dado_negro[5] * dado_blanco[6])
                         + (dado_negro[6] * dado_blanco[5]))

print('La probabilidad de obtener dos dados cuyos números sean consecutivos es de:', probabilidad_consecutivos)




# B. ¿Cuál es la probabilidad de obtener un número par e impar en una tirada?

probabilidad_par_impar = ((dado_negro[1] * dado_blanco[2]) + (dado_negro[1] * dado_blanco[4]) + (dado_negro[1] * dado_blanco[6])
           + (dado_negro[2] * dado_blanco[1]) + (dado_negro[2] * dado_blanco[3]) + (dado_negro[2] * dado_blanco[5])
           + (dado_negro[3] * dado_blanco[2]) + (dado_negro[3] * dado_blanco[4]) + (dado_negro[3] * dado_blanco[6])
           + (dado_negro[4] * dado_blanco[1]) + (dado_negro[4] * dado_blanco[3]) + (dado_negro[4] * dado_blanco[5])
           + (dado_negro[5] * dado_blanco[2]) + (dado_negro[5] * dado_blanco[4]) + (dado_negro[5] * dado_blanco[6])
           + (dado_negro[6] * dado_blanco[1]) + (dado_negro[6] * dado_blanco[3]) + (dado_negro[6] * dado_blanco[5]))

print('La probabilidad de obtener un número par e impar en una tirada es de:', probabilidad_par_impar)




# C. ¿Cuál es la probabilidad de obtener un 7 como suma de ambos dados?


probabilidad_siete = ((dado_negro[1] * dado_blanco[6])
                         + (dado_negro[2] * dado_blanco[5])
                         + (dado_negro[3] * dado_blanco[4])
                         + (dado_negro[4] * dado_blanco[3])
                         + (dado_negro[5] * dado_blanco[2])
                         + (dado_negro[6] * dado_blanco[1]))

print('La probabilidad de obtener un 7 como suma de ambos dados', probabilidad_siete)




# D. ¿Cual es la esperanza del dado Blanco y del dado Negro?

# Esperanza dado blanco:

esperanza_dado_blanco = 0

for clave, valor in dado_blanco.items():
    esperanza_dado_blanco += clave * valor

print('La esperanza del dado Blanco es de:', esperanza_dado_blanco)

print('La esperanza del dado Blanco sacada con función es:', sacar_esperanza(dado_blanco))




# Esperanza dado negro:

esperanza_dado_negro = 0

for clave, valor in dado_negro.items():
    esperanza_dado_negro += clave * valor

print('La esperanza del dado Negro es de:', esperanza_dado_negro)

print('La esperanza del dado Negro sacada con función es:', sacar_esperanza(dado_negro))




# E. ¿Cuál es la varianza del dado Blanco y del dado Negro?

# Dado blanco

varianza_dado_blanco = 0

for clave, valor in dado_blanco.items():
    varianza_dado_blanco = ((clave - esperanza_dado_blanco)**2) * valor

print('La varianza del dado Blanco es de:', varianza_dado_blanco)


# Dado negro

varianza_dado_negro = 0

for clave, valor in dado_negro.items():
    varianza_dado_negro = (((clave - esperanza_dado_negro)**2) * valor)

print('La varianza del dado Negro es de:', varianza_dado_negro)

