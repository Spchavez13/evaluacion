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
    print("10. exit")
    
    opcion = int(input("Seleccione una opción de la operacion que dese realiar: "))
    return opcion

#"Se agregan todas las opciones matematicas"

def sumar(a, b):
    return a + b
 
def restar(a, b):
    return a - b
 
def multiplicar(a, b):
    return a * b
 
def dividir(a, b):
    return a / b
 
def raiz_n(a, b):
    return a ** (1/b)
 
def exponente_n(a, b):
    return a ** b
 
def seno(a):
    return math.sin(a)
 
def coseno(a):
    return math.cos(a)
 
def tangente(a):
    return math.tan(a)

while True:
    opcion = menu()
    if opcion == 1:
 
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)

    elif opcion == 2:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)


    elif opcion == 3:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)


    elif opcion == 4:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)


    elif opcion == 5:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)
    
    elif opcion == 6:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)


    elif opcion == 7:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)


    elif opcion == 8:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)


    elif opcion == 9:
        a= float(input("ingrese el primer numero: "))
        b= float(input("Ingrese un segundo nundo numero:  "))
        resultado = sumar(a,b)
        print ("resultado",resultado)


    elif opcion == 10:
        break


