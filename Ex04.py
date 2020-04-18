#Entrada dos números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

#Ordem Crescente
if(num1 < num2 and num1 < num3):
    posicao1 = num1
    if(num2 < num3):
        posicao2 = num2
        posicao3 = num3
    else:
        posicao2 = num3
        posicao3 = num2
    print("Ordem crescente -> ", posicao1, posicao2, posicao3)

elif(num2 < num1 and num2 < num3):
    posicao1 = num2
    if(num1 < num3):
        posicao2 = num1
        posicao3 = num3
    else:
        posicao2 = num3
        posicao3 = num1
    print("Ordem crescente -> ", posicao1, posicao2, posicao3)
        
elif(num3 < num1 and num3 < num2):
    posicao1 = num3
    if(num1 < num2):
        posicao2 = num1
        posicao3 = num2
    else:
        posicao2 = num2
        posicao3 = num1
    print("Ordem crescente -> ", posicao1, posicao2, posicao3)    

elif (num1 == num2 and num1 == num3):
    print("Os números são iguais")


