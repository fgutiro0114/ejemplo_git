# x=0

# while x<5:
#     print("python")
#     x=x+1

# numero = int(input("Digite un numero: "))
# for i in range(1,11):

#     print(f"{numero} X {i} = {numero*i}")


# for i in range(1,4):
#     usuario = input("Digite su usuario: ")
#     clave = input("Digite su clave:")
#     if usuario == "pepe" and clave == "123":
#         print("Bienvenido")
#         break
#     else:
#         print("Datos incorrectos")
for intento in range(3):
    correo=input("Digite su correo ")
    arroba =False
    valido = False
    for i in correo:
        if i=="@":
            arroba=True
        elif i =="." and arroba == True:
            print("El correo es valido ")
            valido=True
            break
    if valido == False:
        print("Correo no valido")
