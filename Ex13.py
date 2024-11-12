def eh_par(numero):
    """
    Verifica se um número é par.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número for par, False se for ímpar.
    """
    return numero % 2 == 0

def separar_pares_impares(lista):
    """
    Separa os números da lista em duas listas: uma de pares e outra de ímpares.

    Args:
        lista (list): A lista de números a ser separada.

    Returns:
        tuple: Duas listas, a primeira contendo os números pares e a segunda os ímpares.
    """
    pares = []
    impares = []
    for numero in lista:
        if eh_par(numero):
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def main():
    """
    Função principal que cria as listas de pares e ímpares e as exibe.
    """
    lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
    pares, impares = separar_pares_impares(lista)
    print("Números pares:", pares)
    print("Números ímpares:", impares)

if __name__ == "__main__":
    main()