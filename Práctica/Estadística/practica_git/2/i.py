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

dado_negro_par_dado_blanco_pares = {
    2: 0.3,
    4: 0.075,
    6: 0.025
}

dado_negro_impar_dado_blanco_pares = {
    2: 0.05,
    4: 0.15,
    6: 0.4
}


# I. Si el dado blanco obtuvo un número par, ¿Cuál es P(X<=9)?


pares = [2, 4, 6]
impares = [1, 3, 5]

distribucion_probabilidad_X_menor_10 = {}


for numero_dn, probabilidad_dn in dado_negro.items():

    if numero_dn in impares:

        for numero_db, probabilidad_db in dado_negro_impar_dado_blanco_pares.items():

            if (((numero_dn + numero_db) - 7)**2) in distribucion_probabilidad_X_menor_10 and ((((numero_dn + numero_db) - 7)**2) <= 9):
                distribucion_probabilidad_X_menor_10[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db

                print('[', 'dn', numero_dn, 'db', numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=',
                      (probabilidad_dn * probabilidad_db))

            elif ((((numero_dn + numero_db) - 7)**2) <= 9):
                distribucion_probabilidad_X_menor_10[((numero_dn + numero_db) - 7)**2] = probabilidad_dn * probabilidad_db

                print('[', 'dn', numero_dn, 'db', numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=',
                      (probabilidad_dn * probabilidad_db))


    elif numero_dn in pares:

        for numero_db, probabilidad_db in dado_negro_impar_dado_blanco_pares.items():

            if (((numero_dn + numero_db) - 7) ** 2) in distribucion_probabilidad_X_menor_10 and ((((numero_dn + numero_db) - 7)**2) <= 9):
                distribucion_probabilidad_X_menor_10[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db

                print('[', 'dn', numero_dn, 'db', numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=',
                      (probabilidad_dn * probabilidad_db))

            elif ((((numero_dn + numero_db) - 7)**2) <= 9):
                distribucion_probabilidad_X_menor_10[((numero_dn + numero_db) - 7) ** 2] = probabilidad_dn * probabilidad_db

                print('[', 'dn', numero_dn, 'db', numero_db, ']', (((numero_dn + numero_db) - 7) ** 2), '=',
                      (probabilidad_dn * probabilidad_db))

pprint.pprint(distribucion_probabilidad_X_menor_10)

probabilidad_X_menor_10 = sum(distribucion_probabilidad_X_menor_10.values())

print(probabilidad_X_menor_10)