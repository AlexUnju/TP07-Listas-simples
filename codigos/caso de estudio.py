'''Mediante un menú de opciones realizar el siguiente programa modular para gestionar el listado de notas de un examen para los estudiantes de una institución educativa:
a. Registrar estudiantes: para cada uno se debe solicitar DNI, nombre y nota. Validar que la nota se encuentre entre 0 y 10. El proceso finaliza cuando el dni es igual a cero.
b. Mostrar el listado de estudiantes con sus respectivas notas.
c. Buscar un estudiante por su DNI y mostrar su nombre y nota.
d. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).
e. Eliminar un estudiante buscando por DNI. Emitir un mensaje de confirmación.
f. Mostrar el promedio de las notas ingresadas
g. Salir'''



import os

def presionarTecla():
   input('Presione una tecla ...')

def menu():
    os.system('clear') # windows cls
    print('1) Leer estudiantes')
    print('2) Mostrar estudiantes')
    print('3) Buscar por DNI')
    print('4) Modificar un estudiante')
    print('5) Eliminar por DNI')
    print('6) Mostrar promedio')
    print('7) salir ')
    opcion = int(input('Seleccione una opción: '))
    return opcion
    
def leerNota():
    nota = float(input('Nota: '))
    while not(nota >= 0 and nota <= 10):
        print('Nota no válida...')
        nota = float(input('Nota: '))
    return nota    

def buscarPorDni(estudiantes, dni):
    pos = -1
    for i, item in enumerate(estudiantes):
        if(item[0] == dni):
            pos = i
            break
    return pos 

def leer():
    lista = []
    respuesta = 's'
    while respuesta != 'n':
        dni = int(input('DNI: '))
        pos = buscarPorDni(lista, dni)
        if(pos == -1): 
            nombre = input('Nombre: ')
            nota = leerNota()
            lista.append([dni, nombre, nota])
        else:
            print('Estudiante existente: ',lista[pos])     
        respuesta = input('Continuar?: ')
    return lista

def mostrar(estudiantes):
    for i, item in enumerate(estudiantes):
        print(i, item)

def buscar(estudiantes): 
    dni = int(input('DNI: '))
    pos = buscarPorDni(estudiantes, dni)
    if(pos == -1): 
        print('No existe el dni ingresado...')
    else:
        print(estudiantes[pos])    
    presionarTecla()    

def eliminar(estudiantes):
    dni = int(input('DNI: '))
    pos = buscarPorDni(estudiantes, dni)
    if(pos == -1): 
        print('No existe el dni ingresado...')
    else:
        estudiantes.pop(pos)
        print('El estudiante fue elimnado...')
    presionarTecla()    

def modificar(estudiantes):
    dni = int(input('DNI: '))
    pos = buscarPorDni(estudiantes, dni)
    if(pos == -1): 
        print('No existe el dni ingresado...')
    else:
        nombre = input('Nuevo nombre: ')
        nota = float(input('Nueva nota: '))
        estudiantes[pos][1] = nombre
        estudiantes[pos][2] = nota
        print('El estudiante fue modificado...')
    presionarTecla()  

def suma(estudiantes):
    suma = 0.
    for item in estudiantes:
        suma += item[2]
    return suma

def promedio(estudiantes):
    return suma(estudiantes) / len(estudiantes)


#Principal
estudiantes = []
while True: 
    opcion = menu()
    if opcion == 1:
        estudiantes = leer()
    elif opcion == 2:
        mostrar(estudiantes)
        presionarTecla()
    elif opcion == 3: 
        buscar(estudiantes)    
    elif opcion == 4:     
        modificar(estudiantes)    
    elif opcion == 5: 
        eliminar(estudiantes)    
    elif opcion == 6:
        print('Promedio: ', promedio(estudiantes))    
        presionarTecla()
    elif opcion == 7:
        print('Fin del programa...')    
        presionarTecla()
        break


