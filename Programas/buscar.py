def buscar(L,e):
    cont = 0
    while len(L) > 1:
        p_mitad = (len(L) // 2)
        mitad = L[p_mitad]
        print(p_mitad)
        if mitad > e:
            L = L[0:p_mitad]
            print(L)
        elif mitad < e:
            L = L[p_mitad:len(L)]
            print(L)
        else:
            return True
    return False
