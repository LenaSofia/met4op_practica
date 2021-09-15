
es_primo = input("Ingrese un número natural: ")

try:
    es_primo = int(es_primo)
except:
    print("No ingresó un número natural")



def ver_si_es_primo(numero):

    primo = True # Empezamos asumiendo que el número es primo

    for numero in range(2, es_primo): # Dividimos el número por todos los números entre 2 y el número ingresado menos 1
        if es_primo % numero == 0: # Si alguna de esas divisiones da como resto 0, definimos al numero como NO primo (primo = False)
            primo = False
            break # Salimos del ciclo

    return primo