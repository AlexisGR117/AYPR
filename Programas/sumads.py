def suma_diagonal_secundaria(numero):
    """Función que dado un entero N, le pide al usuario ingresar
    los valores de cada fila de tamaño N, dando como resultado
    la suma de los valores de la diagonal secundaria de la matriz de
    tamaño NxN formada por las filas dadas
    (int) -> int"""
    suma_diagonal = 0
    for i in range(numero):
        valores = input().split(",")
        suma_diagonal += int(valores[-i-1])
    return suma_diagonal
def main():
    numero = int(input())
    print(suma_diagonal_secundaria(numero))
main()
