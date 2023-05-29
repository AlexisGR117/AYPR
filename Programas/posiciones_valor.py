def posiciones(arreglo, valor):
    """Funcion que dado un arreglo y un valor, da las posiciones
    del valor en el arreglo
    (list1D, str) -> list1D"""
    posiciones = []
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            posiciones += [i]
    return posiciones
def main():
    arreglo = input().split(",")
    valor = input()
    posicion_valor = posiciones(arreglo, valor)
    if len(posicion_valor) > 0:
        for i in range(len(posicion_valor) - 1):
            print(posicion_valor[i], end = ",")
        print(posicion_valor[len(posicion_valor)-1])
    else:
        print("No se encontro el valor en el arreglo.")
main()
