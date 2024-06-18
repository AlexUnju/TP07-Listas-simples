import os

def presionar_tecla():
    input('Presione una tecla para continuar...')

def menu():
    os.system('clear')  # En Windows, usa 'cls'
    print('Menú de opciones:')
    print('1) Cargar lista de caracteres')
    print('2) Mostrar lista en orden inverso')
    print('3) Buscar un carácter')
    print('4) Contar vocales')
    print('5) Salir')
    opcion = int(input('Seleccione una opción: '))
    return opcion

def cargar_lista():
    lista = []
    print("Ingrese caracteres en la lista. Escriba 'fin' para terminar.")
    while True:
        char = input("Ingrese un carácter: ")
        if char.lower() == 'fin':
            break
        elif len(char) != 1:
            print("Por favor, ingrese solo un carácter.")
        else:
            lista.append(char)
    return lista

def mostrar_lista_invertida(lista):
    print("Lista desde el último valor ingresado hasta el primero:")
    for char in reversed(lista):
        print(char, end=" ")
    print()  # Nueva línea

def buscar_caracter(lista, caracter):
    verificar = -1
    for i, item in enumerate(lista):
        if item == caracter:
            verificar = i
            break
    return verificar

def contar_vocales(lista):
    vocales = 'aeiouAEIOU'
    contador_vocales = sum(1 for char in lista if char in vocales)
    return contador_vocales

# Programa principal
caracteres = []
while True:
    opcion = menu()
    if opcion == 1:
        caracteres = cargar_lista()
        presionar_tecla()
    elif opcion == 2:
        if caracteres:
            mostrar_lista_invertida(caracteres)
        else:
            print("La lista está vacía.")
        presionar_tecla()
    elif opcion == 3:
        if caracteres:
            caracter_a_buscar = input("Ingrese un carácter a buscar en la lista: ")
            posicion = buscar_caracter(caracteres, caracter_a_buscar)
            if posicion != -1:
                print(f"El carácter '{caracter_a_buscar}' se encuentra en la posición {posicion}.")
            else:
                print(f"El carácter '{caracter_a_buscar}' no se encuentra en la lista.")
        else:
            print("La lista está vacía.")
        presionar_tecla()
    elif opcion == 4:
        if caracteres:
            cantidad_vocales = contar_vocales(caracteres)
            print(f"La cantidad de vocales en la lista es: {cantidad_vocales}")
        else:
            print("La lista está vacía.")
        presionar_tecla()
    elif opcion == 5:
        print("Fin del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        presionar_tecla()
