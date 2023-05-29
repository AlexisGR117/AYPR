def todas_las_palabras(texto):
    '''Función que dado un texto da un conjunto con las palabras que lo conforman
    (str) -> list'''
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
def cantidad_con_vocales():
    '''Función que dado un texto dice cuantas plabras inician por vocal y cuales son
    (str) -> (list, int)'''
    palabras_vocal = []
    texto = input("Ingrese el texto al cual desea sabar el numero de palabras que inician por vocal y cuales son")
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]
    num_palabras = 0
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[0] in vocales:
            num_palabras += 1
            palabras_vocal += [i]
    print("Palabras que inicial por vocal del texto dado: " + str(palabras_vocal))
    print("Numero de palabras que inician por vocal en texto dado: " + str(num_palabras))
cantidad_con_vocales()
