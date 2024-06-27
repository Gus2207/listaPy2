'''3 - Uma escola precisa de um programa que ao lançar 4 notas de um aluno
deverá calcular sua média e imprimir o seguinte status: Aprovado média 70
ou superior, Recuperação média entre 50 e 69 E Reprovado inferior a 50.'''
while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A media do aluno é: {media}")

    if(media >= 70):
        print("Aprovado média 70 ou superior")
    elif(media >= 50 and media <= 69):
        print("Recuperação média entre 50 e 69")
    else:
        print("Reprovado media inferior a 50.")

    opcao = int(input("Deseja verificar a media de outro aluno: 1 = SIM   2 = NÃO \n"))

    if(opcao == 1):
        print("Repita o processo \n")
    else:
        break;