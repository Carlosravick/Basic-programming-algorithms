def primos(lista):
    primo = []
    for num in lista:
        if num < 2:
            continue  # Números menores que 2 não são primos
        is_primo = True
        for i in range(2, int(num**0.5) + 1):  # Verifica até a raiz quadrada de num
            if num % i == 0:
                is_primo = False
                break
        if is_primo:
            primo.append(num)
    return primo

print(primos([1,2, 3, 5, 8, 9]))




