# Autor: Jefer Alexis González Romero
# Fecha: 17/03/2021
def main():
    """Función que dice los días en los cuales hubo diferencias en el numero de vacunados
    (str) -> str"""
    puestos_1 = input()
    puestos_2 = input()
    puestos_1 = puestos_1.split(",")
    puestos_2 = puestos_2.split(",")
    dias_diferentes = []
    cadena_diferentes = ""
    for i in range(len(puestos_1)):
        if puestos_1[i] != puestos_2[i]:
            dias_diferentes += [i + 1]
    for i in range(len(dias_diferentes)):
        cadena_diferentes += str(dias_diferentes[i]) + ","
    cadena_diferentes = cadena_diferentes[0:-1]
    if cadena_diferentes != "":
        print(cadena_diferentes)
    else:
        print("No hay diferencias.")
main()
