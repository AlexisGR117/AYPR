# Proyecto segundo tercio. Analisis de textos.
# Autores: Angel Nicolas Cuervo Naranjo - Jefer Alexis González Romero
import libreria_analisis_textos
def main():
    texto = input("Ingrese el texto que desea analizar.\n\n")
    # Punto 1
    print("\nEl texto ingresado tiene " + str(libreria_analisis_textos.cantidad_palabras(texto) + 1) + " palabras\n")
    # Punto 2
    print("\nA continuación se presenta un conjunto con las palabras presentes en el texto con su respectivo numero de silabas: \n\n", libreria_analisis_textos.cantidad_silabas(texto))
    # Punto 3
    [monosilabas, bisilabas, trisilabas, polisilabas] = libreria_analisis_textos.frecuencia_silabas(texto)
    print("\nLas palabras monosílasbas aparecen en el texto " + str(monosilabas) + " veces.")
    print("Las palabras bisílasbas aparecen en el texto " + str(bisilabas) + " veces.")
    print("Las palabras trisílasbas aparecen en el texto " + str(trisilabas) + " veces.")
    print("Las palabras polisílasbas aparecen en el texto " + str(polisilabas) + " veces.\n")
    # Punto 4
    print("Conjunto con las palabras presentes en el texto con su respectivo número de apariciones: \n\n", libreria_analisis_textos.frecuencia_palabras(texto))
    # Punto 5
    [num_sustantivos_plural, sustantivos_plural] = libreria_analisis_textos.cantidad_sustantivos_plural(texto)
    print("\nCantidad de posibles palabras que pueden significar el plural de un sustantivo: ", num_sustantivos_plural)
    print("\nPosibles palabras que pueden significar el plural de un sustantivo: \n\n", sustantivos_plural)
    # Punto 6
    [num_infinitivos_verbos, infinitivo_verbos] = libreria_analisis_textos.cantidad_infinitivo_verbos(texto)
    print("\nCantidad de posibles palabras que pueden significar el infinitivo de un verbo: ", num_infinitivos_verbos)
    print("\nPosibles palabras que pueden significar el infinitivo de un verbo: \n\n", infinitivo_verbos)
    # Punto 7
    [num_preposiciones, preposiciones_total] = libreria_analisis_textos.cantidad_preposiciones(texto)
    print("\nCantidad de preposiciones en el texto: ", num_preposiciones)
    print("\nPreposicones presentes en el texto dado: \n\n", preposiciones_total)
    # Punto 8
    [num_palabras, palabras_vocal] = libreria_analisis_textos.cantidad_inicial_vocales(texto)
    print("\nNúmero de palabras que inician por vocal en el texto dado: " + str(num_palabras))
    print("\nPalabras que inician por vocal: \n\n" + str(palabras_vocal))
    # Punto 9
    [num_palabras, palabras_final_vocal] = libreria_analisis_textos.cantidad_final_vocales(texto)
    print("\nNúmero de palabras que terminan en vocal en el texto dado: " + str(num_palabras))
    print("\nPalabras que terminan en vocal: \n\n" + str(palabras_final_vocal))
    # Punto 10
    [num_palabras, palabras_consonante] = libreria_analisis_textos.cantidad_inicial_consonantes(texto)
    print("\nNúmero de palabras que inician por consonante en el texto dado: " + str(num_palabras))
    print("\nPalabras que inician por consonante en el texto dado: \n\n" + str(palabras_consonante))
    # Punto 11
    [num_palabras, palabras_final_consonante] = libreria_analisis_textos.cantidad_final_consonantes(texto)
    print("\nNúmero de palabras que terminan en consonante en el texto dado: " + str(num_palabras))
    print("\nPalabras que terminan en consonante: \n\n" + str(palabras_final_consonante))
    # Punto 12
    cadena = input("\nIngrese la cadena.\n")
    [num_palabras, palabras_inicial_cadena] = libreria_analisis_textos.cantidad_inicial_cadena(texto, cadena)
    print("\nNúmero de palabras que inician por " + cadena + " en el texto: " + str(num_palabras))
    print("\nPalabras en el texto que inician por " + cadena +": \n\n" + str(palabras_inicial_cadena))
    # Punto 13
    [num_palabras, palabras_final_cadena] = libreria_analisis_textos.cantidad_final_cadena(texto, cadena)
    print("\nNúmero de palabras que finzalizan por " + cadena +" en el texto: " + str(num_palabras))
    print("\nPalabras en el texto que finzalizan por " + cadena +": \n\n" + str(palabras_final_cadena))
    # Punto 14
    print("\nLos posibles familiares de " + cadena + " en el texto son: \n\n", libreria_analisis_textos.familia_palabras(texto, cadena))
main()
