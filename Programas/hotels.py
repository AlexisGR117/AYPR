def hotel():
    '''Funcion que le ayuda a saber a paco que hotel elegir
    (int) -> int'''
    precio_1 = int(input())
    precio_2 = int(input())
    precio_3 = int(input())
    if (precio_1 >= precio_2 and precio_1 <= precio_3) or (precio_1 >= precio_3 and precio_1 <= precio_2):
        print(precio_1)
    elif (precio_2 >= precio_1 and precio_2 <= precio_3) or (precio_2 >= precio_3 and precio_2 <= precio_1):
        print(precio_2)
    else:
        print(precio_3)
hotel()
