print('*************')
print("*CALCULADORA teste*")
print('*************')

num1 = int(input("primeiro número:"))
print("")
opr = int(input("Soma = 1, subtração = 2, multplicação = 3, divisão = 4, elevado = 5:"))
print("")
num2: int = int(input("segundo número:"))

if opr == 1:
    print(num1 + num2)

if opr == 2:
    print(num1 - num2)

if opr == 3:
    print(num1 * num2)

if opr == 4:
    print(num1 / num2)

if opr == 5:
    print(num1 ** num2)