print(">>>BOLETIM<<<")

#Inserindo dados
nome = input("Digite o nome do aluno: ")

print("Insira as notas do aluno.")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

qntfaltas = int(input("Insira o número de faltas do aluno: "))

#Calculando média
media = (nota1 + nota2 + nota3) / 3

#Calculando porcentagem de faltas
prcFaltas = (qntfaltas * 100)  / 80

#Verificando situação final
if(prcFaltas < 25 and media >= 7):
    print("Média: ", round(media,1))
    print("Total de faltas: ", qntfaltas, " faltas de 80 aulas totais, totalizando ", prcFaltas, "% de falta.")
    print("Aluno aprovado!")
elif (prcFaltas > 25 and media >= 7):
    print("Média: ", round(media,1))
    print("Total de faltas: ", qntfaltas, " faltas de 80 aulas totais, totalizando ", prcFaltas, "% de falta.")
    print("Aluno reprovado por falta!")
else:
    print("Média: ", round(media,1))
    print("Total de faltas: ", qntfaltas, " faltas de 80 aulas totais, totalizando ", prcFaltas, "% de falta.")
    print("Aluno reprovado por média!")

