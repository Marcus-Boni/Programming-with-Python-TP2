def contar_vogais():
    """
    Lê uma sequência de caracteres inseridos um por um pelo usuário até encontrar um ponto (.)
    e exibe o número total de vogais digitadas.

    A função conta apenas os caracteres que são vogais ('a', 'e', 'i', 'o', 'u'), ignorando
    caracteres especiais, números e letras consonantes!
    """
    vogais = "aeiouAEIOU"
    contador = 0

    while True:
        caractere = input("Entre com um caractere: ")

        if caractere == ".":
            break

        if caractere in vogais:
            contador += 1

    print("Número de vogais:", contador)

contar_vogais()
