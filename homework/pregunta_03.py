"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    sumas = {}
    with open("files/input/data.csv", "r") as data:
        for line in data:
            renglon = line.strip().split("\t")
            if renglon[0] not in sumas:
                sumas[renglon[0]] = int(renglon[1])
            else:
                sumas[renglon[0]] += int(renglon[1])
        sumas_ordenadas = sorted(sumas.items())
        return sumas_ordenadas

#print(pregunta_03())

"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
