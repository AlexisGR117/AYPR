# Autor: Jefer Alexis González Romero
# Fecha: 05/04/2021
def main():
    entrada = input().split(",")
    matriz = []
    while entrada != [""]:
        elemento = 0
        for i in range(len(entrada)):
            elemento += int(entrada[i])
        matriz += [elemento]
        entrada = input().split(",")
    print(matriz)
main()
