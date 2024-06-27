'''7 - Faça um algoritmo que peça 3 lados de um triângulo, o programa irá
verificar se é um triângulo Isósceles, Equilátero ou Escaleno.'''

while True:
    lado1 = float(input("Digite o primeiro lado do triangulo: "))
    lado2 = float(input("Digite o segundo lado do triangulo: "))
    lado3 = float(input("Digite o terceiro lado do triangulo: "))

    if(lado1 == lado2 == lado3):
        print("O triangulo é equilátero")
    elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        print("O triangulo é escaleno")
    else:
        print("O triangulo é isósceles")

    opcao = int(input("\nDeseja verificar outra caso: 1 = SIM   2 = NÃO \n"))
    if(opcao == 1):
        print("Repita o processo \n")
    else:
        break;