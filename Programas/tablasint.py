def multiplicacion(numero_1, numero_2):
    '''Funcion que calcula la multiplicion
    (int, int) -> int'''
    mult = numero_1 * numero_2
    return mult
def tabla(n,m,p,q):
    '''funcion que calcula la tabla de multiplicar
    (int, int, int, int) -> str'''
    for i in range(n, m+1):
        for j in range(p, q+1):
            print(str(i)+ ' '+ 'X'+ ' '+ str(j)+ ' '+ '=' + ' '+ str(multiplicacion(i,j)))
        if i != m:
            print("---------------")
def main():
    '''Funcion que imprime la tabla de multiplicar del numero n a m en el intervalo [p, q]
    (int, int, int, int) -> str'''
    n = int(input())
    m = int(input())
    p = int(input())
    q = int(input())
    tabla(n,m,p,q)
main()
