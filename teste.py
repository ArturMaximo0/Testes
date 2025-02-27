num = input("Digite um número: ")
ip =  str (num)
ip = int(ip[-1])
if ip == 2 or ip == 4 or ip == 6 or ip == 8 or ip == 0:
    print ("é par!")
else:
    print ("é impar")