# 5. Soma de Pares
# Pergunta:
# Escreva uma função que receba uma lista de números e retorne a soma de todos os números pares da lista.


def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma


# Exemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(soma_pares(numeros))  # Deveria imprimir 30 (2 + 4 + 6 + 8 + 10 = 30)
