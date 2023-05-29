# Proyecto segundo tercio. Analisis de textos.
# Autores: Angel Nicolas Cuervo Naranjo - Jefer Alexis González Romero
# Ultima fecha de modificación: 15/03/2021

# Primera entrega
# Punto 1
def cantidad_palabras():
    '''Función que dice cuántas palabras tiene un texto
    (str) -> int'''
    texto = str(input("Ingrese el texto al cual desea saber cuantas palabras tiene.\n"))
    palabras = 0
    for i in range(len(texto)):
        if texto[i] == " ":
            palabras = palabras + 1     
    print("El texto ingresado tiene: " + str(palabras + 1) + " palabras")
# Subprograma
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
    return(conjunto_palabras)
# Subprograma
def numero_silabas_palabra(palabra):
    '''Funcion que da el numero de silabas de una palabra
    (str) -> int'''
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    diptongos = ["ai", "au", "ei", "eu", "io", "ou", "ia", "ua", "ie", "ue", "oi", "uo", "ui", "iu", "ay", "ey", "oy"]
    triptongos = ["iai", "iei", "uai", "uei", "uau", "iau", "uay", "uey"]
    num_vocales = 0
    recorrer = palabra
    silabas = 0
    for i in range(len(palabra)):
        for j in range(len(vocales)):
            if palabra[i] == vocales[j]:
                silabas = silabas + 1
    if len(recorrer) == 1 and recorrer[0] == "y":
        silabas = silabas + 1
    for i in range(len(recorrer)):
        if i + 3 <= len(recorrer):
            if recorrer[i:i + 2] == "qu" or recorrer[i:i + 2] == "gu":
                for j in range(len(vocales)):
                    if recorrer[i + 2] == vocales[j]:
                        silabas = silabas - 1
                recorrer = str(recorrer[0:i + 1]) + str(recorrer[i + 2:len(recorrer)])
        if i + 3 <= len(recorrer):
            for j in range(len(triptongos)):
                if recorrer[i:i + 3] == triptongos[j]:
                    if recorrer[i + 2] == "y":
                        silabas = silabas + 1 
                    silabas = silabas - 2
                    recorrer = str(recorrer[0:i]) + str(recorrer[i + 3:len(recorrer)])
        if i + 2 <= len(recorrer):
            for j in range(len(diptongos)):
                if recorrer[i:i + 2] == diptongos[j]:
                    if recorrer[i + 1] == "y":
                        silabas = silabas + 1 
                    silabas = silabas - 1
                    recorrer = str(recorrer[0:i]) + str(recorrer[i + 2:len(recorrer)])
    return silabas
# Punto 2
def cantidad_silabas():
    '''Función que dado un texto da un conjunto con las palabras presentes en el texto y otro conjunto con el número de silabas que tiene cada palabra
    (str) -> (list, list)'''
    texto = str(input("Ingrese el texto al cual desea conocer el numero de silabas que tiene cada palabra de este.\n"))
    num_silabas_palabras = []
    conjunto_palabras = todas_las_palabras(texto)
    palabras_silabas = []
    for i in range(len(conjunto_palabras)):
        if conjunto_palabras[i] not in palabras_silabas:
            palabras_silabas += [conjunto_palabras[i]]
            num_silabas_palabras = num_silabas_palabras + [numero_silabas_palabra(conjunto_palabras[i])]
    print("Las palabras presentes en el texto son: ", palabras_silabas)
    print("El numero de silabas de cada palabra en el texto es: " + str(num_silabas_palabras))
# Subprograma
def numero_silabas_texto(texto):
    '''Función que dado un texto da un conjunto con el numero de sílabas que tiene cada palabra del texto
    (str) -> list'''
    num_silabas_palabras = []
    conjunto_palabras = todas_las_palabras(texto)
    for i in range(len(conjunto_palabras)):
        palabra = conjunto_palabras[i]
        num_silabas_palabras = num_silabas_palabras + [numero_silabas_palabra(palabra)]
    return(num_silabas_palabras)
