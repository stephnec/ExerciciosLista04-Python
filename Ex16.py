#Inserindo um número
num = float(input("Digite um número qualquer: "))

#Verificando limites
if(num > 0 and num < 30):
    print("O número ", num, " está entre 0 e 30.")
elif(num > 40 and num < 79):
    print("O número ", num, " está entre 40 e 79.")
else:
    print("O número ", num, " está fora dos limites estabelecidos.")