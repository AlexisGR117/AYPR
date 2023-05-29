def todas_las_palabras(texto):
    '''Función que dado un texto da un conjunto con las palabras que lo conforman
    (str) -> list'''
    posicion = 0
    conjunto_palabras = []
    nueva_posicion = 0
    signos_puntuacion = [".", ",", ";", "?", "¿", "!", "'", "¡", "...", "(", ")", "*", "[", "]", "{", "}", "-", "_", "/"]
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"
    minusculas = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    texto = texto.strip(".")
    for i in range(len(texto)):
        posicion  = posicion + 1
        a = 0
        if texto[i] == " ":
            nueva_palabra = texto[nueva_posicion:(posicion - 1)]
            for j in range(len(nueva_palabra)):
                for k in range(len(signos_puntuacion)):
                    if nueva_palabra[j] == signos_puntuacion[k] and j + 1 == len(nueva_palabra):
                        a = 1
                    elif nueva_palabra[j] == signos_puntuacion[k] and j + 1 == 1:
                        a = 2
            if a == 0:
                nueva_palabra = texto[nueva_posicion:(posicion - 1)]
            elif a == 1:
                nueva_palabra = texto[nueva_posicion:(posicion - 2)]
            else:
                nueva_palabra = texto[nueva_posicion + 1:(posicion - 1)]
            conjunto_palabras = conjunto_palabras + [nueva_palabra]
            nueva_posicion = posicion
    conjunto_palabras = conjunto_palabras + [texto[nueva_posicion:posicion]]
    for i in range(len(conjunto_palabras)):
        palabra = conjunto_palabras[i]
        for k in palabra:
            for j in range(len(mayusculas)):
                if k[0] == mayusculas[j]:
                    palabra_sin_1raletra = palabra[1:len(palabra)]
                    palabra = minusculas[j] + palabra_sin_1raletra
                    conjunto_palabras[i] = palabra
    return conjunto_palabras
def familia_palabras():
    texto = input()
    palabras = todas_las_palabras(texto)
    palabra = input()
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    palabras_familia = []
    if len(palabra) == 1 or len(palabra) == 2 or len(palabra) == 3:
        raiz = palabra
    elif len(palabra) == 4:
        vocal = 0
        for i in vocales:
            if palabra[-1] == i:
                vocal = 1
        if vocal == 1:
            raiz = palabra[0:-1]
        else:
            raiz = palabra
    else:
        vocal = 0
        for i in vocales:
            if palabra[3] == i:
                vocal = 1
        if vocal == 1:
            raiz = palabra[0:3]
        else:
            raiz = palabra[0:4]
    print(raiz)
    for i in palabras:
        for j in range(len(i)):
            if j + len(raiz) <= len(i):
                if i[j:j + len(raiz)] == raiz and i not in palabras_familia:
                        palabras_familia += [i]
    print(palabras_familia)
familia_palabras()
        
