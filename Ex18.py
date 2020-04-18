#Apresentando opções
print(">>>>>>> Menu de opções <<<<<<<")
print("1. Somar dois números")
print("2. Raiz quadrada de um número")
opcao = int(input("Digite a opção desejada: "))

#Considerando opções
while(opcao != 1 and opcao != 2):
    print("Opção inválida!!")
    opcao = int(input("Digite a opção desejada: "))

#Verificando opções
if(opcao == 1): #soma
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    soma = num1 + num2

    print("A soma dos dois números digitados é igual a ", soma)
else: #raiz quadrada
    num1 = int(input("Digite um número: "))

    raiz = num1 * num1

    print("A raiz quadrada do número digitado é igual a ", raiz)
