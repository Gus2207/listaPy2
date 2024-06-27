'''1 - Baltazar precisa saber se um número é positivo ou negativo desenvolva
o algoritmo que resolva isso.'''
while True:
    numero = int(input("Digite um número: "))

    if (numero < 0):
        print("O número é negativo \n")
    else:
        print("O número é positivo \n")

    opcao = int(input("Deseja verificar outro número: 1 = SIM   2 = NÃO"))

    if(opcao == 1):
        print("Repita o processo \n")
    else:
        break;