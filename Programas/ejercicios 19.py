# Autores: Juan Felipe Vivas Manrique, Daniel Rojas Hernandez y Jefer Alexis González Romero
# Fecha: 07/04/2021
def matriz_primer_numero_fila(m, n):
    """Funcion que da en listas la matriz pedida
    (int, int) -> list 2D"""
    matriz = [[i + j for j in range(n)] for i in range(m)]
    return matriz
def suma_columnas():
    """Funcion que suma las columnas de una matriz dada"""
    matriz = []
    valores = input().split(",")
    while valores != [""]:
        matriz += [valores]
        valores = input().split(",")
    matriz_suma = []
    for i in range(len(matriz[0])):
        matriz_suma += [0]
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matriz_suma[i] += int(matriz[j][i])
    return matriz_suma
def main():
    """m,n = input().split(",")
    m = int(m)
    n = int(n)
    matriz = matriz_primer_numero_fila(m, n)
    for i in matriz:
        for j in range(len(i)):
            print(i[j], end = " ")
        print()
    print(suma_columnas())"""
    """n = int(input())
    suma_diagonal = 0
    for i in range(n):
        valores = input().split(",")
        suma_diagonal += int(valores[i])
    print(suma_diagonal)"""
    """n = int(input())
    contador = 0
    suma_encima_diagonal = 0
    for i in range(n):
        valores = input().split(",")
        for i in range(contador + 1, n):
            suma_encima_diagonal += int(valores[i])
        contador += 1
    print(suma_encima_diagonal)"""
    entrada = input().split(",")
    matriz = []
    while entrada != [""]:
        matriz += [entrada]
        entrada = input().split(",")
    print(matriz)
    
main()
