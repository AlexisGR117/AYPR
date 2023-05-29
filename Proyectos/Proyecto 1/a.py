# Punto 6
# Punto 7
# Punto 8
def cantidad_inicial_vocales():
    '''Función que dado un texto dice cuantas plabras inician por vocal y cuales son
    (str) -> (list, int)'''
    palabras_vocal = []
    texto = input("Ingrese el texto al cual desea saber el numero de palabras que inician por vocal y cuales son.\n")
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]
    num_palabras = 0
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[0] in vocales:
            num_palabras += 1
            palabras_vocal += [i]
    print("Palabras que inicial por vocal del texto dado: " + str(palabras_vocal))
    print("Numero de palabras que inician por vocal en texto dado: " + str(num_palabras))
# Punto 9
def cantidad_final_vocales():
    '''Función que dado un texto dice cuantas plabras terminan por vocal y cuales son
    (str) -> (list, int)'''
    num_palabras = 0
    palabras_final_vocal = []
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]
    texto = input("Ingrese el texto al cual desea saber el numero de palabras que terminan por vocal y cuales son.\n")
    palabras = todas_las_palabras(texto)
    for i in palabras:
        if i[-1] in vocales:
            num_palabras +=1
            palabras_final_vocal += [i]
    print("Palabras que terminan en vocal del texto dado: " + str(palabras_final_vocal))
    print("Numero de palabras que terminan en vocal del texto dado: " + str(num_palabras))
