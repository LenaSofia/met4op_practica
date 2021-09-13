import pprint

# Ejercicio 1

# I. Si el dado blanco obtuvo un número par, ¿Cuál es P(X<=7)?

# REVISAR

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

prob_dado_negro_par = dado_negro[2] + dado_negro[4] + dado_negro[6]

dado_blanco_par = {
    2: 0.05,
    4: 0.15,
    6: 0.4
}

distribucion_probabilidad_X_menor_8 = {}

for numero_db, probabilidad_db in dado_blanco_par.items():

    for numero_dn, probabilidad_dn in dado_negro.items():

        if (((numero_dn + numero_db) - 7)**2) in distribucion_probabilidad_X_menor_8 and (((numero_dn + numero_db) - 7)**2) <= 7:
            distribucion_probabilidad_X_menor_8[((numero_dn + numero_db) - 7) ** 2] += probabilidad_dn * probabilidad_db
        elif (((numero_dn + numero_db) - 7)**2) <= 7:
            distribucion_probabilidad_X_menor_8[((numero_dn + numero_db) - 7)**2] = probabilidad_dn * probabilidad_db

pprint.pprint(distribucion_probabilidad_X_menor_8)

probabilidad_X_menor_8 = sum(distribucion_probabilidad_X_menor_8.values())

print("La probabilidad de que X sea <= 7 es de:", probabilidad_X_menor_8)

# Output: 0.50125