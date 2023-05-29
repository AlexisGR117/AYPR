def valor_absoluto(numero):
    '''Funcion que devuelve el valor absoluto de un numero
    (int) -> int'''
    absoluto = abs(numero)
    return absoluto
def main():
    '''Funcion que dado tres valores da el mayor valor
    (int, int, int) -> int'''
    numero_1 = int(input())
    numero_1 = valor_absoluto(numero_1)
    numero_2 = int(input())
    numero_2 = valor_absoluto(numero_2)
    numero_3 = int(input())
    numero_3 = valor_absoluto(numero_3)
    if numero_1 >= numero_2 and numero_1 >= numero_3:
        print(numero_1)
    elif numero_2 >= numero_1 and numero_2 >= numero_3:
        print(numero_2)
    else:
        print(numero_3)
main()
