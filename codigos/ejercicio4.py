import os
os.system('cls')

#Diseñar un algoritmo que permita realizar lo siguiente:
# Mostrar los números ingresados y su posición
# Mostrar si los elementos de la lista se encuentran ordenados en forma descendente
# Mostrar los valores que superen el promedio de los valores ingresados
# Mostrar el mínimo de los valores ingresados y su posición
# Indicar qué elementos son valores primos
# El algoritmo debe considerar que si no se cargó la lista previamente, no se pueda realizar alguna de las
#acciones solicitadas.

def cargar_lista(lista):
    bandera=True
    while bandera:
        valor=int(input('Ingrese el valor que desea cargar a la lista: '))
        lista.append(valor)
        continuar=input('¿Desea continuar? S/N: ')
        continuar.lower()
        if continuar=='n':
            bandera=False
    return lista

def mostrar_num_pos(lista):
    for i in range(len(lista)):
        print(f'Número: {lista[i]} | Posición: {i+1}')

def mostrar_orden_desc(lista):
    ordenada=False
    for i in range(len(lista)):
        if i+1 >= len(lista):
            break
        if lista[i]>lista[i+1]:
            ordenada=True
        else:
            ordenada=False
            break
    if ordenada:
        print('La lista está ordenada de forma descendiente.')
    else:
        print('La lista NO está ordenada de forma descendente.')
    return ordenada

def promedio(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    promedio=suma/len(lista)
    print(f'El promedio es: {round(promedio,2)}')
    return promedio

def mostrar_valores_sobre_promedio(lista, promedio):
    for i in range(len(lista)):
        if lista[i]>promedio:
            print(f'El valor {lista[i]} con posición {i+1} supera el promedio.')

def mostrar_minimo_pos(lista):
    min=0
    bandera=True
    for i in range(len(lista)):
        if bandera:
            min=lista[i]
            pos=i+1
            bandera=False
        elif lista[i]<min:
            min=lista[i]
            pos=i+1
    print(f'El mínimo de los valores ingresados es: {min} con posición {pos}.')

def es_primo(num: int, indice):
    if num <= 1:
        return

    for j in range(2, num):
        if num % j == 0:
            return False
    print(f"El valor {num} con posición {indice} es primo.")


def mostrar_primos(lista):
    for i in range(len(lista)):
        valor = lista[i]
        es_primo(valor, i)

#Principal
lista=[]
lista=cargar_lista(lista)
print(lista)
mostrar_num_pos(lista)
mostrar_orden_desc(lista)
promedio=promedio(lista)
mostrar_valores_sobre_promedio(lista, promedio)
mostrar_minimo_pos(lista)
mostrar_primos(lista)