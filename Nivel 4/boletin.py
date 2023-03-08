# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Modulo de Funciones

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2


"""

def cargar_matriz_estadisticas(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de estadisticas 
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """  
    try:
        archivo = open(ruta_archivo)
    except:
        return []
    linea = archivo.readline().rstrip()
    facultades = 11
    elementos = 9
    estadisticas = []
    for i in range(0,facultades+1):
        estadisticas.append([0]*(elementos+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,elementos+1):
            try:
                estadisticas[i][j] = int(datos[j])
            except:
                try:
                    estadisticas[i][j] = float(datos[j])
                except:
                    estadisticas[i][j] = datos[j]
        i += 1 
        linea = archivo.readline().rstrip()
    archivo.close()
    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    try:
        archivo1 = open(ruta_archivo)
    except:
        return []
    linea = archivo1.readline().rstrip()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0,oferentes+1):
        puestos.append([0] * (ocupantes+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,ocupantes+1):
            try:
                puestos[i][j] = int(datos[j])
            except:
                try:
                    puestos[i][j] = float(datos[j])
                except:
                    puestos[i][j] = datos[j]
        i += 1 
        linea = archivo1.readline().rstrip()
    archivo1.close()
    return puestos

#TODO Implemente las demas funciones de su programa

def cargar_matriz_dobles(ruta_archivo: str) -> list:
    try:
        archivo2 = open(ruta_archivo)
    except:
        return []
    linea = archivo2.readline().rstrip()
    carreras = 35
    dobles = []
    for i in range(carreras + 1):
        dobles.append([0]* (carreras + 1))
    
    i = 0
    while len(linea) > 0:
        datos = linea.split(',')
        for j in range(carreras + 1):
            try:
                dobles[i][j] = int(datos[j])
            except:
                try:
                    dobles[i][j] = float(datos[j])
                except:
                    dobles[i][j] = datos[j]
        i += 1
        linea = archivo2.readline().rstrip()
    archivo2.close()
    return dobles

def puestos_ofrecidos_por_facultad(puestos: list, facultad: str) -> int:
    pof = 0
    for i in range(1, len(puestos)):
        if puestos[i][0] == facultad:
            for j in range(1, len(puestos[i])):
                pof += puestos[i][j]
    return pof

def puestos_ocupados_por_facultad(puestos: list, facultad: str) -> int:
    poc = 0
    for i in range(1, len(puestos)):
        for j in range(1, len(puestos[i])):
            if puestos[0][j] == facultad:
                poc += puestos[i][j]
    return poc

def facultad_mas_servicial(puestos: list) -> tuple:
    mayor_ptje = 0
    for i in range(1, len(puestos)):
        propios = 0
        pof = puestos_ofrecidos_por_facultad(puestos, puestos[i][0])
        for j in range(1, len(puestos[i])):
            if i != j:
                propios += puestos[i][j]
        porcentaje = (propios/pof)*100
        if porcentaje > mayor_ptje:
            mayor_ptje = porcentaje
            tup_fac = (puestos[i][0], round(porcentaje, 2))
    return tup_fac
    
def existe_facultad_generosa(puestos: list, facultad: str, porcentaje: float) -> tuple:
    puestos_tot = puestos_ocupados_por_facultad(puestos, facultad)
    ptje_puestos = int(puestos_tot*porcentaje/100)
    for i in range(1, len(puestos)):
        if puestos[i][0] != facultad:
            for j in range(1, len(puestos)):
                if puestos[0][j] == facultad:
                    if puestos[i][j] > ptje_puestos:
                        return (puestos[i][0],round((puestos[i][j]/puestos_tot)*100,2))
    return ("No existe facultad generosa", 0)
    
def porcentaje_autocubrimiento(puestos: list, estadisticas: list) -> list:
    for i in range(len(puestos)):
        if puestos[i][0]:
            ptje = (puestos_ocupados_por_facultad(puestos, puestos[i][0]))
            ptje /= (puestos_ofrecidos_por_facultad(puestos, puestos[i][0]))
            ptje = round(ptje,2)
            ptje *= 100
        else:
            ptje = 'Autocubrimiento %'
        estadisticas[i].append(ptje)
    return estadisticas

def dic_dobles(dobles: list) -> dict:
    num_dobles = {}
    for i in range(1, len(dobles)):
        for j in range(1, len(dobles[i])):
            if i != j:
                key = f'{dobles[i][0]} - {dobles[0][j]}'
                key2 = f'{dobles[0][j]} - {dobles[i][0]}'
                if key2 in num_dobles:
                    num_dobles[key2] += dobles[i][j]
                elif key in num_dobles:
                    num_dobles[key] += dobles[i][j]
                else:
                    num_dobles[key] = dobles[i][j]
    return num_dobles

def doble_programa_mas_popular(dobles: list) -> tuple:
    num_dobles = dic_dobles(dobles)
    mayor = 0
    for i in num_dobles:
        if num_dobles[i] > mayor:
            mayor = num_dobles[i]
            tup = (i, num_dobles[i])
    return tup

def dobles_con_programa_de_interes(dobles: list, programa: str) -> dict:
    num_dobles = dic_dobles(dobles)
    dob_prog = {}
    for i in num_dobles:
        if programa in i and num_dobles[i] != 0:
            key = i.replace(programa, '')
            key = key[3:] if key.find('-') == 1 else key[:-3]
            dob_prog[key] = num_dobles[i]
    return dob_prog

def estadisticas_pga(estadisticas: list) -> list:
    promedio = 0
    cont = 0
    mayor = 0
    menor = 5
    for i in range(len(estadisticas)):
        for j in range(len(estadisticas[i])):
            if 'pga' in estadisticas[0][j].lower() and estadisticas[i][0]:
                promedio += estadisticas[i][j]
                cont += 1
                if estadisticas[i][j] > mayor:
                    mayor = estadisticas[i][j]
                    tup_mayor = (estadisticas[i][0], estadisticas[i][j])
                if estadisticas[i][j] < menor:
                    menor = estadisticas[i][j]
                    tup_menor = (estadisticas[i][0], estadisticas[i][j])
    promedio = round(promedio/cont,2)
    for i in range(len(estadisticas)):
        for j in range(len(estadisticas[i])):
            if 'pga' in estadisticas[0][j].lower() and estadisticas[i][j] == promedio:
                return [tup_mayor, tup_menor, (estadisticas[i][0], estadisticas[i][j])]
    return [tup_mayor,tup_menor, (None, promedio)]

def facultad_con_porcentaje_de_genero(estadisticas: list, genero: str, porcentaje: float) -> tuple:
    for i in range(len(estadisticas)):
        num_gen = 0
        total = 0
        for j in range(len(estadisticas[i])):
            if'estudiante' in estadisticas[0][j].lower() and estadisticas[i][0]:
                if genero in estadisticas[0][j].lower():
                    num_gen = estadisticas[i][j]
                    total += estadisticas[i][j]
                else:
                    total += estadisticas[i][j]
        if num_gen == 0:
            continue
        if estadisticas[i][0] and (num_gen/total)*100 > porcentaje:
            return (True, estadisticas[i][0], round((num_gen/total)*100, 2))
    return (False, '', 0)
        
me = cargar_matriz_estadisticas('estadisticas_facultades.csv')
mp = cargar_matriz_puestos('matriz_puestos.csv')
md = cargar_matriz_dobles('matriz_dobles.csv')

    