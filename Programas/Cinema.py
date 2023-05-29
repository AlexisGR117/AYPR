def eliminar_billete(contador, billete):
    '''Función que quita un billete pedido de los billetes que se tienen
    (list) -> list'''
    posicion_billetes = []
    for l in range(len(contador)):
        if contador[l] == billete:
            posicion_billetes += [l]
    eliminar = posicion_billetes[0]
    contador = contador[0:eliminar] + contador[eliminar + 1:len(contador)]
    return(contador)
def main():
    '''Función que dado el numero de personas y los billetes que tiene cada una dice si puede dar el cambio a cada una
    (int, str) -> str'''
    personas = int(input())
    billetes = input()
    billetes = billetes.split(" ")
    billetes_conjunto = []
    for m in range(personas):
        billetes_conjunto += [int(billetes[m])]
    contador = []
    d = 0
    if billetes_conjunto[0] == 25:
        if personas > 2:
            for i in range(personas - 1):
                d = 0
                contador += [billetes_conjunto[i]]
                if billetes_conjunto[i + 1] == 50:
                    a = 0
                    for j in contador:
                        if j == 25:
                            a = 1
                    if a == 1:
                        contador = eliminar_billete(contador, 25)
                    else:
                        d = 1
                elif billetes_conjunto[i + 1] == 100:
                    a = 0
                    c = 0
                    e = 0
                    for k in contador:
                        if k == 25:
                            a = 1
                            e = e + 1
                        if k == 50:
                            c = 1
                    if a == 1 and c == 1:
                        contador = eliminar_billete(contador, 25)
                        contador = eliminar_billete(contador, 50)
                    elif (a == 1 and e == 3):
                        contador = eliminar_billete(contador, 25)
                        contador = eliminar_billete(contador, 25)
                        contador = eliminar_billete(contador, 25)
                    else:
                        d = 1
        else:
            if billetes_conjunto[1] != 50:
                d = 1
    else:
        d = 1
    if d == 1:
        print("NO")
    else:
        print("YES")
main()
