def matrices(n_filas):
    """Función que dada el numero de filas, le pide al usuario
    que ingrese ese numero de filas, devoviendo la matriz formada
    por estas
    (int) -> list2D"""
    matriz = []
    for i in range(n_filas):
        valores = input().split(",")
        matriz += [valores]
    return matriz
def suma_matrices(matriz_1, matriz_2):
    """Función que dada dos matrices,devuelve otra con la suma
    de estas
    (list2D, list2D) -> list2D"""
    matriz_suma = []
    for i in range(len(matriz_1)):
        fila_suma = []
        for j in range(len(matriz_1[i])):
            suma = int(matriz_1[i][j]) + int(matriz_2[i][j])
            fila_suma += [suma]
        matriz_suma += [fila_suma]
    return matriz_suma
def main():
    n_filas,n_columnas = input().split(",")
    n_filas = int(n_filas)
    matriz_1 = matrices(n_filas)
    cero = int(input())
    matriz_2 = matrices(n_filas)
    matriz_suma = suma_matrices(matriz_1, matriz_2)
    for i in matriz_suma:
        for j in range(len(i) - 1):
            print(i[j], end = ",")
        print(i[-1], end = "")
        print()
main()
    
