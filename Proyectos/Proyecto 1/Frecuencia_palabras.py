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
def frecuencia_palabras():
    '''Funcion que dado un texto da un conjunto con las palabras presentes en el texto y otro conjunto con el numero de veces que aparece cada palabra
    (str) -> list'''
    veces = []
    mayusculas = "ABCDEFGHIJKLMÑOPQRSTUVWXYZ"
    minusculas = "abcdefghijlmnñopqrstuvwxyz"
    texto = input("Ingrese el texto al cual desea conocer la frecuencia con la que aparecen cada palabra presente en este.\n")
    palabras = todas_las_palabras(texto)
    recorrer_palabras = []
    for i in palabras:
        for k in range(len(mayusculas)):
            if i[0] ==  mayusculas[k]:
                palabra_sin_1raletra = i[1:len(i)]
                i = minusculas[k] + palabra_sin_1raletra
        if i not in recorrer_palabras:
            recorrer_palabras.append(i)
            veces.append(1)
        else:
            for j in range(len(recorrer_palabras)):
                if recorrer_palabras[j] == i:
                    veces[j] = veces[j] + 1
    print("Las palabras presentes en el texto son: " + str(recorrer_palabras))
    print("La cantidad de veces que aparece cada palabra en la lista anterior es: " + str(veces))
frecuencia_palabras()
