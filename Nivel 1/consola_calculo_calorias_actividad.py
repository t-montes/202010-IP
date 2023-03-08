import calculadora_indices as calc

print("\nEn esta función se va a calcular la cantidad de calorías que quema una persona en actividad.")

peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en centímetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: "))
valor_actividad = float(input("Ingrese el valor que corresponda a su actividad física semanal:"
    +"\n\t1.2: poco o ningún ejercicio"
    +"\n\t1.375: ejercicio ligero (1 a 3 días a la semana)"
    +"\n\t1.55: ejercicio moderado (3 a 5 días a la semana)"
    +"\n\t1.72: deportista (6 a 7 días a la semana)\n\t1.9: atleta (entrenamientos mañana y tarde)\n"))

TMB_act = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)

print("\n\nEl número de calorías que quemas en actividad es", TMB_act)
