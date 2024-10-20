def segundo_maior(lista):
   
    maior = max(lista)
   
    lista_filtrada = [num for num in lista if num != maior]
    
    
    return max(lista_filtrada)

# Exemplo de uso
lista = [10, 20, 4, 45, 99, 99]
resultado = segundo_maior(lista)
print(resultado)