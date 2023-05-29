def cantidad_palabras():
    '''Funcion que dice cuantas palabras tiene un texto
    (str) -> int'''
    texto = str(input("Ingrese el texto al cual desea saber cuantas palabras tiene\n"))
    palabras = 0
    for i in range(len(texto)):
        if texto[i] == " ":
            palabras = palabras + 1     
    print("El texto ingresado tiene: " + str(palabras + 1) + " palabras")
cantidad_palabras()
