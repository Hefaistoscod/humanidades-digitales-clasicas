"""
toponimos_pausanias.py
Lista de toponimos mencionados en el recorrido de Pausanias
por la Corintia (Descripcion de Grecia, Libro 2), ordenados
alfabeticamente y clasificados por tipo.
"""

# Cada tupla: (toponimo, tipo)
lugares_pausanias = [
    ("Corinto", "ciudad"),
    ("Istmo", "accidente geografico"),
    ("Cencreas", "puerto"),
    ("Lecaion", "puerto"),
    ("Acrocorinto", "acropolis"),
    ("Sicion", "ciudad"),
    ("Titane", "ciudad"),
    ("Flio", "ciudad"),
]

# Lista simple de nombres, ordenada alfabeticamente
nombres_ordenados = sorted(lugar[0] for lugar in lugares_pausanias)

print("Topónimos ordenados alfabéticamente:")
for nombre in nombres_ordenados:
    print(f"  - {nombre}")

# Comprension de lista: solo las ciudades (filtrando por el segundo elemento de la tupla)
ciudades = [lugar[0] for lugar in lugares_pausanias if lugar[1] == "ciudad"]

print(f"\nCiudades mencionadas ({len(ciudades)}):")
for ciudad in sorted(ciudades):
    print(f"  - {ciudad}")

# Comprension de lista: solo los que NO son ciudades (puertos, accidentes, acropolis)
otros_lugares = [lugar[0] for lugar in lugares_pausanias if lugar[1] != "ciudad"]

print(f"\nOtros tipos de lugar ({len(otros_lugares)}):")
for lugar in sorted(otros_lugares):
    print(f"  - {lugar}")