# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:18:28 2020

@author: Tony Santiago Montes
"""

def cargar_atletas(nombre_archivo: str) -> list:
    tipo_archivo = 'csv'
    atl = []
    primera_linea = True
    llaves = []
    try:
        file = open(f'{nombre_archivo}.{tipo_archivo}', 'r')
    except:
        return []
    for i in file:
        if primera_linea:
            primera_linea = False
            llaves = i.rstrip().split(',')
            continue
        datos = i.rstrip().split(',')
        atleta = {}
        for j in range(len(llaves)):
            atleta[llaves[j]] = int(datos[j]) if datos[j].isdigit() else datos[j]
        atl.append(atleta)
    file.close()
    return atl

def atletas_por_anio(atletas: list, anio: int) -> dict:
    atl_a = {}
    for i in atletas:
        if i['anio'] == anio:
            if not i['evento'] in atl_a:
                atl_a[i['evento']] = [i['nombre']]
            else:
                atl_a[i['evento']].append(i['nombre'])
    return atl_a

def medallas_en_rango(atletas: list, anio_i: int, anio_f: int, nombre: str) -> list:
    med = []
    for i in atletas:
        if i['nombre'] == nombre.lower() and anio_i <= i['anio'] <= anio_f and i['medalla'] != 'na':
            med.append({'evento':i['evento'], 'anio':i['anio'], 'medalla':i['medalla']})
    return med

def atletas_por_pais(atletas: list, pais: str) -> list:
    atl_p = []
    for i in atletas:
        if i['pais'] == pais.lower():
            atl_p.append({'nombre':i['nombre'],'evento':i['evento'],'anio':i['anio']})
    return atl_p

def pais_con_mas_medallistas(atletas: list) -> dict:
    comparador = {}
    medallistas = []
    for i in atletas:
        if i['medalla'] != 'na' and i['nombre'] not in medallistas:
            comparador[i['pais']] = comparador.get(i['pais'], 0) + 1
        medallistas.append(i['nombre'])
    mayor = 0
    for i in comparador:
        if comparador[i] > mayor:
            mayor = comparador[i]
            pais_m = {i:comparador[i]}
    return pais_m

def medallistas_por_evento(atletas: list, evento: str) -> list:
    atl = []
    for i in atletas:
        if i['evento'] == evento.lower() and i['nombre'] not in atl:
            atl.append(i['nombre'])
    return atl

def atletas_con_mas_medallas_que(atletas: list, limite: int) -> dict:
    atls_m = {}
    for i in atletas:
        if i['medalla'] != 'na':
            atls_m[i['nombre']] = atls_m.get(i['nombre'], 0) + 1
    atletas_a_borrar = []
    for i in atls_m:
        if atls_m[i] <= limite:
            atletas_a_borrar.append(i)
    for i in atletas_a_borrar:
        del atls_m[i]
    
    return atls_m

def atleta_estrella(atletas: list) -> dict:
    atl_e = {}
    medallas = {}
    for i in atletas:
        if i['medalla'] != 'na':
            medallas[i['nombre']] = medallas.get(i['nombre'], 0) + 1
    mayor = max(medallas.values())
    for i in medallas:
        if medallas[i] == mayor:
            atl_e[i] = mayor
    return atl_e
            
def mejor_pais_en_un_evento(atletas: list, evento: str) -> dict:
    gold_p = {}
    silv_p = {}
    bron_p = {}
    pais_es = []
    for i in atletas:
        if i['medalla'] == 'gold' and i['evento'] == evento:
            gold_p[i['pais']] = gold_p.get(i['pais'], 0) + 1
        elif i['medalla'] == 'silver' and i['evento'] == evento:
            silv_p[i['pais']] = silv_p.get(i['pais'], 0) + 1
        elif i['medalla'] == 'bronze' and i['evento'] == evento:
            bron_p[i['pais']] = bron_p.get(i['pais'], 0) + 1
        else:
            gold_p[i['pais']] = gold_p.get(i['pais'], 0)
            silv_p[i['pais']] = silv_p.get(i['pais'], 0)
            bron_p[i['pais']] = bron_p.get(i['pais'], 0)
    mayor = max(gold_p.values())
    for i in gold_p:
        if gold_p[i] == mayor:
            pais_es.append(i)
    if len(pais_es) == 1:
        return {pais_es[0]:[gold_p[pais_es[0]], silv_p[pais_es[0]], bron_p[pais_es[0]]]}
    silv_p_mod = {}
    for i in silv_p:
        if i in pais_es:
            silv_p_mod[i] = silv_p[i]
    mayor = max(silv_p_mod.values())
    pais_es = []
    for i in silv_p_mod:
        if silv_p_mod[i] == mayor:
            pais_es.append(i)
    if len(pais_es) == 1:
        return {pais_es[0]:[gold_p[pais_es[0]], silv_p_mod[pais_es[0]], bron_p[pais_es[0]]]}
    bron_p_mod = {}
    for i in bron_p:
        if i in pais_es:
            bron_p_mod[i] = bron_p[i]
    mayor = max(bron_p_mod.values())
    pais_es = []
    for i in bron_p_mod:
        if bron_p_mod[i] == mayor:
            pais_es.append(i)
    final = {}
    for i in pais_es:
        final[i] = [gold_p[i], silv_p_mod[i], bron_p_mod[i]]
    return final if gold_p[i] != 0 else []
    
def todoterreno(atletas: list) -> str:
    eve_a = {}
    eventos = {}
    for i in atletas:
        if i['evento'] not in eventos.get(i['nombre'], []):
            eve_a[i['nombre']] = eve_a.get(i['nombre'], 0) + 1
            lista = eventos.get(i['nombre'], [])
            lista.append(i['evento'])
            eventos[i['nombre']] = lista
    mayor = max(eve_a.values())
    for i in eve_a:
        if eve_a[i] == mayor:
            return i
    
def medallistas_por_nacion_y_genero(atletas: list, pais: str, genero: str) -> dict:
    atl_pg = {}
    for i in atletas:
        if i['genero'] == genero and i['pais'] == pais and i['medalla'] != 'na':
            lista = atl_pg.get(i['nombre'], [])
            lista.append({'evento':i['evento'], 'anio':i['anio'], 'medalla':i['medalla']})
            atl_pg[i['nombre']] = lista
    return atl_pg

def porcentaje_medallistas(atletas: list) -> float:
    atl_m = 0
    medallistas = []
    for i in atletas:
        if i['nombre'] not in medallistas and i['medalla'] != 'na':
            medallistas.append(i['nombre'])
            atl_m += 1
    return round(atl_m/(len(atletas)),2)

#Ejercicio de Examen Práctico de Nivel 3 IP - 04/05/2020    
def medallas_del_pais(atletas: list, pais: str) -> list:
    eventos = []
    for i in atletas:
        if (i['medalla'] == 'silver' or i['medalla'] == 'gold') and i['evento'] not in eventos and i['pais'] == pais:
            eventos.append(i['evento'])
    return eventos if eventos else None

