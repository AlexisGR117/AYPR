def factorial(num):
    '''Funcion que calcula el factorial de un numero dado
    (int) -> int'''
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
def main():
    '''Funcion que calcula el coeficioente binomial C(n,k)
    (int, int) -> Int'''
    entrada = str(input())
    separador = ","
    valores = entrada.split(separador)
    num_n = valores[0]
    num_k = valores[1]
    coef_bin = factorial(int(num_n)) / (factorial(int(num_k)) * (factorial(int(num_n)-int(num_k))))
    print(int(coef_bin))
main()
