'''5 - Faça um Programa que verifique se uma letra digitada é vogal ou
consoante.'''
while True:
    letra = input("Digite a letra a ser comparada: ")

    if(str.lower(letra) in "aeiou"):
        print(f"A letra {letra} é uma vogal")
    else:
        print(f"A letra {letra} não é uma vogal")

    opcao = int(input("\nDeseja verificar outra letra: 1 = SIM   2 = NÃO \n"))
    
    if(opcao == 1):
        print("Repita o processo \n")
    else:
        break;