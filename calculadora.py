#!/usr/bin/python


def numero1():
    a=float(input("ingresa un numero: "))
    return a
def numero2():
    b=float(input("ingresa un numero: "))
    return b
def suma(a, b):
    resultado= a+b
    print(f" {a} + {b} es  {resultado}")

def resta(a, b):
    resultado= a-b
    print(f" {a} + {b} es  {resultado}")

def multiplicación(a, b):
    resultado= a*b
    print(f" {a} * {b} es  {resultado}")

def división(a, b):
    resultado= a/b
    print(f"La división de {a} y {b} es = {resultado}")

def potencia(a, b):
    resultado= a**b
    print(f"La potecia de {a} a  {b} es = {resultado}")

menu= """
1-Suma
2-Resta
3-Multiplicación
4-División
5-Potencia
Bienvenido, ¿Qué operación deseas realizar?: """

opcion= input(menu)

if opcion == "1":
    suma(numero1(), numero2())
elif opcion=="2":
    resta(numero1(), numero2())
elif opcion=="3":
    multiplicación(numero1(), numero2())
elif opcion=="4":
    división(numero1(), numero2())
elif opcion=="5":
    potencia(numero1(), numero2())
else:
    print("Elige una opción correcta")