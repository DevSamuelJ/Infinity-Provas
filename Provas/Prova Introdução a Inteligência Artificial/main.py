qnt_alunos = int(input("Digite a quantidade de alunos: "))
alunos = []
soma_geral = 0.0

for aluno in range(1, qnt_alunos + 1):
    nome = input(f"\nDigite o nome do {aluno}º aluno: ")
    soma = 0.0

    notas = []
    for contagem_notas in range(1, 4):
        valor_notas = float(input(f"Digite a {contagem_notas}º nota de {nome}: "))
        notas.append(valor_notas)
        soma += valor_notas

    media_aluno = soma / 3

    if media_aluno > 6.9:
        status = "Aprovado"
        print(f"Média do aluno: {media_aluno:.2f}")
        print("Aluno aprovado!")
    else:
        status = "Recuperação"
        print(f"Média do aluno: {media_aluno:.2f}")
        print("Aluno em recuperação!")

    aluno_info = {
        "nome": nome,
        "notas": notas,
        "media": media_aluno,
        "status": status
    }
    alunos.append(aluno_info)
    soma_geral += media_aluno

print("\n===== Boletim dos Alunos =====")
for aluno in alunos:
    print(f"\nNome do Aluno: {aluno['nome']}")
    print(f"Notas: {aluno['notas'][0]:.2f}, {aluno['notas'][1]:.2f}, {aluno['notas'][2]:.2f}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['status']}")

media_geral_turma = soma_geral / qnt_alunos
print(f"\nMédia geral da turma: {media_geral_turma:.2f}")
