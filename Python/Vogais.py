# 8. Contagem de Vogais
# Pergunta:
# Escreva uma função que conte o número de vogais em uma string.


def contar_vogais(string):
    vogais = "aeiouAEIOU"  # Vogais minúsculas e maiúsculas
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador


# Exemplo de uso:
texto = "Python é uma linguagem de programação poderosa e versátil."
print(contar_vogais(texto))  # Deveria imprimir 20 (contagem de vogais na string)
