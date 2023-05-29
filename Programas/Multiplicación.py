factor_1 = int(input("escriba el primer factor de la multiplicacion"))
factor_2 = int(input("escriba el segundo factor de la multiplicacion"))
producto = 0
for i in range(abs(factor_2)):
        producto = producto + abs(factor_1)
if (factor_1 < 0 and factor_2 < 0) or (factor_1 > 0 and factor_2 > 0):
        print (producto)
elif (factor_1 < 0 and factor_2 > 0) or (factor_1 > 0 and factor_2 < 0):
        print (-(producto))
else:
        print (0)
