'''9 - Faça um algoritmo que cadastre um usuário e uma senha em duas
variáveis, o seu algoritmo deve validar para o usuário cadastrar somente
senhas com mais de 8 caracteres, do contrário informar ao usuário do erro,
usar função len para essa validação.'''

email = input("Crie um usuário: ")
senha = input("Crie sua senha (minimo 8 caracteres): ")

if len(senha) < 8:
    print("Não foi possivel realizar seu cadastro, pois sua senha contem menos de 8 caracteres")
else:
    print("Senha cadastrada")
