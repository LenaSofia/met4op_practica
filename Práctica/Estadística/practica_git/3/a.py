# 3. Se tira una moneda equilibrada 20 veces y se observa el número de veces que salió cara.

import pprint

monedas = {
'1' : ['C', 'X'],
'2' : ['C', 'X'],
'3' : ['C', 'X'],
'4' : ['C', 'X'],
'5' : ['C', 'X'],
'6' : ['C', 'X'],
'7' : ['C', 'X'],
'8' : ['C', 'X'],
'9' : ['C', 'X'],
'10' : ['C', 'X'],
'11' : ['C', 'X'],
'12' : ['C', 'X'],
'13' : ['C', 'X'],
'14' : ['C', 'X'],
'15' : ['C', 'X'],
'16' : ['C', 'X'],
'17' : ['C', 'X'],
'18' : ['C', 'X'],
'19' : ['C', 'X'],
'20' : ['C', 'X']
}

dic_monedas = {}

x = 0

for valor_1 in monedas['1']:
    for valor_2 in monedas['2']:
        for valor_3 in monedas['3']:
            for valor_4 in monedas['4']:
                for valor_5 in monedas['5']:
                    for valor_6 in monedas['6']:
                        for valor_7 in monedas['7']:
                            for valor_8 in monedas['8']:
                                for valor_9 in monedas['9']:
                                    for valor_10 in monedas['10']:
                                        for valor_11 in monedas['11']:
                                            for valor_12 in monedas['12']:
                                                for valor_13 in monedas['13']:
                                                    for valor_14 in monedas['14']:
                                                        for valor_15 in monedas['15']:
                                                            for valor_16 in monedas['16']:
                                                                for valor_17 in monedas['17']:
                                                                    for valor_18 in monedas['18']:
                                                                        for valor_19 in monedas['19']:
                                                                            for valor_20 in monedas['20']:
                                                                                dic_monedas[x] = valor_1, valor_2, valor_3, valor_4, valor_5, \
                                                                                         valor_6, valor_7, valor_8, valor_9, valor_10, \
                                                                                         valor_11, valor_12, valor_13, valor_13, valor_15,\
                                                                                         valor_16, valor_17, valor_18, valor_19, valor_20
                                                                                x += 1


pprint.pprint(dic_monedas)

contador = 0

for evento, valor in dic_monedas.items():

