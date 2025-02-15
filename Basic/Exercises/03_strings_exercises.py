# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.

print("Hola" + " " + "Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.

sentence = "Cadena que va a tener \nun salto de linea"
print(sentence)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

name = "Richard"
surname = "Sanz"
age = 28

print(f"Me llamo {name} {surname} y tengo {age} años.")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.

word = "Python"
print(word[:1])
print(word[1:2])
print(word[2:3])
print(word[3:4])
print(word[4:5])
print(word[5:6])

a, b, c, d, e, f = word
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
word2 = "Programación"
print(word2[3:8])

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
word3 = "Python"
print(word3[::-1])

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
sentence2 = "aprendiendo python"
print(sentence2.upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.

sentence3 = "Programación en Python"
print(text.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
numbers = "12345"
print(numbers.isnumeric())