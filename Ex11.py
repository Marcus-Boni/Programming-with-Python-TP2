def buscar_elemento(lista, elemento):
    """
    Busca um elemento na lista e retorna sua posição.
    Se não encontrar, retorna -1.

    Args:
        lista (list): A lista de números onde será feita a busca.
        elemento (int): O número a ser procurado na lista.

    Returns:
        int: A posição do elemento na lista ou -1 se não for encontrado.
    """
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice
    return -1

def main():
    """
    Lê um número do teclado e verifica se está presente na lista.
    Exibe a posição se encontrado ou -1 caso contrário.
    """
    lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]
    numero = int(input("Digite um número: "))
    posicao = buscar_elemento(lista, numero)
    if posicao != -1:
        print(f"O número {numero} foi encontrado na posição {posicao}.")
    else:
        print("-1")

if __name__ == "__main__":
    main()