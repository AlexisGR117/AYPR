matriz = []
from random import randint
tamano = int(input())
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
print(matriz)
