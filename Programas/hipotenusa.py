def hipotenusa():
    '''Funcion que calcula la hipotenusa de un triangulo rectangulo
    (float) -> float'''
    a = float(input())
    b = float(input())
    hip = (a ** 2 + b ** 2)** 0.5
    print(hip)
hipotenusa()
