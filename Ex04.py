def mostrar_tabuada():
    """
    Exibe a tabuada dos números de 1 a 10.
    """
    for num in range(1, 11):
        print(f"Tabuada do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
        print("-" * 20)

mostrar_tabuada()