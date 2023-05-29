# Autores: Juan Felipe Alfonso Martinez-Jefer Alexis González Romero
# Fecha: 17/03/2021
def juego(palabra, oportunidades):
    '''Esta función nos permite realizar la valaidación de la entrada del jugador y saber si pertenece o no a la palabra escondida
    (str) -> str'''
    ahorcado = "_ " * len(palabra)
    ahorcado = ahorcado.split()
    munequito = ["____", "| |", "| o", "| /\ ", "| /\ ", "|"]
    errores = 0
    posiciones = []
    letras = []
    fin = 0
    for k in range(oportunidades):
        if errores < oportunidades and fin == 0:
            letra = input("\nSerá que si está la letra...")
            contador = 0
            if len(letra) < 2:
                if letra not in letras:
                    letras += [letra]
                    for i in range(len(palabra)):
                        if letra == palabra[i]:
                            ahorcado[i] = letra
                            contador_2 = 0
                            for l in range(len(ahorcado)):
                                if ahorcado[l] != "_":
                                    contador_2 += 1
                            if contador_2 == len(ahorcado):
                                print("\nUsted ha ganado :v")
                                fin = 1
                        else:
                            contador += 1
                    if contador == len(palabra):
                        if errores <= len(munequito):
                            for j in range(errores + 1):
                                print(munequito[j])
                                if j == errores + 1:
                                    print(munequito[j])
                            errores += 1
                            if errores == len(munequito):
                                print("\nF\nGame Over")
                                fin = 1 
                    else:
                        print(*ahorcado, "\n")
                else:
                    print()
                    print("YA DIGITÓ ESTA LETRA!!! (pierde una oportunidad)\n")
                    if errores <= len(munequito):
                        for j in range(errores + 1):
                            print(munequito[j])
                            if j == errores + 1:
                                print(munequito[j])
                        errores += 1
                        if errores == len(munequito):
                            print("\nF\nGame Over")
                            fin = 1                  
            else:
                print()
                print("SOLO ES UNA LETRA!!!!!\n")
    if fin == 0:
        print("\nF\nGame Over")
        for i in range(len(munequito)):
            print(munequito[i])
def main():
    palabras = ["precioso", "pueblo", "respirar", "aire", "puro", "valle", "naturaleza", "casa", "salpicar", "paisaje", "montañas", "habitantes", "tiempo", "alimentos", "familia", "ganado", "plantar", "cereales", "pan", "pasteles"]
    from random import choice
    palabra = choice(palabras)
    oportunidades = len(palabra) + len(palabra) // 2
    print("Vamos a jugar ahorcadito. Debe encontrar la palabra escondida.\nLa palabra es de", len(palabra), "letras, tiene", oportunidades, "oportunidades.\n","_ " * len(palabra))
    juego(palabra, oportunidades)
main()
