# Vamos a guardar el valor de la preproinsulina en una variable

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# Almacenar el valor de cada subsecuencia

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = 	"fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = 	"giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"



# Suma el valor de las subsecuencias más pequeñas
insulin = bInsulin + aInsulin

# Imprimiendo los valores de la insulina humana
print("La secuencia de la preproInsulina", preproInsulin)

# Imprimiendo los valores usando concatenación
print("El valor de la cadena aInsulin " + aInsulin)

# Calcular el peso de los aminociados en la insulina

# Define el valor del peso de cada aminoacido
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 

# Conteo de cuántas veces aparece cada aminoacido en la cadena
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})


"""

# Multiplicar los pesos con las apariciones y sumar su valor

molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values()) 


# Es equivalente a:
pesos_totales = {}
for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']:
    # Calculo el peso total de cada aminoacido
    valor = aaCountInsulin[x] * aaWeights[x]
    
    #guardar en el diccionario
    pesos_totales[x] = valor

print("El valor de los pesos totales es", pesos_totales)

['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']

