def criptografar():
    pi = 3.14159265358979323846

    lista_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_d = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    

    print("Sistema de Criptografia de Senhas")
    print("Digite 'sair' para encerrar o programa a qualquer momento.")
    print("Digite 0 para encerrar o programa a qualquer momento.")
    print("Digite o login e a senha para criptografar e descriptografar.")
    login = input("Digite o login: ")
    if login == "sair":
        print("Encerrando o programa...")
        

    senha = int(input("Digite a senha: "))
    if senha == 0:
        print("Encerrando o programa...")
        
    
    login1 = input("Digite o login: ")
    if login1 == "sair":
        print("Encerrando o programa...")
        

    senha1 = int(input("Digite a senha: "))
    if senha1 == 0:
        print("Encerrando o programa...")
        
	
    login2 = input("Digite o login: ")
    if login2 == "sair":
        print("Encerrando o programa...")
        

    senha2 = int(input("Digite a senha: "))
    if senha2 == 0:
        print("Encerrando o programa...")
        
	
    login3 = input("Digite o login: ")
    if login3 == "sair":
        print("Encerrando o programa...")
        

    senha3 = int(input("Digite a senha: "))
    if senha3 == 0:
        print("Encerrando o programa...")

    
    senhac = senha   * pi
    senhac1 = senha1 * pi
    senhac2 = senha2 * pi
    senhac3 = senha3 * pi

    lista_c = [login, senhac, login1, senhac1, login2, senhac2, login3, senhac3]

    senhadc = senhac   / pi
    senhadc1 = senhac1 / pi
    senhadc2 = senhac2 / pi
    senhadc3 = senhac3 / pi

    lista_d = [login, senhadc, login1, senhadc1, login2, senhadc2, login3, senhadc3]
    return lista_c, lista_d