def cantidad_palabras(texto):
    '''Funcion que dado un texto da un conjunto con las palabras que lo conforman
    (str) -> str'''
    posicion = 0
    conjunto_palabras = []
    nueva_posicion = 0
    signos_puntuacion = [".", ",", ";", "?", "¿", "!", "'", "¡", "...", "(", ")", "*", "[", "]", "{", "}", "-", "_", "/"]
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
    return(conjunto_palabras)
def posicion_vocal(palabra, posicion):
    '''Funcion que indica en que posicion se encuentra una vocal con respescto a una posicion incial
    (str, int) -> int'''
    vocales = ["a", "e", "i", "o", "u"]
    buscar = posicion
    inicio = posicion
    while buscar == inicio and posicion + 1 <= len(palabra):
        for i in range(len(vocales)):
            if palabra[posicion] == vocales[i]:
                buscar = buscar + 1
        posicion = posicion + 1
    return (posicion - 1)
def silabas(palabra, posicion_voc, posicion):
    '''Funcion que devuelve la silaba dada una posicion incial y la posicion de la vocal
    (str, int, int) -> str'''
    diptongos_in = ["ai", "au", "ei", "eu", "io", "ou", "ia", "ua", "ie", "ue", "oi", "uo", "ui", "iu", "ay", "ey", "oy"]
    vocales = ["a", "e", "i", "o", "u"]
    consonanticos = ["br", "bl", "cn", "cr", "cl", "dr", "fr", "fl", "gr", "gl", "ll", "pr", "pl", "tr", "rr", "ch"] 
    a = 0
    b = 0
    c = 0
    d = 0
    if posicion_voc + 3 <= len(palabra):
        for i in range(len(vocales)):
            if palabra[posicion_voc + 2] == vocales[i]:
                b = 1
    else:
        b = 2
    if  posicion_voc + 2 <= len(palabra):
        for i in range(len(vocales)):
            if palabra[posicion_voc + 1] == vocales[i]:
                a = 1
    else:
        a = 2
    if  posicion_voc + 4 <= len(palabra):
        for i in range(len(vocales)):
            if palabra[posicion_voc + 3] == vocales[i]:
                d = 1
    else:
        d = 2
    if a == 0 and b == 0:
        for i in range(len(consonanticos)):
            if  palabra[posicion_voc + 1:posicion_voc + 3] == consonanticos[i]:
                c = 1
        if c == 1:
            silaba = palabra[posicion:posicion_voc + 1]
        else:
            silaba = palabra[posicion:posicion_voc + 2]
    elif a == 0 and b == 1:
        silaba = palabra[posicion:posicion_voc + 1]
    elif a == 1:
        for i in range(len(diptongos_in)):
            if palabra[posicion_voc:posicion_voc + 2] == diptongos_in[i]:
                c = 1
        if c == 1:
            if (b == 0 and d == 0) or (b == 0 and d == 2):
                silaba = palabra[posicion:posicion_voc + 3]
            elif (b == 0 and d == 1) or (b == 2 and d == 2):
                silaba = palabra[posicion:posicion_voc + 2]
        else:
            silaba = palabra[posicion:posicion_voc + 1]
    elif a == 0 and b == 2:
        silaba = palabra[posicion:posicion_voc + 2]
    elif a == 2:
        silaba = palabra[posicion:posicion_voc + 1]
    return silaba
def main():
    '''Funcion que dado un texto da un conjunto con el numero de silabas que tiene cada palabra del texto
    (str) -> int'''
    texto = str(input("Ingrese el texto al cual desea conocer el numero de silabas que tiene cada palabra de este.\n"))
    num_silabas_palabras = []
    conjunto_palabras = cantidad_palabras(texto)
    for i in range(len(conjunto_palabras)):
        palabra = conjunto_palabras[i]
        posicion = 0
        conjunto_silabas = []
        contador = 0
        while posicion + 1 <= len(palabra):
            posicion_voc = posicion_vocal(palabra, posicion)
            nueva_silaba = silabas(palabra, posicion_voc, posicion)
            conjunto_silabas = conjunto_silabas + [nueva_silaba]
            posicion = posicion + len(nueva_silaba) 
        num_silabas_palabras = num_silabas_palabras + [len(conjunto_silabas)]
    print("El numero de silabas de cada palabra en el texto es: " + str(num_silabas_palabras))
main()
