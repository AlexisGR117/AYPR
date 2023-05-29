# Autores: Juan Felipe Vivas Manrique, Daniel Rojas Hernandez y Jefer Alexis González Romero
# Fecha: 07/04/2021
def main():
    matriz = []
    valores = input().split(",")
    while valores != [""]:
        matriz += [valores]
        valores = input().split(",")
    matriz_final = []
    for i in range(len(matriz[0])):
        matriz_final += [0]
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matriz_final[i] += int(matriz[j][i])
    print(matriz_final)
main()
