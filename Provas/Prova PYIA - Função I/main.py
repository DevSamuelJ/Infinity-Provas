def media(num1, num2, num3):
    soma = num1 + num2 + num3
    resultado = soma / 3
    return resultado

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))


resultado = media(num1,num2,num3)
print(f"A média é: {resultado:.2f}") a