#Punto 3
def frecuencia_silabas():
    '''Función que dado un texto da la frecuencia con la que aparecen palabras monosílabas, bisílabas, trisílabas y polisílabas
    (str) -> int'''
    texto = input("Ingrese el texto al cual desea conocer la frecuencia con la que aparecen las palabras monosílabas, bisílabas, trisílasbas y polisílabas.\n")
    num_silabas_palabras = numero_silabas_texto(texto)
    monosilabas = 0
    bisilabas = 0
    trisilabas = 0
    polisilabas = 0
    for i in range(len(num_silabas_palabras)):
        if num_silabas_palabras[i] == 1:
            monosilabas = monosilabas + 1
        elif num_silabas_palabras[i] == 2:
            bisilabas = bisilabas + 1
        elif num_silabas_palabras[i] == 3:
            trisilabas = trisilabas + 1
        else:
            polisilabas = polisilabas + 1
    print("Las palabras monosílasbas aparecen en el texto " + str(monosilabas) + " veces.")
    print("Las palabras bisílasbas aparecen en el texto " + str(bisilabas) + " veces.")
    print("Las palabras trisílasbas aparecen en el texto " + str(trisilabas) + " veces.")
    print("Las palabras polisílasbas aparecen en el texto " + str(polisilabas) + " veces.")
# Punto 4
def frecuencia_palabras():
    '''Función que dado un texto da un conjunto con las palabras presentes en el texto y otro conjunto con el número de veces que aparece cada palabra
    (str) -> (list, list)'''
    veces = []
    texto = input("Ingrese el texto al cual desea conocer la frecuencia con la que aparecen cada palabra presente en este.\n")
    palabras = todas_las_palabras(texto)
    recorrer_palabras = []
    for i in palabras:
        if i not in recorrer_palabras:
            recorrer_palabras.append(i)
            veces.append(1)
        else:
            for j in range(len(recorrer_palabras)):
                if recorrer_palabras[j] == i:
                    veces[j] = veces[j] + 1
    print("Las palabras presentes en el texto son: " + str(recorrer_palabras))
    print("La cantidad de veces que aparece cada palabra en la lista anterior es: " + str(veces))
# Segunda entrega
# Punto 5
def cantidad_sustantivos_plural():
    '''Función que dado un texto dice cuántas posibles palabras pueden significar el plural de un sustantivo y cuales son
    (str) -> (list, int)'''
    texto = input("Ingrese el texto al cual desea saber el número de palabras que pueden significar el plural de un sustantivo y cuales son.\n")
    palabras = todas_las_palabras(texto)
    num_sustantivos_plural = 0
    sustantivos_plural = []
    excepciones = ["es", "las", "los", "todos", "todas", "ellos", "ellas", "unos", "unas", "nosotros", "nosotras", "ustedes", "vosotros", "vosotras", "sus", "mas", "más"]
    for i in palabras:
        if i not in excepciones:
            if i[-1] == "s":
                num_sustantivos_plural += 1
                if i not in sustantivos_plural:
                    sustantivos_plural += [i]
    print("Posibles palabras que pueden significar el plural de un sustantivo: ", sustantivos_plural)
    print("Cantidad de posibles palabras que pueden significar el plural de un sustantivo: ", num_sustantivos_plural)
# Punto 6
def cantidad_infinitivo_verbos():
    '''Función que dado un texto dice cuántas posibles palabras pueden significar el infinitivo de un verbo y cuales son
    (str) -> (list, int)'''
    texto = input("Ingrese el texto al cual desea saber el número de palabras que pueden significar el infinitivo de un verbo y cuales son.\n")
    palabras = todas_las_palabras(texto)
    num_infinitivos_verbos = 0
    infinitivo_verbos = []
    for i in palabras:
        if i[-2:len(i)] == "ar" or i[-2:len(i)] == "er" or i[-2:len(i)] == "ir":
            num_infinitivos_verbos += 1
            if i not in infinitivo_verbos:
                infinitivo_verbos += [i]
    print("Posibles palabras que pueden significar el infinitivo de un verbo: ", infinitivo_verbos)
    print("Cantidad de posibles palabras que pueden significar el infinitivo de un verbo: ", num_infinitivos_verbos)
# Punto 7
def cantidad_preposiciones():
    '''Función que dado un texto dice cuántas preposiciones hay y cuales son
    (str) -> (list, int)'''
    texto = input("Ingrese el texto al cual desea saber el número de preposiciones y cuales son.\n")
    preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía", "atras"]
    palabras = todas_las_palabras(texto)
    num_preposiciones = 0
    preposiciones_total = []
    for i in palabras:
        for j in preposiciones:
            if i == j:
                num_preposiciones += 1
                if i not in preposiciones_total:
                    preposiciones_total += [i]
    print("Preposicones presentes en el texto dado: ", preposiciones_total)
    print("Cantidad de preposiciones en el texto: ", num_preposiciones)
