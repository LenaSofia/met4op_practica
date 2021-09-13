# Ejercicio 1

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


# C. ¿Cuál es la probabilidad de obtener un 7?

probabilidad_siete = ((dado_negro[1] * dado_blanco[6])
                         + (dado_negro[2] * dado_blanco[5])
                         + (dado_negro[3] * dado_blanco[4])
                         + (dado_negro[4] * dado_blanco[3])
                         + (dado_negro[5] * dado_blanco[2])
                         + (dado_negro[6] * dado_blanco[1]))

print('La probabilidad de obtener un 7 como suma de ambos dados', probabilidad_siete)