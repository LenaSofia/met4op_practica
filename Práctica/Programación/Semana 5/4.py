def imprimir_nombre_n_veces():
    nombre = input('Por favor ingrese el nombre que desea imprimir: ')
    numero = input('Por favor ingrese en números enteros la cantidad de veces que desea imprimir ese nombre: ')

    try:
        numero = int(numero)

        for x in range(1, numero + 1):
            print(nombre)

    except:
        print('Lo siento, usted no ingresó un número, no podemos realizar la operación')

imprimir_nombre_n_veces()
