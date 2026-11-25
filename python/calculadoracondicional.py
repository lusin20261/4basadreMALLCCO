print("--------------------")
print("  mi   calculadora")
print("--------------------")

while True:
    print("")
    print("¿Qué operación deseas realizar?")
    print("1) sumar")
    print("2) resta")

    print("3) salir")
    print("-------------------------------")

    opcion = input("ingrese una opcion")

    if opcion == "1":
        num1 = input ("ingresa el primer numero: ")
        num1 = int (num1)
        num2 = input ("ingresa el segundo numero: ")
