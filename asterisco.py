#Elabore un algoritmo que lea un valor N y que imprima un triángulo de asteriscos. Si el valor leído es 5 imprimir:
# *
# **
# ***
# ****
# *****

N = 5

x = 1
asteriscos = ""

while x <= N:
     
     asteriscos = asteriscos + "*"  

     print(asteriscos)             
     x= x + 1    











# estudiantes = 750
# actual = 2026


# while actual < 2035:
#     actual = actual + 1
#     aumento = estudiantes * 0.12
#     estudiantes = estudiantes + aumento
    
#     print(f"Año {actual}: se sumaron {int(aumento)} -> Nuevo total: {int(estudiantes)}")  
   
#     print(f"El total despues de 10 años fue de: {estudiantes:,.0f} estudiantes.")         

# cantidad = int(input("¿Cuántos números vas a ingresar? "))

# numero = float(input("Ingrese el número 1: "))
# mayor = numero
# menor = numero

# contador = 2

# while contador <= cantidad:
#     numero = float(input(f"Ingrese el número {contador}: "))
    
#     if numero > mayor:
#         mayor = numero
        
#     if numero < menor:
#         menor = numero
        
#     contador = contador + 1

# print(f"\nEl número mayor es: {mayor}")
# print(f"El número menor es: {menor}")