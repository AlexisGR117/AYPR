def duplicado_conjunto ():
    '''Subprograma que determina si hay
    elementos duplicados en un arreglo dado'''
    cantidad = int(input("cantidad"))
    conjunto = []
    for i in range(cantidad):
        valor = int(input("valor"))
        conjunto = conjunto + [valor]
    n_valores = 0
    for i in range(cantidad):
        buscar = conjunto[i]
        for j in range(cantidad):
            if buscar == conjunto[j]:
                n_valores = n_valores + 1
    if n_valores > cantidad:
        print("Si")
    else:
        print("No")
duplicado_conjunto()
