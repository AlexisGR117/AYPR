#Algoritmo que ayuda a Juan a calcular una potencia a^b sin usar *
base = int(input())
exponente = int(input())
def multiplicacion (base, resultado):
    '''Funcion que multiplica sin usar *'''
    producto = 0
    for i in range(abs(resultado)):
        producto = producto + abs(base)
    if (base < 0 and resultado < 0) or (base > 0 and resultado > 0):
        return(producto)
    elif (base < 0 and resultado > 0) or (base > 0 and resultado < 0):
        return(-(producto))
    else:
        return(0)
residuo_exponente = abs(exponente)
resultado = 1
while residuo_exponente > 0:
    resultado = multiplicacion(base, resultado)
    residuo_exponente = residuo_exponente - 1
while residuo_exponente > 0:
    resultado = multiplicacion (base, resultado)
    residuo_exponente = residuo_exponente - 1
if exponente < 0:
    resultado = 1/resultado
print(resultado)
