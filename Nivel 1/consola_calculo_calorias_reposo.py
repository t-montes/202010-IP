import calculadora_indices as calc

print("\nEn esta función se va a calcular la cantidad de calorías que quema una persona en reposo.")

peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en centímetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: "))

TMB = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)

print("\n\nEl número de calorías que quemas en reposo es", TMB)
