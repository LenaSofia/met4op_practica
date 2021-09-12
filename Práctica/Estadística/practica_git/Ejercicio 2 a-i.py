# Ejercicio 2:

# A = 0.08

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
print(probabilidad_obtener_7)


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




# 2. D) ESPERANZA de Dado Negro Y Dado Blanco

# No sé




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




# F. Si se define a X = ((dado_negro+dado_blanco) - 7)^2, construya la distribución de probabilidad de X

pares = [2, 4, 6]
impares = [1, 3, 5]

distribucion_probabilidad_X = {}


for numero_dn, probabilidad_dn in dado_negro.items():

    if numero_dn in impares:
        for numero_db, probabilidad_db in dado_negro_impar_dado_blanco.items():
            if (((numero_dn + numero_db) - 7)**2) in distribucion_probabilidad_X:
                distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
            else:
                distribucion_probabilidad_X[((numero_dn + numero_db) - 7)**2] = probabilidad_dn * probabilidad_db

            print('[', numero_dn, numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=', (probabilidad_dn * probabilidad_db))

    elif numero_dn in pares:
        for numero_db, probabilidad_db in dado_negro_impar_dado_blanco.items():
            if (((numero_dn + numero_db) - 7) ** 2) in distribucion_probabilidad_X:
                distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
            else:
                distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] = probabilidad_dn * probabilidad_db

            print('[', numero_dn, numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=', (probabilidad_dn * probabilidad_db))

pprint.pprint(distribucion_probabilidad_X)




# G. ¿Cuál es la esperanza de X?

esperanza_X = sacar_esperanza(distribucion_probabilidad_X)
print('La esperanza de X es:', esperanza_X)




# H. ¿Cuál es la Varianza de X?

varianza_X = sacar_varianza(distribucion_probabilidad_X, esperanza_X)
print('La varianza de X es:', varianza_X)




# I. Si el dado blanco obtuvo un número par, ¿Cuál es P(X<=9)?

distribucion_probabilidad_X = {}


for numero_dn, probabilidad_dn in dado_negro.items():

    if numero_dn in impares:
        for numero_db, probabilidad_db in dado_negro_impar_dado_blanco.items():
            if numero_db in pares:
                if (((numero_dn + numero_db) - 7)**2) in distribucion_probabilidad_X:
                    distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
                else:
                    distribucion_probabilidad_X[((numero_dn + numero_db) - 7)**2] = probabilidad_dn * probabilidad_db

    elif numero_dn in pares:
        for numero_db, probabilidad_db in dado_negro_impar_dado_blanco.items():
            if numero_db in pares:
                if (((numero_dn + numero_db) - 7) ** 2) in distribucion_probabilidad_X:
                    distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
                else:
                    distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] = probabilidad_dn * probabilidad_db

pprint.pprint(distribucion_probabilidad_X)

promedio_X_menor_igual_9 = 0

for numero, probabilidad in distribucion_probabilidad_X.items():
    if numero <= 9:
        promedio_X_menor_igual_9 += probabilidad

print(promedio_X_menor_igual_9)

# Me da 0.55
