print('*************')
print("*CALCULADORA teste*")
print('*************')

num1 = int(input("primeiro número:"))
print("")
opr = input("soma = + subtração = - multiplicação = * divisão = / potência = **\nEscolha a operação:")
print("")
num2: int = int(input("segundo número:"))

if opr == "+":
    print(num1 + num2)

if opr == "-":
    print(num1 - num2)

if opr == "*":
    print(num1 * num2)

if opr == "/":
    print(num1 / num2)

if opr == "**":
    print(num1 ** num2)