# Punto 8
def cantidad_inicial_vocales():
    '''Función que dado un texto dice cuántas palabras inician por vocal y cuales son
    (str) -> (list, int)'''
    palabras_vocal = []
    texto = input("Ingrese el texto al cual desea saber el numero de palabras que inician por vocal y cuales son.\n")
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    num_palabras = 0
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[0] in vocales:
            num_palabras += 1
            if i not in palabras_vocal:
                palabras_vocal += [i]
    print("Palabras que inicial por vocal en el texto dado: " + str(palabras_vocal))
    print("Numero de palabras que inician por vocal en el texto dado: " + str(num_palabras))
# Punto 9
def cantidad_final_vocales():
    '''Función que dado un texto dice cuántas palabras terminan por vocal y cuales son
    (str) -> (list, int)'''
    num_palabras = 0
    palabras_final_vocal = []
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    texto = input("Ingrese el texto al cual desea saber el número de palabras que terminan por vocal y cuales son.\n")
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[-1] in vocales:
            num_palabras += 1
            if i not in palabras_final_vocal:
                palabras_final_vocal += [i]
    print("Palabras que terminan en vocal en el texto dado: " + str(palabras_final_vocal))
    print("Número de palabras que terminan en vocal en el texto dado: " + str(num_palabras))
# Punto 10
def cantidad_inicial_consonantes():
    '''Función que dado un texto dice cuántas palabras inician por consonante y cuales son
    (str) -> (list, int)'''
    palabras_consonante = []
    texto = input("Ingrese el texto al cual desea saber el número de palabras que inician por consonante y cuales son.\n")
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    num_palabras = 0
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[0] not in vocales:
            num_palabras += 1
            if i not in palabras_consonante:
                palabras_consonante += [i]
    print("Palabras que inicial por consonante en el texto dado: " + str(palabras_consonante))
    print("Número de palabras que inician por consonante en el texto dado: " + str(num_palabras))
# Punto 11
def cantidad_final_consonantes():
    '''Función que dado un texto dice cuántas plabras terminan por consonante y cuales son
    (str) -> (list, int)'''
    num_palabras = 0
    palabras_final_consonante = []
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    texto = input("Ingrese el texto al cual desea saber el número de palabras que terminan por consonante y cuales son.\n")
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[-1] not in vocales:
            num_palabras += 1
            if i not in palabras_final_consonante:
                palabras_final_consonante += [i]
    print("Palabras que terminan en consonante en el texto dado: " + str(palabras_final_consonante))
    print("Número de palabras que terminan en consonante en el texto dado: " + str(num_palabras))
# Punto 12
def cantidad_inicial_cadena():
    '''Función que dado un texto dice cuántas y cuales palabras inician por una cadena dada 
    (str, str) -> (list, int)'''
    texto = input("Ingrese el texto al cual desea saber el número de palabras que inician por una cadena dada y cuales son.\n")
    cadena = input("Ingrese la cadena.\n")
    palabras = todas_las_palabras(texto)
    palabras_inicial_cadena = []
    num_palabras = 0
    for i in palabras:
        if i[0:len(cadena)] == cadena:
            num_palabras += 1
            if i not in palabras_inicial_cadena:
                palabras_inicial_cadena += [i]
    print("Palabras en el texto que inician por la cadena dada: " + str(palabras_inicial_cadena))
    print("Número de palabras que inician por la cadena dada en el texto: " + str(num_palabras))
# Punto 13
def cantidad_final_cadena():
    '''Función que dado un texto dice cuántas y cuales palabras finalizan por una cadena dada 
    (str, str) -> (list, int)'''
    texto = input("Ingrese el texto al cual desea saber el número de palabras que finzalizan por una cadena dada y cuales son.\n")
    cadena = input("Ingrese la cadena.\n")
    palabras = todas_las_palabras(texto)
    palabras_final_cadena = []
    num_palabras = 0
    for i in palabras:
        if i[-len(cadena):len(i)] == cadena:
            num_palabras += 1
            if i not in palabras_final_cadena:
                palabras_final_cadena += [i]
    print("Palabras en el texto que finzalizan por la cadena dada: " + str(palabras_final_cadena))
    print("Número de palabras que finzalizan por la cadena dada: " + str(num_palabras))
# Punto 14
   
