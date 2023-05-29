# Autores: Daniel Fernando Moreno Cerón, Jefer Alexis González Romero
# Fecha: 15/03/2021
def saludo():
    '''Función que introduce al usuario al programa
    (none) -> str'''
    print("Este programa convierte temperaturas en un rango dado")
    print("Digite (C) para converitr de Farenheit a Celsius")
    print("Digite (F) para convertir de Celsius a Farenheit")
def lee_opcion():
    '''Función que lee si el usuario quiere convertir de C a F o de F a C
    (str) -> str'''
    opcion = input("\nDigite su leccion ")
def con_fahrentoce1(inicio, fin):
    '''Función que convierte de grados farenheit a celsius
    (int) -> (float, str)'''
    celsius = []
    farenheit = []
    for i in range(inicio, fin + 1):
        celsius += [5 * (inicio - 32) / 9]
        farenheit += [i]
    print("\nCelsius ", "Farenheit")
    for i in range(len(farenheit)):
        if celsius[i] < 10:
            print("  " + str(float(celsius[i])) + "       " + str(float(farenheit[i]))) 
        elif celsius[i] < 100 and celsius[i] >= 10:
            print(" " + str(float(celsius[i])) + "       " + str(float(farenheit[i]))) 
def con_celsiusfahren(inicio, fin):
    '''Función que convierte de grados celsius a fahrenheit
    (int) -> (float, str)'''
    farenheit = []
    celsius = []
    for i in range(inicio, fin + 1):
        farenheit += [(i * 1.8) + 32]
        celsius += [i]
    print("\nCelsius ", "Farenheit")
    for i in range(len(farenheit)):
        if celsius[i] < 10:
            print("  " + str(float(celsius[i])) + "        " + str(float(farenheit[i]))) 
        elif celsius[i] < 100 and celsius[i] >= 10:
            print(" " + str(float(celsius[i])) + "        " + str(float(farenheit[i]))) 
def main():
    saludo()
    opc = lee_opcion()
    inicio = int(input("\nDiga temperatura inicial "))
    fin = int(input("Diga temperatura final "))
    if opc == "C":
        con_fahrentoce1(inicio, fin)
    else:
        con_celsiusfahren(inicio, fin)
main()
        
