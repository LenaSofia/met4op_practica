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



# Esperanzas:

esperanza_dado_negro = 2.15

esperanza_DB_si_DN_impar = 4.85

esperanza_DB_si_DN_par = 2.15

esperanza_conjunta_dado_blanco = 3.77



# 2. E) ¿Cuál es la varianza del dado Blanco y del dado Negro?



# Varianza dado negro

def sacar_varianza(distribución, esperanza):
    '''Introducis la distribución cuya varianza querés obtener, se iteran las claves y valores '''
    varianza = 0
    for numero, probabilidad in distribución.items():
        varianza += (((numero - esperanza)**2) * probabilidad)
    return varianza

varianza_DN = sacar_varianza(dado_negro, esperanza_dado_negro)

print('La varianza del dado negro es', varianza_DN)



# Varianza dado blanco si dado negro es par

varianza_DB_si_DN_par = sacar_varianza(dado_negro_par_dado_blanco, esperanza_DB_si_DN_par)
print('Si el dado negro es par, la varianza del dado blanco es:', varianza_DB_si_DN_par)



# Varianza dado blanco si dado negro es impar

varianza_DB_si_DN_impar = sacar_varianza(dado_negro_impar_dado_blanco, esperanza_DB_si_DN_impar)
print('Si el dado negro es impar, la varianza del dado blanco es:', varianza_DB_si_DN_impar)



# Varianza conjunta dado bñlanco, ¿tendría que marginalizar?

prob_dado_negro_impar = dado_negro[1] + dado_negro[3] + dado_negro[5]

prob_dado_negro_par = dado_negro[2] + dado_negro[4] + dado_negro[6]


varianza_conjunta_dado_blanco = (varianza_DB_si_DN_par * prob_dado_negro_par) + (varianza_DB_si_DN_impar * prob_dado_negro_impar)

print("La varianza conjunta del dado blanco es:", varianza_conjunta_dado_blanco)