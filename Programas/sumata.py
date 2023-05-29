def suma_arriba_diagonal(numero):
    """Función que dado el tamaño de la matriz
    le pide al usuario ingresar los valores de cada fila, dando
    como resultado la suma de los valores por encima de la matriz
    ingresada por el usuario
    (int) -> int"""
    contador = 0
    suma_encima_diagonal = 0
    for i in range(numero):
        valores = input().split(",")
        for i in range(contador + 1, numero):
            suma_encima_diagonal += int(valores[i])
        contador += 1
    return suma_encima_diagonal
def main():
    numero = int(input())
    print(suma_arriba_diagonal(numero))
main()
