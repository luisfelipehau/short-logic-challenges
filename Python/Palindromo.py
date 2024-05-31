# 2. Palíndromo
# Pergunta:
# Escreva uma função que verifique se uma string é um palíndromo.


def is_palindrome(s):
    return s == s[::-1]


# Exemplo de uso:
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
