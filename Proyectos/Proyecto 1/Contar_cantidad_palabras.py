def contar_cantidad_palabras():
    '''Función que dado un texto da el numero de palabras que hay en el
    (str) -> int'''
    texto = input("Ingrese el texto al cual desea saber el numero de palabras tiene.\n")
    contador = 0
    for i in texto:
        if i == " ":
            contador += 1
    contador = contador + 1
    print("El texto ingresado tiene: " + str(contador) + " palabras")
contar_cantidad_palabras()
