"""
metrica.py
Funcion reutilizable para aproximar el conteo de silabas metricas
(nucleos silabicos) de un verso griego, respetando diptongos y diaeresis.
"""

import unicodedata

VOCALES_BASE = "αεηιουωΑΕΗΙΟΥΩ"
DIPTONGOS_VALIDOS = {"αι", "ει", "οι", "υι", "αυ", "ευ", "ηυ", "ωυ"}


def _analizar_caracter(caracter):
    """Funcion auxiliar interna: devuelve (es_vocal, base_minuscula, tiene_diaeresis)."""
    descompuesto = unicodedata.normalize('NFD', caracter)
    letra_base = descompuesto[0]
    tiene_diaeresis = '\u0308' in descompuesto
    return (letra_base in VOCALES_BASE, letra_base.lower(), tiene_diaeresis)


def _contar_nucleos_palabra(palabra):
    """Funcion auxiliar interna: cuenta nucleos silabicos en UNA palabra."""
    info = [_analizar_caracter(c) for c in palabra]
    nucleos = 0
    i = 0
    while i < len(info):
        es_vocal, base, _ = info[i]
        if not es_vocal:
            i += 1
            continue
        if i + 1 < len(info):
            es_vocal_sig, base_sig, diaeresis_sig = info[i + 1]
            if es_vocal_sig and (base + base_sig) in DIPTONGOS_VALIDOS and not diaeresis_sig:
                nucleos += 1
                i += 2
                continue
        nucleos += 1
        i += 1
    return nucleos


def contar_silabas_metricas(verso):
    """
    Aproxima el numero de silabas metricas de un verso griego,
    contando nucleos silabicos (vocales sueltas o diptongos) por palabra.

    Nota: esto NO es escansion metrica completa (no distingue
    silabas largas/breves ni elision entre palabras), pero es
    la base sobre la que se construye ese analisis mas fino.
    """
    try:
        palabras = verso.split()
        return sum(_contar_nucleos_palabra(palabra) for palabra in palabras)
    except (TypeError, AttributeError):
        return 0   # si "verso" no es un string valido, evita que el programa truene


# Bloque de prueba: solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    verso = "Μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος"
    total = contar_silabas_metricas(verso)
    print(f"Verso: {verso}")
    print(f"Núcleos silábicos (aprox. sílabas): {total}")