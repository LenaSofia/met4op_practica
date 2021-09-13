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

            print('[', 'dn', numero_dn, 'db', numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=', (probabilidad_dn * probabilidad_db))

    elif numero_dn in pares:
        for numero_db, probabilidad_db in dado_negro_impar_dado_blanco.items():
            if (((numero_dn + numero_db) - 7) ** 2) in distribucion_probabilidad_X:
                distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
            else:
                distribucion_probabilidad_X[((numero_dn + numero_db) - 7) ** 2] = probabilidad_dn * probabilidad_db

            print('[', 'dn', numero_dn, 'db', numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=', (probabilidad_dn * probabilidad_db))

pprint.pprint(distribucion_probabilidad_X)
