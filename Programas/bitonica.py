# Autor: Jefer Alexis Gonzalez Romero
# Fecha: 03/05/2021
def n_mayor(secuencia):
    '''Funcion que busca el mayor valor de una secuencia y su posicion
    (list1D) -> int, int'''
    mayor = int(secuencia[0])
    for i in range(len(secuencia)):
        if int(secuencia[i]) >= mayor:
            mayor = int(secuencia[i])
            cont = i
    return mayor, cont
def bitonica(mayor, cont, secuencia):
    '''Funcion que dice si la secuencia dada es bitonica
    (int, int, list1D) -> bool'''
    bandera = True
    for i in range(cont):
        if int(secuencia[i]) > int(secuencia[i+1]):
            return False
    for i in range(cont, len(secuencia)-1):
        if int(secuencia[i+1]) > int(secuencia[i]):
            return False
    return bandera
def main():
    secuencia = input().split(",")
    mayor, cont = n_mayor(secuencia)
    print(bitonica(mayor, cont, secuencia))
main()
