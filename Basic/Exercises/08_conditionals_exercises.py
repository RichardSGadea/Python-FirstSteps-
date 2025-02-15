# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.

my_number = 5
if my_number > 0:
    print(f"El número {my_number} es positivo")
elif my_number < 0:
    print(f"El número {my_number} es negativo")
else:
    print(f"El número {my_number} es cero")    

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.

age = int(input("Por favor, introduce tu edad: "))

if age >= 18:
    print("Eres mayor de edad")
else:    
    print("Eres menor de edad")


# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.

text = input("Introduce una cadena: ")
if not text:
    print("Texto vacío")
else:
    print(f"{text}")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

number_1 = int(input("Escribe un número: "))
number_2 = int(input("Escribe otro número: "))

if number_1 > number_2:
    print(f"El número {number_1} es mayor qué {number_2}")
elif number_2 > number_1:
    print(f"El número {number_2} es mayor qué {number_1}")
else:
    print(f"El número {number_1} es igual qué {number_2}")
    
# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.

number = int(input("Introduce un número: "))

if number%3 == 0 and number%5 == 0:
    print(f"El número {number} es divisible por 3 y por 5")
else:
    print(f"El número {number} no es divisible por 3 y por 5 al mismo tiempo")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
number_par_impar = int(input("Introduce un número: "))
if number_par_impar % 2 == 0:
    print(f"El número {number_par_impar} es par")
else:
    print(f"El número {number_par_impar} es impar")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.

person_age = int(input("Introduce tu edad: "))

if person_age >= 18:
    print(f"Puedes votar")
elif person_age < 18 and person_age >= 16:
    print(f"Puedes votar con permiso especial")
else:
    print(f"No puedes votar")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.

default_password = "enero31"
password = input("Escribe tu contraseña: ")

if password != default_password:
    print("Credenciales incorrectas")
else:
    print("Acceso permitido")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).

number_between= int(input("Introduce"))
if number_between >= 10 and number_between<=20:
    print(f"El número {number_between} está entre 10 y 20 (incluidos)")
else:
    print(f"El número {number_between} NO está entre 10 y 20 (incluidos)")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

color = input("Introduce un color (rojo, amarillo, verde): ").lower()
if color == "rojo":
    print("Detente")
elif color == "amarillo":
    print("PrecauciÃ³n")
elif color == "verde":
    print("Avanza")
else:
    print("Color no válido")
