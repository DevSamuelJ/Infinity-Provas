# começo = int(input("Digite o numero de começo:  "))
# fim = int(input("Digite o numero de final: "))

# for i in range(começo,fim+1):
#     if i % 2 == 0:
#         print(i)
#     else:
#         print(f"O numero {i} não é par")


# print(f"O resultado da soma de todos os numeros pares é {i+i}")



# começo = int(input("Digite o numero de começo:  "))
# fim = int(input("Digite o numero de final: "))

# soma_pares = 0
# tem_pares = False

# for i in range(começo, fim + 1):
#     if i % 2 == 0:
#         soma_pares += i
#         tem_pares = True

# if tem_pares:
#     print(f"O resultado da soma de todos os números pares é {soma_pares}")
# else:
#     print("Não há números pares no intervalo.")







# começo = int(input("Digite o numero de começo:  "))
# fim = int(input("Digite o numero de final: "))

# soma_pares = 0

# for i in range(começo, fim + 1):
#     if i % 2 == 0:
#         soma_pares += i

# if soma_pares > 0:
#     print(f"O resultado da soma de todos os números pares é {soma_pares}")
# else:
#     print("Não há números pares no intervalo.")


começo = int(input("Digite o numero de começo:  "))
fim = int(input("Digite o numero de final: "))

soma_pares = 0

for i in range(começo, fim + 1):
    if i % 2 == 0:
        soma_pares += i
else:
    # A estrutura 'else' do for só será executada se o loop terminar normalmente
    if soma_pares == 0:
        print("Não há números pares no intervalo.")

if soma_pares > 0:
    print(f"O resultado da soma de todos os números pares é {soma_pares}")
