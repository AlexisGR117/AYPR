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
def cantidad_final_cadena():
    '''Función que dado un texto dice cuántas y cuales plabras finalizan por una cadena dada 
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
