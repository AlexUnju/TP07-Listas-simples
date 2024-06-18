import os
os.system('cls')

def cargar_lista(lista):
    valor=1
    while valor!=0:
        valor=int(input('Ingrese el valor que desea agregar a la lista. O ingrese 0 para finalizar: '))
        if validar(lista, valor):
            lista.append(valor)
    return lista

def validar(lista, valor):
    duplicados=lista.count(valor)
    if duplicados>=1:
        print('Este valor ya existe en la lista. Por favor, ingresa uno distinto.')
    else:
        return True

def mostrar_lista(lista):
    print(lista)    
        
def agregar_elemento(lista):
    elemento=int(input('Ingrese el elemento que desea agregar al final de la lista: '))
    if validar(lista, elemento):
        lista.append(elemento)
    else:
        agregar_elemento(lista)
    
def insertar_elemento(lista):
    elemento=int(input('Ingrese un elemento que desee agregar a la lista: '))
    if validar(lista, elemento):
        pos=int(input('Ingrese la posición en donde desea insertar el elemento.'))
        lista.insert(pos, elemento)
    else:
        insertar_elemento(lista)
    
def eliminar_elemento(lista):
    elem_a_eliminar=int(input('¿Cuál es el elemento que desea eliminar? '))
    encontrado=False
    for i in lista:
        if i==elem_a_eliminar:
            encontrado=True
            lista.remove(i)
            print(lista)
    if not encontrado:
        print('No se encontró el elemento.')
    return lista
    
def copiar_pares(lista, listaPares):
    for i in lista:
        if i%2==0:
            listaPares.append(i)
    return listaPares
    
def mostrar_listas(lista, listaPares):
    print(f'La lista final es {lista}')
    print(f'La lista de pares es {listaPares}')
    
#Principal
lista=[]
listaPares=[]

lista=cargar_lista(lista)
mostrar_lista(lista)
agregar_elemento(lista)
print(lista)
insertar_elemento(lista)
print(lista)
eliminar_elemento(lista)
listaPares=copiar_pares(lista,listaPares)
mostrar_listas(lista, listaPares)