def main():
    n,m = input().split(",")
    n = int(n)
    matriz = []
    for i in range(n):
        fila = input().split(",")
        fila = [int(fila[j]) for j in range(len(fila))]
        matriz += [fila]
    print(matriz)
main()
