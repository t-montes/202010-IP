import calculadora_indices as calc

print("\nEn esta función se va a calcular el índice de masa corporal de una persona.")

peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en metros): "))

IMC = calc.calcular_IMC(peso, altura)

print("\n\nTu índice de masa corporal (IMC) es", IMC)
