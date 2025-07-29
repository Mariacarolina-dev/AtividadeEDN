def media_turma():
    total_alunos = int(input("Quantos alunos na turma? "))
    soma = 0

    for i in range(total_alunos):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        soma += nota

    media = soma / total_alunos
    print(f"Média da turma: {media:.2f}")

media_turma()
