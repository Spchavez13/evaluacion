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
    return int(input("Seleccione una opción de la operacion que dese realiar: "))

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
 

opcion = menu()
a= float(input("ingrese el primer numero: "))
b= float(input("Ingrese un segundo nundo numero:  "))

