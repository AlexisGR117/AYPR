def todas_las_palabras(texto):
    '''Función que dado un texto da un conjunto con las palabras que lo conforman
    (str) -> list'''
    posicion = 0
    conjunto_palabras = []
    nueva_posicion = 0
    signos_puntuacion = [".", ",", ";", "?", "¿", "!", "'", "¡", "...", "(", ")", "*", "[", "]", "{", "}", "-", "_", "/"]
    mayusculas = "ABCDEFGHIJKLMÑOPQRSTUVWXYZÁÉÍÓÚ"
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
    print(conjunto_palabras)
    for i in range(len(conjunto_palabras)):
        palabra = conjunto_palabras[i]
        for k in palabra:
            for j in range(len(mayusculas)):
                if k[0] == mayusculas[j]:
                    palabra_sin_1raletra = palabra[1:len(palabra)]
                    palabra = minusculas[j] + palabra_sin_1raletra
                    conjunto_palabras[i] = palabra
    return(conjunto_palabras)
def main():
    '''Funcion que dado un texto dice cuantas posibles palabras pueden significar el plurar de un sustantivo y cuales son
    (str) -> (list, int)'''
    texto = input()
    palabras = todas_las_palabras(texto)
    print(palabras)
    num_sustantivos_plural = 0
    sustantivos_plural = []
    excepciones = ["es", "las", "los", "todos", "todas", "ellos", "ellas", "unos", "unas", "nosotros", "nosotras", "ustedes", "vosotros", "vosotras", "sus", "mas", "más"]
    for i in palabras:
        if i not in excepciones:
            if i[-1] == "s":
                num_sustantivos_plural += 1
                if i not in sustantivos_plural:
                    sustantivos_plural += [i]
    print("Posibles palabras que pueden significar el plurar de un sustantivo: ", sustantivos_plural)
    print("Cantidad de posibles palabras que pueden significar el plurar de un sustantivo: ", num_sustantivos_plural)
main()
