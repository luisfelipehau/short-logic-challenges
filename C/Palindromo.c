// 2. Palíndromo
// Pergunta:
// Escreva uma função que verifique se uma string é um palíndromo.


#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Função para verificar se uma string é um palíndromo
int isPalindrome(char str[]) {
    int left = 0;
    int right = strlen(str) - 1;

    // Converte todos os caracteres para minúsculas para uma comparação case-insensitive
    while (left < right) {
        // Ignora caracteres não alfanuméricos
        if (!isalnum(str[left])) {
            left++;
        } else if (!isalnum(str[right])) {
            right--;
        } else {
            // Compara os caracteres
            if (tolower(str[left]) != tolower(str[right])) {
                return 0; // Não é um palíndromo
            }
            left++;
            right--;
        }
    }
    return 1; // É um palíndromo
}

int main() {
    char str[100];

    printf("Digite uma string: ");
    fgets(str, sizeof(str), stdin);

    // Remove o newline character se presente
    str[strcspn(str, "\n")] = 0;

    if (isPalindrome(str)) {
        printf("A string e um palindromo.\n");
    } else {
        printf("A string nao e um palindromo.\n");
    }

    return 0;
}
