# 7. Maior Elemento
# Pergunta:
# Escreva uma função que encontre o maior elemento em uma lista de números.


def maior_elemento(lista):
    if len(lista) == 0:
        return None  # Retorna None se a lista estiver vazia
    else:
        maximo = lista[0]  # Assume o primeiro elemento como o máximo inicialmente
        for num in lista:
            if num > maximo:
                maximo = num
        return maximo


# Exemplo de uso:
numeros = [10, 4, 23, 7, 45, 12]
print(maior_elemento(numeros))  # Deveria imprimir 45 (o maior elemento na lista)


def maior_elemento_luis(lista):
    if len(lista) == 0:
        return None  # Retorna None se a lista estiver vazia
    else:
        lista = sorted(lista)
        return lista[-1]


# Exemplo de uso:
numeros = [10, 4, 23, 7, 45, 12]
print(maior_elemento_luis(numeros))
