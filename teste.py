name = input("Digite o nome: ")
code = input("Digite o código: ")
matri = input("Digite a matrícula: ")
tipo = input("Digite o tipo: ")  # evite usar "type"

BD = {
    "nome": name,
    "codigo": code,
    "matricula": matri,
    "tipo": tipo
}

request = input("Digite a requisição (nome,codigo,matricula,tipo): ")
