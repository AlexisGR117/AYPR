def matriz_traspuesta(matriz):
    """Función que dada una matriz, devuelve la traspuesta de esta
    (list 2D) -> list 2D"""
    contador = 0
    for i in range(len(matriz)):
        for j in range(contador + 1, len(matriz)):
            cambio = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = cambio
        contador += 1
    return matriz
def main():
    numero = int(input())
    matriz = []
    for i in range(numero):
        valores = input().split(",")
        matriz += [valores]
    matriz = matriz_traspuesta(matriz)
    for i in matriz:
        for j in range(len(i)-1):
            print(i[j], end = ",")
        print(i[j + 1], end = "")
        print()
main()
