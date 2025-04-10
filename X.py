from Cad_Log import cl  # Certifique-se de que o nome do arquivo está correto
import random

def gerar_numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

na1 = gerar_numero_aleatorio(1, 100000)
na2 = gerar_numero_aleatorio(1, 100000)
na3 = gerar_numero_aleatorio(1, 100000)

cl()  # Chama a função que faz o login ou cadastro

AC = input("Fazer uma postagem? (s/n): ")
if AC == 's':
    post = input("Digite seu post: ")
    print(post)
    print("💬", na1, "🔃", na2, "❤", na3)
else:
    sair = input("Sair da sua conta? (s/n): ")
    if sair == 's':
        print("Conta deslogada")
