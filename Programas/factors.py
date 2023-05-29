def primo(numero):
    '''Funcion que dice si el numero entregado es primo
    (int) -> int'''
    cont = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            cont = cont + 1
    return cont
def divisor(num):
    '''Funcion que da los divisores de un numero
    (int) -> str'''
    divisores = []
    for i in range(1,num+1):
        if num % i == 0:
            divisores = divisores + [i]
    return divisores
def main():
    '''Funcion que suma los primos de los divisores de un numero no primo
    (int) -> int'''
    n = int(input())
    cont = 0
    suma = 0
    if primo(n) == 2:
        print("Es primo.")
    else:
        for i in range(len(divisor(n))):
            if primo((divisor(n))[i]) == 2:
                suma = suma + (divisor(n))[i]
        print(suma)
main()
