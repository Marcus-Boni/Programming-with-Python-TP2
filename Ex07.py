def mostrar_lista_invertida(lista):
    """
    Mostra o conteúdo da lista na ordem invertida.

    Args:
        lista (list): A lista de números a ser invertida.
    """
    indice = len(lista) - 1
    while indice >= 0:
        print(lista[indice])
        indice -= 1

def main():
    """
    Define a lista e chama a função para exibir a lista invertida.
    """
    lista = [10, 20, 30, 40, 50, 60, 70, 80]
    mostrar_lista_invertida(lista)

if __name__ == "__main__":
    main()