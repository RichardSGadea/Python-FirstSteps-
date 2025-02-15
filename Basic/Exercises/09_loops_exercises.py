# 1. Usa un bucle while para imprimir los números del 1 al 10.

i = 1
while i <= 10:
    print(i)
    i+= 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.

n_list = [10, 20, 30, 40, 50]
for n in n_list:
    print(n)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

result = 0
i = 1

while i <= 100:
    result += i
    i += 1

print(result)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".

word = "Python"

for char in word:
    print(char)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.

number_divisible = 0
i = 8

while i <= 50:
    if i % 7 == 0:
        number_divisible = i
        break
    i += 1

print(f"Número divisible por 7: {number_divisible}")

# 6. Usa un bucle for para recorrer el diccionario {"name": "Richard", "age": 28, "country": "España"} e imprime las claves.

person_dict = {"name": "Richard", "age": 28, "country": "España"}
for key in person_dict:
    print(key)

# y los valores
    for value in person_dict.values():
        print(value)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.

for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].

counter = 0
n_list = [30, 10, 30, 20, 30, 40]

for n in n_list:
    if n == 30:
        counter += 1
print(counter)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Richard".

names = ["Sara", "Richard", "Pedro"]
for name in names:
    if name == "Richard":
        print("Se encontró a Richard")
        break
    print(name)