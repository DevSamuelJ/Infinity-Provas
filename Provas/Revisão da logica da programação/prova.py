nome = "samuel"
senha = "123"

tentativa = 0

while True:
  qual_nome = input("Informe o usuario para login: ")
  qual_senha = input("Informe a senha para login: ")

  if qual_nome == nome and qual_senha == senha:
    print(f"Bem-vindo, {nome.upper()}!")
    break 
  
  tentativa += 1
  if tentativa <3:
    print(f"Usuario e senha incorretos, tentativa {tentativa}/3")

  else:
     print(f"Usuario e senha incorretos, tentativa {tentativa}/3")
     for i in range(3):
       print("Acesso bloquedo.")
     break