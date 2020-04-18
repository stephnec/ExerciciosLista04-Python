#Entrada dados para lados triâgulo
lado1 = float(input("Digite o valor do primeiro lado do triângulo: ")) 
lado2 = float(input("Digite o valor do segundo lado do triângulo: ")) 
lado3 = float(input("Digite o valor do terceiro lado do triângulo: ")) 

#Verificando a existência para o triângulo
if(lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2):
    print("Os valores inseridos não podem formar um triângulo.")
else:   
    #Verificando tipo de triângulo
    if(lado1 == lado2 and lado1 == lado3):
        print("O triângulo é Equilátero!")
    elif (lado1 == lado2 and lado1 != lado3):
        print("O triângulo é Isósceles!")
    else:
        print("O triângulo é Escaleno!")