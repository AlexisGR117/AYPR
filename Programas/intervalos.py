def intervalos():
    numero_intervalos = int(input())
    menor = 0
    mayor = 0
    posicion = 0
    intervalo = str(input())
    for j in range(len(intervalo)):
        while intervalo[j] != ",":
            posicion = posicion + 1
    menor = intervalo[0:posicion + 1]
    print(menor)
intervalos()
