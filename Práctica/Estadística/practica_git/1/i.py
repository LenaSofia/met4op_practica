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

prob_DB_cond_DN_2 =