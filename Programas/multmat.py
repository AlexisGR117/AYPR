# Autor: Jefer Alexis González Romero
# Fecha: 12/05/2021
def matrices(filas):
    """Funcion que dada el numero de filas que tiene la matriz le pide al
    usuario que ingrese las filas con los valores separados por comas
    pasandolas a una matriz y convirtiendo los valores a enteros
    (int) -> list 2D"""
    matriz = []
    for i in range(int(filas)):
        fila = input().split(",")
        matriz += [fila]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    return matriz
def pro_matrices(matriz1, matriz2):
    """Funcion que dado dos matrices da el producto de estas
    (list 2D, list 2D) -> list 2D"""
    matriz_r = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            valor = 0
            for k in range(len(matriz1[0])):
                    valor += matriz1[i][k] * matriz2[k][j]
            fila += [valor]
        matriz_r += [fila]
    return matriz_r
def main():
    filas1, columnas1 = input().split(",")
    matriz1 = matrices(filas1)
    filas2, columnas2 = input().split(",")
    matriz2 = matrices(filas2)
    if columnas1 != filas2:
        print("No es posible")
    else:
        producto = pro_matrices(matriz1, matriz2)
        for i in range(len(producto)):
            for j in range(len(producto[0]) - 1):
                print(producto[i][j], end = ",")
            print(producto[i][-1])
main()

