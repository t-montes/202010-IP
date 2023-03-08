import calculadora_indices as calc

print("\nEn esta función see va a calcular la cantidad de calorías recomendadas que una persona debe"+
      "consumir a diario, en caso de que desee adelgazar.")

peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en centímetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: "))

str_cal_adel = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)

print("\n" + str_cal_adel)
