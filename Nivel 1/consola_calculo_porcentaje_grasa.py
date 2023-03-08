import calculadora_indices as calc

print("\nEn esta función se va a calcular el porcentaje de masa corporal de una persona.")

peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en metros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: "))

GC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

print("n\nTu porcentaje de grasa corporal (%GC) es", GC)
