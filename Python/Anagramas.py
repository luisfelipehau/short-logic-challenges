# 4. Anagramas
# Pergunta:
# Escreva uma função que determine se duas strings são anagramas uma da outra.


def are_anagrams(str1, str2):
    # Remover espaços e converter para minúsculas para uma comparação case-insensitive
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Comparar as strings ordenadas
    return sorted(str1) == sorted(str2)


# Exemplos de uso
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("apple", "pale"))  # False
