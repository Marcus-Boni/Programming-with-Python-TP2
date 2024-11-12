def main():
    """
    Mostra o menor, o maior, a soma e a média dos elementos da lista. Estatísticas básicas.
    """
    lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
    menor = min(lista)
    maior = max(lista)
    soma = sum(lista)
    media = soma / len(lista)
    
    print(f"Menor elemento: {menor}")
    print(f"Maior elemento: {maior}")
    print(f"Soma dos elementos: {soma}")
    print(f"Média dos elementos: {media}")
    
if __name__ == "__main__":
    main()