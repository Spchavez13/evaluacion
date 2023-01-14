import math
 
def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz n")
    print("6. Exponente n")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    return int(input("Seleccione una opción: "))

opcion = menu()
a= float(input("ingrese el primer numero: "))
