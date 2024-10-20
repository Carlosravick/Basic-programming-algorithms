#lista = [1,5,7,9,5]
def calculate(lista):
    impa = []  
    for listas in lista:
        if listas % 2 == 1:
            impa.append(listas)
    return impa  

print(calculate([5, 6, 8, 7, 6]))