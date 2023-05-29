def main():
    '''Función que dada las alturas de las paredes da el numero de saltos hacia arriba y hacia abajo en los casos que de
    (int, int, str) -> str'''
    casos = int(input())
    conjunto_casos = []
    for i in range(casos):
        paredes = int(input())
        saltos_arriba = 0
        saltos_abajo = 0
        alturas = input().split()
        conjunto_alturas = []
        for k in alturas:
            conjunto_alturas += [int(k)]
        anterior = conjunto_alturas[0]
        for l in range(1,len(conjunto_alturas)):
            if conjunto_alturas[l] > anterior:
                saltos_arriba = saltos_arriba + 1
            elif conjunto_alturas[l] < anterior:
                saltos_abajo = saltos_abajo + 1
            anterior = conjunto_alturas[l]
        conjunto_casos += [str(saltos_arriba) + " " + str(saltos_abajo)]
    for i in range(len(conjunto_casos)):
        print("Case" + " " + str(i + 1) + ":" + " " + conjunto_casos[i])
main()

