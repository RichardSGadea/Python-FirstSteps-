# 1. Crea una lista con los números del 1 al 5 e imprímela.
my_list= [1,2,3,4,5]

print(my_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
my_other_list = [10, 20, 30, 40, 50]
print(my_other_list[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.

my_list.append(6)

print(my_list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].

my_other_list.insert(2,15)
print(my_other_list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

my_third_list = [10, 20, 30, 30, 40, 50]

my_third_list.remove(30)
print(my_third_list)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.

my_fourth_list = [1, 2, 3, 4, 5]
item_removed = my_fourth_list.pop()

print(item_removed)
print(my_fourth_list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.

list_to_reverse = [100, 200, 300, 400, 500]
list_to_reverse.reverse()
print(list_to_reverse)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
list_to_sort = [3, 1, 4, 2, 5]
list_to_sort.sort()
print(list_to_sort)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
lr= l1 + l2

print(lr)


# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).

final_list = [10, 20, 30, 40, 50]
sublist =  final_list[1:3]

print(sublist)