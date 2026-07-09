"""
analizador_verso.py
Analiza un verso griego: caracteres, palabras, vocales y
núcleos silábicos (vocales sueltas o diptongos), respetando
la diéresis como marca de hiato.
"""

import unicodedata

verso = "Μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος"

vocales_base = "αεηιουωΑΕΗΙΟΥΩ"
diptongos_validos = {"αι", "ει", "οι", "υι", "αυ", "ευ", "ηυ", "ωυ"}


def analizar_caracter(caracter):
    """Devuelve (es_vocal, letra_base_minuscula, tiene_diaeresis)."""
    descompuesto = unicodedata.normalize('NFD', caracter)
    letra_base = descompuesto[0]
    tiene_diaeresis = '\u0308' in descompuesto  # COMBINING DIAERESIS
    return (letra_base in vocales_base, letra_base.lower(), tiene_diaeresis)


def contar_nucleos_silabicos(palabra):
    """Cuenta núcleos silábicos (vocal suelta o diptongo) en una palabra."""
    info = [analizar_caracter(c) for c in palabra]
    nucleos = 0
    i = 0
    while i < len(info):
        es_vocal, base, _ = info[i]
        if not es_vocal:
            i += 1
            continue
        if i + 1 < len(info):
            es_vocal_sig, base_sig, diaeresis_sig = info[i + 1]
            par = base + base_sig
            if es_vocal_sig and par in diptongos_validos and not diaeresis_sig:
                nucleos += 1
                i += 2
                continue
        nucleos += 1
        i += 1
    return nucleos


palabras = verso.split()
print(f"Verso: {verso}\n")

total_nucleos = 0
for palabra in palabras:
    n = contar_nucleos_silabicos(palabra)
    total_nucleos += n
    print(f"  {palabra:15s} → {n} núcleo(s) silábico(s)")

print(f"\nTotal de núcleos silábicos (aprox. sílabas): {total_nucleos}")