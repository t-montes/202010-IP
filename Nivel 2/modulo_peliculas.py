"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    n_pel = {}
    
    n_pel["nombre"] = nombre
    n_pel["genero"] = genero
    n_pel["duracion"] = duracion
    n_pel["anio"] = anio
    n_pel["clasificacion"] = clasificacion
    n_pel["hora"] = hora
    n_pel["dia"] = dia
    
    return n_pel


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    if(nombre_pelicula == p1["nombre"]):
        return p1
    elif(nombre_pelicula == p2["nombre"]):
        return p2
    elif(nombre_pelicula == p3["nombre"]):
        return p3
    elif(nombre_pelicula == p4["nombre"]):
        return p4
    elif(nombre_pelicula == p5["nombre"]):
        return p5
    else:
        return None
    

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    temp = p1["duracion"]
    pel = p1
    
    if(p2["duracion"] > temp):
        temp = p2["duracion"]
        pel = p2
    if(p3["duracion"] > temp):
        temp = p3["duracion"]
        pel = p3
    if(p4["duracion"] > temp):
        temp = p4["duracion"]
        pel = p4
    if(p5["duracion"] > temp):
        temp = p5["duracion"]
        pel = p5
    
    return pel
    
    

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    tiempo_p  = p1["duracion"]
    tiempo_p += p2["duracion"]
    tiempo_p += p3["duracion"]
    tiempo_p += p4["duracion"]
    tiempo_p += p5["duracion"]
    tiempo_p //= 5
    
    horas_t = tiempo_p//60
    minutos_t = tiempo_p%60
    
    if(horas_t < 10):
        formato_t = f"0{horas_t}"
    else:
        formato_t = f"{horas_t}"

    if(minutos_t < 10):
        formato_t += f":0{minutos_t}"
    else:
        formato_t += f":{minutos_t}"
    
    return formato_t

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    peliculas = ""
    
    if(p1["anio"] > anio):
        peliculas += p1["nombre"] + ","
    if(p2["anio"] > anio):
        peliculas += p2["nombre"] + ","
    if(p3["anio"] > anio):
        peliculas += p3["nombre"] + ","
    if(p4["anio"] > anio):
        peliculas += p4["nombre"] + ","
    if(p5["anio"] > anio):
        peliculas += p5["nombre"] + ","
        
    if(peliculas.endswith(',')):
        peliculas = peliculas[:-1]
    
    if(peliculas == ""):
        peliculas = "Ninguna"
    
    return peliculas


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    cont = 0
    
    if(p1["clasificacion"] == "18+"):
        cont += 1
    if(p2["clasificacion"] == "18+"):
        cont += 1
    if(p3["clasificacion"] == "18+"):
        cont += 1
    if(p4["clasificacion"] == "18+"):
        cont += 1
    if(p5["clasificacion"] == "18+"):
        cont += 1
    
    return cont

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    #Para esta función se utilizan todas las funciones recurrentes a partir de decidir_invitar.
    
    #Para verificar si se cruza con alguna otra película, se repite el proceso con todas las películas y
    # se verifica que ningun rango de horas contenga al esperado, ni viseversa.
    
    #HORA INICIAL DE LA PELÍCULA:
    hi_p = num_dia_sem(nuevo_dia)*10000 + nueva_hora
    #HORA FINAL DE LA PELÍCULA:
    hf_p = corregir_formato(hi_p + ((peli["duracion"]//60)*100 + peli["duracion"]%60))
    
    print(f"El control_horario es {control_horario}")
    
    if(verificar_cruce(hi_p, hf_p, p1) or verificar_cruce(hi_p, hf_p, p2) or verificar_cruce(hi_p, hf_p, p3) or
       verificar_cruce(hi_p, hf_p, p4) or verificar_cruce(hi_p, hf_p, p5)):
        return False
    
    if(control_horario):
        if(nueva_hora >= 2200 and peli["genero"].lower() == "documental"):
            return False
        if(num_dia_sem(nuevo_dia) == 5 and peli["genero"].lower() == "drama"):
            return False
        if((nueva_hora >= 2300 or nueva_hora <= 600) and (1 <= num_dia_sem(nuevo_dia) <= 5)):
            return False        
    
    peli["dia"] = nuevo_dia
    peli["hora"] = nueva_hora
    
    return True
    

def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    
    restriccion = 0
    if(peli["clasificacion"] == "7+"):
        restriccion = 7
    elif(peli["clasificacion"] == "13+"):
        restriccion = 13
    elif(peli["clasificacion"] == "16+"):
        restriccion = 16
    elif(peli["clasificacion"] == "18+"):
        restriccion = 18    
    
    
    if(edad_invitado < 15 and peli["genero"].lower() == "terror"):
        return False
    if(edad_invitado < 10):
        if(peli["genero"].lower() == "familiar"):
            return True
        else:
            return False
    if(edad_invitado < restriccion):
        if(peli["genero"].lower() == "documental"):
            return True
        if(autorizacion_padres):
            return True
        else:
            return False
    
    return True
    

#FUNCIONES RECURRENTES DE reagendar_pelicula:
        
#Las funciones hora_inicial y hora_final retornan un formato con el que es fácil comparar los número y rangos.
#Dicho formato es:
    
#Si la película iniciaría el Martes a las 21:30, el formato de hi_p = 22130 (hora inicial de la película)

def hora_inicial(pelicula: dict) -> int:
    
    dia = pelicula["dia"]
    hora = pelicula["hora"]
    
    hi = num_dia_sem(dia)*10000 + hora
    return hi

#Si la película inicia el Martes a las 21:30 y dura 3:40 (220 minutos)
# el nuevo formato de la hora final sería hf_p = 30110, ya que terminaría el Miércoles a la 01:10

def hora_final(pelicula: dict) -> int:
    
    dia = pelicula["dia"]
    hora = pelicula["hora"]
    duracion = pelicula["duracion"]
    
    hi = num_dia_sem(dia)*10000 + hora
    hf = corregir_formato(hi + ((duracion//60)*100 + duracion%60)) 
    return hf

#La función num_dia_sem convierte el día de str a número, siendo Lunes = 1 y Domingo = 7.

def num_dia_sem(dia: str) -> int:
    if(dia.lower() == "lunes"):
        return 1
    elif(dia.lower() == "martes"):
        return 2
    elif(dia.lower() == "miércoles"):
        return 3
    elif(dia.lower() == "jueves"):
        return 4
    elif(dia.lower() == "viernes"):
        return 5
    elif(dia.lower() == "sábado"):
        return 6
    elif(dia.lower() == "domingo"):
        return 7
    else:
        return 0
    
#La función corregir_formato se encarga de evitar que hayan más de 60 minutos en el formato, o más de 24 horas.

def corregir_formato(form: int) -> int:
    
    if(form%100 >= 60):
        form -= 60
        form += 100
    if(((form%10000 - form%100)//100) >= 24):
        form -= 2400
        form += 10000
    
    return form

#La funcion verificar_cruce, precísamente verifica que no se crucen los dos rangos dados por parámetro
#En el caso de las películas verificaría que no se crucen las horas iniciales y finales de estas.
#Retorna True si se cruzan, False de lo contrario.
    
def verificar_cruce(hi_p: int, hf_p: int, otra_peli: dict) -> bool:
    
    hi2 = hora_inicial(otra_peli)
    hf2 = hora_final(otra_peli)
    
    if(hi_p < hi2 < hf_p):
        return True
    if(hi_p < hf2 < hf_p):
        return True
    if(hi2 < hi_p < hf2):
        return True
    if(hi2 < hf_p < hf2):
        return True
    
    return False



