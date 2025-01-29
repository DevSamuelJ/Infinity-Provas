produtos = {}
contador = 0
while contador < 5:
  nome_produto= input("digite o nome do produto: ")
  preco_produto= float(input("digite o preco do produto: "))
  produtos[nome_produto] = preco_produto
  print(f"depois de inserir: {produtos}")
  contador+=1
total = 0
for chave_do_dicionario in produtos:
  total += produtos[chave_do_dicionario]
print(f"total com a soma: {total}")