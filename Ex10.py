def ler_numeros():
    """
    Lê uma sequência de números terminada por zero e retorna uma lista com os números lidos (exceto o zero).

    Returns:
        list: Lista de números lidos.
    """
    numeros = []
    while True:
        numero = float(input("Digite um número (0 para sair): "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def exibir_numeros_filtrados(numeros):
    """
    Exibe os números maiores ou iguais à média dos números fornecidos.

    Args:
        numeros (list): Lista de números para filtrar e exibir.
    """
    if not numeros:
        print("Nenhum número foi informado.")
        return
    media = sum(numeros) / len(numeros)
    print(f"Média dos números: {media}")
    print("Números maiores ou iguais à média:")
    for numero in numeros:
        if numero >= media:
            print(numero)

def main():
    """
    Função principal que coordena a leitura e exibição dos números filtrados.
    """
    numeros = ler_numeros()
    exibir_numeros_filtrados(numeros)

if __name__ == "__main__":
    main()