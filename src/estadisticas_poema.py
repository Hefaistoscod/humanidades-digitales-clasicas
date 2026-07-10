"""
estadisticas_poema.py
Script de linea de comandos: recibe la ruta a un archivo .txt
con un poema clasico y devuelve estadisticas basicas.
"""

import sys
from metrica import contar_silabas_metricas


def cargar_versos(ruta_archivo):
    """Lee un archivo de texto y devuelve una lista de versos (sin lineas vacias)."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        return [linea.strip() for linea in lineas if linea.strip()]
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo: {ruta_archivo}")
        return []


PUNTUACION = ".,;:·!?«»\"()[]"
ELISION_VARIANTES = "᾽᾿'’ʼ`´"   # todas las formas de apostrofo de elision que puedas encontrar


def normalizar_palabra(palabra):
    """
    Normaliza una palabra para conteo de frecuencias:
    minusculas, sin puntuacion en los bordes, y sin marcas de
    elision, sea cual sea el caracter Unicode exacto usado en la fuente.
    """
    palabra = palabra.lower().strip(PUNTUACION)
    palabra = palabra.rstrip(ELISION_VARIANTES)  # la elision siempre va al final de la palabra
    return palabra


def palabra_mas_frecuente(versos):
    """Devuelve la palabra que mas se repite en todo el poema."""
    frecuencias = {}
    for verso in versos:
        for palabra in verso.split():
            palabra_normalizada = normalizar_palabra(palabra)
            if palabra_normalizada:  # evita contar strings vacios si algo se recorta por completo
                frecuencias[palabra_normalizada] = frecuencias.get(palabra_normalizada, 0) + 1

    if not frecuencias:
        return None, 0

    palabra_top = max(frecuencias, key=frecuencias.get)
    return palabra_top, frecuencias[palabra_top]


def longitud_media_verso(versos):
    """Promedio de caracteres por verso."""
    if not versos:
        return 0
    total_caracteres = sum(len(verso) for verso in versos)
    return total_caracteres / len(versos)

def longitud_media_verso_palabras(versos):
    """Promedio de palabras por verso."""
    if not versos:
        return 0
    total_palabras = sum(len(verso.split()) for verso in versos)
    return total_palabras / len(versos)

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 estadisticas_poema.py <ruta_al_archivo.txt>")
        return

    ruta = sys.argv[1]
    versos = cargar_versos(ruta)

    if not versos:
        return

    palabra_top, frecuencia = palabra_mas_frecuente(versos)
    longitud_media_caracteres = longitud_media_verso(versos)
    longitud_media_palabras = longitud_media_verso_palabras(versos)
    total_silabas = sum(contar_silabas_metricas(v) for v in versos)

    print(f"Archivo analizado: {ruta}")
    print(f"Número de versos: {len(versos)}")
    print(f"Palabra más frecuente: '{palabra_top}' ({frecuencia} vez/veces)")
    print(f"Longitud media de verso (caracteres): {longitud_media_caracteres:.1f}")
    print(f"Longitud media de verso (palabras): {longitud_media_palabras:.1f}")
    print(f"Total de núcleos silábicos (aprox.): {total_silabas}")


if __name__ == "__main__":
    main()