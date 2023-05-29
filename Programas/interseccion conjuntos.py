def interseccion_conjuntos ():
    '''subprograma que dado dos conjuntos encuentra la
    intersección de estos'''
    cantidad_a = int(input("cantidad en a"))
    conjunto_a = []
    conjunto_b = []
    for i in range(cantidad_a):
        valor = int(input("valor"))
        conjunto_a = conjunto_a + [valor]
    cantidad_b = int(input("cantidad en b"))
    for i in range(cantidad_b):
        valor = int(input("valor"))
        conjunto_b = conjunto_b + [valor]
    conjunto_inter = []
    for i in range(cantidad_a):
        buscar = conjunto_a[i]
        for j in range(cantidad_b):
            if buscar == conjunto_b[j]:
                conjunto_inter = conjunto_inter + [buscar]
    if conjunto_inter == []:
        print("vacio")
    else:
        print(conjunto_inter)
interseccion_conjuntos()      
