# 1. Declara y asigna valores a las siguientes variables:
# •	name: una cadena que contenga tu nombre.
# •	age: un número entero que represente tu edad.
# •	height: un número flotante que represente tu altura.
# •	Imprime cada variable en una línea separada.

name    = "Richard"
age     = 28
height  = 1.83

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.

print("Tienes", str(age) ,"años")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.

is_student = False
print(is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.

name_characters = len(name)
print(name_characters)

# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

name, surname, city = "Richard","Sanz","Valencia"
print(name, surname, city)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.

favorite_color = input("¿Color favorito?")
print(favorite_color)

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = "Apple"
fruit = "Banana"
print(fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 1.6
print(int(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address_len = len(city)
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone: int = 123456789
print(type(phone))
phone = 987654321
print(type(phone))