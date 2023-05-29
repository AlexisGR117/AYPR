# Proyecto segundo tercio. Analisis de textos.
# Autores: Angel Nicolas Cuervo Naranjo - Jefer Alexis González Romero
# Ultima fecha de modificación: 15/03/2021

# Primera entrega
# Punto 1
def cantidad_palabras(texto):
    '''Función que dice cuántas palabras tiene un texto
    (str) -> int'''
    palabras = 0
    for i in range(len(texto)):
        if texto[i] == " ":
            palabras = palabras + 1
    return palabras
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
    return conjunto_palabras
# Subprograma
def numero_silabas_palabra(palabra):
    '''Funcion que da el numero de silabas de una sola palabra
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
def cantidad_silabas(texto):
    '''Función que dado un texto da un conjunto con las palabras presentes en este y cada una con su respectivo número de silabas
    (str) -> list'''
    num_silabas_palabras = []
    conjunto_palabras = todas_las_palabras(texto)
    palabras_silabas = []
    palabras_num_silabas = []
    for i in range(len(conjunto_palabras)):
        if conjunto_palabras[i] not in palabras_silabas:
            palabras_silabas += [conjunto_palabras[i]]
            num_silabas_palabras = num_silabas_palabras + [numero_silabas_palabra(conjunto_palabras[i])]
    for i in range(len(palabras_silabas)):
        palabras_num_silabas += [palabras_silabas[i] + " - " + str(num_silabas_palabras[i])]  
    return palabras_num_silabas
# Subprograma
def numero_silabas_texto(texto):
    '''Función que dado un texto da un conjunto con el numero de sílabas que tiene cada palabra del texto
    (str) -> list'''
    num_silabas_palabras = []
    conjunto_palabras = todas_las_palabras(texto)
    for i in range(len(conjunto_palabras)):
        palabra = conjunto_palabras[i]
        num_silabas_palabras = num_silabas_palabras + [numero_silabas_palabra(palabra)]
    return num_silabas_palabras
#Punto 3
def frecuencia_silabas(texto):
    '''Función que dado un texto da la frecuencia con la que aparecen palabras monosílabas, bisílabas, trisílabas y polisílabas
    (str) -> int'''    
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
    return [monosilabas, bisilabas, trisilabas, polisilabas]
# Punto 4
def frecuencia_palabras(texto):
    '''Función que dado un texto da un conjunto con las palabras presentes en este y cada una con su respectivo número de veces que aparece en el texto
    (str) -> list)'''
    veces = []    
    palabras = todas_las_palabras(texto)
    recorrer_palabras = []
    palabras_veces = []
    for i in palabras:
        if i not in recorrer_palabras:
            recorrer_palabras += [i]
            veces += [1]
        else:
            for j in range(len(recorrer_palabras)):
                if recorrer_palabras[j] == i:
                    veces[j] = veces[j] + 1
    for i in range(len(recorrer_palabras)):
        palabras_veces += [recorrer_palabras[i] + " - " + str(veces[i])]
    return palabras_veces
# Segunda entrega
# Punto 5
def cantidad_sustantivos_plural(texto):
    '''Función que dado un texto dice cuántas posibles palabras pueden significar el plural de un sustantivo y cuales son
    (str) -> (list, int)'''    
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
    return [num_sustantivos_plural, sustantivos_plural]
# Punto 6
def cantidad_infinitivo_verbos(texto):
    '''Función que dado un texto dice cuántas posibles palabras pueden significar el infinitivo de un verbo y cuales son
    (str) -> (list, int)'''    
    palabras = todas_las_palabras(texto)
    num_infinitivos_verbos = 0
    infinitivo_verbos = []
    for i in palabras:
        if i[-2:len(i)] == "ar" or i[-2:len(i)] == "er" or i[-2:len(i)] == "ir":
            num_infinitivos_verbos += 1
            if i not in infinitivo_verbos:
                infinitivo_verbos += [i]
    return [num_infinitivos_verbos, infinitivo_verbos]
# Punto 7
def cantidad_preposiciones(texto):
    '''Función que dado un texto dice cuántas preposiciones hay y cuales son
    (str) -> (list, int)'''
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
    return [num_preposiciones, preposiciones_total]
# Punto 8
def cantidad_inicial_vocales(texto):
    '''Función que dado un texto dice cuántas palabras inician por vocal y cuales son
    (str) -> (list, int)'''
    palabras_vocal = []
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    num_palabras = 0
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[0] in vocales:
            num_palabras += 1
            if i not in palabras_vocal:
                palabras_vocal += [i]
    return [num_palabras, palabras_vocal]
# Punto 9
def cantidad_final_vocales(texto):
    '''Función que dado un texto dice cuántas palabras terminan por vocal y cuales son
    (str) -> (list, int)'''
    num_palabras = 0
    palabras_final_vocal = []
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[-1] in vocales:
            num_palabras += 1
            if i not in palabras_final_vocal:
                palabras_final_vocal += [i]
    return [num_palabras, palabras_final_vocal]
# Punto 10
def cantidad_inicial_consonantes(texto):
    '''Función que dado un texto dice cuántas palabras inician por consonante y cuales son
    (str) -> (list, int)'''
    palabras_consonante = []
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    num_palabras = 0
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[0] not in vocales:
            num_palabras += 1
            if i not in palabras_consonante:
                palabras_consonante += [i]
    return [num_palabras, palabras_consonante]
# Punto 11
def cantidad_final_consonantes(texto):
    '''Función que dado un texto dice cuántas plabras terminan por consonante y cuales son
    (str) -> (list, int)'''
    num_palabras = 0
    palabras_final_consonante = []
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[-1] not in vocales:
            num_palabras += 1
            if i not in palabras_final_consonante:
                palabras_final_consonante += [i]
    return [num_palabras, palabras_final_consonante]
# Punto 12
def cantidad_inicial_cadena(texto, cadena):
    '''Función que dado un texto dice cuántas y cuales palabras inician por una cadena dada 
    (str, str) -> (list, int)'''
    palabras = todas_las_palabras(texto)
    palabras_inicial_cadena = []
    num_palabras = 0
    for i in palabras:
        if i[0:len(cadena)] == cadena:
            num_palabras += 1
            if i not in palabras_inicial_cadena:
                palabras_inicial_cadena += [i]
    return [num_palabras, palabras_inicial_cadena]
# Punto 13
def cantidad_final_cadena(texto, cadena):
    '''Función que dado un texto dice cuántas y cuales palabras finalizan por una cadena dada 
    (str, str) -> (list, int)'''
    palabras = todas_las_palabras(texto)
    palabras_final_cadena = []
    num_palabras = 0
    for i in palabras:
        if i[-len(cadena):len(i)] == cadena:
            num_palabras += 1
            if i not in palabras_final_cadena:
                palabras_final_cadena += [i]
    return [num_palabras, palabras_final_cadena]
# Punto 14
def main():
    texto = input("Ingrese el texto que desea analizar.\n\n")
    # Punto 1
    print("\nEl texto ingresado tiene " + str(cantidad_palabras(texto) + 1) + " palabras\n")
    # Punto 2
    print("\nA continuación se presenta un conjunto con las palabras presentes en el texto con su respectivo numero de silabas: \n\n", cantidad_silabas(texto))
    # Punto 3
    [monosilabas, bisilabas, trisilabas, polisilabas] = frecuencia_silabas(texto)
    print("\nLas palabras monosílasbas aparecen en el texto " + str(monosilabas) + " veces.")
    print("Las palabras bisílasbas aparecen en el texto " + str(bisilabas) + " veces.")
    print("Las palabras trisílasbas aparecen en el texto " + str(trisilabas) + " veces.")
    print("Las palabras polisílasbas aparecen en el texto " + str(polisilabas) + " veces.\n")
    # Punto 4
    print("Conjunto con las palabras presentes en el texto con su respectivo número de apariciones: \n\n", frecuencia_palabras(texto))
    # Punto 5
    [num_sustantivos_plural, sustantivos_plural] = cantidad_sustantivos_plural(texto)
    print("\nCantidad de posibles palabras que pueden significar el plural de un sustantivo: ", num_sustantivos_plural)
    print("\nPosibles palabras que pueden significar el plural de un sustantivo: \n\n", sustantivos_plural)
    # Punto 6
    [num_infinitivos_verbos, infinitivo_verbos] = cantidad_infinitivo_verbos(texto)
    print("\nCantidad de posibles palabras que pueden significar el infinitivo de un verbo: ", num_infinitivos_verbos)
    print("\nPosibles palabras que pueden significar el infinitivo de un verbo: \n\n", infinitivo_verbos)
    # Punto 7
    [num_preposiciones, preposiciones_total] = cantidad_preposiciones(texto)
    print("\nCantidad de preposiciones en el texto: ", num_preposiciones)
    print("\nPreposicones presentes en el texto dado: \n\n", preposiciones_total)
    # Punto 8
    [num_palabras, palabras_vocal] = cantidad_inicial_vocales(texto)
    print("\nNúmero de palabras que inician por vocal en el texto dado: " + str(num_palabras))
    print("\nPalabras que inician por vocal: \n\n" + str(palabras_vocal))
    # Punto 9
    [num_palabras, palabras_final_vocal] = cantidad_final_vocales(texto)
    print("\nNúmero de palabras que terminan en vocal en el texto dado: " + str(num_palabras))
    print("\nPalabras que terminan en vocal: \n\n" + str(palabras_final_vocal))
    # Punto 10
    [num_palabras, palabras_consonante] = cantidad_inicial_consonantes(texto)
    print("\nNúmero de palabras que inician por consonante en el texto dado: " + str(num_palabras))
    print("\nPalabras que inician por consonante en el texto dado: \n\n" + str(palabras_consonante))
    # Punto 11
    [num_palabras, palabras_final_consonante] = cantidad_final_consonantes(texto)
    print("\nNúmero de palabras que terminan en consonante en el texto dado: " + str(num_palabras))
    print("\nPalabras que terminan en consonante: \n\n" + str(palabras_final_consonante))
    # Punto 12
    cadena = input("\nIngrese la cadena.\n")
    [num_palabras, palabras_inicial_cadena] = cantidad_inicial_cadena(texto, cadena)
    print("\nNúmero de palabras que inician por " + cadena + " en el texto: " + str(num_palabras))
    print("\nPalabras en el texto que inician por " + cadena +" : \n\n" + str(palabras_inicial_cadena))
    # Punto 13
    cadena = input("\nIngrese la cadena.\n")
    [num_palabras, palabras_final_cadena] = cantidad_final_cadena(texto, cadena)
    print("\nNúmero de palabras que finzalizan por " + cadena +" en el texto: " + str(num_palabras))
    print("\nPalabras en el texto que finzalizan por " + cadena +" : \n\n" + str(palabras_final_cadena))
    # Punto 14
main()
