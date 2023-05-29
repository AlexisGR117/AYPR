def silabas(palabra):
    """Funcion que dada una palabra da el numero de silabas que tiene esta
    (str) -> int"""
    vocales = ["a", "e", "i", "o", "u"]
    silabas = 0
    for i in palabra:
        for j in range(len(vocales)):
            if i == vocales[j]:
                silabas += 1
    return silabas

