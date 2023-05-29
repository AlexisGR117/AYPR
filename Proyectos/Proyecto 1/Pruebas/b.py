def familia_palabras(texto, palabra):
  familia =[]
  for i in texto:
    letras = 0
    for j in range(len(palabra)):
      if palabra[j] == i[j]:
        letras = letras + 1
    if len(palabra) == letras:
      familia.append(i)
  print(familia)
def main():
  texto = ["florero", "florida", "Nicole", "Nicolasito", "Nicolasita", "Nicolas", "floro", "florista", "florido", "floricultura", "florecer", "floral", "celulas", "computado"]
  palabra = input()
  familia_palabras(texto, palabra)
main()
