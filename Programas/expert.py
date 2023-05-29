def fabricantes(num_fabricantes):
    """Función que da una matriz con los fabricantes y sus respectivos limites de precio
    (int) -> list"""
    fabricantes = []
    for i in range(num_fabricantes):
            fabricante = input().split()
            fabricantes += [fabricante]
    return fabricantes
def consultas(num_consultas):
    """Función que da una lista con las diferentes consultas que se piden
    (int) -> list"""
    consultas = []
    for i in range(num_consultas):
        consultas += [int(input())]
    return consultas
def consulta(num_consultas, num_fabricantes, fabricantes, consultas):
    """Función que da el resultado de cada consulta
    (int, int, list, list) -> str"""
    resultado_consulta = ""
    for i in range(num_consultas):
        opcion = 0
        for k in range(num_fabricantes):
            if int(fabricantes[k][1]) <= consultas[i] and int(fabricantes[k][2]) >= consultas[i]:
                opcion += 1
                nombre_fabricante = fabricantes[k][0]
        if opcion == 1:
            resultado_consulta += str(nombre_fabricante) + "\n"
        else:
            resultado_consulta += "UNDETERMINED\n"
    return resultado_consulta
def main():
    casos = int(input())
    for j in range(casos):
        num_fabricantes = int(input())
        todos_fabricantes = fabricantes(num_fabricantes)
        num_consultas = int(input())
        todas_consultas = consultas(num_consultas)
        print(consulta(num_consultas, num_fabricantes, todos_fabricantes, todas_consultas))
main()
