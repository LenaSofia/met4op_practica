# Que es más probable, sacar generala (6 dados iguales)
# arrojando 7 dados en 3 tiradas o sacar generala arrojando 6 dados en 4 tiradas?

# Caso 1
# La probabilidad de que salga 6 en el dado 1 es 1/6, al igual que en el dado 2, 3 ... 6.
# Como en el dado 7 nos da igual el número que salga (1, 2, 3, 4, 5, 6) la probabilidad es 6/6 (es decir,
# todos los valores posibles del dado.
p_dado1_c1 = 1/6
p_dado2_c1 = 1/6
p_dado3_c1 = 1/6
p_dado4_c1 = 1/6
p_dado5_c1 = 1/6
p_dado6_c1 = 1/6
p_dado7_c1 = 6/6

# Calculo la probabilidad de cada dado como evento independiente y, como son independientes las multiplico
probabilidad_evento_1_caso1 = p_dado1_c1 * p_dado2_c1 * p_dado3_c1 * p_dado4_c1 * p_dado5_c1 * p_dado6_c1 * p_dado7_c1

# La generala puede salir en 7 ordenes diferentes, dado que sólo necesito que en 6 de los 7 dados salga en número 6,
# por lo que en el dado restante puede salir 1, 2, 3, 4, 5 o 6. Hay 7 maneras diferentes de tener 6 dados en los
# que salga 6 y un dado en el que salga 1 (Opción 1: 6, 6, 6, 6, 6, x // Opción 2: x, 6, 6, 6, 6, 6, 6 // etc.)
# Cada uno de estos eventos es independiente, entonces multiplico por 7, que son las formas distintas en que me
# puede salir generala
probabilidad_eventos_posibles_caso1 = probabilidad_evento_1_caso1 * 7

# Sumo la probabilidad de cada tirada porque son eventos disjuntos (en este caso 3 tiradas)
probabilidad_tiradas_totales_caso1 = probabilidad_eventos_posibles_caso1 + probabilidad_eventos_posibles_caso1 + probabilidad_eventos_posibles_caso1

# Imprimo la probabilidad total del caso 1
print(probabilidad_tiradas_totales_caso1)




# Caso 2
# La probabilidad de que salga 6 en el dado 1 es 1/6, al igual que en el dado 2, 3 ... 6. Como en este caso necesitamos
# que en todos los dados salga 6, la probabilidad de cada dado es de 1/6.
p_dado1_c2 = 1/6
p_dado2_c2 = 1/6
p_dado3_c2 = 1/6
p_dado4_c2 = 1/6
p_dado5_c2 = 1/6
p_dado6_c2 = 1/6

# Como cada dado tiene una probabilidad de 1/6 de valer 6, y cada evento es independiente del otro
# multiplico la probabilidad de cada dado (como evento independiente)
probabilidad_evento_1_caso2 = p_dado1_c2 * p_dado2_c2 * p_dado3_c2 * p_dado4_c2 * p_dado5_c2 * p_dado6_c2


# En este caso hay una única manera de obtener el resultado que espero (que en todos los dados salga 6), así que lo
# multiplico por 1 (podría saltearme esta operación pero es para ser más clara)
probabilidad_eventos_posibles_caso2 = probabilidad_evento_1_caso2 * 1

# Como tengo 4 tiradas para conseguir generala, sumo la probabilidad de cada
# tirada, dado que son eventos disjuntos (en este caso 4)
probabilidad_tiradas_totales_caso2 = probabilidad_eventos_posibles_caso2 + probabilidad_eventos_posibles_caso2 \
                                     + probabilidad_eventos_posibles_caso2 + probabilidad_eventos_posibles_caso2

# Imprimo la probabilidad total del caso 2
print(probabilidad_tiradas_totales_caso2)


if probabilidad_tiradas_totales_caso1 > probabilidad_tiradas_totales_caso2:
    print('La probabilidad de sacar generala (6 dados iguales) arrojando 7 dados en 3 tiradas es de', probabilidad_tiradas_totales_caso1,
    'y es mayor a la probabilidad de sacar generala arrojando 6 dados en 4 tiradas, que es', probabilidad_tiradas_totales_caso2)

elif probabilidad_tiradas_totales_caso2 > probabilidad_tiradas_totales_caso1:
    print('La probabilidad de sacar generala arrojando 6 dados en 4 tiradas es de', probabilidad_tiradas_totales_caso2,
          'y es mayor a la probabilidad de sacar generala (6 dados iguales) arrojando 7 dados en 3 tiradas, que es de',
          probabilidad_tiradas_totales_caso1)

elif probabilidad_tiradas_totales_caso1 == probabilidad_tiradas_totales_caso2:
    print('Las probabilidades son iguales y son de', probabilidad_tiradas_totales_caso1)

else:
    print('Lo siento, algo falló!')