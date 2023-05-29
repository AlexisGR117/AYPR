# Autor: Jefer Alexis Gonzalez Romeor
# Fecha: 03/05/2021
def n_picos(secuencia):
    """Funcion que dada una secuencia entrega el número de picos que
    hay en esta
    (list1D) -> int"""
    picos = 0
    for i in range(1, len(secuencia)-1):
        if int(secuencia[i-1]) < int(secuencia[i]) > int(secuencia[i+1]):
            picos += 1
    return picos
def main():
    secuencia = input().split(",")
    print(n_picos(secuencia))
main()
