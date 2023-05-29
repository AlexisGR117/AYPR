# Autor: Jefer Alexis González Romero
# Fecha: 15/05/2021
def estanteria(filas):
    """Funcion que dado el numero de repisas le pide al usuario
    que ingrese las filas, devuelve una matriz con los valores en enteros
    (int) -> list2D"""
    repisas = []
    for i in range(filas):
        repisas.append(input().split())
    for i in range(len(repisas)):
        for j in range(len(repisas[i])):
            repisas[i][j] = int(repisas[i][j])
    return repisas
def ventarron(repisas):
    """Funcion que dada la matriz que representa la estanteria con cajas
    da otra matriz con el resultado de la estanteria despues de ocurrir un ventarron
    (list2D) -> list2D"""
    matriz = []
    for i in range(len(repisas)):
        fila = []
        for j in range(len(repisas[i])):
            if repisas[i][j] == 2:
                fila.append(j - 1)
        matriz.append(fila)
        if matriz[i] == []:
            matriz[i].append(len(repisas[i]))
    for i in range(len(repisas)):
        cont = 1
        while cont <= matriz[i][0]:
            if matriz[i][0] - cont + 1 < len(repisas[i]):
                if repisas[i][matriz[i][0] - cont] == 1 and repisas[i][matriz[i][0] - cont + 1] == 0:
                    repisas[i][matriz[i][0] - cont] = 0
                    repisas[i][matriz[i][0] - cont + 1] = 1
                    cont -= 2
            cont += 1
    return repisas
def main():
    filas, columnas = input().split()
    filas = int(filas)
    repisas = estanteria(filas)
    matriz  = ventarron(repisas)
    for i in range(len(matriz)):
        for j in range(len(matriz[i]) - 1):
            print(matriz[i][j], end = " ")
        print(matriz[i][-1])
main()
