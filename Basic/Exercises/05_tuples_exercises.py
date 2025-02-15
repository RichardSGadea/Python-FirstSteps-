# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

my_tuple_two = (100, 200, 300, 400, 500)
print(my_tuple_two[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

tuple_to_modify = (1, 2, 3)
# tuple_to_modify[0] = 10     #-------------- TypeError: 'tuple' object does not support item assignment
# print(tuple_to_modify)

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

tuple_to_count = (1, 2, 3, 3, 4, 5, 3)
print(tuple_to_count.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

languages_tuple = ("Java", "Python", "JavaScript", "Python")
print(languages_tuple.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)

print(tuple_1 + tuple_2)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

tuple_3 = (10, 20, 30, 40, 50)
sub_tuple = tuple_3[2:4]

print(sub_tuple)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

colors_tuple = ("rojo", "verde", "azul")
colors_list = list(colors_tuple)
colors_list[1] = "amarillo"

colors_tuple = tuple(colors_list)

print(colors_tuple)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

my_tuple_to_delete = (1,2,3)

del my_tuple_to_delete


# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

my_tuple = (100, )
print(my_tuple)