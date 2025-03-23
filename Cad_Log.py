def cadastrar_usuario(usuarios):
    print("CADASTRAR CONTA")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    senha = input("Digite sua senha: ")
    senha2 = input("Confirme sua senha: ")

    if senha == senha2:
        usuarios[email] = {'nome': nome, 'senha': senha}
        print("CADASTRO EFETUADO COM SUCESSO")
        return True  # Indica que o cadastro foi realizado
    else:
        print("As senhas não são iguais")
        return False  # Indica que o cadastro falhou

def fazer_login(usuarios):
    print("LOGIN")
    emailLog = input("Digite seu email: ")
    senhaLog = input("Digite sua senha: ")

    # Verificando se o email está cadastrado e se a senha está correta
    if emailLog in usuarios:
        if senhaLog == usuarios[emailLog]['senha']:
            print("BEM VINDO(A)", usuarios[emailLog]['nome'])
            return True  # Login bem-sucedido
        else:
            print("Email ou senha incorreta")
    else:
        print("Email ou senha incorreta")
    return False  # Login falhou

def cl():
    usuarios = {}  # Dicionário para armazenar usuários cadastrados
    while True:
        if not fazer_login(usuarios):  # Tenta fazer login
            if cadastrar_usuario(usuarios):  # Se não conseguir, tenta cadastrar
                break  # Sai do loop se o cadastro foi bem-sucedido
        else:
            break  # Sai do loop se o login foi bem-sucedido
