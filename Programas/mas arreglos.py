# Autor: Jefer Alexis González Romero
# Fecha: 19/04/2021
def encontrar_valor(arreglo, valor):
    """Función que dado un arreglo y un valor, busca si se
    encuentra el valor en el arreglo
    Función de python: in
    (list1D, int) -> bool"""
    encontrar = False
    for i in range(len(arreglo)):
        if valor == arreglo[i]:
            encontrar = True
    return encontrar
def primera_posicion_valor(arreglo, valor):
    """Función que dado un arreglo y un valor, da la primera
    ocurrencia del valor en el arreglo
    Función de python: index()
    (list1D, int) -> int"""
    bandera = True
    columna = -1
    for i in range(len(arreglo)):
        if valor == arreglo[i] and bandera:
            columna = i
            bandera = False
    return columna
def cantidad_veces_valor(arreglo, valor):
    """Función que dado un arreglo y un valor, busca cuantas veces
    se encuentra el valor en el arreglo
    Función de python: count()
    (list1D, int) -> int"""
    veces = 0
    for i in range(len(arreglo)):
        if valor == arreglo[i]:
            veces += 1
    return veces
def posiciones_valor(arreglo, valor):
    """Función que dado un arreglo y un valor, da las posiciones
    del valor en el arreglo
    (list1D, int) -> list"""
    posiciones = []
    for i in range(len(arreglo)):
        if valor == arreglo[i]:
            posiciones += [i + 1]
    return posiciones
def eliminar_valor(arreglo, valor):
    """Función que dado un arreglo y un valor, elimina
    todas las apariciones del valor en el arreglo
    Función de python: remove(), pop(), delete()
    (list1D, int) -> list"""
    arreglo_sv = []
    for i in range(len(arreglo)):
        if valor != arreglo[i]:
            arreglo_sv += [arreglo[i]] 
    return arreglo_sv
def tipo_valores(arreglo):
    """Función que dado un arreglo dice si todos los
    valores en el arreglo son tipo int
    (list1D) -> bool"""
    bandera = True
    for i in range(len(arreglo)):
        try:
            int(arreglo[i])
        except ValueError:
            bandera = False
    return bandera
def sumar_valores(arreglo):
    """Función que dado un arreglo suma todos los
    valores en el arreglo
    Función de python: sum()
    (list1D) -> int"""
    suma = 0
    for i in range(len(arreglo)):
        suma += int(arreglo[i])
    return suma
def media_aritmética(arreglo):
    """Función que dado un arreglo saca la media de todos los
    valores en el arreglo
    Función de python: mean()
    (list1D) -> float"""
    media = sumar_valores(arreglo) / len(arreglo)
    return media
def mayor_valor(arreglo):
    """Función que dado un arreglo da el mayor valor de los
    valores en el arreglo
    Función de python: max()
    (list1D) -> float"""
    mayor = int(arreglo[0])
    for i in range(1, len(arreglo)):
        if int(arreglo[i]) >= mayor:
            mayor = int(arreglo[i])
    return mayor
def menor_valor(arreglo):
    """Función que dado un arreglo da el menor valor de los
    valores en el arreglo
    Función de python: min()
    (list1D) -> float"""
    menor = int(arreglo[0])
    for i in range(1, len(arreglo)):
        if int(arreglo[i]) <= menor:
            menor = int(arreglo[i])
    return menor
def mas_apariciones(arreglo):
    """Función que dado un arreglo da el o los valores que mas
    se repiten con el numero de repeticiones
    Función de python: from statistics import mode()
    (list1D) -> list1D, int"""
    apariciones = []
    for j in range(len(arreglo)):
        veces = 0
        for i in range(len(arreglo)):
            if arreglo[j] == arreglo[i]:
                veces += 1
        apariciones += [veces]
    m_repet = apariciones[0]
    for i in range(1, len(arreglo)):
        if apariciones[i] >= m_repet:
            m_repet = apariciones[i]
    r_valor = []
    for i in range(len(apariciones)):
        if apariciones[i] == m_repet and arreglo[i] not in r_valor:
            r_valor += [arreglo[i]]
    return r_valor, m_repet
