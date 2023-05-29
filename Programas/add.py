a = int(input())
b = int(input())
suma = a + b
if a < 0 and b < 0:
    print('(' +str(a)+ ')' +'+'+'(' +str(b)+ ')' + '=' +str(suma))
elif a>0 and b<0:
    print(str(a)+'+'+'(' +str(b)+ ')' + '=' +str(suma))
elif a<0 and b>0:
    print('(' +str(a)+ ')' +'+'+str(b)+ '=' +str(suma))
elif a>=0 and b>=0:
    print(str(a)+'+'+str(b)+ '=' +str(suma))
