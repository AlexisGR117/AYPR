import time
def burbuja(arreglo):
    """Funcion que implementa ordenamiento por burbuja
    (list1D) -> list1D
    """
    for i in range(1,len(arreglo)-1):
        for j in range(len(arreglo)-1):
            if arreglo[j] < arreglo[j+1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = temp
    return arreglo
def inserccion(arreglo):
    """Funcion que implementa ordenamiento por inserccion
    (list1D) -> list1D
    """
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i -1
        while j >= 0 and clave < arreglo[j]:
            arreglo[j+1] = arreglo[j]
            j -= 1
        arreglo[j+1] = clave
    return arreglo
def main(arreglo):
    tiempo1 = time.time()
    arreglo1 = burbuja(arreglo)
    tiempo2 = time.time()
    tiempo =  tiempo2 - tiempo1
    print(arreglo1)
    print(tiempo)
    tiempo1 = time.time()
    arreglo2 = inserccion(arreglo)
    tiempo2 = time.time()
    tiempo =  tiempo2 - tiempo1
    print(arreglo2)
    print(tiempo)

