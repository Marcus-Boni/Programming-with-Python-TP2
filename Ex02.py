def calcular_soma(n):
    """
    Calcula a soma dos números de 1 até n.

    Args:
    n (int): O número até onde calcular a soma.

    Returns:
    int: A soma dos números de 1 até n.
    """
    return sum(range(1, n + 1))

def calcular_media(soma, n):
    """
    Calcula a média dos números de 1 até n.

    Args:
    soma (int): A soma dos números de 1 até n.
    n (int): O número até onde calcular a média.

    Returns:
    float: A média dos números de 1 até n.
    """
    return soma / n

soma = calcular_soma(100)

media = calcular_media(soma, 100)

print(f"Soma: {soma}")
print(f"Média: {media}")