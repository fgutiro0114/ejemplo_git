#Solicite el nombre del artículo, la clave del artículo y su precio original en USD. Calcule e imprima el precio con descuento según la siguiente tabla (solo existen dos claves válidas): 
#•  Clave 01: descuento del 10 %.
#•  Clave 02: descuento del 20 %. Salidas esperadas: nombre del artículo, clave, precio original y precio con descuento aplicado. 

nombre = input("Ingrese el nombre del artículo: ")
clave = input("Ingrese la clave del artículo (01 o 02): ").lower()
precio = float(input("Ingrese el precio original en USD: "))

# Determinar el descuento
if clave == "01":
    descuento = 0.10
else:
    descuento = 0.20

# Calcular el precio con descuento
precio_descuento = precio - (precio * descuento)

# Mostrar resultados
print("\n--- DATOS DEL ARTÍCULO ---")
print("El nombre del articulo es:", nombre)
print("La clave del articulo es:", clave)
print(f"El precio original es: ${precio:.2f} USD")
print(f"El precio con descuento es: ${precio_descuento:.2f} USD")