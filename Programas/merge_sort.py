def merge_sort(arreglo):
    """Ordenamiento de una secuencia, tecnica recurrente
    (list 1D) -> list 1D """
    if len(arreglo) == 1:
        return arreglo
    else:
        mitad = len(arreglo) // 2
        izq = merge_sort(arreglo[:mitad])
        der = merge_sort(arreglo[mitad:])
        nueva = mezcla(izq, der)
        return nueva
def mezcla(uno, dos):
    """Algoritmo que mezcla valores de dos listas ordenadas
    (list 1D, list 1D) -> list 1D, list 1D"""
    lon_uno = len(uno)
    lon_dos = len(dos)
    nuevo = []
    i = 0
    j = 0
    while i < lon_uno and j < lon_dos:
        if uno[i] < dos[j]:
            nuevo.append(uno[i])
            i += 1
        else:
            nuevo.append(dos[j])
            j += 1
    while i < lon_uno:
        nuevo.append(uno[i])
        i += 1
    while j < lon_dos:
        nuevo.append(dos[j])
        j += 1
    return nuevo
    
