def ler_dados_aluno():
    """
    Lê o nome e as duas notas de um aluno.

    Returns:
        tuple: Nome do aluno e suas duas notas.
    """
    nome = input("Entre com o nome: ")
    if nome.lower() == "fim":
        return nome, 0, 0
    nota1 = float(input("Entre com a nota 1: "))
    nota2 = float(input("Entre com a nota 2: "))
    return nome, nota1, nota2

def calcular_media_aluno(nota1, nota2):
    """
    Calcula a média de duas notas.

    Args:
        nota1 (float): A primeira nota.
        nota2 (float): A segunda nota.

    Returns:
        float: A média das duas notas.
    """
    return (nota1 + nota2) / 2

def calcular_media_turma(medias):
    """
    Calcula a média geral da turma.

    Args:
        medias (list): Lista das médias dos alunos.

    Returns:
        float: A média geral da turma.
    """
    return sum(medias) / len(medias)

def main():
    """
    Função principal que coordena a leitura dos dados dos alunos, cálculo das médias e exibição dos resultados.
    """
    medias = []
    while True:
        nome, nota1, nota2 = ler_dados_aluno()
        if nome.lower() == "fim":
            break
        media = calcular_media_aluno(nota1, nota2)
        medias.append(media)
        print(f"Média = {round(media, 1)}")
        if media >= 6:
            print("Aluno aprovado")
        else:
            print("Aluno em prova final")
    
    if medias:
        media_turma = calcular_media_turma(medias)
        print(f"Média da turma = {round(media_turma, 1)}")

if __name__ == "__main__":
    main()