import os
os.system('cls')

def desviacion_estandar(lista_valores):
    def promedio(lista_valores):
        suma=0
        for i in lista_valores:
            suma+=i
        promedio=suma/len(lista_valores)
        return promedio
    promedio=promedio(lista_valores)
        
    def resta_al_cuadrado(lista_valores, promedio):
        for i in range(len(lista_valores)):
            lista[i]=lista[i]-promedio
            lista[i]=lista[i]**2
        return lista_valores
    lista_valores=resta_al_cuadrado(lista_valores, promedio)
        
    def sumatoria(lista_valores):
        sumatoria=0
        for i in lista_valores:
            sumatoria+=i
        return sumatoria
    sumatoria=sumatoria(lista_valores)
        
    def dividir_suma(lista_valores, sumatoria):
        division = sumatoria/(len(lista_valores)-1)
        return division
    division=dividir_suma(lista_valores, sumatoria)
    
    def raiz_cuadrada(lista_valores, division):
        division = division**(1/2)
        return division
    division=raiz_cuadrada(lista_valores, division)
    print(f'El resultado es {division}')
#Principal

lista = [4.0, 1.0, 11.0, 13.0, 2.0, 7.0]
desviacion_estandar(lista)