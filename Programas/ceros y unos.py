# Autor: Jefer Alexis Gonzalez Romeor
# Fecha: 03/05/2021
def m_lon_sub(secuencia):
    """Funcion que dada una secuencia de ceros y unos da
    la longitud de la subsecuencia mas larga
    (list1D) --> int"""
    lon = 1
    m_lon = 1
    for i in range(len(secuencia)-1):
        if int(secuencia[i]) == 1 and int(secuencia[i+1]) == 0:
            lon = 1
        else:
            lon += 1
            if lon > m_lon:
                m_lon = lon
    return m_lon
def main():
    secuencia = input()
    print(m_lon_sub(secuencia))
main()
