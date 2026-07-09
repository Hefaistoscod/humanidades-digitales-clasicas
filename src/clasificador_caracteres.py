"""
clasificador_caracteres.py
Clasifica cada caracter de un texto griego politónico como
vocal, consonante, signo diacritico o espacio/puntuacion.
"""

import unicodedata

texto = "Μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος"

vocales_base = "αεηιουωΑΕΗΙΟΥΩ"
consonantes_base = "βγδζθκλμνξπρστφχψςΒΓΔΖΘΚΛΜΝΞΠΡΣΤΦΧΨ"

for caracter in texto:
    descompuesto = unicodedata.normalize('NFD', caracter)
    letra_base = descompuesto[0]

    if letra_base in vocales_base:
        categoria = "vocal"
    elif letra_base in consonantes_base:
        categoria = "consonante"
    elif unicodedata.combining(caracter) != 0:
        # combining() devuelve distinto de 0 si el caracter ES,
        # el mismo, una marca diacritica suelta (no debería pasar
        # aqui porque recorremos el texto en forma NFC, pero lo
        # dejamos como salvaguarda)
        categoria = "signo diacritico"
    elif caracter.isspace():
        categoria = "espacio"
    else:
        categoria = "otro / puntuacion"

    print(f"{caracter!r:8s} → {categoria}")