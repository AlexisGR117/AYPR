def cantidad_palabras(texto):
    '''Funcion que dado un texto da un conjunto con las palabras que lo conforman
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
def numero_silabas_palabra(palabra):
    '''Funcion que da el numero de silabas de una palabra
    (str) -> int'''
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]
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
def main():
    '''Funcion que dado un texto da un conjunto con el numero de silabas que tiene cada palabra del texto
    (str) -> list'''
    texto = str(input("Ingrese el texto al cual desea conocer el numero de silabas que tiene cada palabra de este.\n"))
    num_silabas_palabras = []
    conjunto_palabras = cantidad_palabras(texto)
    for i in range(len(conjunto_palabras)):
        palabra = conjunto_palabras[i]
        num_silabas_palabras = num_silabas_palabras + [numero_silabas_palabra(palabra)]
    print("El numero de silabas de cada palabra en el texto es: " + str(num_silabas_palabras))
main()
