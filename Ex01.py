#Inserindo notas e validação do dado
trabLab = float(input("Digite a nota do Trabalho de Laboratório: "))
while(trabLab < 0 or trabLab > 10):
    print("Nota inválida!")
    trabLab = float(input("Digite a nota do Trabalho de Laboratório: "))


avaliacaoSem = float(input("Digite a nota da Avaliação Semestral: "))
while(avaliacaoSem < 0 or avaliacaoSem > 10):
    print("Nota inválida!")
    avaliacaoSem = float(input("Digite a nota da Avaliação Semestral: "))


exameFinal = float(input("Digite a nota do Exame Final: "))
while(exameFinal < 0 or exameFinal > 10):
    print("Nota inválida!")
    exameFinal = float(input("Digite a nota do Exame Final: "))

#Calculo da media
media = (trabLab * 2 + avaliacaoSem * 3 + exameFinal * 5) / 10

#Determinação do Conceito
if(media < 5):
    print("Média: ", round(media,1), " - Conceito E")
elif(media < 6):
    print("Média: ", round(media,1), " - Conceito D")
elif(media < 7):
    print("Média: ", round(media,1), " - Conceito C")
elif(media < 8):
    print("Média: ", round(media,1), " - Conceito B")
else:
    print("Média: ", round(media,1), " - Conceito A")
