'''8 - Faça um programa que peça o email e a senha para o usuário, o programa
irá verificar se o usuário é igual a admin e a senha igual a 123, se sim mostrar
usuário logado, se não informar se o usuário ou senha ou ambos estão
incorretos.'''

while True:
    email = "admin"
    senha = "123"

    emailVerificacao = input("Digite o email: ")
    senhaVerificacao = input("Digite sua senha: ")

    if emailVerificacao == email and senhaVerificacao == senha:
        print("usuário logado")
        break;
    elif emailVerificacao != email and senhaVerificacao == senha:
        print("acesso negado, usuário não encontrado")
        print("Tente novamente")
    elif emailVerificacao == email and senhaVerificacao != senha:
        print("acesso negado, senha incorreta")
        print("Tente novamente")
    else:
        print("acesso negado, usuário e senha inválidos")
        print("Tente novamente")