def intercalados(arreglo, arreglo2):
    """Función que dado dos arreglo da un tercero con los valores
    de los dos intercalados
    (list1D, list1D) -> list1D"""
    bandera1 = len(arreglo)
    bandera2 = len(arreglo2)
    n_arreglo = []
    while bandera1 != 0 and bandera2 != 0: 
        n_arreglo += [arreglo[len(arreglo) - bandera1]]
        bandera1 += -1
        n_arreglo += [arreglo2[len(arreglo2) - bandera2]]
        bandera2 += -1
    if bandera1 == 0 and bandera2 != 0:
        for i in range(bandera2):
            n_arreglo += [arreglo2[-bandera2 + i]]
    elif bandera2 == 0 and bandera1 != 0:
        for i in range(bandera1):
            n_arreglo += [arreglo[-bandera1 + i]]
    return n_arreglo
def insertar_valor(arreglo, posicion, valor):
    """Función que dado un valor, una posición y un arreglo
    inserta el valor en la posición dentro del arreglo
    Función de python: insert()
    (list, int, int) -> list1D"""
    n_matriz = arreglo[0:posicion] + [valor] + arreglo[posicion: len(arreglo) + 1]
    return n_matriz
def main():
    arreglo = input("Ingrese el arreglo, valores separados por comas\n").split(",")
    valor = input("Ingrese un valor\n")
    # 1
    encontrar = encontrar_valor(arreglo, valor)
    if encontrar == True:
        respuesta = "si"
    else:
        respuesta = "no"
    print("*" + valor, respuesta, "esta en el arreglo dado")
    # 2
    columna = primera_posicion_valor(arreglo, valor)
    if columna >= 0:
        print("*La primera ocurrencia del valor esta en la columna " + str(columna + 1))
    else:
        print("*No se puede dar la primera ocurrencia del valor en arreglo.")
    #3
    print("*El valor aparece " + str(cantidad_veces_valor(arreglo, valor)) + " veces en el arreglo.")
    #4
    posiciones = posiciones_valor(arreglo, valor)
    if posiciones != []:
        print("*El valor ingresado se encuentra en las siguientes posiciones: ")
        for i in range(len(posiciones)):
            print("Columna " + str(posiciones[i]))
    else:
        print("*No se puede dar las posiciones del valor en el arreglo.")
    #5
    print("*El arreglo sin el valor dado es: \n" + str(eliminar_valor(arreglo, valor)))
    #6
    bandera = tipo_valores(arreglo)
    if bandera:
        print("*El arreglo se compone de solo valores tipo int.")
        #7
        print("*La suma de los valores en el arreglo es: " + str(sumar_valores(arreglo)))
        #8
        print("*La media aritmética de los valores en el arreglo es: " + str(media_aritmética(arreglo)))
        #9
        print("*El mayor valor en el arreglo es: " + str(mayor_valor(arreglo)))
        #10
        print("*El menor valor en el arreglo es: " + str(menor_valor(arreglo)))
    else:
        print("*El arreglo no se compone de solo valores tipo int.")
    #11
    r_valor, m_repet = mas_apariciones(arreglo)
    print("*El/Los valores que mas se repiten son: " + str(r_valor) + " con " + str(m_repet) + " repeticiones.")
    #12
    arreglo2 = input("*Ingrese otro arreglo, valores separados por comas\n").split(",")
    print("El arreglo resultante de intercalar los arreglos dados es: \n" + str(intercalados(arreglo, arreglo2)))
    #13
    posicion = int(input("*¿En qué posición del arreglo quiere insertar el valor?\n"))
    print("La matriz " + str(arreglo) + "insertandole " + valor + " en la posicion " + str(posicion) + " queda: \n" + str(insertar_valor(arreglo, posicion, valor)))
main()
