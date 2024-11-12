def eh_primo(n):
    """
    Verifica se um número é primo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    """
    Lê um intervalo inferior e superior e mostra os números primos encontrados,
    além da quantidade total de primos no intervalo.
    """
    inferior = int(input("Digite o limite inferior do intervalo: "))
    superior = int(input("Digite o limite superior do intervalo: "))
    primos = []
    for num in range(inferior, superior + 1):
        if eh_primo(num):
            primos.append(num)
    if primos:
        print("Números primos encontrados:")
        print(", ".join(map(str, primos)))
    else:
        print("Nenhum número primo encontrado no intervalo!")
    print(f"Quantidade de números primos encontrados: {len(primos)}")

if __name__ == "__main__":
    main()