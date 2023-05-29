# Autor: Jefer Alexis González Romero
# Fecha: 19 de abril de 2021
def crear_tablero(tamano, puntos_vacios):
    """Función que dado el tamaño y numero de puntos vacios genera el tablero a jugar
    (int, int) -> list2D"""
    import random
    tablero = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila += [-1]
        tablero += [fila]
    contador = 0
    while contador < puntos_vacios:
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)
        if tablero[fila][columna] == -1:
            tablero[fila][columna] += 1
            contador += 1
    for i in range(tamano):
        for j in range(tamano):
            if tablero[i][j] != 0:
                tablero[i][j] = random.randint(1, tamano ** 2)
    return tablero
def juego(jugador, tablero_descubierto, tablero, puntaje, v_jugador, contador):
    """Función que juega un turno del juego para el jugador dado
    (str, list2D, list2D, int, int) -> int, int"""
    fila = int(input("\n" +jugador + " ingresa la fila que deseas: "))
    columna = int(input(jugador + " ingresa la columna que deseas: "))
    print()
    bandera = False
    while bandera == False:
        if fila - 1 >= len(tablero) or columna - 1 >= len(tablero):
            print("La posición dada no esta dentro del tamaño del tablero, ingresa otra.")
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            print()
        elif tablero_descubierto[fila - 1][columna - 1] != 0:
            print("Ya se escogió esa posición, ingresa otra.")
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            print()
        else:
            bandera = True
    if tablero[fila - 1][columna - 1] != 0:
        tablero_descubierto[fila - 1][columna - 1] = tablero[fila - 1][columna - 1]
        puntaje += tablero[fila - 1][columna - 1]
        print("\n" +jugador + " llevas " + str(puntaje) + " puntos" + "\n")
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if tablero_descubierto[i][j] == 0:
                    print("{:2}".format(" "), end = "|")
                else:
                    print("{:2}".format(tablero_descubierto[i][j]), end = "|")
            print()
        contador += 1
    else:
        tablero_descubierto[fila - 1][columna - 1] = "x"
        print(jugador + " caiste en el vacio, se termina el juego.\n")
        v_jugador = 1
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if tablero_descubierto[i][j] == 0:
                    print("{:2}".format(" "), end = "|")
                else:
                    print("{:2}".format(tablero_descubierto[i][j]), end = "|")
            print()
    return puntaje, v_jugador, contador
def main():
    import random
    jugador_1 = input("Nombre del jugador N°1: \n")
    jugador_2 = input("Nombre del jugador N°2: \n")
    tamano = random.randint(2, 9)
    puntos_vacios = random.randint(2, tamano ** 2) - 1
    print("El tamaño del tablero en el que se va jugar es: " + str(tamano) + "x" + str(tamano) + "\n")
    print("En el tablero hay: " + str(puntos_vacios) + " puntos vacios.")
    tablero = crear_tablero(tamano, puntos_vacios)
    pjugador_1 = 0
    pjugador_2 = 0
    tablero_descubierto = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila += [0]
        tablero_descubierto += [fila]
    vacio = 0
    v_jugador_1 = 0
    v_jugador_2 = 0
    pjuador_1 = 0
    pjugador_2 = 0
    contador = 0
    while vacio == 0:
        pjugador_1, vacio, contador = juego(jugador_1, tablero_descubierto, tablero, pjugador_1, vacio, contador)
        if contador == tamano ** 2 - puntos_vacios:
            vacio = 1
            print("Ya se seleccionaron todos los puntos no vacios, se termina el juego.")
        pjugador_2, vacio, contador = juego(jugador_2, tablero_descubierto, tablero, pjugador_2, vacio, contador)
        if contador == tamano ** 2 - puntos_vacios:
            vacio = 1
            print("Ya se seleccionaron todos los puntos no vacios, se termina el juego.")
    if pjugador_1 > pjugador_2:
        print("\nEl ganador es "+ jugador_1 + " con " + str(pjugador_1) + " puntos.")
    elif pjugador_2 > pjugador_1:
        print("\nEl ganador es "+ jugador_2 + " con " + str(pjugador_2) + " puntos.")
    else:
        print("\nLos dos son ganadores, hubo un empate cada uno tiene " + str(pjugador_1) + " puntos.")
    print("El tablero jugado era:\n")
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 0:
                print("{:2}".format(" "), end = "|")
            else:
                print("{:2}".format(tablero[i][j]), end = "|")
        print()
main()
        
