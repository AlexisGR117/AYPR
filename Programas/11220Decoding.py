def decodificacion(mensaje, decodificado_total):
    """Función que dado el mensaje que se quiere enviar devuelve la forma decodificada de este
    (str, str) -> str"""
    while mensaje != "":
        palabras = mensaje.split()
        decodificado = ""
        cont = 0
        for i in range(len(palabras)):
            if cont < len(palabras[i]) :
                decodificado += palabras[i][cont]
                cont += 1
        decodificado_total += decodificado + "\n"
        mensaje = input()
    return decodificado_total
def main():
    casos = int(input())
    espacio = input()
    for i in range(1, casos + 1):
        mensaje = input()
        decodificado_total = "Case #"+ str(i) + ":\n"
        print(decodificacion(mensaje, decodificado_total))
main()
