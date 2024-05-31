# 6. Fatorial
# Pergunta:
# Escreva uma função que calcule o fatorial de um número
# 𝑛.


def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
            # print(resultado)
        return resultado


# Exemplo de uso:
numero = 5
print(fatorial(numero))  # Deveria imprimir 120 (5 * 4 * 3 * 2 * 1 = 120)
