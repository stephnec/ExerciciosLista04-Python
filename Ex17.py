print("<<<LUCRO DO PRODUTO>>>")

#Inserindo valor do produto
produto = float(input("Insira o valor do produto a ser vendido: "))

#Verificando lucro
if(produto < 20):
    produtoLucro = produto * 1.45
else:
    produtoLucro = produto * 1.3

print("O produto deverá ser vendido por R$", round(produtoLucro,2))