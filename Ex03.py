def calcular_fatorial(n):
    """
    Calcula o fatorial de um número inteiro positivo n.

    Args:
        n (int): O número inteiro positivo para calcular o fatorial.

    Returns:
        int: O fatorial de n.
    """
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def main():
    """
    Lê uma sequência de números inteiros positivos e exibe o fatorial de cada um.
    A leitura termina quando o usuário digita zero.
    """
    while True:
        numero = int(input("Digite um número inteiro positivo (0 para sair): "))
        if numero == 0:
            break
        elif numero < 0:
            print("Por favor, digite um número positivo.")
        else:
            resultado = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é {resultado}!")

if __name__ == "__main__":
    main()