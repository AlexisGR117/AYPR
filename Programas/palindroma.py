def mayuscula(palabra):
    """Función que dada una palbra, si esta tiene mayuscula inicial, la cambia por minuscula
    (str) -> str"""
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(len(mayusculas)):
        if palabra[0] == mayusculas[i]:
            palabra = palabra[1:len(palabra)]
            palabra = minusculas[i] + palabra
    return palabra
def main():
    """Función que dado un conjunto de palabras dice cual es palíndroma y cual no
    (str) -> str"""
    palabra = "a"
    while palabra != "":
        palabra = input()
        if palabra != "":
            letras = []
            letras_contrario = []
            contador = 0
            palabra = mayuscula(palabra)
            for i in palabra:
                letras += [i]
            for i in letras:
                letras_contrario = [i] + letras_contrario
            for i in range(len(letras)):
                if letras_contrario[i] == letras[i]:
                    contador += 1
            if contador == len(letras):
                print("Si")
            else:
                print("No") 
main()
