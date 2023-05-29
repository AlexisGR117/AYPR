def matriz_aleatoria(tamano):
    matriz = []
    from random import randint
    for i in range(tamano):
        fila = []
        contador = 0
        while contador < tamano:
            buscar = 0
            valor =  randint(0, tamano * tamano)
            for k in matriz:
                for l in k:
                    if valor == l:
                        buscar = 1
            for j in fila:
                if valor == j:
                    buscar = 1 
            if buscar == 0:
                fila += [valor]
                contador += 1
        matriz += [fila]
    return matriz
def matriz_manual(tamano):
    matriz = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            valor = int(input("fila " + str(i + 1) + ", columna " + str(j + 1)+ ": "))
            fila += [valor]
        matriz += [fila]
    return matriz
def main():
    tamano = int(input())
    eleccion = input()
    if eleccion == "M":
        matriz = matriz_aleatoria(tamano)
    else:
        matriz = matriz_manual(tamano)
    analizador = []
    print(matriz)
    for i in range(tamano):
        analizador += [0]
    for i in range(tamano):
        for j in range(tamano):
            analizador[i] += matriz[i][j]
            print(analizador[i])
    print(analizador)
main()

