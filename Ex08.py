def somar_listas(lista1, lista2):
    """
    Soma duas listas elemento por elemento.

    Args:
        lista1 (list): A primeira lista de números.
        lista2 (list): A segunda lista de números.

    Returns:
        list: Uma nova lista contendo a soma dos elementos correspondentes de lista1 e lista2.
    """
    lista_soma = []
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        lista_soma.append(soma)
    return lista_soma

def main():
    """
    Define as duas listas e exibe o resultado da soma.
    """
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
    lista2 = [10, 20, 30, 40, 50, 60, 70, 80]
    lista_soma = somar_listas(lista1, lista2)
    print("A soma das listas é:")
    print(lista_soma)

if __name__ == "__main__":
    main()