'''4 - A empresa que você trabalha resolveu dar um aumento de salário aos
seus colaboradores, você deve programar uma aplicação que receba o
salário atual de um colaborador e o reajuste cumprindo as seguintes regras:
Os salários até R$ 280,00 aumento de 20%
Os salários entre R$ 281,00 e R$ 700,00: aumento de 15%
Os salários entre R$ 701,00 e R$ 1500,00: aumento de 10%
Os salários superiores a R$ 1501,00 aumento de 5%.
Após o aumento ser realizado, informe na tela:
O salário antes do reajuste;
O percentual de aumento aplicado;
O valor do aumento;
O novo salário, após o aumento;'''
while True:
    salarioAtual = float(input("Digite o seu sálario atual: "))
    reajuste = 0
    salarioReajuste = 0

    if(salarioAtual <= 280):
        reajuste = salarioAtual * 0.2
        salarioReajuste = salarioAtual + reajuste
        print(f"O salário antes do reajuste: {salarioAtual}")
        print("O porcentual de aumento foi de 20%")
        print(f"O valor de aumento foi de {reajuste}")
        print(f"O valor do salario com o reajuste fica no total de: {salarioReajuste}")
    elif(salarioAtual >= 281 and salarioAtual <= 700):
        reajuste = salarioAtual * 0.15
        salarioReajuste = salarioAtual + reajuste
        print(f"O salário antes do reajuste: {salarioAtual}")
        print("O porcentual de aumento foi de 15%")
        print(f"O valor de aumento foi de {reajuste}")
        print(f"O valor do salário com o reajuste fica no total de: {salarioReajuste}")
    elif(salarioAtual >= 701 and salarioAtual <= 1500):
        reajuste = salarioAtual * 0.1
        salarioReajuste = salarioAtual + reajuste
        print(f"O salário antes do reajuste: {salarioAtual}")
        print("O porcentual de aumento foi de 10%")
        print(f"O valor de aumento foi de {reajuste}")
        print(f"O valor do salário com o reajuste fica no total de: {salarioReajuste}")
    else:
        reajuste = salarioAtual * 0.05
        salarioReajuste = salarioAtual + reajuste
        print(f"O salário antes do reajuste: {salarioAtual}")
        print("O porcentual de aumento foi de 5%")
        print(f"O valor de aumento foi de {reajuste}")
        print(f"O valor do salário com o reajuste fica no total de: {salarioReajuste}")

    opcao = int(input("\nDeseja verificar outro reajuste salarial: 1 = SIM   2 = NÃO \n"))
    
    if(opcao == 1):
        print("Repita o processo \n")
    else:
        break;
