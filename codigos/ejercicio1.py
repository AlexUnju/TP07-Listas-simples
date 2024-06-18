# Definición de las listas
a = [5, 1, 4, 9, 0]
b = list(range(3, 10)) + list(range(20, 23))  # [3, 4, 5, 6, 7, 8, 9, 20, 21, 22]
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]  # ['a', [5, 1, 4, 9, 0], [5, 1, 4, 9, 0, 5, 1, 4, 9, 0]]



# Resultados esperados:
# a[2]: 4 , Tipo: <class 'int'>
# b[9]: 22 , Tipo: <class 'int'>
# c[1][2]: 5 , Tipo: <class 'int'>
# e[0] == e[1]: False , Tipo: <class 'bool'>
# len(c): 3 , Tipo: <class 'int'>
# len(c[0]): 2 , Tipo: <class 'int'>
# len(e): 3 , Tipo: <class 'int'>
# c[-1]: [6, 7] , Tipo: <class 'list'>
# c[-1][+1]: 7 , Tipo: <class 'int'>
# c[2:] + d[2:]: [[6, 7], 'jirafa', 'elefante'] , Tipo: <class 'list'>
# a[3:10]: [9, 0] , Tipo: <class 'list'>
# a[3:10:2]: [9] , Tipo: <class 'list'>
# d.index('jirafa'): 2 , Tipo: <class 'int'>
# e[c[0][1]].count(5): 2 , Tipo: <class 'int'>
