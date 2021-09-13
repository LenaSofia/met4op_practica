import pprint

# Ejercicio 1 f-i:

dado_negro = {
    1: 0.4,
    2: 0.3,
    3: 0.15,
    4: 0.075,
    5: 0.05,
    6: 0.025
}

dado_blanco = {
    1: 0.025,
    2: 0.05,
    3: 0.075,
    4: 0.15,
    5: 0.3,
    6: 0.4
}




# F. Si se define a X = ((dado_negro+dado_blanco) - 7)^2, construya la distribución de probabilidad de X

distribucion_probabilidad_X = {}


for numero_dn, probabilidad_dn in dado_negro.items():

    for numero_db, probabilidad_db in dado_blanco.items():

        if (((numero_dn + numero_db) - 7)**2) in distribucion_probabilidad_X:
            distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
        else:
            distribucion_probabilidad_X[((numero_dn + numero_db) - 7)**2] = probabilidad_dn * probabilidad_db

pprint.pprint(distribucion_probabilidad_X)




# G. ¿Cuál es la esperanza de X?

def sacar_esperanza(distribución):
    '''Introducis la distribución cuya esperanza querés obtener, se iteran las claves y valores (multiplicandolos) y se suman a la esperanza'''
    esperanza = 0
    for numero, probabilidad in distribución.items():
        esperanza += numero * probabilidad
    return esperanza

esperanza_de_X = sacar_esperanza(distribucion_probabilidad_X)
print('La esperanza de la distribución X es', esperanza_de_X)




# H. ¿Cuál es la varianza de X?

def sacar_varianza(distribución, esperanza):
    '''Introducis la distribución cuya varianza querés obtener, se iteran las claves y valores '''
    varianza = 0
    for numero, probabilidad in distribución.items():
        varianza += (((numero - esperanza)**2) * probabilidad)
    return varianza

varianza_de_X = sacar_varianza(distribucion_probabilidad_X, esperanza_de_X)

print('La varianza de X es', varianza_de_X)




# I. Si el dado blanco obtuvo un número par, ¿Cuál es P(X<=7)?

