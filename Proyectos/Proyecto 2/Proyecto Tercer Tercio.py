# Autores: Angel Nicolas Cuervo Naranjo y Jefer Alexis Gonzalez Romero
# Fecha: 05/05/2021
def modificar(arreglo):
    """Funcion que arregla los datos punto flotantes,
    elimina el salto de linea del ultimo elemento de cada fila,
    si encuentra un dato vacio que debería ser un numero lo reemplaza por un cero,
    los elementos en las columnas que deberian tener una "enhe", cambia esta por una "n"
    (list) --> list
    """
    for i in range(len(arreglo) - 1):
        arreglo[i][-1] = (arreglo[i][-1])[0:-1]
        for j in range(len(arreglo[i])):
            if arreglo[i][j] == "" and j > 3:
                arreglo[i][j] = '0'
            cont = 0
            for k in arreglo[i][j]:
                if k == "Ã":
                    arreglo[i][j] = (arreglo[i][j])[0:cont] + "N" + (arreglo[i][j])[cont+2:len(arreglo[i][j])]
                cont += 1
    for i in range(len(arreglo)):
        if len(arreglo[i]) > 8:
            for j in range(8):
                for k in arreglo[i][j]:
                    buscar = '"'
                    if k == buscar and buscar in arreglo[i][j+1]:
                        unir = (arreglo[i][j])[1:len(arreglo[i][j])] + "." + (arreglo[i][j+1])[0:-1]
                        arreglo[i].insert(j, unir)
                        arreglo[i].pop(j+1)
                        arreglo[i].pop(j+1)
                    elif k == buscar:
                        unir = (arreglo[i][j])[1:len(arreglo[i][j])] + arreglo[i][j+1] + "." + (arreglo[i][j+2])[0:-1]
                        arreglo[i].insert(j, unir)
                        arreglo[i].pop(j+1)
                        arreglo[i].pop(j+1)
                        arreglo[i].pop(j+1)
    return arreglo
def ordenamiento1(arreglo):
    """Funcion que dado un arreglo con las filas del archivo escogido
    ordena de mayor a menor dependiendo del rendimiento por area sembrada
    (list2D) -> list2D
    """
    n_arreglo = []
    for i in range(1,len(arreglo)):
        n_arreglo += [arreglo[i]]
        cont = 0
        bandera = True
        while bandera and cont < len(n_arreglo) and len(n_arreglo) > 1:
            if float(arreglo[i][7]) == float(n_arreglo[cont][7]):
                if float(arreglo[i][4]) <= float(n_arreglo[cont][4]):
                    n_arreglo.insert(cont, arreglo[i])
                    n_arreglo.pop(-1)
                    bandera = False
            elif float(arreglo[i][7]) >= float(n_arreglo[cont][7]): 
                n_arreglo.insert(cont, arreglo[i])
                n_arreglo.pop(-1)
                bandera = False
            cont += 1
    n_arreglo.insert(0, arreglo[0])
    return n_arreglo
def ordenamiento2(arreglo):
    """Funcion que dado un arreglo con las filas del archivo escogido
    ordena por el metodo "Burbuja" de mayor a menor dependiendo del rendimiento por area sembrada
    (list2D) -> list2D
    """
    n_arreglo = []
    for i in arreglo:
        n_arreglo += [i]
    for i in range(2, len(n_arreglo) - 1):
        for j in range(1, len(n_arreglo) - 1):
            if float(n_arreglo[j][7]) == float(n_arreglo[j+1][7]):
                if float(n_arreglo[j][4]) > float(n_arreglo[j+1][4]):
                    temp = n_arreglo[j]
                    n_arreglo[j]= n_arreglo[j+1]
                    n_arreglo[j+1] = temp
            elif float(n_arreglo[j][7]) < float(n_arreglo[j+1][7]):
                temp = n_arreglo[j]
                n_arreglo[j]= n_arreglo[j+1]
                n_arreglo[j+1] = temp
    return n_arreglo
