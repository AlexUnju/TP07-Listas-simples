def mayores_que(x, lista_valores):
    contador = 0
    for valor in lista_valores:
        if valor > x:
            contador += 1
    return contador

# Ejemplo de uso
print(mayores_que(5, [7, 3, 6, 0, 4, 5, 10]))  # Debería devolver 3
