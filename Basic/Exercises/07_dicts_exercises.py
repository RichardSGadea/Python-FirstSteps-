# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

my_dict = {
    "name"      : "Richard",
    "age"       : 28,
    "country"   : "España"  
}

print(type(my_dict))
print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.

print(my_dict["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

my_dict["job"] = "Programador"
print(my_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

my_dict["age"] = 38
print(my_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

del my_dict["country"]
print(my_dict)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

my_other_dict = {
    1: 1**2,
    2: 2**2,
    3: 3**2,
    4: 4**2,
    5: 5**2
}
print(my_other_dict)

squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Richard", "age": 28, "country": "España"}.

my_dict = {
    "name"      : "Richard",
    "age"       : 28,
    "country"   : "España"  
}
print("age" in my_dict)

# 8. Imprime solo las claves del diccionario.

print(my_dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

my_list = list(my_dict.keys())
print(my_list)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

my_other_list = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_other_list,"Desconocido")

print(my_new_dict)