def mezcla(uno, dos):
    """Algoritmo que mezcla valores de dos listas ordenadas
    (list 1D, list 1D) -> list 1D, list 1D"""
    lon_uno = len(uno)
    lon_dos = len(dos)
    nuevo = []
    i = 0
    j = 0
    while i < lon_uno and j < lon_dos:
        if float(uno[i][7]) > float(dos[j][7]):
            nuevo.append(uno[i])
            i += 1
        elif float(uno[i][7]) == float(dos[j][7]):
            if float(uno[i][4]) < float(dos[j][4]):
               nuevo.append(uno[i])
               i += 1
            else:
               nuevo.append(dos[j])
               j += 1
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
def ordenamiento4(arreglo):
    """Funcion que dado un arreglo con las filas del archivo escogido
    ordena por el metodo "merge sort" (ordenamiento que usa tecnica recurrente)
    (list2D) -> list2D
    """
    if len(arreglo) == 1:
        return arreglo
    else:
        mitad = len(arreglo) // 2
        izq = ordenamiento4(arreglo[:mitad])
        der = ordenamiento4(arreglo[mitad:])
        nueva = mezcla(izq, der)
        return nueva
def busqueda1(arreglo, municipio, cultivo):
    """Funcion que dado un arreglo con las filas del archivo escogido
    usando busqueda secuencial encuentras las filas que coinciden con el municipio y cultivo dado
    devolviendo estas y el numero total de hectareas cosechadas
    (list2D, str, str) -> list2D, int
    """    
    busqueda = []
    area_c = 0
    mun = 0
    cul = 0
    for i in range(len(arreglo)):
        if arreglo[i][1] == municipio and arreglo[i][2] == cultivo:
            busqueda += [arreglo[i]]
            area_c += float(arreglo[i][5])
        elif arreglo[i][1] == municipio:
            mun = 1
        elif arreglo[i][2] == cultivo:
            cul = 1
    return busqueda,area_c,mun,cul
def busqueda2(arreglo, municipio, cultivo):
    '''Funcion que dado un arreglo con las filas ordenadas alfabéticamente por municipio
    usando busqueda binaria encuentra el muncipio y busca si el cultivo está en este.
    Da el numero total de hectareas cosechadas y las filas que coinciden con lo dado
    (list2D, str, str) -> list2D, int
    '''
    inicio = 0
    fin = len(arreglo) - 1
    mitad = len(arreglo) // 2
    busqueda = []
    area_c = 0
    mun = 0
    while inicio <= fin:
        if arreglo[mitad][1] == municipio:
            mun = 1
            cont1 = 1
            bandera = True
            while bandera:
                if arreglo[mitad - cont1][1] != municipio:
                    bandera = False
                cont1 += 1
            cont1 -= 2
            cont2 = 1
            bandera = True
            while bandera:
                if arreglo[mitad + cont2][1] != municipio:
                    bandera = False
                cont2 += 1
            cont2 -= 1
            for i in range(mitad - cont1, mitad + cont2):
                if arreglo[i][2] == cultivo:
                    busqueda += [arreglo[i]]
                    area_c += float(arreglo[i][5])
            return busqueda,area_c,mun
        elif arreglo[mitad][1] > municipio:
            fin = mitad - 1
            mitad = (inicio + fin) // 2
        elif arreglo[mitad][1] < municipio:
            inicio = mitad + 1
            mitad = (inicio + fin) // 2
    return busqueda,area_c,mun
