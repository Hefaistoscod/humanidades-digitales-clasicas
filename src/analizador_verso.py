"""
analizador_verso.py
Analiza un verso griego y devuelve estadísticas básicas:
número de caracteres, palabras y vocales — usando normalización
Unicode para detectar correctamente vocales acentuadas y con espíritus.
"""

import unicodedata

verso = "Μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος"

vocales_base = "αεηιουωΑΕΗΙΟΥΩ"

def es_vocal(caracter):
    """Determina si un carácter es una vocal griega,
    sin importar qué acento o espíritu lleve encima."""
    descompuesto = unicodedata.normalize('NFD', caracter)
    letra_base = descompuesto[0]   # el primer componente es siempre la letra sin diacríticos
    return letra_base in vocales_base

num_caracteres = len(verso)
palabras = verso.split()
num_palabras = len(palabras)

num_vocales = sum(1 for letra in verso if es_vocal(letra))

print(f"Verso: {verso}")
print(f"Número de caracteres: {num_caracteres}")
print(f"Número de palabras: {num_palabras}")
print(f"Número de vocales: {num_vocales}")