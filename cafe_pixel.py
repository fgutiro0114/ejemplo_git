# Café Pixel vende sándwiches y jugos por internet. Su propietaria necesita 
# calcular el costo de un pedido,
# aplicar un descuento a los productos y agregar el valor del domicilio.
# Datos que debe solicitar el programa
# • Nombre del cliente • Precio unitario del jugo
# • Cantidad de sándwiches • Porcentaje de descuento
# • Precio unitario del sándwich • Costo fijo del domicilio
# • Cantidad de jugos


nombre_cliente = input("Digite el nombre del cliente:\n")
precio_jugo = float(input("Digite el precio unitario del jugo:\n"))
cantidad_jugos = int(input("Digite la cantidad de jugos:\n"))
precio_sandwich = float(input("Digite el precio unitario del sándwich:\n"))
cantidad_sandwich = int(input("Digite la cantidad de sándwich:\n"))
porcentaje_descuento = float(input("Digite el porcentaje de descuento de (1 a 100 ):\n"))
costo_domicilio = float(input("Digite el costo del domicilio: \n"))

valor_total_jugo= cantidad_jugos *precio_jugo
valor_total_sandwich= cantidad_sandwich *precio_sandwich

total_pedido = valor_total_jugo + valor_total_sandwich
total_descuento= total_pedido * porcentaje_descuento/100
total=total_pedido - total_descuento - costo_domicilio


print("-" * 20, "FACTURA", "-" * 20)
print(f"Cliente: {nombre_cliente}")
print("-" * 55)

print(f"Cantidad de jugos: {cantidad_jugos} | Total: ${valor_total_jugo:,.0f}")
print(f"Cantidad de sándwiches: {cantidad_sandwich} | Total: ${valor_total_sandwich:,.0f}")

print("-" * 55)
print(f"Subtotal: ${total_pedido:,.0f}")
print(f"Descuento: ${total_descuento:,.0f}")
print(f"Domicilio: ${costo_domicilio:,.0f}")
print(f"TOTAL A PAGAR: ${total:,.0f} pesos")
print("-" * 55)
print("¡Gracias por tu compra! En Café Pixel esperamos verte pronto.")
print("-" * 55)