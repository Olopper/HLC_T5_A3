def contar_palabras(lista):
    diccionario = {palabra: len(palabra) for palabra in lista}
    print("Diccionario: "+str (diccionario))


lista = ["Hola", "Mundo", "Hola"]
print(lista)
contar_palabras(lista)