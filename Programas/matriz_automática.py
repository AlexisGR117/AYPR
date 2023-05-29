# Programa que genera de manera automática una matriz cuadrada
# Autor: Jefer Alexis González Romero
# Fecha 05/04/2021
def main():
    n = int(input())
    # Generar matriz de ceros
    matriz = []
    for i in range(n):
        fila = [0] * n
        matriz += [fila]
    print(matriz)
    # Recorrer matriz
    for i in range(n):
        for j in range(n):
            matriz[i][j] = (i + 1) * (j + 1)
    print(matriz)
main()
            
