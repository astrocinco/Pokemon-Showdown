import csv


def lector_por_numero(nro, nombre_archivo):
    """
    Lee el archivo ingresado por parametro, ignora la primera linea y retorna un diccionario con el numero de linea como llave.
    El diccionario contiene toda la información de la linea solicitada como lista.
    Retorna la información de solo un pokemon.
    """
    if type(nro) is str:
        nro = int(nro)
    contador = -1
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            leido = linea
            contador += 1
            if contador == nro:
                
                return leido[:-1].split(';')


def extraer_integrantes_equipo(equipo):
    """
    Recibe una lista con toda la información de un equipo.
    Retorna una lista de números de pokemones. 
    """
    resultado = []
    for i in range (2, len(equipo), 2):
        if equipo[i] == '': continue
        resultado.append(equipo[i])
    print ('28 |', resultado)
    return resultado


def movimiento_en_pokemon(numero, archivo):
    return 1 # HACER
