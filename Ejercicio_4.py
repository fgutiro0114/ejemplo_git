#Enunciado: En un laboratorio se mezclan dos soluciones de la misma sustancia con diferentes concentraciones porcentuales. Se requiere hallar la concentración final de la mezcla, asumiendo que los volúmenes son aditivos y la sustancia se distribuye homogéneamente. 

solucion_a=float(input("Ingrese el volumen de la solucion A en ml: "))
concentracion_a=float(input("Ingrese la concentracion de la solucion A "))/100
solucion_b=float(input("Ingrese el volumen de la solucion B en ml: "))
concentracion_b=float(input("Ingrese la concentracion de la solucion B "))/100

cantidad_a= solucion_a * concentracion_a
cantidad_b= solucion_b * concentracion_b
total= cantidad_a + cantidad_b
volumen_total= solucion_a+solucion_b
concentracion_final= (total/volumen_total)*100

print(f"El total de las dos soluciones es de: {total:,.0f} ml.")
print(f"El volumen total de las dos soluciones es de: {volumen_total:,.0f} ml.")
print(f"La concentracion final es: {concentracion_final:,.1f}%")