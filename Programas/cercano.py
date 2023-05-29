# Autor: Jefer Alexis González Romero
# Fecha: 12/05/2021
def inserccion(arreglo):
    """Funcion que implementa ordenamiento por inserccion
    (list1D) -> list1D
    """
    for i in range(1, len(arreglo)):
        clave = int(arreglo[i])
        j = i -1
        while j >= 0 and clave > int(arreglo[j]):
            arreglo[j+1] = int(arreglo[j])
            j -= 1
        arreglo[j+1] = clave
    return arreglo
def cercano(linea):
    """Funcion que busca en la lista ordenada los valores mas cercanos
    (list1D) -> list1D
    """
    m_cercano = linea[0] - linea[1]
    cercanos = str(linea[1]) + "," + str(linea[0])
    for i in range(1, len(linea) - 1):
        cercania = linea[i] - linea[i + 1]
        if cercania <= m_cercano:
            m_cercano = cercania
            cercanos = str(linea[i + 1]) + "," + str(linea[i])
    return cercanos
def main():
    n_lineas = int(input())
    for i in range(n_lineas):
        linea = input().split(",")
        linea = inserccion(linea)
        linea[0] = int(linea[0])
        print(cercano(linea))
main()
