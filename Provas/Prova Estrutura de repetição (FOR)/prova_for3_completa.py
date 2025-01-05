começo = int(input("Digite o numero de começo:  "))
fim = int(input("Digite o numero de final: "))

soma_pares = 0

for i in range(começo, fim + 1):
    if i % 2 == 0:
        soma_pares += i
else:    
    if soma_pares == 0:
        print("Não há números pares no intervalo.")

if soma_pares > 0:
    print(f"O resultado da soma de todos os números pares é {soma_pares}")
