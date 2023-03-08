def calcular_IMC (peso: float, altura: float)-> float:
    return round((peso)/(altura**2), 2)

def calcular_porcentaje_grasa (peso: float, altura: float, edad: int, valor_genero: float) -> float:
    return round(1.2*calcular_IMC(peso, altura) + 0.23*edad -5.4 - valor_genero, 2)

def calcular_calorias_en_reposo (peso: float, altura: float, edad: int, valor_genero: float) -> float:
    return round(10*peso + 6.25*altura -5*edad + valor_genero, 2)

def calcular_calorias_en_actividad (peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float) -> float:
    return round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*valor_actividad, 2)

def consumo_calorias_recomendado_para_adelgazar (peso: float, altura: float, edad: int, valor_genero: float) -> str:
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return "Para adelgazar es recomendado que consumas entre: "+str(round(0.8*TMB, 2))+" y "+str(round(0.85*TMB, 2))+" calorías al día"
