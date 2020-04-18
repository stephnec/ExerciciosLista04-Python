#Entrada dos números
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

soma = num1 + num2
print("Soma: ", soma)

if(soma > 10):
    print("Soma dos números maior que 10")
else:
    print("Soma menor ou igual a 10")