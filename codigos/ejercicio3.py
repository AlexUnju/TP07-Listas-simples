import os
os.system('cls')

def promedio(lista):
    suma = 0
    long = len(lista)
    for i in range(len(lista)):
        if lista[i] == None:
            print(f"En el aforo {i+1} se encontró: {lista[i]}")
            long -= 1
        else:
            suma += lista[i]
    promedio = suma / long
    print(promedio)
    return promedio


# Principal
lista = [7.5, 0.0, None, 8.2, 6.9, None, 8.5]
promedio(lista)