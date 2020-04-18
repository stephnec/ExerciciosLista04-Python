#Entrada dos números
num1 = int(input("Digite um número qualquer: "))
num2 = int(input("Digite outro número: "))

#Verificação
if(num1 % num2 == 0):
    print("O primeiro número (", num1,") é divisível pelo segundo número (", num2, ")")
else:
    print("O primeiro número (", num1,") NÃO é divisível pelo segundo número (", num2, ")")