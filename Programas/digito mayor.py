#Algoritmo que dado un numero de cuatro digitos, da el digito mayor
numero = int(input())
digito_mayor = 0
for i in range(4):
    digito = numero // (10 ** (3-i))
    if digito >= digito_mayor:
        digito_mayor = digito
    numero = numero % (10 ** (3-i))
print(digito_mayor)
