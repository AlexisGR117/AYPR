# Autor: Jefer Alexis Gonzalez Romero
# Fecha: 19/05/2021
def rodear(matriz):
    """Funcion que rodea la matriz dada con el numero no entero "0.5"
    (list 2D) -> list 2D """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    fila_ceros = [0.5] * (len(matriz[0]) + 2)
    for i in range(len(matriz)):
        matriz[i].insert(0, 0.5)
        matriz[i].insert(len(matriz[i]), 0.5)
    matriz.insert(0, fila_ceros)
    matriz.insert(len(matriz), fila_ceros)
    return matriz
def num_alrededor(matriz, numero):
    """Funcon que encuentra la posicion del numero y da los numeros alrededor de este
    (list 2D, int) -> list 1D """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if int(matriz[i][j]) == numero:
                fila = i
                columna = j
    alrededor = []
    if matriz[fila-1][columna] != 0.5:
        alrededor.append(matriz[fila-1][columna])
    if matriz[fila-1][columna+1] != 0.5:
        alrededor.append(matriz[fila-1][columna+1])
    if matriz[fila][columna+1] != 0.5:
        alrededor.append(matriz[fila][columna+1])
    if matriz[fila+1][columna+1] != 0.5:
        alrededor.append(matriz[fila+1][columna+1])
    if matriz[fila+1][columna] != 0.5:
        alrededor.append(matriz[fila+1][columna])
    if matriz[fila+1][columna-1] != 0.5:
        alrededor.append(matriz[fila+1][columna-1])
    if matriz[fila][columna-1] != 0.5:
        alrededor.append(matriz[fila][columna-1])
    if matriz[fila-1][columna-1] != 0.5:
        alrededor.append(matriz[fila-1][columna-1])
    return alrededor
def suma_alrededor(alrededor):
    """Funcion que dada los numeros alrededor de un numero
    da la suma de los pares e impares
    (list1D) -> int, int"""
    suma_pares = 0
    suma_impares = 0
    for i in range(len(alrededor)):
        if alrededor[i] % 2 == 0:
            suma_pares += alrededor[i]
        else:
            suma_impares += alrededor[i]
    return suma_pares, suma_impares
def main():
    fila = input().split(",")
    matriz = []
    while fila != ["*"]:
        matriz.append(fila)
        fila = input().split(",")
    numero = int(input())
    matriz = rodear(matriz)
    print(matriz)
    alrededor = num_alrededor(matriz, numero)
    print(alrededor)
    suma_pares, suma_impares = suma_alrededor(alrededor)
    print(str(suma_pares) + "," + str(suma_impares))
main()
