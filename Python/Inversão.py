# 9. Inversão de String
# Pergunta:
# Escreva uma função que inverta uma string.


def inverter_string(string):
    return string[::-1]


# Exemplo de uso:
texto = "Python"
print(inverter_string(texto))  # Deveria imprimir "nohtyP" (string invertida)
print(list(inverter_string(texto)))
print(list(inverter_string(texto))[::-1])
