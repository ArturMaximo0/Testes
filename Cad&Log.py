
senha = ''
senha2 = '2'

while senha != senha2:
    print ("CADASTRAR CONTA")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    senha = input("Digite sua senha: ")
    senha2 = input("confirme sua senha: ")

    if senha == senha2:
        print ("CADASTRO EFETUADO COM SUCESSO")
   
    else:
        print ("As senhas não são iguais")

print ("LOGIN")
emailLog = input("Digite seu email: ")
senhaLog = input("Digite sua senha: ")

if emailLog == email:
    if senhaLog == senha:
        print ("BEM VINDO(A) ", nome)
    else:
        print ("Email ou senha incorreta")

else:
        print ("Email ou senha incorreta")