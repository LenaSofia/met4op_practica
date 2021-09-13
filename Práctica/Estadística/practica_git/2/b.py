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


# B. ¿Cuál es la probabilidad de obtener dos dados cuyos números sean consecutivos?

# No sé si está bien porque acá estoy multiplicando directamente uno por otro, pero no estoy usando probabilidad condicional ni marginal

probabilidad_consecutivos = ((dado_negro[1] * dado_negro_impar_dado_blanco[2])
                         + (dado_negro[2] * dado_negro_par_dado_blanco[1])
                         + (dado_negro[2] * dado_negro_par_dado_blanco[3])
                         + (dado_negro[3] * dado_negro_impar_dado_blanco[2])
                         + (dado_negro[3] * dado_negro_impar_dado_blanco[4])
                         + (dado_negro[4] * dado_negro_par_dado_blanco[3])
                         + (dado_negro[4] * dado_negro_par_dado_blanco[5])
                         + (dado_negro[5] * dado_negro_impar_dado_blanco[4])
                         + (dado_negro[5] * dado_negro_impar_dado_blanco[6])
                         + (dado_negro[6] * dado_negro_par_dado_blanco[5]))

print('La probabilidad de obtener dos dados cuyos números sean consecutivos es de:', probabilidad_consecutivos)





# B. ¿Cual es la probabilidad de obtener un número par e impar en una tirada?

# No sé si está bien porque acá estoy multiplicando directamente uno por otro, pero no estoy usando probabilidad condicional ni marginal

probabilidad_par_impar = ((dado_negro[1] * dado_negro_impar_dado_blanco[2]) + (dado_negro[1] * dado_negro_impar_dado_blanco[4]) + (dado_negro[1] * dado_negro_impar_dado_blanco[6])
           + (dado_negro[2] * dado_negro_par_dado_blanco[1]) + (dado_negro[2] * dado_negro_par_dado_blanco[3]) + (dado_negro[2] * dado_negro_par_dado_blanco[5])
           + (dado_negro[3] * dado_negro_impar_dado_blanco[2]) + (dado_negro[3] * dado_negro_impar_dado_blanco[4]) + (dado_negro[3] * dado_negro_impar_dado_blanco[6])
           + (dado_negro[4] * dado_negro_par_dado_blanco[1]) + (dado_negro[4] * dado_negro_par_dado_blanco[3]) + (dado_negro[4] * dado_negro_par_dado_blanco[5])
           + (dado_negro[5] * dado_negro_impar_dado_blanco[2]) + (dado_negro[5] * dado_negro_impar_dado_blanco[4]) + (dado_negro[5] * dado_negro_impar_dado_blanco[6])
           + (dado_negro[6] * dado_negro_par_dado_blanco[1]) + (dado_negro[6] * dado_negro_par_dado_blanco[3]) + (dado_negro[6] * dado_negro_par_dado_blanco[5]))

print('La probabilidad de obtener un número par e impar en una tirada es de:', probabilidad_par_impar)