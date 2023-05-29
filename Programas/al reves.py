def main():
    secuencia = input().split(",")
    for i in range(len(secuencia) // 2):
        numero = secuencia[i]
        secuencia[i] = secuencia[-1-i]
        secuencia[-1 - i] = numero
    for i in range(len(secuencia) - 1):
        print(secuencia[i], end = ",")
    print(secuencia[-1])
main()
