#Algoritmo que en base de las medidas de los lados de un triangulo dice si es un triangulo equilatero, escaleno o isosceles
lado_1 = int(input())
lado_2 = int(input())
lado_3 = int(input())
if lado_1 <= 0 or lado_2 <= 0 or lado_3 <= 0:
    print("Error, lado(s) cero.")
elif lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_1 + lado_3 > lado_2:
    if lado_1== lado_2 and lado_2 == lado_3:
        print("Equilatero")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("No se puede armar un triangulo.")
