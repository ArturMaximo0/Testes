import random
def gerar_numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)
na1 = gerar_numero_aleatorio(1, 100000)
na2 = gerar_numero_aleatorio(1, 100000)
na3 = gerar_numero_aleatorio(1, 100000)
retweet_symbol = "\U0001F501"
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

AC = input("Fazer uma postagem? (s/n): ")
if AC == 's':
    post = input("Digite seu post: ")
    print (post)
    print ("💬",na1 ,"🔃",na2  ,"❤", na3 )
else:
    print ("sair da sua conta?  (s/n): ")
    sair = input()
    if sair == 's':
        print ("Conta deslogada")
    else:
        AC = input("Fazer uma postagem? (s/n): ")
if AC == 's':
    post = input("Digite seu post: ")
    print (post)
    print ("💬",na1 ,"🔃",na2  ,"❤", na3 )