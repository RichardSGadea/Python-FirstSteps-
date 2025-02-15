# 1. Imprime "¡Hola Mundo!" por consola.
print("¡Hola Mundo!")

# 2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.
# Imprime por consola 

# 3. Imprime tu nombre y edad en la misma línea utilizando la función print.
print("Mi nombre es Richard y tengo", 28 ," años")

# 4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.
print(type("Hola"))
print(type(12))
print(type(3.4))

# 5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
"""
Se refiere a la clasificación de los valores que pueden ser almacenados en una variable. 
Cada tipo de dato tiene características y propiedades específicas 
que lo hacen adecuado para ciertos usos y operaciones

En Python, los tipos de datos mÃ¡s comunes son:
- str: para cadenas de texto
- int: para nÃºmeros enteros
- float: para nÃºmeros con decimales
- bool: para valores booleanos (True/False)
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print("Hola"+"Mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
nombre = "Richard"
edad = 28

print(f"Hola me llamo {nombre} y tengo {edad} años.")

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
nombre = input('¿Cómo te llamas?')
print(f"Hola {nombre}, ¡Bienvenido!")

# 9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.
numero1 = 43
numero2 = 32

print(f"La suma de {numero1} y {numero2} es igual a {numero1 + numero2}")
print(f"El dato {numero1 + numero2} es de tipo -> {type(numero1 + numero2)}")

# 10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.
"""
numero1 = 43 #almacenar en variable
numero2 = 32 #almacenar en variable

print(f"La suma de {numero1} y {numero2} es igual a {numero1 + numero2}") #sumar y imprimir
print(type(numero1 + numero2)) #imprimir el tipo del resultado de la suma
"""