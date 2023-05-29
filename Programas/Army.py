def main():
    '''Función que dice cuantos años deben pasar para que Vasya suba de rango
    (int, str, str) -> int'''
    maximo_rango = int(input())
    anos = input().split(" ")
    anos_conjunto = []
    anos_final = []
    for i in range(len(anos)):
        anos_conjunto += [int(anos[i])]
    rangos = input().split(" ")
    rango_inicial = int(rangos[0])
    rango_final = int(rangos[1])
    rangos_conjunto = []
    anos_total = 0
    for i in range(rango_inicial, maximo_rango + 1):
        rangos_conjunto += [i]
    if len(anos_conjunto) < len(rangos_conjunto):
        for i in range(len(rangos_conjunto) - len(anos_conjunto)):
            anos_conjunto.insert(0, 0)
    if len(rangos_conjunto) < len(anos_conjunto):
        for i in range(len(anos_conjunto) - len(rangos_conjunto)):
            rangos_conjunto.insert(0, 0)
    for i in range(len(rangos_conjunto)):
        if rangos_conjunto[i] == rango_final:
            posicion_final = i
    for i in range(len(rangos_conjunto)):
        if rangos_conjunto[i] == rango_inicial:
            posicion_inicial = i
    for i in range(posicion_inicial + 1, posicion_final + 1):
        anos_total += anos_conjunto[i]
    print(anos_total)
main()
