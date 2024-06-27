'''2 - Um usuário precisar saber o maior entre dois números digitados.
Desenvolva o algoritmo que resolva isso.'''
while True:
    numero1 = float(input("Digite o primeiro número "))
    numero2 = float(input("Digite o segundo número "))

    if(numero1 == numero2):
        print("Os números são iguais \n")
    else:
        if(numero1 > numero2):
            print(f"O numero {numero1} é maior que o número {numero2} \n")
        else:
            print(f"O numero {numero2} é maior que o número {numero1} \n")

    opcao = int(input("Deseja verificar outros números: 1 = SIM   2 = NÃO"))

    if(opcao == 1):
        print("Repita o processo \n")
    else:
        break;
