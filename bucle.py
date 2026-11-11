#"""""if opcion == 1:
###elif opcion == 2:
#    print(numero1-numero2)
#elif opcion == 3:
#    print(numero1*numero2)
#elif opcion == 4:
#    print(numero1/numero2)"""

#TEMA MATCH
numero1=int(input("Digite un número "))
numero2=int(input("Digite un número "))

opciones="""
1.Suma
2.Resta
3.Multiplicación
4.División
"""

print(opciones)
print("Digite el numero de la operacion que desea realizar: ")
opcion = int(input("Digite la opcion: "))

match opcion:
    case 1:
        print(numero1+numero2)
    case 2:
        print(numero1+numero2)
    case 3:
        print(numero1+numero2)
    case 4:
        print(numero1+numero2)

    case _ :
        print ("Digito una opcion incorrecta")
    


