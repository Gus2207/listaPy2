'''6 - Faça um algoritmo que peça 3 números para o usuário e verifique qual o
maior e menor número, mostrar também quando tiver números iguais.'''

while True:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    if(n1 == n2 == n3):
        print("os numeros são iguais")
    else:
        maior = n1

        if(n2 > n3 and n2 > n1):
            maior = n2
        elif(n3 > n2 and n3 > n1):
            maior = n3
        
        menor = n1

        if(n2 < n3 and n2 < n1):
            menor = n2
        elif(n3 < n2 and n3 < n1):
            menor = n3
        
        print(f"\nO número {maior} é o maior número")
        print(f"O número {menor} é o menor número")
  

    opcao = int(input("\nDeseja verificar outra caso: 1 = SIM   2 = NÃO \n"))
    if(opcao == 1):
        print("Repita o processo \n")
    else:
        break;