#Entrada dos números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print(num1)
print(num2)
print(num3)

#Ordem Crescente
if(num1 < num2 and num2 < num3):
    print("Os números foram digitados em ordem crescente")

elif (num1 == num2 and num1 == num3):
    print("Os números são iguais")

else:
    print("Os números não foram digitados em ordem crescente")

