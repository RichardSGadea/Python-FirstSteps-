# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting(name = ""):
    if not name: return "Hola, desconocido"
    return f"Hola, {name}"

print(personalized_greeting("Richard"))
print(personalized_greeting())

# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.

def multiply(n1,n2):
    return n1 * n2

print(multiply(4,8))

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.

def is_even(number: int):
    if not number % 2 == 0: return "Impar"
    return "Par"

print(is_even(3))

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.

def convert_to_uppercase (text: str):
    return text.upper()

print(convert_to_uppercase("Hola Mundo fanático."))

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.

# def arbitrary_sum(*numbers):
#     sum = 0
#     for number in numbers:
#         sum += number
#     return sum

# print(arbitrary_sum(1,5,3,7,4))
def arbitrary_sum(*numbers):
    return sum(numbers)

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting(name,surname):
    print(f"Hola, {name} {surname}")

generate_full_greeting(surname="Sanz", name="Richard")

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.

def power(base,exp):
    return base**exp

print(power(2,3))

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.

def calculate_average(n1,n2,n3):
    return (n1+n2+n3) / 3

print(calculate_average(3,4,5))

def calculate_average_arbitrary(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    
    return sum/len(numbers)

print(calculate_average_arbitrary(3,4,5,5,6,7,3,7))

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.

def count_characters(text):
    return len(text)

print(count_characters("pelos"))

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*texts):
    for text in texts:
        print(text.upper())

display_messages("Hola Mundo", "Señor bienvenido", "Superman")