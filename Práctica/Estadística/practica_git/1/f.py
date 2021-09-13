# Ejercicio 1

import pprint

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


# F. Se define a X = ((dado_negro+dado_blanco) - 7)^2
# Construya la distribución de probabilidad de X

distribucion_probabilidad_X = {}

for numero_dn, probabilidad_dn in dado_negro.items():

    for numero_db, probabilidad_db in dado_blanco.items():

        if (((numero_dn + numero_db) - 7)**2) in distribucion_probabilidad_X:
            distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
        else:
            distribucion_probabilidad_X[((numero_dn + numero_db) - 7)**2] = probabilidad_dn * probabilidad_db

pprint.pprint(distribucion_probabilidad_X)


# Output :

# {0: 0.28125,
#  1: 0.3624999999999998,
#  4: 0.18374999999999997,
#  9: 0.0975,
#  16: 0.05500000000000001,
#  25: 0.020000000000000004}
