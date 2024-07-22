print("hole")
# para nombrar una variable o asignar un valor así:
num = 2
num2 = 2
num_entero = 5
n = 10
print(num+num_entero)
print(type(num))

resultado = num + num_entero
print(resultado)

# vemos el tipo de dato con type()
print(type(num)) # <class 'int'>



# Forma práctica de imprimir con variables
# Uso del f-string

print(f"Hola, sumé el valor {num} y el valor {num2} dando {resultado}")

### float : números decimales
### se separa el entero del decimal con punto

num = 4.5
num2 = 3.2

resultado = num * num2
print(f"Hola, multipliqué el valor {num} y el valor {num2} dando {resultado}")
print(f"El tipo de dato de {num} es {type(num)}")

### complex : Complejo o imaginari
### se representa con una j al final del número
### Vienen del problema de raiz de menos 1

num = 4j
num2 = 2j

resultado = num - num2

print(f"Hola, resté el valor {num} y el valor {num2} dando {resultado}")
print(f"El tipo de dato de {num} es {type(num)}")