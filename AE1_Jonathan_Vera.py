# -------------------------------------------------------------------
# S35 - Estructuración y transformación básica de datos en Python

# Jonathan Raúl Vera Gómez
# C.C. 1152697176
# 04/09/2026
# Análisis de Datos
# Quinto semestre
# Ingeniería de Software y Datos

# Para correr el archivo de manera correcta, verificar que el archivo 
# "personas.csv" se encuentre en la misma carpeta que este script.
# -------------------------------------------------------------------


import csv
import json
from collections import defaultdict


# -------------------------------------------------------------------
# PARTE 1 - Lectura de datos
# -------------------------------------------------------------------
def leer_csv(ruta_csv):
    """
    Lee el archivo csv y devuelve una lista de diccionarios con las 
    claves: nombre, edad(int), ciudad.
    """
    personas = []

    with open(ruta_csv, mode="r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            persona = {
                "nombre": fila["nombre"].strip(),
                "edad": int(fila["edad"]),
                "ciudad": fila["ciudad"].strip(),
            }
            personas.append(persona)
    return personas


# -------------------------------------------------------------------
# PARTE 2 - Transformación
# -------------------------------------------------------------------
def calcular_promedio_edad(personas):
    """
    Calcula el promedio de edad de la lista de personas.
    """
    if not personas:
        return 0
    total = sum(p["edad"] for p in personas)
    return round(total / len(personas), 2)


def contar_personas_por_ciudad(personas):
    """
    Devuelve un diccionario {ciudad: cantidad_de_personas}.
    """
    conteo = defaultdict(int)
    for p in personas:
        conteo[p["ciudad"]] += 1
    return dict(conteo)


def personas_mayores_a(personas, edad_limite=22):
    """
    Devuelve la lista de nombres de personas mayores a la edad_limite.
    """
    return [p["nombre"] for p in personas if p["edad"] > edad_limite]


# -------------------------------------------------------------------
# PARTE 3 - Exportación a JSON
# -------------------------------------------------------------------
def exportar_json(ruta_json, promedio_edad, personas_por_ciudad, mayores_22):
    """
    Exporta los resultados a un archivo JSON.
    """
    resultado = {
        "promedio_edad": promedio_edad,
        "personas_por_ciudad": personas_por_ciudad,
        "mayores_22": mayores_22,
    }

    with open(ruta_json, mode="w", encoding="utf-8") as archivo:
        json.dump(resultado, archivo, ensure_ascii=False, indent=4)
    return resultado


# -------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------------
if __name__ == "__main__":
    RUTA_CSV = "personas.csv"
    RUTA_JSON = "resultado.json"

    # Parte 1
    personas = leer_csv(RUTA_CSV)
    print(f"Se leyeron {len(personas)} registros del archivo CSV.\n")
    print("Ejemplo de los primeros 3 registros:")
    for p in personas[:3]:
        print(p)

    # Parte 2
    promedio = calcular_promedio_edad(personas)
    por_ciudad = contar_personas_por_ciudad(personas)
    mayores = personas_mayores_a(personas, 22)

    print(f"\nPromedio de edad: {promedio}")
    print(f"Personas por ciudad: {por_ciudad}")
    print(f"Personas mayores de 22 años ({len(mayores)}): {mayores}")

    # Parte 3
    resultado = exportar_json(RUTA_JSON, promedio, por_ciudad, mayores)
    print(f"\nArchivo '{RUTA_JSON}' generado correctamente.")


# -------------------------------------------------------------------
# PARTE 4 - Evidencia conceptual
# -------------------------------------------------------------------
#
# 1. ¿Qué es un objeto en Python?
#    Un objeto es una instancia de una clase: una unidad que agrupa
#    datos (atributos) y comportamientos (métodos) relacionados.
#    En Python, absolutamente todo es un objeto (números, cadenas,
#    listas, funciones, etc.), y cada uno tiene un tipo, un valor
#    y una identidad única en memoria.
#
# 2. ¿Cuál es la diferencia entre función y método?
#    Una función es un bloque de código independiente que se define
#    con "def" y se invoca por su nombre, sin pertenecer a ningún
#    objeto (ej: len(lista)). Un método es una función que está
#    definida dentro de una clase y se asocia a un objeto específico,
#    por lo que se llama usando la notación punto y siempre recibe
#    implícitamente ese objeto como primer parámetro (ej: lista.append(x)).
#
# 3. ¿Por qué las listas no son ideales para análisis masivo?
#    Las listas de Python son estructuras genéricas y dinámicas: no
#    están optimizadas para operaciones numéricas ni vectorizadas,
#    consumen más memoria (cada elemento es un objeto independiente)
#    y las operaciones sobre ellas suelen recorrerse con bucles en
#    Python puro, lo cual es lento. Para análisis masivo de datos es
#    preferible usar estructuras como los arrays de NumPy o los
#    DataFrames de Pandas, que almacenan los datos de forma contigua
#    y homogénea en memoria y permiten operaciones vectorizadas mucho
#    más rápidas y eficientes.