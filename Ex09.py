def ler_numeros():
    """
    Lê uma sequência de números terminada por zero e retorna uma lista com os números lidos (exceto o zero).
    
    Returns:
        list: Lista de números inteiros lidos do usuário.
    """
    numeros = []
    while True:
        numero = int(input("Digite um número (0 para terminar): "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def exibir_invertido(lista):
    """
    Exibe os elementos de uma lista na ordem invertida.
    
    Args:
        lista (list): A lista de números a ser exibida na ordem inversa.
    """
    for elemento in reversed(lista):
        print(elemento)

def main():
    """
    Função principal que coordena a leitura e a exibição invertida dos números.
    """
    numeros = ler_numeros()
    print("Números na ordem invertida:")
    exibir_invertido(numeros)

if __name__ == "__main__":
    main()