pi = 3.14159265358979323846

def criptografar():
	print("Sistema de Criptografia de Senhas")
	print("Digite 'sair' para encerrar o programa a qualquer momento.")
	print("Digite 0 para encerrar o programa a qualquer momento.")
	print("Digite o login e a senha para criptografar e descriptografar.")
	login = input("Digite o login: ")
	if login == "sair":
		print("Encerrando o programa...")
		exit()

	senha = int(input("Digite a senha: "))
	if senha == 0:
		print("Encerrando o programa...")
		exit()
    
	login1 = input("Digite o login: ")
	if login1 == "sair":
		print("Encerrando o programa...")
		exit()

	senha1 = int(input("Digite a senha: "))
	if senha1 == 0:
		print("Encerrando o programa...")
		exit()
	
	login2 = input("Digite o login: ")
	if login2 == "sair":
		print("Encerrando o programa...")
		exit()

	senha2 = int(input("Digite a senha: "))
	if senha2 == 0:
		print("Encerrando o programa...")
		exit()
	
	login3 = input("Digite o login: ")
	if login3 == "sair":
		print("Encerrando o programa...")
		exit()

	senha3 = int(input("Digite a senha: "))
	if senha3 == 0:
		print("Encerrando o programa...")
		exit()
    
	senhac = senha   * pi
	senhac1 = senha1 * pi
	senhac2 = senha2 * pi
	senhac3 = senha3 * pi

	crip = [login, senhac, login1, senhac1, login2, senhac2, login3, senhac3]

	senhadc = senhac   / pi
	senhadc1 = senhac1 / pi
	senhadc2 = senhac2 / pi
	senhadc3 = senhac3 / pi

	dcrip = [login, senhadc, login1, senhadc1, login2, senhadc2, login3, senhadc3]
	return crip, dcrip