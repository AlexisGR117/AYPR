def suma_diagonal(numero):
    """Función que dado un entero N, le pide al usuario ingresar
    los valores de cada fila de tamaño N, dando como resultado
    la suma de los valores de la diagonal principal de la matriz de
    tamaño NxN formada por las filas dadas
    (int) -> int"""
    suma_diagonal = 0
    for i in range(numero):
        valores = input().split(",")
        suma_diagonal += int(valores[i])
    return suma_diagonal
def main():
    numero = int(input())
    print(suma_diagonal(numero))
main()
