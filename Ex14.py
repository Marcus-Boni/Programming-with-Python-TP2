def ler_numero_positivo():
    """
    Lê um número do teclado e garante que ele seja maior ou igual a zero.
    Enquanto a entrada não for válida, exibe uma mensagem de erro e pede uma nova entrada.

    Returns:
        int: Um número inteiro maior ou igual a zero.
    """
    while True:
        numero = int(input("Digite um número maior ou igual a zero: "))
        if numero >= 0:
            return numero
        else:
            print("Erro: O número deve ser maior ou igual a zero. Tente novamente.")

def main():
    """
    Função principal que lê um número positivo e o exibe.
    """
    numero = ler_numero_positivo()
    print(f"Você digitou o número: {numero}")

if __name__ == "__main__":
    main()