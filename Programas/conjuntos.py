def interseccion(conjunto_a, conjunto_b):
    """Función que dado dos conjuntos da un conjunto con los elementos en común
    (list, list) -> list"""
    conjunto_interseccion = []
    for i in range(len(conjunto_a)):
        for j in range(len(conjunto_b)):
            if conjunto_a[i] == conjunto_b[j] and conjunto_a[i] not in conjunto_interseccion:
               conjunto_interseccion += [conjunto_a[i]]
    return conjunto_interseccion
def diferencia(conjunto_a, conjunto_b):
    """Función que dado dos conjuntos da un conjunto con los elementos del conjunto A que no estan en un conjunto B
    (list, list) -> list"""
    conjunto_diferencia = []
    for i in range(len(conjunto_a)):
        buscar = 0
        for j in range(len(conjunto_b)):
            if conjunto_a[i] == conjunto_b[j]:
               buscar = 1
        if buscar == 0 and conjunto_a[i] not in conjunto_diferencia:
            conjunto_diferencia += [conjunto_a[i]]
    return conjunto_diferencia
def pertenencia(elemento, conjunto_a):
    """Función que dado un conjunto A y un elemento, determina si esta o no en el conjunto A
    (list, str) -> str"""
    pertenece = "no"
    for i in range(len(conjunto_a)):
        if elemento == conjunto_a[i]:
            pertenece = "si"
    return pertenece
def main():
    conjunto_a = input().split(",")
    conjunto_b = input().split(",")
    print("La intersección entre los dos conjuntos es: ", interseccion(conjunto_a, conjunto_b))
    print("La diferencia entre los dos conjuntos es: ", diferencia(conjunto_a, conjunto_b))
    elemento = input()
    print(elemento, pertenencia(elemento, conjunto_a), "pertenece al conjunto a")
main()
