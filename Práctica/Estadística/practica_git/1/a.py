# Ejercicicio 1

# A. ¿Cuál es la probabilidad de obtener dos dados iguales?

prob_dados_iguales = 0

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

for numero, probabilidad in dado_negro.items():
    prob_dados_iguales += dado_negro[numero] * dado_blanco[numero]

print("La probabilidad de obtener dos dados iguales es de", prob_dados_iguales)

# Print = La probabilidad de obtener dos dados iguales es de 0.07250000000000001