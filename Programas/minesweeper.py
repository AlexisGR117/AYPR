# Autor: Jefer Alexis Gnzález Romero
# Fecha: 15/05/2021
def tablero(filas):
    """Funcion que dado el numero de filas le pide al usuario que ingrese cada una
    reemplaza los * por 9 y los . por 0 e inserta alrededor de tablero ceros
    (int) -> list 2D"""
    tablero = []
    for i in range(int(filas)):
        tablero.append(input())
    juego = []
    for i in range(len(tablero)):
        fila = []
        for j in range(len(tablero[i])):
            if tablero[i][j] == "*":
                fila.append(9)
            else:
                fila.append(0)
        juego.append(fila)
    fila_ceros = [0] * (len(juego[0]) + 2)
    for i in range(len(juego)):
        juego[i].insert(0, 0)
        juego[i].insert(len(juego[i]), 0)
    juego.insert(0, fila_ceros)
    juego.insert(len(juego), fila_ceros)
    return juego
def numeros(tablero):
    """Funcion que dado el tablero de nueves y ceros suma alrededor de los nueves uno,
    elimina lo que recubre el tablero
    (list 2D) -> list 2D"""
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] > 8:
                tablero[i][j+1] += 1
                tablero[i][j-1] += 1
                tablero[i+1][j] += 1
                tablero[i+1][j+1] += 1
                tablero[i+1][j-1] += 1
                tablero[i-1][j] += 1
                tablero[i-1][j+1] += 1
                tablero[i-1][j-1] += 1
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] > 8:
                tablero[i][j] = "*"
    for i in range(len(tablero)):
        tablero[i].pop(0)
        tablero[i].pop(-1)
    tablero.pop(0)
    tablero.pop(-1)
    return tablero
def main():
    filas, columnas = input().split()
    cont = 1
    while filas != "0" and columnas != "0":
        if cont > 1:
            print() 
        tablero_juego = tablero(filas)
        juego = numeros(tablero_juego)
        print("Field #" + str(cont) + ":") 
        for i in range(len(juego)):
            for j in range(len(juego[i]) - 1):
                print(juego[i][j], end = "")
            print(juego[i][-1])
        cont += 1
        filas, columnas = input().split()        
main()
