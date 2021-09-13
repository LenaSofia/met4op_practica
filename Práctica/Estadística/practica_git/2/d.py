# Ejercicio 2:

# A = 0.08 ó La probabilidad de obtener dos dados iguales es de: 0.1325

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


# D. ¿Cuál es la esperanza del dado Blanco y del dado Negro?


# Dado negro sólo:

def sacar_esperanza(distribución):
    '''Introducis la distribución cuya esperanza querés obtener, se iteran las claves y valores (multiplicandolos) y se suman a la esperanza'''
    esperanza = 0
    for numero, probabilidad in distribución.items():
        esperanza += numero * probabilidad
    return esperanza

esperanza_dado_negro = sacar_esperanza(dado_negro)
print('La esperanza del dado negro es de', esperanza_dado_negro)



# Dado blanco si dado negro fue par:

esperanza_DB_si_DN_par = sacar_esperanza(dado_negro_par_dado_blanco)
print('Si el dado negro fue par, la esperanza del dado blanco es:', esperanza_DB_si_DN_par)



# Dado blanco si dado negro fue par:

esperanza_DB_si_DN_impar = sacar_esperanza(dado_negro_impar_dado_blanco)
print('Si el dado negro fue impar, la esperanza del dado blanco es:', esperanza_DB_si_DN_impar)




# Esperanza conjunta Dado Blanco

prob_dado_negro_impar = dado_negro[1] + dado_negro[3] + dado_negro[5]

prob_dado_negro_par = dado_negro[2] + dado_negro[4] + dado_negro[6]


esperanza_conjunta_dado_blanco = (esperanza_DB_si_DN_par * prob_dado_negro_par) + (esperanza_DB_si_DN_impar * prob_dado_negro_impar)

print("La esperanza conjunta del dado blanco es de:", esperanza_conjunta_dado_blanco)
