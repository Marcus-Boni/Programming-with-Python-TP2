def gerar_pa(primeiro_termo, segundo_termo, quantidade_termos):
    """
    Gera uma Progressão Aritmética (PA) a partir de dois números inteiros.

    Args:
        primeiro_termo (int): O primeiro termo da PA.
        segundo_termo (int): O segundo termo da PA.
        quantidade_termos (int): A quantidade de termos da PA a serem gerados.

    Returns:
        list: Uma lista contendo os termos da PA.
    """
    razao = segundo_termo - primeiro_termo
    pa = [primeiro_termo]
    for i in range(1, quantidade_termos):
        termo = primeiro_termo + i * razao
        pa.append(termo)
    return pa

def main():
    """
    Função principal que solicita ao usuário os dados e exibe a PA gerada.
    """
    primeiro_termo = int(input("Digite o primeiro número inteiro: "))
    segundo_termo = int(input("Digite o segundo número inteiro: "))
    quantidade_termos = int(input("Digite a quantidade de termos da PA: "))
    pa = gerar_pa(primeiro_termo, segundo_termo, quantidade_termos)
    print("A Progressão Aritmética é:")
    for termo in pa:
        print(termo)

if __name__ == "__main__":
    main()