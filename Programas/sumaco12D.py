def suma_columnas(n_filas):
    """Funcion que dada el numero de filas de la matriz
    le pide al usuario que ingrese estas, dando la
    suma de las columnas de la matriz que se forma
    (int) -> list1D"""
    matriz = []
    for i in range(n_filas):
        valores = input().split(",")
        matriz += [valores]
    matriz_suma = []
    for i in range(len(matriz[0])):
        matriz_suma += [0]
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matriz_suma[i] += int(matriz[j][i])
    return matriz_suma
def main():
    n_filas,n_columnas = input().split(",")
    n_filas = int(n_filas)
    matriz_suma = suma_columnas(n_filas)
    for i in range(len(matriz_suma) - 1):
        print(matriz_suma[i], end = ",")
    print(matriz_suma[i + 1])
main()
