# 3. Fibonacci
# Pergunta:
# Escreva uma função para gerar os n primeiros números da sequência de Fibonacci.


def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


n = int(input("Qual será o n?"))


resultado = fibonacci(n)
print(resultado)
