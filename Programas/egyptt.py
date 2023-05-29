def egypt_ed():
    '''Funcion que dice basado en los lados de un triangulo si es rectangulo
    (int) -> str'''
    lado_1 = int(input())
    lado_2 = int(input())
    lado_3 = int(input())
    if lado_1 > 0 and lado_2 > 0 and lado_3 > 0:
        if lado_1 > lado_2 and lado_1 > lado_3:
            if ((lado_2**2) + (lado_3**2)) == lado_1**2:
                print("right")
            else:
                print("wrong")
        elif lado_2 > lado_1 and lado_2 > lado_3:
            if ((lado_1**2) + (lado_3**2)) == lado_2**2:
                print("right")
            else:
                print("wrong")
        else:
            if ((lado_1**2) + (lado_2**2)) == lado_3**2:
                print("right")
            else:
                print("wrong")
    else:
            print("wrong")
            
egypt_ed()
