def eh_primo(numero):
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    # 2 e 3 são primos
    elif numero <= 3:
        return True
    # Números divisíveis por 2 ou 3 não são primos
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        # Verifica apenas divisores até a raiz quadrada do número
        i = 5
        # Verifica divisibilidade apenas por números da forma 6k ± 1
        # onde k é um inteiro, até a raiz quadrada do número
        while i * i <= numero:
            # Verifica se o número é divisível por i ou i + 2
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            # Incrementa i para o próximo candidato primo
            i += 6
        return True


# Exemplo de uso:
print(eh_primo(17))  # Deveria imprimir True (17 é primo)
print(eh_primo(25))  # Deveria imprimir False (25 não é primo)


def primo(numero):
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    # 2 e 3 são primos
    elif numero <= 3:
        return True
    # Números divisíveis por 2 ou 3 não são primos
    else:
        for x in range(3, numero + 1):
            if numero == x:
                # print(x, numero)
                return True
            elif numero % x == 0:
                # print(x, numero)
                return False
            else:
                # print("nada")
                pass


print(primo(17))  # Deveria imprimir True (17 é primo)
print(primo(25))  # Deveria imprimir False (25 não é primo)
