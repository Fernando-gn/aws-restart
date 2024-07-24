"""
Función

Es un conjunto de instrucciones que puedo reutilizar en mi código
Tip: Cada vez que vean que un código se repite mucho piensen en una función

"""


# La función utiliza la palabra clave def para definición de la función
# def nombrefuncion (argumentos)
# argumento: una variable que recibe una función

def saludar(nombre):
    print(f"Hola {nombre}, cómo estás?")

# Invocar o utilizar una función
saludar("Maritza")


# Toda función puede retornar un valor de cualquier tipo
# El return se coloca al final de la función
def calcularAreaCirculo(radio):
    area = 3.14159 * radio ** 2 # area = pi * r^2
    return area

a = calcularAreaCirculo(5)

print("El área del circulo es", a)

"""
EJERCICIO
Crea una función que te permita hallar el valor del perimetro
dado el área de un círculo

def calcularPerimetro(area):
"""


def calcularPerimetro(area):
    pi = 3.14159
    
    # 2 * pi * raiz(area/pi)
    perimetro = 2 * pi * (area / pi) ** (1/2)
    
    return perimetro

resultado = calcularPerimetro(6)

print("El perimetro es", resultado)