def main():
    import time
    nombre = input("Ingrese el nombre del archivo: ")
    file = open(nombre, 'r')
    arreglo = []
    linea = (file.readline()).split(",")
    while linea != [""]:
        arreglo += [linea]
        linea = (file.readline()).split(",")
    arreglo = modificar(arreglo)
    fila_0 = arreglo[0]
    print("\nAlgoritmo de ordenamiento N°1")
    tiempo1 = time.time()
    arreglo1 = ordenamiento1(arreglo)
    tiempo2 = time.time()
    tiempot1 = tiempo2 - tiempo1
    ruta = input("Ingrese la ruta en la que desea guardar el ordenamiento N°1: \n")
    ordenamiento_1 = open(ruta, 'w')
    contenido = ""
    for i in range(len(arreglo1)):
        for j in range(len(arreglo1[i])-1):
            contenido += arreglo1[i][j] +  ","
        contenido += arreglo1[i][-1] + "\n"
    ordenamiento_1.write(contenido)
    print("\nTiempo del ordenamiento N°1: ", tiempot1)
    print("\nAlgoritmo de ordenamiento N°2")
    tiempo1 = time.time()
    arreglo2 = ordenamiento2(arreglo)
    tiempo2 = time.time()
    tiempot2 = tiempo2 - tiempo1
    ruta = input("Ingrese la ruta en la que desea guardar el ordenamiento N°2: \n")
    ordenamiento_2 = open(ruta, 'w')
    contenido = ""
    for i in range(len(arreglo2)):
        for j in range(len(arreglo2[i])-1):
            contenido += arreglo2[i][j] + ","
        contenido += arreglo2[i][-1] + "\n"
    ordenamiento_2.write(contenido)
    print("\nTiempo del ordenamiento N°2: ", tiempot2)
    if tiempot2 < tiempot1:
        print("\nEl algoritmo de ordemamiento mas rapido fue el 2.")
    else:
        print("\nEl algoritmo de ordemamiento mas rapido fue el 1.")
    arreglo.pop(0)
    tiempo1 = time.time()
    arreglo3 = sorted(arreglo, key=lambda redimiento: float(redimiento[7]), reverse = True)
    tiempo2 = time.time()
    tiempot3 = tiempo2 - tiempo1
    ruta = input("Ingrese la ruta en la que desea guardar el ordenamiento con la funcion sorted(): \n")
    ordenamiento_3 = open(ruta, 'w')
    contenido = ""
    arreglo.insert(0, fila_0)
    arreglo3.insert(0, fila_0)
    for i in range(len(arreglo3)):
        for j in range(len(arreglo3[i])-1):
            contenido += arreglo3[i][j] + ","
        contenido += arreglo3[i][-1] + "\n"
    ordenamiento_3.write(contenido)
    print("\nTiempo del ordenamiento con la funcion sorted(): ", tiempot3)
    print("\nAlgoritmo de ordenamiento N°4 (merge_sort)")
    arreglo.pop(0)
    tiempo1 = time.time()
    arreglo4 = ordenamiento4(arreglo)
    tiempo2 = time.time()
    tiempot2 = tiempo2 - tiempo1
    arreglo4.insert(0, fila_0)
    ruta = input("Ingrese la ruta en la que desea guardar el ordenamiento N°4: \n")
    ordenamiento_4 = open(ruta, 'w')
    contenido = ""
    for i in range(len(arreglo4)):
        for j in range(len(arreglo4[i])-1):
            contenido += arreglo4[i][j] + ","
        contenido += arreglo4[i][-1] + "\n"
    ordenamiento_4.write(contenido)
    print("\nTiempo del ordenamiento N°4 (merge_sort): ", tiempot2)
    municipio = input("\nIngrese el municipio de Boyaca que desee: ").upper()
    cultivo = input("Ingrese el cultivo que desee: ").upper()
    print()
    tiempo1 = time.time()
    busqueda,area_c,mun,cul = busqueda1(arreglo, municipio, cultivo)
    tiempo2 = time.time()
    tiempot1 = tiempo2 - tiempo1
    if busqueda == []:
        if mun == 1 and cul == 1:
            print("\nNo hay registros sobre la presencia de este cultivo en el municipio.")
        elif mun == 0 and cul == 1:
            print("\nNo hay registros sobre este municipio.")
        elif mun == 1 and cul == 0:
            print("\nNo hay registros sobre este cultivo.")
        else:
            print("\nNo hay registros sobre este cultivo y municipio.")
    else:
        for i in range(len(busqueda)):
            for j in range(len(busqueda[i])-1):
                print(busqueda[i][j], end = ",")
            print(busqueda[i][-1])
        print("\nSe han consechado ", area_c, " hectareas de ", cultivo, " en el municipio de ", municipio)
    print("\nTiempo de la busqueda N°1: ", tiempot1)
    arreglo.pop(0)
    arreglo4 = sorted(arreglo, key=lambda redimiento: redimiento[1])
    arreglo.insert(0, fila_0)
    print()
    tiempo1 = time.time()
    busqueda,area_c,mun = busqueda2(arreglo4, municipio, cultivo)
    tiempo2 = time.time()
    tiempot2 = tiempo2 - tiempo1
    if busqueda == []:
        if mun == 1:
            print("\nNo hay registros sobre la presencia de este cultivo en el municipio.")
        elif mun == 0:
            print("\nNo hay registros sobre este municipio.")
    else:
        for i in range(len(busqueda)):
            for j in range(len(busqueda[i])-1):
                print(busqueda[i][j], end = ",")
            print(busqueda[i][-1])
        print("\nSe han consechado ", area_c, " hectareas de ", cultivo, " en el municipio de ", municipio)
    print("\nTiempo de la busqueda N°2: ", tiempot2)
    if tiempot2 < tiempot1:
        print("\nEl algoritmo de busqueda mas rapido fue el 2.")
    else:
        print("\nEl algoritmo de busqueda mas rapido fue el 1.")
main()
