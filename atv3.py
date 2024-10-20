def elementos_unicos(lista1, lista2):
    unicos = []
    for elemento in lista1:
        if elemento not in lista2:
            unicos.append(elemento)

    for elemento in lista2:
        if elemento not in lista1:
            unicos.append(elemento)

    return unicos


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = elementos_unicos(lista1, lista2)
print(resultado)