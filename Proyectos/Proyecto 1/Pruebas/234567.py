def palabras():
    '''Funcion que dado un texto da un conjunto con las palabras que lo conforman
    (str) -> list'''
    texto = input()
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
    print(conjunto_palabras)
palabras()
